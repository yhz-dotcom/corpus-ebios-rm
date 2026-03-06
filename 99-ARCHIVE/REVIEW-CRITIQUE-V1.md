# 🔍 REVUE CRITIQUE — Corpus EBIOS-RM IA "Usage-First"

**Date** : 06/03/2026  
**Relecteur** : Kimi Claw  
**Objectif** : Identifier angles morts, faiblesses et proposer plan d'action refonte

---

## 1. SYNTHÈSE EXÉCUTIVE

| Aspect | Évaluation | Score /10 |
|:-------|:-----------|:----------|
| **Complétude méthodologique** | Très bon | 8/10 |
| **Opérabilité** | Moyen à bon | 6/10 |
| **Cohérence transversale** | Moyen | 5/10 |
| **Maintenabilité** | Faible à moyen | 4/10 |
| **Adoption facilitée** | Moyen | 5/10 |

**Verdict** : Le corpus est **riche en contenu** mais **fragile en structure**. Il risque l'obsolescence rapide sans refonte architecturale.

---

## 2. ANGLES MORTS IDENTIFIÉS

### 🔴 CRITIQUE — Risque d'échec déploiement

#### 2.1 Absence de Versioning Sémantique Coherent

| Problème | Impact |
|:---------|:-------|
| V1 vs V2 du qualifier coexistent sans stratégie de convergence | Confusion utilisateur, maintenance double |
| Registre V1 et V2 sans migration path | Données fragmentées, incohérences |
| Documents en v1.0, 2.0-beta, brouillon | Pas de maturité claire |

**Exemple concret** : Un utilisateur doit choisir entre :
- `00.2-usage-first-qualifier.md` (V1)
- `00.2-usage-first-qualifier-V2.md` (V2-beta)
- Sans guide de choix explicite

#### 2.2 Manque de Données de Validation Terrain

| Manque | Conséquence |
|:-------|:------------|
| Aucun retour d'expérience réel intégré | Templates théoriques, pas éprouvés |
| Pas de métriques d'usage des templates | On ne sait pas ce qui marche |
| Exemples fictifs uniquement (DiagnoAI) | Pas de crédibilité terrain |

#### 2.3 Gouvernance des Versions Non Définie

- Qui décide du passage V1 → V2 ?
- Comment gérer les breaking changes ?
- Quelle fréquence de release ?

---

### 🟡 MAJEUR — Risque d'adoption difficile

#### 2.4 Fracture Entre "Méthodologie" et "Opérationnel"

| Côté Méthodo | Côté Opérationnel | Écart |
|:-------------|:------------------|:------|
| Grille 5 min | Ateliers 2h-1j | Pas de pont |
| Templates YAML | Fiches markdown | Formats divergents |
| Roadmap 90 jours | Pas de playbook jour J | Trop abstrait |

#### 2.5 Absence de Matériel de Formation "Clé en Main"

| Manquant | Besoin réel |
|:---------|:------------|
| Slide deck facilitateur | Pour vendre la démarche |
| Vidéo 5 min "première qualification" | Pour réduire friction |
| Cheat sheet A4 laminée | Pour les ateliers |
| Exemples avant/après | Pour comprendre l'intérêt |

#### 2.6 Intégration Technique Fragile

| Problème | Détail |
|:---------|:-------|
| Script Python basique | Pas de tests, pas de CI/CD |
| Pas d'API registre | Impossible d'intégrer aux outils existants |
| Validation YAML manuelle | Risque d'erreurs de syntaxe |

---

### 🟢 MINEUR — Risque de friction

#### 2.7 Cohérence Terminologique

| Terme | Usage 1 | Usage 2 | Problème |
|:------|:--------|:--------|:---------|
| "Usage" | Qualifier | Registre | Parfois "système", parfois "usage" |
| "Niveau" | EBIOS | Qualification | 🟢/🟡/🔴 vs Light/Standard/Renforcé |
| "Fiche" | Light | Standard | Formats très différents |

#### 2.8 Redondances Documentaires

| Redondance | Localisation |
|:-----------|:-------------|
| Définitions EBIOS | 00.1 + 01 + 02 + 03 |
| Processus qualification | Qualifier + Roadmap |
| Exigences AI Act | Mapping + Templates + Registre |

---

## 3. FAIBLESSES STRUCTURELLES

### 3.1 Architecture de l'Information

```
Problème : Arborescence profonde et fragmentée

00-METHODOLOGIE/
├── 10-PROCESSUS/          ← Pourquoi 10- ?
├── 20-OUTILS/
│   └── templates/         ← Pas de versionning
├── 30-REFERENCES/
└── 90-DEPLOYMENT/         ← Écart numérique étrange

11-SIA/                    ← Numérotation arbitraire
├── 11.2-sources-risque    ← Pas cohérent avec 00-
├── 11.3-scenarios
└── ...

99-REGISTRE/               ← Pourquoi 99 ?
99-ARCHIVE/                ← Même numéro ?
```

**Proposition** : Numérotation sémantique par domaine

### 3.2 Gestion des Dépendances

| Dépendance | État |
|:-----------|:-----|
| Template → Registre | Champ `fiche_reference` peuplé manuellement |
| Qualifier → Template | Pas de lien automatique |
| Roadmap → Outils | Pas de checklist d'outillage |

### 3.3 Évolutivité

| Scénario | Capacité actuelle |
|:-----------|:------------------|
| 100+ usages | Registre YAML devient illisible |
| Multi-sites | Pas de gestion de périmètre géo |
| Équipes distribuées | Pas de workflow validation async |

---

## 4. ANALYSE PAR COMPOSANT

### 4.1 Usage-Qualifier (V1 et V2)

