#!/usr/bin/env python3
"""
CLI EBIOS-RM IA — Qualification et validation des usages

Usage:
    sia-cli qualify --mode express          # Qualification rapide
    sia-cli validate registry.yaml          # Validation schéma
    sia-cli export --format csv             # Export registre
    sia-cli dashboard                       # Vue d'ensemble
"""

import argparse
import json
import sys
import yaml
from datetime import datetime
from pathlib import Path
from typing import Optional

# Schéma JSON intégré (simplifié pour l'exemple)
SCHEMA_VERSION = "2.0.0"


def load_schema() -> dict:
    """Charge le schéma JSON de validation"""
    schema_path = Path(__file__).parent.parent.parent / "registry" / "schema.json"
    if schema_path.exists():
        with open(schema_path, 'r') as f:
            return json.load(f)
    return {}


def validate_yaml(file_path: str) -> tuple[bool, list]:
    """Valide un fichier YAML contre le schéma"""
    errors = []
    
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return False, [f"Erreur YAML: {e}"]
    except FileNotFoundError:
        return False, [f"Fichier non trouvé: {file_path}"]
    
    # Validation basique (schéma complet serait avec jsonschema)
    if not isinstance(data, dict):
        return False, ["Le fichier doit contenir un objet YAML"]
    
    if 'sia_id' not in data and 'metadata' not in data:
        errors.append("Champ 'sia_id' ou 'metadata' requis")
    
    # Vérification des entrées si c'est un registre
    if 'sia_entries' in data:
        entries = data['sia_entries']
        if not isinstance(entries, list):
            errors.append("'sia_entries' doit être une liste")
        else:
            for i, entry in enumerate(entries):
                if not isinstance(entry, dict):
                    errors.append(f"Entrée {i}: doit être un objet")
                    continue
                if 'sia_id' not in entry:
                    errors.append(f"Entrée {i}: 'sia_id' manquant")
                elif not isinstance(entry.get('sia_id'), str):
                    errors.append(f"Entrée {i}: 'sia_id' doit être une chaîne")
    
    # Vérification d'une entrée unique
    elif 'sia_id' in data:
        required_fields = ['identification', 'technical', 'usage', 'assessment', 'governance']
        for field in required_fields:
            if field not in data:
                errors.append(f"Champ requis manquant: '{field}'")
    
    return len(errors) == 0, errors


