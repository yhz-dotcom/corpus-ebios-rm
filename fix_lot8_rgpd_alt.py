#!/usr/bin/env python3
"""
Correction Lot 8: RGPD pour cas restants - approche alternative
"""

import os
import re

CORPUS_DIR = "/tmp/corpus-ebios-rm/v2/analyses"

def get_cases_without_rgpd():
    cases = []
    for f in os.listdir(CORPUS_DIR):
        if f.startswith('ebios-analysis-') and f.endswith('.md'):
            filepath = os.path.join(CORPUS_DIR, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            if 'DPIA' not in content and 'Art. 35' not in content and 'Art. 9' not in content and 'Art. 8' not in content and 'RGPD' not in content:
                cases.append(f)
    return cases

def add_rgpd_alternative(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Chercher "Classification AI Act" ou "Piège"
    patterns = [
        r"(## 1\.2.*Classification.*\n\n\|)",
        r"(\*\*Piège.*\*\*)",
        r"(## 1\. CADRE.*\n\n### 1\.2)",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content)
        if match:
            # Insérer après la ligne de tableau ou avant Piège
            pos = match.end()
            new_text = "\n| **RGPD Art. 35** | Données personnelles = DPIA obligatoire | 🔴 **REQUIS** |"
            content = content[:pos] + new_text + content[pos:]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Ajouté (alt)"
    
    # Dernier recours: ajouter après SYNTHÈSE EXÉCUTIVE
    match = re.search(r"(## 📋 SYNTHÈSE EXÉCUTIVE.*?\n\|.*?\|.*?\|)\n", content, re.DOTALL)
    if match:
        pos = match.end()
        new_text = "| **RGPD** | Données personnelles traitées | 🔴 **DPIA requise** |\n"
        content = content[:pos] + new_text + content[pos:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Ajouté (syn)"
    
    return False, "Aucun pattern trouvé"

if __name__ == "__main__":
    print("=== CORRECTION LOT 8: RGPD APPROCHE ALTERNATIVE ===\n")
    
    cases = get_cases_without_rgpd()
    print(f"Cas sans RGPD: {len(cases)}\n")
    
    ajoutes = 0
    echecs = 0
    
    for cas in cases:
        filepath = os.path.join(CORPUS_DIR, cas)
        success, msg = add_rgpd_alternative(filepath)
        if success:
            ajoutes += 1
            print(f"✓ {cas}: {msg}")
        else:
            echecs += 1
            print(f"○ {cas}: {msg}")
    
    print(f"\n=== LOT 8 TERMINÉ ===")
    print(f"Ajoutés: {ajoutes}, Échecs: {echecs}")
