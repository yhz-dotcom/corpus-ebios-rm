#!/usr/bin/env python3
"""
Correction Lot 6: Arbitrages restants (cas complexes)
"""

import os
import re

CORPUS_DIR = "/tmp/corpus-ebios-rm/v2/analyses"

# Cas restants sans arbitrage - approche manuelle
CAS_ARBITRAGE_RESTANTS = {
    "ebios-analysis-audiencedna.md": """

---

## ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Suppression ciblage émotionnel enfants + consentement parental | ✅ **CHOISIR** |
| PIVOT | Publicité contextuelle sans profilage comportemental | ⚠️ Possible mais perte de rentabilité |
| KILL | Arrêt AudienceDNA | ⚠️ **ENVISAGEABLE** si protection enfants non résolue |

""",
    "ebios-analysis-climatoracle.md": """

---

## ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Prédiction probabiliste avec incertitudes + supervision scientifique | ✅ **CHOISIR** |
| PIVOT | Recherche climatique sans application publique directe | ⚠️ Possible mais perte d'impact |
| KILL | Arrêt CLIMAT-ORACLE | ⚠️ **ENVISAGEABLE** si panique sociale confirmée |

""",
    "ebios-analysis-climatoracle-incidents.md": """

---

## ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| FIX | Voir rapport principal climatoracle.md | — |
| PIVOT | — | — |
| KILL | — | — |

""",
    "ebios-analysis-echomorph.md": """

---

## ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Suppression manipulation subliminale + étiquetage contenu IA | ✅ **CHOISIR** |
| PIVOT | Outil créatif assisté sans génération autonome | ⚠️ Possible mais perte d'efficacité |
| KILL | Arrêt ECHO-MORPH | 🚫 **OBLIGATOIRE** — Art. 5(1)(a) subliminal interdit |

""",
    "ebios-analysis-helios.md": """

---

## ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Robustesse modèles + redondance + supervision humaine | ✅ **CHOISIR** |
| PIVOT | Gestion solaire sans ML critique | ⚠️ Possible mais perte d'optimisation |
| KILL | Arrêt HELIOS-GRID | ❌ Trop préjudiciable (transition énergétique) |

""",
    "ebios-analysis-helios-incidents.md": """

---

## ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| FIX | Voir rapport principal helios.md | — |
| PIVOT | — | — |
| KILL | — | — |

""",
    "ebios-analysis-hybridrecruit.md": """

---

## ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Séparation entités civil/militaire + audit discrimination | ✅ **CHOISIR** |
| PIVOT | Système recrutement civil uniquement | ⚠️ Possible mais perte contrat défense |
| KILL | Arrêt HybridRecruit | ⚠️ **ENVISAGEABLE** si dual-use non résoluble |

""",
    "ebios-analysis-optirecrut.md": """

---

## ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Anonymisation CV + audit biais + transparence | ✅ **CHOISIR** |
| PIVOT | Recrutement traditionnel sans IA | ⚠️ Possible mais perte d'efficacité |
| KILL | Arrêt OptiRecrut | ❌ Trop préjudiciable (RH) |

""",
    "ebios-analysis-psycholoot-incidents.md": """

---

## ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| FIX | Voir rapport principal psycholoot.md | — |
| PIVOT | — | — |
| KILL | — | — |

""",
    "ebios-analysis-vitalpredict.md": """

---

## ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Conformité MDR + supervision médicale + transparence | ✅ **CHOISIR** |
| PIVOT | Aide au diagnostic sans prédiction autonome | ⚠️ Possible mais perte d'autonomie |
| KILL | Arrêt VitalPredict | ❌ Trop préjudiciable (santé publique) |

""",
}

def add_arbitrage_simple(filepath, content_to_add):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'ARBITRAGE FIX' in content or 'Fix / Pivot / Kill' in content:
        return False, "Déjà présent"
    
    # Insérer avant CONCLUSION
    match = re.search(r"\n## \d+\. CONCLUSION", content)
    if match:
        pos = match.start()
        content = content[:pos] + content_to_add + content[pos:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Ajouté"
    
    return False, "Pattern CONCLUSION non trouvé"

if __name__ == "__main__":
    print("=== CORRECTION LOT 6: ARBITRAGES RESTANTS ===\n")
    
    for cas, arbitrage_content in CAS_ARBITRAGE_RESTANTS.items():
        filepath = os.path.join(CORPUS_DIR, cas)
        if os.path.exists(filepath):
            success, msg = add_arbitrage_simple(filepath, arbitrage_content)
            status = "✓" if success else "○"
            print(f"{status} {cas}: {msg}")
        else:
            print(f"✗ {cas}: Fichier non trouvé")
    
    print("\n=== LOT 6 TERMINÉ ===")