def interactive_qualification(mode: str = "express") -> dict:
    """Qualification interactive"""
    print(f"🤖 EBIOS-RM IA Qualifier ({mode.title()} Mode)\n")
    
    entry = {
        "sia_id": "",
        "identification": {},
        "technical": {},
        "usage": {},
        "assessment": {},
        "governance": {},
        "tags": []
    }
    
    # Identification
    print("📋 Identification")
    entry["sia_id"] = input("ID SIA (ex: SIA-XXX-001): ").strip() or "SIA-XXX-001"
    entry["identification"]["name"] = input("Nom de l'usage: ").strip()
    entry["identification"]["team"] = input("Équipe responsable: ").strip()
    entry["identification"]["qualification_date"] = datetime.now().strftime("%Y-%m-%d")
    entry["identification"]["qualified_by"] = [input("Qualifié par: ").strip()]
    
    if mode == "detailed":
        print("\n🔧 Aspects techniques")
        entry["technical"]["base_model"] = input("Modèle de base: ").strip()
        entry["technical"]["provider"] = input("Fournisseur: ").strip()
        entry["technical"]["interface"] = input("Interface (API/web/etc.): ").strip()
        entry["technical"]["modified"] = input("Modèle modifié? (o/n): ").lower() == 'o'
        
        print("\n📊 Usage")
        print("Niveaux d'automatisation:")
        print("  1. Conversational only")
        print("  2. Assisted")
        print("  3. Semi-automated")
        print("  4. Automated with supervision")
        print("  5. Fully automated")
        auto_levels = [
            "Conversational only",
            "Assisted",
            "Semi-automated",
            "Automated with supervision",
            "Fully automated"
        ]
        choice = int(input("Choix (1-5): ") or "1")
        entry["usage"]["automation_level"] = auto_levels[choice - 1]
        
        print("\nImpact:")
        print("  1. None  2. Low  3. Medium  4. High  5. Critical  6. Regulatory")
        impacts = ["None", "Low", "Medium", "High", "Critical", "Regulatory"]
        choice = int(input("Choix (1-6): ") or "1")
        entry["usage"]["impact"] = impacts[choice - 1]
    
    # Qualification (toujours)
    print("\n🎯 Qualification EBIOS-RM")
    print("\nQ1: L'IA agit-elle sur des données/processus métier ?")
    print("  (vs. simple conversation / brainstorming)")
    q1 = input("  Oui/Non: ").lower().startswith('o')
    
    if not q1:
        level = "🟢 Level 1"
        template = "template-level-1"
    else:
        print("\nQ2: La sortie influence-t-elle une décision ou action ?")
        q2 = input("  Oui/Non: ").lower().startswith('o')
        
        if not q2:
            level = "🟢 Level 1"
            template = "template-level-1"
        else:
            print("\nQ3: La décision/action est-elle automatisée ou à fort impact ?")
            print("  (vs. validation humaine systématique)")
            q3 = input("  Oui/Non: ").lower().startswith('o')
            
            if not q3:
                level = "🟡 Level 2"
                template = "template-level-2"
            else:
                level = "🔴 Level 3"
                template = "template-level-3"
    
    print("\nQ4: L'usage concerne-t-il un domaine 'haut risque' (Annexe III AI Act) ?")
    q4 = input("  Oui/Non: ").lower().startswith('o')
    
    if q4:
        level = "🔴 Level 3"
        template = "template-level-3"
        entry["ai_act"] = {"annex_iii": True}
    
    entry["assessment"]["ebios_level"] = level
    entry["assessment"]["template_used"] = template
    entry["assessment"]["next_assessment"] = (
        datetime.now().replace(year=datetime.now().year + 1).strftime("%Y-%m-%d")
    )
    
    entry["governance"]["status"] = "Active"
    entry["governance"]["next_review"] = entry["assessment"]["next_assessment"]
    
    # Résumé
    print(f"\n{'='*50}")
    print(f"✅ Qualification terminée!")
    print(f"   Niveau: {level}")
    print(f"   Template: {template}")
    print(f"   Prochaine revue: {entry['assessment']['next_assessment']}")
    print(f"{'='*50}")
    
    return entry


def export_registry(file_path: str, format: str = "yaml") -> str:
    """Exporte le registre dans différents formats"""
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        return f"❌ Erreur: {e}"
    
    if format == "json":
        output = json.dumps(data, indent=2, ensure_ascii=False)
        ext = "json"
    elif format == "csv":
        # Export CSV simplifié
        entries = data.get('sia_entries', [])
        if not entries:
            return "❌ Aucune entrée à exporter"
        
        import csv
        import io
        output_buffer = io.StringIO()
        fieldnames = ['sia_id', 'name', 'team', 'level', 'status']
        writer = csv.DictWriter(output_buffer, fieldnames=fieldnames)
        writer.writeheader()
        
        for entry in entries:
            writer.writerow({
                'sia_id': entry.get('sia_id', ''),
                'name': entry.get('identification', {}).get('name', ''),
                'team': entry.get('identification', {}).get('team', ''),
                'level': entry.get('assessment', {}).get('ebios_level', ''),
                'status': entry.get('governance', {}).get('status', '')
            })
        output = output_buffer.getvalue()
        ext = "csv"
    else:
        output = yaml.dump(data, allow_unicode=True, sort_keys=False)
        ext = "yaml"
    
    output_path = f"export.{ext}"
    with open(output_path, 'w') as f:
        f.write(output)
    
    return f"✅ Exporté vers {output_path}"