| Force | Faiblesse |
|:------|:----------|
| Rapide (5 min) | V1 et V2 coexistent sans stratégie |
| 5 questions claires | Q3bis "Réversibilité" mal placée |
| Format YAML | Pas de validation schéma |

**Recommandation** : Fusionner V1 et V2 en une seule version avec modes "Express" / "Détaillé"

### 4.2 Templates EBIOS (Light/Standard/Renforcé)

| Force | Faiblesse |
|:------|:----------|
| 3 niveaux adaptés | Pas de continuité entre niveaux |
| Format markdown | Pas de rendu PDF/HTML |
| Timeboxés | Durées théoriques non validées |

**Recommandation** : Créer une "fiche intermédiaire" pour les cas limites 🟡/🔴

### 4.3 Registre SIA (V1 et V2)

| Force | Faiblesse |
|:------|:----------|
| Structure riche (V2) | Trop complexe pour démarrage |
| 4 exemples | Pas de cas "vrai" anonymisé |
| Script export | Pas d'import, pas de sync |

**Recommandation** : V1 = MVP démarrage, V2 = production, avec migration documentée

### 4.4 Roadmap 30-60-90

| Force | Faiblesse |
|:------|:----------|
| Très détaillée | Trop dense pour lecture rapide |
| 12 semaines planifiées | Pas de plan B si retard |
| Livrables clairs | Pas de templates associés |

**Recommandation** : Créer un "Executive Summary" 2 pages + détails annexés

---

## 5. PLAN D'ACTION — REFONTE V2.0

### Phase 1 : Fondation (Sprint 1-2)

| Action | Priorité | Livrable |
|:-------|:---------|:---------|
| Définir stratégie versioning | 🔴 Critique | ADR-001 : Stratégie versions |
| Fusionner V1/V2 qualifier | 🔴 Critique | `usage-qualifier-v2.0.md` unique |
| Créer schéma JSON registre | 🔴 Critique | `schema-registre-v2.json` |
| Valider arborescence | 🟡 Majeur | Nouvelle structure validée |

### Phase 2 : Cœur (Sprint 3-4)

| Action | Priorité | Livrable |
|:-------|:---------|:---------|
| Refondre registre avec schéma | 🔴 Critique | `registre-sia-v2.0.yaml` |
| Créer validateur CLI | 🟡 Majeur | `sia-validator` (Python/Go) |
| Harmoniser templates | 🟡 Majeur | Templates avec sections communes |
| Ajouter tests unitaires | 🟡 Majeur | Suite de tests > 80% coverage |

### Phase 3 : Adoption (Sprint 5-6)

| Action | Priorité | Livrable |
|:-------|:---------|:---------|
| Créer kit facilitateur | 🟡 Majeur | Slide deck + vidéo + cheat sheet |
| Documenter 3 cas réels (anonymisés) | 🟡 Majeur | `cas-reels/` avec avant/après |
| Créer API REST simple | 🟢 Mineur | `api-registre/` (FastAPI) |
| Intégration Notion/Confluence | 🟢 Mineur | Connecteurs documentés |

### Phase 4 : Production (Sprint 7-8)

| Action | Priorité | Livrable |
|:-------|:---------|:---------|
| Pilotage avec 2-3 bêta-testeurs | 🔴 Critique | Retours intégrés |
| Documentation migration V1→V2 | 🟡 Majeur | `MIGRATION.md` |
| Release v2.0.0 | 🔴 Critique | Tag GitHub + changelog |
| Formation interne équipe | 🟡 Majeur | Session 2h équipe projet |

---

## 6. ARCHITECTURE CIBLE V2.0

```
corpus-ebios-rm-v2/
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

## 7. RECOMMANDATIONS IMMÉDIATES

### À faire cette semaine

1. **Geler les ajouts de contenu** — Focus sur structure
2. **Créer ADR-001** — Architecture Decision Record pour versioning
3. **Identifier 2-3 bêta-testeurs** — Pour validation terrain
4. **Prioriser les 5 actions critiques** — Voir Phase 1

### À ne PAS faire

1. ❌ Ne pas créer de V3 du qualifier
2. ❌ Ne pas ajouter de nouveaux exemples fictifs
3. ❌ Ne pas complexifier le registre V2
4. ❌ Ne pas ignorer la dette technique du script Python

---

## 8. MÉTRIQUES DE SUCCÈS DE LA REFONTE

| Métrique | Cible V2.0 |
|:---------|:-----------|
| Temps pour première qualification | < 10 min |
| Taux d'erreur registre (validation) | < 5% |
| Satisfaction facilitateur (test) | ≥ 8/10 |
| Adoption bêta (3 mois) | ≥ 2 organisations pilotes |
| Documentation / Code ratio | ≥ 3:1 |

---

## 9. CONCLUSION

Le corpus EBIOS-RM IA "Usage-First" est une **base solide mais mal structurée**. Le risque principal n'est pas le contenu — qui est de qualité — mais la **fragmentation et l'absence de stratégie de convergence**.

**La refonte V2.0 doit prioriser** :
1. **Unification** (V1/V2 → une seule version)
2. **Validation** (schémas, tests, bêta)
3. **Adoption** (formation, matériel, cas réels)

**Budget estimé** : 2-3 sprints (8-12 semaines) à 50% temps  
**ROI attendu** : Corpus maintenable, adoptable, et crédible pour déploiement client

---

*Revue critique réalisée le 06/03/2026*  
*Prochaine revue prévue après Phase 1 de refonte*

---

> 💡 **Note pour l'utilisateur** : Cette review est conçue pour être actionnable. Chaque point critique a une recommandation associée. Le plan d'action est priorisé par risque et valeur.
