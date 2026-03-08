#!/usr/bin/env python3
"""
Correction Lot 4: Diagrammes Mermaid - cas restants
"""

import os
import re

CORPUS_DIR = "/tmp/corpus-ebios-rm/v2/analyses"

# Cas restants sans diagramme
CAS_RESTANTS = {
    "ebios-analysis-adpulse-incidents.md": {
        "system": "AdPulse",
        "context": "Publicité ciblée émotions",
        "risk": "Manipulation",
        "impact": "Consommateurs vulnérables",
        "scandal": "L'IA manipule nos émotions",
        "authorities": "CNIL + DGCCRF"
    },
    "ebios-analysis-aegis.md": {
        "system": "Aegis",
        "context": "Défense active cyber",
        "risk": "Hack-back illégal",
        "impact": "Dommages collatéraux",
        "scandal": "L'IA attaque des innocents",
        "authorities": "Interpol + Tribunaux"
    },
    "ebios-analysis-climatoracle-incidents.md": {
        "system": "CLIMAT-ORACLE",
        "context": "Prédiction climatique",
        "risk": "Panique sociale",
        "impact": "Migrations massives",
        "scandal": "L'IA prédit la fin du monde",
        "authorities": "ONU + Gouvernements"
    },
    "ebios-analysis-helios-incidents.md": {
        "system": "HELIOS-GRID",
        "context": "Gestion énergie solaire",
        "risk": "Blackout",
        "impact": "Villes sans électricité",
        "scandal": "L'IA plonge dans le noir",
        "authorities": "Régulateurs énergie"
    },
    "ebios-analysis-psycholoot-incidents.md": {
        "system": "PsychoLoot",
        "context": "Gaming prédation",
        "risk": "Addiction",
        "impact": "Suicides adolescents",
        "scandal": "L'IA tue nos enfants",
        "authorities": "Justice + Protection enfance"
    },
}

TEMPLATE = """
```mermaid
flowchart TB
    C1[Déploiement {system}<br/>{context}]
    --
    R1[{risk}<br/>+ Escalade]
    --
    C2[Crise majeure<br/>{impact}]
    --
    M1[Scandale "{scandal}"<br/>+ Médias + {authorities}]
    --
    I1[Interdiction système<br/>Poursuites pénales]
    --
    F1[Faillite<br/>Régulation drastique]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style R1 fill:#fff3e0,stroke:#ef6c00
    style C2 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```
"""

def add_mermaid(filepath, config):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '```mermaid' in content:
        return False, "Déjà présent"
    
    diagram = TEMPLATE.format(**config)
    
    # Chercher n'importe quelle section de niveau ##
    match = re.search(r"\n## \d+\. ", content)
    if match:
        # Insérer avant la dernière section (CONCLUSION ou PLAN)
        sections = list(re.finditer(r"\n## \d+\. ", content))
        if len(sections) >= 2:
            pos = sections[-2].start()
        else:
            pos = match.start()
        
        content = content[:pos] + diagram + "\n" + content[pos:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Ajouté"
    
    return False, "Pattern non trouvé"

if __name__ == "__main__":
    print("=== CORRECTION LOT 4: MERMAID CAS RESTANTS ===\n")
    
    for cas, config in CAS_RESTANTS.items():
        filepath = os.path.join(CORPUS_DIR, cas)
        if os.path.exists(filepath):
            success, msg = add_mermaid(filepath, config)
            status = "✓" if success else "○"
            print(f"{status} {cas}: {msg}")
        else:
            print(f"✗ {cas}: Fichier non trouvé")
    
    print("\n=== LOT 4 TERMINÉ ===")