def show_dashboard(file_path: str):
    """Affiche un tableau de bord simple"""
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return
    
    entries = data.get('sia_entries', [])
    
    print("\n" + "="*60)
    print("📊 DASHBOARD EBIOS-RM IA")
    print("="*60)
    print(f"\nTotal usages: {len(entries)}")
    
    # Comptage par niveau
    levels = {}
    statuses = {}
    for entry in entries:
        level = entry.get('assessment', {}).get('ebios_level', 'Unknown')
        status = entry.get('governance', {}).get('status', 'Unknown')
        levels[level] = levels.get(level, 0) + 1
        statuses[status] = statuses.get(status, 0) + 1
    
    print("\nPar niveau:")
    for level, count in sorted(levels.items()):
        print(f"  {level}: {count}")
    
    print("\nPar statut:")
    for status, count in sorted(statuses.items()):
        print(f"  {status}: {count}")
    
    # Revues à venir
    today = datetime.now()
    upcoming = []
    for entry in entries:
        review_str = entry.get('governance', {}).get('next_review', '')
        if review_str:
            try:
                review_date = datetime.strptime(review_str, '%Y-%m-%d')
                days = (review_date - today).days
                if 0 <= days <= 30:
                    upcoming.append((entry['sia_id'], days))
            except ValueError:
                pass
    
    if upcoming:
        print(f"\n⏰ Revues à venir (≤ 30 jours): {len(upcoming)}")
        for sia_id, days in sorted(upcoming, key=lambda x: x[1]):
            print(f"  {sia_id}: dans {days} jours")
    
    print("\n" + "="*60)


def main():
    parser = argparse.ArgumentParser(
        description='CLI EBIOS-RM IA — Qualification et validation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
    sia-cli qualify --mode express              # Qualification rapide
    sia-cli validate registry.yaml              # Validation
    sia-cli export registry.yaml --format csv   # Export CSV
    sia-cli dashboard registry.yaml             # Vue d'ensemble
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commandes disponibles')
    
    # Commande qualify
    qualify_parser = subparsers.add_parser('qualify', help='Qualification interactive')
    qualify_parser.add_argument('--mode', choices=['express', 'detailed'], 
                                default='express', help='Mode de qualification')
    qualify_parser.add_argument('--output', '-o', help='Fichier de sortie')
    
    # Commande validate
    validate_parser = subparsers.add_parser('validate', help='Validation schéma')
    validate_parser.add_argument('file', help='Fichier YAML à valider')
    
    # Commande export
    export_parser = subparsers.add_parser('export', help='Export registre')
    export_parser.add_argument('file', help='Fichier registre')
    export_parser.add_argument('--format', choices=['yaml', 'json', 'csv'], 
                               default='yaml', help='Format de sortie')
    
    # Commande dashboard
    dashboard_parser = subparsers.add_parser('dashboard', help='Tableau de bord')
    dashboard_parser.add_argument('file', help='Fichier registre')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    if args.command == 'qualify':
        entry = interactive_qualification(args.mode)
        output = yaml.dump(entry, allow_unicode=True, sort_keys=False)
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
            print(f"\n💾 Sauvegardé dans {args.output}")
        else:
            print("\n" + "="*50)
            print("Entrée générée (YAML):")
            print("="*50)
            print(output)
    
    elif args.command == 'validate':
        is_valid, errors = validate_yaml(args.file)
        if is_valid:
            print("✅ Fichier valide")
        else:
            print("❌ Erreurs de validation:")
            for error in errors:
                print(f"  - {error}")
            sys.exit(1)
    
    elif args.command == 'export':
        result = export_registry(args.file, args.format)
        print(result)
    
    elif args.command == 'dashboard':
        show_dashboard(args.file)


if __name__ == '__main__':
    main()
