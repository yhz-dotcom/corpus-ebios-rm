#!/usr/bin/env python3
"""
Script utilitaire pour exporter et analyser le registre SIA
Usage: python export-registre.py [command] [options]
"""

import yaml
import json
import csv
import sys
from datetime import datetime
from pathlib import Path
from collections import Counter

def load_registry(filepath):
    """Charge le registre YAML"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def export_csv(registry, output_path):
    """Exporte le registre en CSV pour Excel"""
    entries = registry.get('sia_entries', [])
    
    fieldnames = [
        'sia_id', 'nom_usage', 'equipe_responsable', 'niveau_ebios',
        'statut', 'date_qualification', 'prochaine_revue',
        'annex_iii', 'rgpd_concerne', 'incidents_signales'
    ]
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for entry in entries:
            row = {
                'sia_id': entry.get('sia_id', ''),
                'nom_usage': entry.get('identification', {}).get('nom_usage', ''),
                'equipe_responsable': entry.get('identification', {}).get('equipe_responsable', ''),
                'niveau_ebios': entry.get('qualification', {}).get('niveau_ebios', ''),
                'statut': entry.get('gouvernance', {}).get('statut', ''),
                'date_qualification': entry.get('identification', {}).get('date_qualification', ''),
                'prochaine_revue': entry.get('gouvernance', {}).get('prochaine_revue', ''),
                'annex_iii': entry.get('ai_act', {}).get('annex_iii', False),
                'rgpd_concerne': entry.get('rgpd', {}).get('concerne', False),
                'incidents_signales': entry.get('risques_synthese', {}).get('incidents_signales', 0)
            }
            writer.writerow(row)
    
    print(f"✅ Export CSV : {output_path}")

def export_json(registry, output_path):
    """Exporte le registre en JSON pour intégration"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Export JSON : {output_path}")

def generate_stats(registry):
    """Génère des statistiques du registre"""
    entries = registry.get('sia_entries', [])
    
    stats = {
        'total_entries': len(entries),
        'par_niveau': Counter(e.get('qualification', {}).get('niveau_ebios', 'Inconnu') for e in entries),
        'par_statut': Counter(e.get('gouvernance', {}).get('statut', 'Inconnu') for e in entries),
        'par_domaine': Counter(e.get('usage', {}).get('domaine_metier', 'Inconnu') for e in entries),
        'annex_iii': sum(1 for e in entries if e.get('ai_act', {}).get('annex_iii') == True),
        'rgpd': sum(1 for e in entries if e.get('rgpd', {}).get('concerne') == True),
        'incidents_total': sum(e.get('risques_synthese', {}).get('incidents_signales', 0) for e in entries)
    }
    
    return stats

def print_report(registry):
    """Affiche un rapport dans le terminal"""
    stats = generate_stats(registry)
    
    print("\n" + "="*60)
    print("📊 RAPPORT REGISTRE SIA")
    print("="*60)
    print(f"\nTotal usages : {stats['total_entries']}")
    
    print("\n📈 Par niveau EBIOS :")
    for niveau, count in sorted(stats['par_niveau'].items()):
        print(f"  {niveau} : {count}")
    
    print("\n📋 Par statut :")
    for statut, count in sorted(stats['par_statut'].items()):
        print(f"  {statut} : {count}")
    
    print("\n🏢 Par domaine :")
    for domaine, count in sorted(stats['par_domaine'].items()):
        print(f"  {domaine} : {count}")
    
    print(f"\n⚠️  Annex III AI Act : {stats['annex_iii']}")
    print(f"🔒 RGPD concerné : {stats['rgpd']}")
    print(f"🚨 Incidents signalés (12 mois) : {stats['incidents_total']}")
    
    print("\n" + "="*60)

