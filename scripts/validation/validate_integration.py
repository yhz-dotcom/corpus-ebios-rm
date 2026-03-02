#!/usr/bin/env python3
"""Script de validation croisée EBIOS RM ↔ AI Act.

Vérifie la cohérence entre l'analyse EBIOS et la classification AI Act.
"""

import json
import sys
from typing import Dict, List, Optional


def validate_ebios_aiact_consistency(ebios_report: dict, aiact_classification: str) -> List[str]:
    """Vérifie la cohérence entre l'analyse EBIOS et la classification AI Act.
    
    Args:
        ebios_report: Rapport EBIOS avec scénarios et menaces
        aiact_classification: Classification AI Act (high_risk, limited_risk, minimal_risk)
    
    Returns:
        Liste des erreurs ou avertissements détectés
    """
    errors = []
    
    # Vérification 1: Système haut risque doit avoir des scénarios IA
    if aiact_classification == "high_risk":
        scenarios = ebios_report.get("scenarios", [])
        ia_scenarios = [s for s in scenarios if s.startswith("SR-IA-")]
        
        if "SR-IA-03" not in scenarios:
            errors.append("⚠️  Système haut risque : scénario biais (SR-IA-03) manquant")
        
        if len(ia_scenarios) < 2:
            errors.append("⚠️  Système haut risque : moins de 2 scénarios IA détectés")
    
    # Vérification 2: Menace prompt injection doit avoir scénario correspondant
    threats = ebios_report.get("threats", [])
    scenarios = ebios_report.get("scenarios", [])
    
    if "prompt injection" in threats and "SR-IA-04" not in scenarios:
        errors.append("⚠️  Menace prompt injection identifiée : scénario SR-IA-04 recommandé")
    
    if "biais" in threats and "SR-IA-03" not in scenarios:
        errors.append("⚠️  Menace biais identifiée : scénario SR-IA-03 recommandé")
    
    if "drift" in threats and "SR-IA-01" not in scenarios:
        errors.append("⚠️  Menace drift identifiée : scénario SR-IA-01 recommandé")
    
    # Vérification 3: Classification cohérente avec biens essentiels
    biens = ebios_report.get("biens_essentiels", [])
    
    if aiact_classification == "minimal_risk" and any(b.get("criticité") == "🔴" for b in biens):
        errors.append("⚠️  Classification minimal_risk mais biens essentiels haute criticité détectés")
    
    # Vérification 4: Exemption Art 6(3) cohérente avec scénarios
    exemption = ebios_report.get("exemption_art6_3", False)
    
    if exemption and "SR-IA-03" in scenarios:
        errors.append("⚠️  Exemption Art 6(3) invoquée mais profilage détecté (SR-IA-03)")
    
    return errors


def validate_annex_iv_completeness(doc_annex_iv: dict) -> List[str]:
    """Vérifie la complétude de la documentation technique Annexe IV.
    
    Args:
        doc_annex_iv: Documentation technique structurée
    
    Returns:
        Liste des sections manquantes ou incomplètes
    """
    errors = []
    required_sections = [
        "01-informations-generales",
        "02-description-systeme", 
        "03-elements-conception",
        "04-donnees-training",
        "05-mesures-risques",
        "06-modification-systeme",
        "07-systeme-qualite",
        "08-surveillance-post-marche",
        "09-informations-deployeur",
        "10-previsibilite",
        "11-logique-systeme",
        "12-cybersecurite"
    ]
    
    sections = doc_annex_iv.get("sections", [])
    section_ids = [s.get("id") for s in sections]
    
    for required in required_sections:
        if required not in section_ids:
            errors.append(f"⚠️  Section Annexe IV manquante: {required}")
    
    return errors


def main():
    """Point d'entrée principal."""
    if len(sys.argv) < 2:
        print("Usage: python validate_integration.py <ebios_report.json>")
        sys.exit(1)
    
    # Chargement du rapport EBIOS
    with open(sys.argv[1], 'r') as f:
        ebios_report = json.load(f)
    
    # Extraction de la classification AI Act
    aiact_classification = ebios_report.get("classification_aiact", "unknown")
    
    print(f"🔍 Validation du rapport EBIOS pour {ebios_report.get('system_name', 'Système')}")
    print(f"   Classification AI Act: {aiact_classification}")
    print()
    
    # Validation EBIOS ↔ AI Act
    errors = validate_ebios_aiact_consistency(ebios_report, aiact_classification)
    
    if errors:
        print("❌ Erreurs de cohérence détectées:")
        for error in errors:
            print(f"   {error}")
    else:
        print("✅ Cohérence EBIOS ↔ AI Act validée")
    
    # Validation Annexe IV si présente
    if "documentation_annex_iv" in ebios_report:
        annex_errors = validate_annex_iv_completeness(ebios_report["documentation_annex_iv"])
        if annex_errors:
            print("\n❌ Documentation Annexe IV incomplète:")
            for error in annex_errors:
                print(f"   {error}")
        else:
            print("\n✅ Documentation Annexe IV complète")
    
    print()
    print(f"📊 Résumé: {len(errors)} problème(s) détecté(s)")
    
    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    main()
