# Corpus EBIOS-RM IA "Usage-First" — Version 2.0

**Statut** : En construction | **Base** : V1.0 stable dans `/` | **Cible** : `/v2/`

---

## 🎯 Objectif V2.0

Transformer le corpus riche mais fragmenté en une **méthodologie unifiée, validée et adoptable**.

| Aspect V1 | Amélioration V2 |
|:----------|:----------------|
| V1/V2 coexistent | Une seule version avec modes Express/Détaillé |
| Templates disparates | Structure harmonisée avec sections réutilisables |
| Registre YAML manuel | Schéma JSON + validation CLI |
| Exemples fictifs | Cas réels anonymisés |
| Pas de matériel formation | Kit facilitateur complet |

---

## 📁 Structure V2.0

```
v2/
├── README.md                    ← Vue d'ensemble + quickstart
├── CHANGELOG.md                 ← Versions et breaking changes
├── MIGRATION.md                 ← Guide V1 → V2
│
├── docs/                        ← Documentation utilisateur
│   ├── quickstart.md            ← 15 min pour qualifier
│   ├── methodology.md           ← Explication Usage-First
│   └── faq.md                   ← Questions fréquentes
│
├── methodology/                 ← Méthodologie (unique)
│   ├── qualifier/
│   │   ├── index.md             ← Grille unique (modes Express/Détaillé)
│   │   └── decision-tree.md     ← Arbre de décision
│   │
│   ├── levels/
│   │   ├── level-1-conversational.md   ← 🟢 (ex-Light)
│   │   ├── level-2-workflow.md         ← 🟡 (ex-Standard)
│   │   ├── level-3-decisional.md       ← 🔴 (ex-Renforcé)
│   │   └── level-2-3-boundary.md       ← ⭐ Cas limites
│   │
│   └── deployment/
│       ├── roadmap-90d.md       ← Executive summary
│       ├── roadmap-90d-detailed.md ← Détails complets
│       └── playbooks/           ← Playbooks par semaine
│
├── registry/                    ← Registre SIA
│   ├── schema.json              ← Schéma de validation
│   ├── registry.yaml            ← Registre principal
│   ├── examples/                ← Exemples validés
│   │   ├── example-1-rh.yaml
│   │   ├── example-2-finance.yaml
│   │   └── example-3-poc.yaml
│   └── exports/                 ← Exports générés
│
├── templates/                   ← Templates harmonisés
│   ├── template-level-1.md
│   ├── template-level-2.md
│   ├── template-level-3.md
│   └── sections/                ← Sections réutilisables
│       ├── header.md
│       ├── risk-assessment.md
│       └── validation.md
│
├── tools/                       ← Outils
│   ├── cli/                     ← CLI Python
│   │   ├── validator.py
│   │   ├── exporter.py
│   │   └── tests/
│   ├── api/                     ← API REST (optionnel)
│   └── integrations/            ← Connecteurs
│
├── training/                    ← Matériel formation
│   ├── slides/                  ← Deck facilitateur
│   ├── videos/                  ← Vidéos courtes
│   ├── cheatsheets/             ← A4 laminables
│   └── cases/                   ← Cas réels anonymisés
│
└── references/                  ← Références normatives
    ├── mapping-ai-act.md
    ├── risk-dictionary/
    └── bibliography.md
```

---

## 🗺️ Mapping V1 → V2

| Fichier V1 | Destination V2 | Statut |
|:-----------|:---------------|:-------|
| `00.2-usage-first-qualifier.md` | `methodology/qualifier/index.md` | 🟡 À adapter |
| `00.2-usage-first-qualifier-V2.md` | Fusionné dans `qualifier/index.md` | 🔴 À fusionner |
| `01-EBIOS-LIGHT.md` | `methodology/levels/level-1-conversational.md` | 🟡 À adapter |
| `02-EBIOS-STANDARD.md` | `methodology/levels/level-2-workflow.md` | 🟡 À adapter |
| `03-EBIOS-RENFORCE.md` | `methodology/levels/level-3-decisional.md` | 🟡 À adapter |
| `04-arbre-decision.md` | `methodology/qualifier/decision-tree.md` | 🟢 Direct |
| `90-DEPLOYMENT/ROADMAP-30-60-90.md` | `methodology/deployment/roadmap-90d-detailed.md` | 🟡 À adapter |
| `99-REGISTRE/registre-sia.yaml` | `registry/registry.yaml` | 🟡 À migrer |
| `99-REGISTRE/registre-sia-V2.yaml` | `registry/registry.yaml` | 🔴 À fusionner |
| `11-SIA/11.*-*.md` | `references/` | 🟡 À réorganiser |

Légende :
- 🟢 Direct : Copie sans modification
- 🟡 À adapter : Restructuration nécessaire
- 🔴 À fusionner : Consolidation V1+V2

---

## 🚀 Démarrage Rapide

```bash
# 1. Cloner le corpus
git clone https://github.com/yhz-dotcom/corpus-ebios-rm.git
cd corpus-ebios-rm/v2

# 2. Lire le quickstart
cat docs/quickstart.md

# 3. Première qualification
python tools/cli/qualifier.py --mode express

# 4. Valider le registre
python tools/cli/validator.py registry/registry.yaml
```

---

## 📊 Progression Construction V2.0

| Module | Statut | Priorité |
|:-------|:-------|:---------|
| Documentation (docs/) | 🚧 En cours | 🔴 Haute |
| Méthodologie (methodology/) | 🚧 En cours | 🔴 Haute |
| Registre (registry/) | 📋 Planifié | 🔴 Haute |
| Templates (templates/) | 📋 Planifié | 🟡 Moyenne |
| Outils (tools/) | 📋 Planifié | 🟡 Moyenne |
| Formation (training/) | 📋 Planifié | 🟢 Basse |
| Références (references/) | 🚧 En cours | 🟡 Moyenne |

Légende :
- ✅ Terminé
- 🚧 En cours
- 📋 Planifié
- ⏸️ En attente

---

## 🔄 Compatibilité V1

La V1 reste **pleinement fonctionnelle** dans la racine du repository. La V2 est construite en parallèle sans casser l'existant.

```
corpus-ebios-rm/
├── 00-METHODOLOGIE/        ← V1 stable
├── 11-SIA/                 ← V1 stable
├── 99-REGISTRE/            ← V1 stable
├── 99-ARCHIVE/             ← V1 stable
├── v2/                     ← 🆕 V2 en construction
│   ├── docs/
│   ├── methodology/
│   └── ...
└── README.md               ← Vue d'ensemble V1
```

---

## 📅 Feuille de Route V2.0

| Phase | Durée | Objectif |
|:------|:------|:---------|
| **Fondation** | S1-S2 | Structure, schéma, fusion V1/V2 |
| **Cœur** | S3-S4 | Registre, templates, CLI |
| **Adoption** | S5-S6 | Formation, cas réels, API |
| **Production** | S7-S8 | Bêta, migration, release |

---

## 🤝 Contribution

Voir `CONTRIBUTING.md` pour les guidelines de contribution à la V2.

---

**Version** : 2.0-alpha | **Dernière mise à jour** : 06/03/2026

---

> 💡 **Note** : Cette V2 est construite incrémentalement. Chaque fichier est validé avant intégration. La V1 reste la référence stable jusqu'à la release v2.0.0.