def check_reviews(registry):
    """Vérifie les revues à venir"""
    entries = registry.get('sia_entries', [])
    today = datetime.now()
    
    upcoming = []
    overdue = []
    
    for entry in entries:
        review_date_str = entry.get('gouvernance', {}).get('prochaine_revue', '')
        if review_date_str and review_date_str != 'YYYY-MM-DD':
            try:
                review_date = datetime.strptime(review_date_str, '%Y-%m-%d')
                days_until = (review_date - today).days
                
                sia_id = entry.get('sia_id', '')
                nom = entry.get('identification', {}).get('nom_usage', '')
                
                if days_until < 0:
                    overdue.append((sia_id, nom, review_date_str, abs(days_until)))
                elif days_until <= 30:
                    upcoming.append((sia_id, nom, review_date_str, days_until))
            except ValueError:
                pass
    
    print("\n" + "="*60)
    print("📅 REVUES À VENIR (< 30 jours)")
    print("="*60)
    if upcoming:
        for sia_id, nom, date, days in sorted(upcoming, key=lambda x: x[3]):
            print(f"  ⏰ {sia_id} - {nom}")
            print(f"     Date : {date} (dans {days} jours)")
    else:
        print("  Aucune revue imminente")
    
    print("\n" + "="*60)
    print("⚠️  REVUES EN RETARD")
    print("="*60)
    if overdue:
        for sia_id, nom, date, days in sorted(overdue, key=lambda x: x[3], reverse=True):
            print(f"  🚨 {sia_id} - {nom}")
            print(f"     Date prévue : {date} (retard de {days} jours)")
    else:
        print("  Aucune revue en retard ✅")
    
    print("\n" + "="*60)

def generate_audit_report(registry, output_path):
    """Génère un rapport d'audit en Markdown"""
    entries = [e for e in registry.get('sia_entries', []) 
               if e.get('gouvernance', {}).get('statut') in ['Actif', 'En test pilote']]
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Rapport d'Audit Registre SIA\n\n")
        f.write(f"**Date de génération :** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write("---\n\n")
        
        for entry in entries:
            sia_id = entry.get('sia_id', '')
            ident = entry.get('identification', {})
            qualif = entry.get('qualification', {})
            gov = entry.get('gouvernance', {})
            
            f.write(f"## {sia_id} : {ident.get('nom_usage', '')}\n\n")
            f.write(f"- **Équipe :** {ident.get('equipe_responsable', '')}\n")
            f.write(f"- **Niveau EBIOS :** {qualif.get('niveau_ebios', '')}\n")
            f.write(f"- **Statut :** {gov.get('statut', '')}\n")
            f.write(f"- **Prochaine revue :** {gov.get('prochaine_revue', '')}\n")
            f.write(f"- **Fiche référence :** {qualif.get('fiche_reference', '')}\n\n")
            f.write("---\n\n")
    
    print(f"✅ Rapport audit : {output_path}")

def main():
    if len(sys.argv) < 2:
        print("""
Usage: python export-registre.py [command] [options]

Commands:
  csv [output.csv]        Exporte en CSV
  json [output.json]      Exporte en JSON
  stats                   Affiche les statistiques
  reviews                 Vérifie les revues à venir
  audit [output.md]       Génère rapport d'audit
  all                     Toutes les commandes

Examples:
  python export-registre.py csv registre-export.csv
  python export-registre.py stats
  python export-registre.py all
        """)
        sys.exit(1)
    
    command = sys.argv[1]
    registry_path = Path(__file__).parent / 'registre-sia-V2.yaml'
    
    if not registry_path.exists():
        print(f"❌ Fichier non trouvé : {registry_path}")
        sys.exit(1)
    
    registry = load_registry(registry_path)
    
    if command == 'csv':
        output = sys.argv[2] if len(sys.argv) > 2 else 'registre-export.csv'
        export_csv(registry, output)
    
    elif command == 'json':
        output = sys.argv[2] if len(sys.argv) > 2 else 'registre-export.json'
        export_json(registry, output)
    
    elif command == 'stats':
        print_report(registry)
    
    elif command == 'reviews':
        check_reviews(registry)
    
    elif command == 'audit':
        output = sys.argv[2] if len(sys.argv) > 2 else 'rapport-audit.md'
        generate_audit_report(registry, output)
    
    elif command == 'all':
        export_csv(registry, 'registre-export.csv')
        export_json(registry, 'registre-export.json')
        print_report(registry)
        check_reviews(registry)
        generate_audit_report(registry, 'rapport-audit.md')
        print("\n✅ Tous les exports ont été générés")
    
    else:
        print(f"❌ Commande inconnue : {command}")
        sys.exit(1)

if __name__ == '__main__':
    main()
