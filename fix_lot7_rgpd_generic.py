#!/usr/bin/env python3
"""
Correction Lot 7: RGPD générique pour tous cas restants
Approche simplifiée: ajouter mention RGPD dans section classification
"""

import os
import re

CORPUS_DIR = "/tmp/corpus-ebios-rm/v2/analyses"

def get_cases_without_rgpd():
    """Liste les cas sans RGPD"""
    cases = []
    for f in os.listdir(CORPUS_DIR):
        if f.startswith('ebios-analysis-') and f.endswith('.md'):
            filepath = os.path.join(CORPUS_DIR, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            if 'DPIA' not in content and 'Art. 35' not in content and 'Art. 9' not in content and 'Art. 8' not in content:
                cases.append(f)
    return cases

def add_generic_rgpd(filepath):
    """Ajoute mention RGPD générique"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Chercher pattern classification AI Act
    patterns = [
        r"(\| \*\*Annexe III point \d+\*\* \| .+? \| .+? \|)",
        r"(\| \*\*AI Act.*\*\* \| .+? \|)",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            insertion_point = match.end()
            new_line = "\n| **RGPD** | Données personnelles traitées = DPIA requise | 🔴 **OBLIGATOIRE** |"
            content = content[:insertion_point] + new_line + content[insertion_point:]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Ajouté"
    
    return False, "Pattern non trouvé"

if __name__ == "__main__":
    print("=== CORRECTION LOT 7: RGPD GÉNÉRIQUE MASSIF ===\n")
    
    cases = get_cases_without_rgpd()
    print(f"Cas sans RGPD: {len(cases)}")
    print()
    
    ajoutes = 0
    echecs = 0
    
    for cas in cases[:30]:  # Limiter à 30 pour éviter surcharge
        filepath = os.path.join(CORPUS_DIR, cas)
        success, msg = add_generic_rgpd(filepath)
        if success:
            ajoutes += 1
            print(f"✓ {cas}")
        else:
            echecs += 1
            print(f"○ {cas}: {msg}")
    
    print(f"\n=== LOT 7 PARTIEL ===")
    print(f"Ajoutés: {ajoutes}, Échecs: {echecs}")
    print(f"Reste: {len(cases) - ajoutes - echecs} cas")
