#!/usr/bin/env python3
"""
Correction Lot 3: Diagrammes Mermaid
"""

import os
import re

CORPUS_DIR = "/tmp/corpus-ebios-rm/v2/analyses"

# Templates Mermaid par catégorie
MERMAID_TEMPLATES = {
    "education": """
```mermaid
flowchart TB
    C1[Déploiement {system}<br/>{context}]
    --
    B1[Biais {bias_type}<br/>+ {secondary_risk}]
    --
    D1[Discrimination systémique<br/>{impact_group} = désavantagés<br/>+ {consequence}]
    --
    M1[Scandale "{scandal_title}"<br/>+ Médias + {authorities}<br/>+ Manifestations]
    --
    I1[Interdiction système<br/>Poursuites {company}<br/>Réforme {regulation}]
    --
    F1[Faillite {company}<br/>Retour {alternative}<br/>{final_impact}]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style B1 fill:#fff3e0,stroke:#ef6c00
    style D1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```
""",
    "default": """
```mermaid
flowchart TB
    C1[Déploiement {system}<br/>{context}]
    --
    R1[{risk_type}<br/>+ {secondary_risk}]
    --
    C2[Crise {crisis_type}<br/>{impact_detail}]
    --
    M1[Scandale "{scandal_title}"<br/>+ Médias + {authorities}]
    --
    I1[{sanction_type}<br/>Poursuites {company}<br/>{regulatory_action}]
    --
    F1[Faillite {company}<br/>{final_impact}]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style R1 fill:#fff3e0,stroke:#ef6c00
    style C2 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```
"""
}

# Configurations spécifiques par cas
CAS_MERMAID = {
    "ebios-analysis-cognia.md": {
        "template": "education",
        "system": "Cognia",
        "context": "Systèmes éducatifs EU",
        "bias_type": "socio-économique",
        "secondary_risk": "Déterminisme social",
        "impact_group": "Élèves défavorisés",
        "consequence": "Orientation filières pro",
        "scandal_title": "L'IA détermine l'avenir des enfants",
        "authorities": "Ministères + CNIL",
        "company": "Cognia",
        "regulation": "éducation nationale",
        "alternative": "orientation humaine",
        "final_impact": "Perte confiance éducation IA"
    },
    "ebios-analysis-edumood.md": {
        "template": "education", 
        "system": "EduMood AI",
        "context": "Surveillance émotionnelle écoles",
        "bias_type": "surveillance",
        "secondary_risk": "Profilage émotionnel",
        "impact_group": "Enfants",
        "consequence": "Autocensure + Anxiété",
        "scandal_title": "L'IA surveille les émotions de nos enfants",
        "authorities": "Protecteur Enfance + CNIL",
        "company": "EduTech",
        "regulation": "protection enfance",
        "alternative": "pédagogie sans tracking",
        "final_impact": "Crise confiance école"
    },
    "ebios-analysis-neuroboost.md": {
        "template": "default",
        "system": "NEURO-BOOST",
        "context": "Neurotechnologie militaire",
        "risk_type": "Enhancement cognitif",
        "secondary_risk": "Armes autonomes",
        "crisis_type": "éthique",
        "impact_detail": "Soldats augmentés + Dilemmes moraux",
        "scandal_title": "L'armée crée des super-soldats",
        "authorities": "Parlement + CNDP",
        "sanction_type": "Interdiction neuro-militaire",
        "company": "NeuroDef",
        "regulatory_action": "Traité neuro-éthique",
        "final_impact": "Moratoire neurotechnologie"
    },
    "ebios-analysis-newsrank.md": {
        "template": "default",
        "system": "NewsRank",
        "context": "Algorithmes information",
        "risk_type": "Censure algorithmique",
        "secondary_risk": "Polarisation",
        "crisis_type": "démocratique",
        "impact_detail": "Information filtrée + Désinformation",
        "scandal_title": "L'IA décide ce que nous lisons",
        "authorities": "Médias + Commission EU",
        "sanction_type": "Intervention régulateur",
        "company": "NewsAI",
        "regulatory_action": "DSA + AI Act",
        "final_impact": "Régulation algorithmes info"
    },
}

def add_mermaid(filepath, config):
    """Ajoute diagramme Mermaid"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '```mermaid' in content:
        return False, "Déjà présent"
    
    template = MERMAID_TEMPLATES.get(config["template"], MERMAID_TEMPLATES["default"])
    diagram = template.format(**config)
    
    # Insérer avant "## PLAN DE TRAITEMENT" ou "## CONCLUSION"
    match = re.search(r"\n## \d+\. (PLAN DE TRAITEMENT|CONCLUSION)", content)
    if match:
        pos = match.start()
        content = content[:pos] + diagram + "\n" + content[pos:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Ajouté"
    
    return False, "Pattern non trouvé"

if __name__ == "__main__":
    print("=== CORRECTION LOT 3: DIAGRAMMES MERMAID ===\n")
    
    for cas, config in CAS_MERMAID.items():
        filepath = os.path.join(CORPUS_DIR, cas)
        if os.path.exists(filepath):
            success, msg = add_mermaid(filepath, config)
            status = "✓" if success else "○"
            print(f"{status} {cas}: {msg}")
        else:
            print(f"✗ {cas}: Fichier non trouvé")
    
    print("\n=== LOT 3 TERMINÉ ===")
