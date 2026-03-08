#!/usr/bin/env python3
"""
Correction systématique Lot 1: RGPD/DPIA pour cas sensibles
"""

import os
import re

CORPUS_DIR = "/tmp/corpus-ebios-rm/v2/analyses"

# Cas nécessitant RGPD/DPIA avec justification spécifique
CAS_RGPD = {
    # Éducation - données enfants
    "ebios-analysis-cognia.md": "RGPD Art. 8/35 : Données enfants + orientation scolaire = DPIA obligatoire",
    "ebios-analysis-pathfinder.md": "RGPD Art. 8/35 : Données enfants + déterminisme social = DPIA obligatoire",
    "ebios-analysis-edumood.md": "RGPD Art. 8/35 : Données enfants + émotions = DPIA obligatoire",
    "ebios-analysis-learnadapt.md": "RGPD Art. 35 : Données engagement apprenants = DPIA requise",
    
    # Santé - données médicales
    "ebios-analysis-vitalpredict.md": "RGPD Art. 9/35 : Données santé sensibles + prédiction médicale = DPIA obligatoire",
    "ebios-analysis-triageflow.md": "RGPD Art. 9/35 : Données santé + décision clinique = DPIA obligatoire",
    "ebios-analysis-carecoord.md": "RGPD Art. 9/35 : Données patients + allocation ressources = DPIA obligatoire",
    "ebios-analysis-neuroboost.md": "RGPD Art. 9 : Données neurotechnologie = catégorie spéciale",
    
    # Données personnelles sensibles
    "ebios-analysis-narrativeflow.md": "RGPD Art. 9/35 : Données psychographiques + opinions = DPIA requise",
    "ebios-analysis-lifeguard.md": "RGPD Art. 9/35 : Données santé inférées + scoring = DPIA obligatoire",
    "ebios-analysis-vitarisk.md": "RGPD Art. 9/35 : Données santé + comportement = DPIA obligatoire",
    "ebios-analysis-medrisk.md": "RGPD Art. 9/35 : Données santé + tarification = DPIA obligatoire",
    
    # Biométrie/surveillance
    "ebios-analysis-surveileye.md": "RGPD Art. 9 : Données biométriques (reconnaissance faciale) = catégorie spéciale",
    "ebios-analysis-terravox.md": "RGPD Art. 9/35 : Données vocales agricoles + localisation = DPIA requise",
}

def add_rgpd_to_case(filepath, justification):
    """Ajoute RGPD/DPIA à un cas"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifier si déjà présent
    if 'DPIA' in content or 'Art. 35' in content:
        return False, "Déjà présent"
    
    # Chercher le tableau de classification AI Act
    pattern = r"(\| \*\*Annexe III point \d+\*\* \| .+? \| .+? \|)"
    match = re.search(pattern, content)
    
    if match:
        # Insérer après la dernière ligne du tableau de classification
        insertion_point = match.end()
        new_line = f"\n| **RGPD Art. 35** | {justification.split(' : ')[1]} | 🔴 **OBLIGATOIRE** |"
        
        content = content[:insertion_point] + new_line + content[insertion_point:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Ajouté"
    
    return False, "Pattern non trouvé"

if __name__ == "__main__":
    print("=== CORRECTION LOT 1: RGPD/DPIA ===\n")
    
    for cas, justification in CAS_RGPD.items():
        filepath = os.path.join(CORPUS_DIR, cas)
        if os.path.exists(filepath):
            success, msg = add_rgpd_to_case(filepath, justification)
            status = "✓" if success else "○"
            print(f"{status} {cas}: {msg}")
        else:
            print(f"✗ {cas}: Fichier non trouvé")
    
    print("\n=== LOT 1 TERMINÉ ===")
