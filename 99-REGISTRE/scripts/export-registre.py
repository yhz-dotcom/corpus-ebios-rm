#!/usr/bin/env python3
"""
Export du registre SIA vers différents formats

Usage:
    python export-registre.py --format csv --filter "statut:Actif"
    python export-registre.py --format json --filter "annex_iii:true"
    python export-registre.py --format audit --output rapport-2026-Q1
"""

import yaml
import json
import csv
import sys
import argparse
from pathlib import Path
from datetime import datetime


def load_registre(path: str) -> dict:
    """Charge le registre YAML"""
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def filter_entries(entries: list, filter_expr: str) -> list:
    """Filtre basique : 'statut:Actif' ou 'annex_iii:true'"""
    if not filter_expr:
        return entries
    
    key, val = filter_expr.split(':')
    result = []
    
    for e in entries:
        # Navigation simple dans le dictionnaire
        parts = key.split('.')
        curr = e
        
        for p in parts:
            curr = curr.get(p, {}) if isinstance(curr, dict) else None
            if curr is None:
                break
        
        if curr is not None and str(curr).lower() == val.lower():
            result.append(e)
    
    return result


def to_csv(entries: list, output: str):
    """Exporte les entrées en CSV"""
    if not entries:
        print("⚠️  Aucune entrée à exporter")
        return
    
    # Aplatir les champs principaux pour le CSV
    flat_entries = []
    for e in entries:
        flat = {
            'sia_id': e.get('sia_id'),
            'nom_usage': e.get('identification', {}).get('nom_usage'),
            'equipe': e.get('identification', {}).get('equipe_responsable'),
            'niveau_ebios': e.get('qualification', {}).get('niveau_ebios'),
            'annex_iii': e.get('ai_act', {}).get('annex_iii'),
            'role_ai_act': e.get('ai_act', {}).get('role'),
            'rgpd': e.get('rgpd', {}).get('concerne'),
            'statut': e.get('gouvernance', {}).get('statut'),
            'prochaine_revue': e.get('gouvernance', {}).get('prochaine_revue'),
            'fiche_reference': e.get('qualification', {}).get('fiche_reference'),
        }
        flat_entries.append(flat)
    
    with open(output, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=flat_entries[0].keys())
        writer.writeheader()
        writer.writerows(flat_entries)
    
    print(f"✅ Export CSV : {output} ({len(flat_entries)} entrées)")


def to_json(entries: list, output: str):
    """Exporte les entrées en JSON"""
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Export JSON : {output} ({len(entries)} entrées)")


def report_audit(entries: list, output: str):
    """Génère un rapport texte simple pour audit"""
    with open(output, 'w', encoding='utf-8') as f:
        f.write(f"# Rapport d'audit SIA — {datetime.now().strftime('%Y-%m-%d')}\n\n")
        f.write(f"Total entrées : {len(entries)}\n\n")
        
        # Comptage par niveau
        niveaux = {'🟢 Light': 0, '🟡 Standard': 0, '🔴 Renforcé': 0, '⚪️ Non qualifié': 0}
        for e in entries:
            niv = e.get('qualification', {}).get('niveau_ebios', '')
            if niv in niveaux:
                niveaux[niv] += 1
        
        f.write("## Répartition par niveau EBIOS\n")
        for niv, count in niveaux.items():
            f.write(f"- {niv} : {count}\n")
        
        # Annex III
        annex3 = [e for e in entries if e.get('ai_act', {}).get('annex_iii')]
        if annex3:
            f.write(f"\n## ⚠️  Usages Annex III (haut risque) : {len(annex3)}\n")
            for e in annex3:
                role = e.get('ai_act', {}).get('role', 'Non défini')
                f.write(f"- {e['sia_id']} : {e['identification']['nom_usage']} (Rôle: {role})\n")
        
        # RGPD
        rgpd = [e for e in entries if e.get('rgpd', {}).get('concerne')]
        if rgpd:
            f.write(f"\n## 🔐 Usages RGPD : {len(rgpd)}\n")
            for e in rgpd:
                aipd = e.get('rgpd', {}).get('aipd_reference', 'Non référencée')
                f.write(f"- {e['sia_id']} : AIPD = {aipd}\n")
        
        # Revues à venir
        today = datetime.now()
        upcoming = []
        for e in entries:
            review_str = e.get('gouvernance', {}).get('prochaine_revue', '')
            if review_str and review_str not in ['YYYY-MM-DD', 'À définir']:
                try:
                    review_date = datetime.strptime(review_str, '%Y-%m-%d')
                    days = (review_date - today).days
                    if 0 <= days <= 30:
                        upcoming.append((e['sia_id'], e['identification']['nom_usage'], review_str, days))
                except ValueError:
                    pass
        
        if upcoming:
            f.write(f"\n## 📅 Revues à venir (≤ 30 jours) : {len(upcoming)}\n")
            for sia_id, nom, date, days in sorted(upcoming, key=lambda x: x[3]):
                f.write(f"- {sia_id} : {nom} — {date} (dans {days} jours)\n")
    
    print(f"✅ Rapport audit : {output}")


def main():
    parser = argparse.ArgumentParser(
        description='Export du registre SIA',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
    python export-registre.py --format csv
    python export-registre.py --format json --filter "annex_iii:true"
    python export-registre.py --format audit --filter "statut:Actif"
    python export-registre.py --format csv --filter "niveau_ebios:🔴 Renforcé"
        """
    )
    
    parser.add_argument(
        '--file', 
        default='99-REGISTRE/registre-sia-V2.yaml',
        help='Chemin du registre YAML (défaut: 99-REGISTRE/registre-sia-V2.yaml)'
    )
    
    parser.add_argument(
        '--format', 
        choices=['csv', 'json', 'audit'], 
        required=True,
        help='Format de sortie'
    )
    
    parser.add_argument(
        '--filter', 
        default='',
        help='Filtre simple : champ:valeur (ex: statut:Actif, annex_iii:true)'
    )
    
    parser.add_argument(
        '--output', 
        default='export-sia',
        help='Nom de fichier de sortie (sans extension)'
    )
    
    args = parser.parse_args()
    
    # Vérifier que le fichier existe
    file_path = Path(args.file)
    if not file_path.exists():
        print(f"❌ Fichier non trouvé : {file_path}")
        print(f"   Chemin absolu : {file_path.absolute()}")
        sys.exit(1)
    
    # Charger et filtrer
    registre = load_registre(str(file_path))
    entries = filter_entries(registre.get('sia_entries', []), args.filter)
    
    print(f"📊 {len(entries)} entrées trouvées")
    if args.filter:
        print(f"   Filtre appliqué : {args.filter}")
    
    # Exporter selon le format
    ext = {'csv': 'csv', 'json': 'json', 'audit': 'txt'}.get(args.format)
    output = f"{args.output}.{ext}"
    
    if args.format == 'csv':
        to_csv(entries, output)
    elif args.format == 'json':
        to_json(entries, output)
    elif args.format == 'audit':
        report_audit(entries, output)


if __name__ == '__main__':
    main()
