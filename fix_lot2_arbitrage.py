#!/usr/bin/env python3
"""
Correction systématique Lot 2: Arbitrage Fix/Pivot/Kill
"""

import os
import re

CORPUS_DIR = "/tmp/corpus-ebios-rm/v2/analyses"

# Template d'arbitrage
ARBITRAGE_TEMPLATE = """

---

## ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | {fix} | ✅ **CHOISIR** |
| PIVOT | {pivot} | ⚠️ Possible mais {pivot_risk} |
| KILL | Arrêt du système | {kill_rec} |

"""

# Cas sans arbitrage avec descriptions spécifiques
CAS_ARBITRAGE = {
    "ebios-analysis-aegisdrone.md": {
        "fix": "Supervision humaine renforcée + chaîne de commandement",
        "pivot": "Système d'aide à la décision sans autonomie",
        "pivot_risk": "perte de réactivité militaire",
        "kill_rec": "⚠️ Envisageable si éthique incompatible"
    },
    "ebios-analysis-agriopti.md": {
        "fix": "Audit biais + validation agronome + transparence",
        "pivot": "Recommandation sans prescription automatique",
        "pivot_risk": "perte d'efficacité",
        "kill_rec": "❌ Trop préjudiciable (agriculture)"
    },
    "ebios-analysis-edumood.md": {
        "fix": "Suppression surveillance émotionnelle + consentement",
        "pivot": "Outil pédagogique sans tracking émotionnel",
        "pivot_risk": "perte de personnalisation",
        "kill_rec": "⚠️ Envisageable si surveillance confirmée"
    },
    "ebios-analysis-forceselect.md": {
        "fix": "Séparation civil/militaire + supervision éthique",
        "pivot": "Système uniquement civil",
        "pivot_risk": "perte de marché défense",
        "kill_rec": "⚠️ Envisageable si dual-use non résolu"
    },
    "ebios-analysis-gridsmart.md": {
        "fix": "Robustesse modèles + redondance + supervision",
        "pivot": "Optimisation sans ML critique",
        "pivot_risk": "perte d'efficacité",
        "kill_rec": "❌ Trop préjudiciable (énergie)"
    },
    "ebios-analysis-hybridrecruit.md": {
        "fix": "Séparation entités + audit discrimination",
        "pivot": "Système civil uniquement",
        "pivot_risk": "perte de contrat militaire",
        "kill_rec": "⚠️ Envisageable si séparation impossible"
    },
    "ebios-analysis-mediagen.md": {
        "fix": "Étiquetage contenu IA + transparence",
        "pivot": "Outil assisté sans génération automatique",
        "pivot_risk": "perte d'efficacité",
        "kill_rec": "❌ Trop préjudiciable (médias)"
    },
    "ebios-analysis-milselect.md": {
        "fix": "Séparation civil/militaire + supervision",
        "pivot": "Système civil uniquement",
        "pivot_risk": "perte de marché défense",
        "kill_rec": "⚠️ Envisageable si dual-use confirmé"
    },
    "ebios-analysis-neuroboost.md": {
        "fix": "Consentement éclairé + supervision médicale",
        "pivot": "Recherche uniquement sans application",
        "pivot_risk": "perte de commercialisation",
        "kill_rec": "⚠️ Envisageable si risques neuro non maîtrisés"
    },
    "ebios-analysis-optirecrut.md": {
        "fix": "Audit biais + transparence + recours",
        "pivot": "Anonymisation complète CV",
        "pivot_risk": "perte de personnalisation",
        "kill_rec": "❌ Trop préjudiciable (RH)"
    },
    "ebios-analysis-scorelife.md": {
        "fix": "Impossible — scoring social interdit",
        "pivot": "N/A",
        "pivot_risk": "N/A",
        "kill_rec": "✅ **OBLIGATOIRE** — Arrêt immédiat"
    },
    "ebios-analysis-surveileye.md": {
        "fix": "Impossible — reconnaissance faciale interdite",
        "pivot": "N/A",
        "pivot_risk": "N/A",
        "kill_rec": "✅ **OBLIGATOIRE** — Arrêt immédiat"
    },
    "ebios-analysis-terravox.md": {
        "fix": "Suppression tracking vocal + consentement",
        "pivot": "Météo standard sans données agricoles",
        "pivot_risk": "perte de précision",
        "kill_rec": "⚠️ Envisageable si tracking non résolu"
    },
    "ebios-analysis-vitalpredict.md": {
        "fix": "Conformité MDR + supervision médicale",
        "pivot": "Aide au diagnostic sans décision",
        "pivot_risk": "perte d'autonomie",
        "kill_rec": "❌ Trop préjudiciable (santé)"
    },
    "ebios-analysis-workvibe.md": {
        "fix": "Suppression surveillance émotionnelle",
        "pivot": "Feedback anonyme sans tracking",
        "pivot_risk": "perte de personnalisation",
        "kill_rec": "⚠️ Envisageable si surveillance confirmée"
    },
}

def add_arbitrage(filepath, config):
    """Ajoute section arbitrage"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'ARBITRAGE FIX' in content or 'Fix / Pivot / Kill' in content:
        return False, "Déjà présent"
    
    # Chercher "## CONCLUSION"
    match = re.search(r"\n## \d+\. CONCLUSION", content)
    if match:
        arbitrage = ARBITRAGE_TEMPLATE.format(**config)
        pos = match.start()
        content = content[:pos] + arbitrage + content[pos:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Ajouté"
    
    return False, "Pattern CONCLUSION non trouvé"

if __name__ == "__main__":
    print("=== CORRECTION LOT 2: ARBITRAGE FIX/PIVOT/KILL ===\n")
    
    for cas, config in CAS_ARBITRAGE.items():
        filepath = os.path.join(CORPUS_DIR, cas)
        if os.path.exists(filepath):
            success, msg = add_arbitrage(filepath, config)
            status = "✓" if success else "○"
            print(f"{status} {cas}: {msg}")
        else:
            print(f"✗ {cas}: Fichier non trouvé")
    
    print("\n=== LOT 2 TERMINÉ ===")
