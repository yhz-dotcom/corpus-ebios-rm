#!/usr/bin/env python3
"""
Correction Lot 9: RGPD final - derniers cas
"""

import os

CORPUS_DIR = "/tmp/corpus-ebios-rm/v2/analyses"

# Liste des 14 cas restants avec texte spécifique
CAS_FINaux = {
    "ebios-analysis-adpulse-incidents.md": "Données comportementales publicitaires",
    "ebios-analysis-aegiscounter.md": "Logs cybersécurité critiques",
    "ebios-analysis-agriopti.md": "Données agricoles parcellaires",
    "ebios-analysis-agriscore.md": "Données exploitation agricole",
    "ebios-analysis-ecocredit-sus.md": "Données ESG entreprises",
    "ebios-analysis-ecocredit.md": "Données consommation bancaire",
    "ebios-analysis-forceselect.md": "Données militaires sensibles",
    "ebios-analysis-helios.md": "Données production énergétique",
    "ebios-analysis-narrativeflow.md": "Données psychographiques",
    "ebios-analysis-neuroboost.md": "Données neurotechnologie",
    "ebios-analysis-scorelife.md": "Scoring social interdit",
    "ebios-analysis-surveileye.md": "Biométrie faciale",
    "ebios-analysis-workvibe.md": "Surveillance émotionnelle",
    "ebios-analysis-aegisdrone.md": "Données cibles militaires",
}

def add_rgpd_final(filepath, description):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Chercher n'importe où dans les 200 premières lignes
    lines = content.split('\n')
    
    # Chercher ligne avec tableau de classification
    for i, line in enumerate(lines[:100]):
        if '| **' in line and ('AI Act' in line or 'Annexe' in line or 'HIGH-RISK' in line or 'PROHIBITED' in line):
            # Insérer après cette ligne
            new_line = f"| **RGPD** | {description} | 🔴 **OBLIGATOIRE** |"
            lines.insert(i+1, new_line)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            return True, f"Ajouté ligne {i+1}"
    
    return False, "Pattern tableau non trouvé"

if __name__ == "__main__":
    print("=== CORRECTION LOT 9: RGPD FINAL ===\n")
    
    ajoutes = 0
    echecs = 0
    
    for cas, desc in CAS_FINaux.items():
        filepath = os.path.join(CORPUS_DIR, cas)
        if os.path.exists(filepath):
            success, msg = add_rgpd_final(filepath, desc)
            if success:
                ajoutes += 1
                print(f"✓ {cas}: {msg}")
            else:
                echecs += 1
                print(f"○ {cas}: {msg}")
        else:
            print(f"✗ {cas}: Fichier non trouvé")
    
    print(f"\n=== LOT 9 TERMINÉ ===")
    print(f"Ajoutés: {ajoutes}, Échecs: {echecs}")
