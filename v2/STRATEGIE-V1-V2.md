# Stratégie V1 + V2 — Complémentarité

**Principe** : V1 = richesse documentaire | V2 = opérationnel client

---

## 🎯 Positionnement

| Aspect | V1 (Stable) | V2 (Opérationnel) |
|:-------|:------------|:------------------|
| **Usage** | Référence complète | Mission client |
| **Public** | Expert, chercheur, régulateur | Consultant, praticien |
| **Format** | Longs documents, analyses profondes | Templates, checklists, CLI |
| **Langue** | Français (200 pages 😄) | Bilingue FR/EN possible |
| **Mise à jour** | Stable, corrections uniquement | Itératif, agile |

---

## 📚 V1 comme Source de Contenu V2

### Mapping Enrichissement

| Document V1 | Extraction V2 | Usage Client |
|:------------|:--------------|:-------------|
| `11.6-dictionnaire-risques-cycle-vie.md` (OWASP ASI 2026) | → `references/risk-dictionary/` | Référence risques par phase |
| `11.7-dictionnaire-risques-par-metier.md` (12 secteurs) | → `training/cases/` | Cas sectoriels |
| `11.5-mapping-ai-act.md` (EBIOS/AI Act/ISO 42001) | → `references/mapping-normatif.md` | Argumentaire conformité |
| `90-DEPLOYMENT/ROADMAP-30-60-90.md` (détaillé) | → `methodology/deployment/playbooks/` | Plans de mission |
| `99-REGISTRE/registre-sia-V2.yaml` (exemples riches) | → `registry/examples.yaml` | Démonstration |

### Processus d'Extraction

```
V1 (Source riche)
    │
    ├──► Analyse : Quel contenu réutilisable ?
    │
    ├──► Synthèse : Extraire l'essentiel
    │
    ├──► Adaptation : Format opérationnel
    │
    └──► V2 (Livrable client)
```

---

## 🎭 Scénarios d'Usage

### Scénario 1 : Mission Consulting Standard

```
Client : "On veut se conformer à l'AI Act"
    │
    ├──► V2 : Atelier express (2h) → 10 usages identifiés
    │
    ├──► V2 : Qualification L1/L2/L3 → Registre créé
    │
    └──► V1 : Si besoin de justification réglementaire profonde
         (ex: "Pourquoi l'exception Art. 6(3) s'applique")
```

### Scénario 2 : Mission Haute Conformité

```
Client : "L'autorité de régulation nous surveille"
    │
    ├──► V2 : Audit rapide des usages existants
    │
    ├──► V1 : Analyse approfondie (200 pages de référence)
    │
    └──► Livrable : Dossier complet V1 + Synthèse V2
```

### Scénario 3 : Formation Équipe

```
Client : "Formez nos équipes"
    │
    ├──► V2 : Atelier pratique (cas réels, templates)
    │
    ├──► V1 : Lecture préparatoire (pour les volontaires)
    │
    └──► Certification : Quiz sur V2 + Référence V1
```

---

## 📖 Produits Dérivés V1 → V2

### 1. Livre Blanc "EBIOS-RM IA" (V1 comme base)

| Chapitre | Source V1 | Adaptation V2 |
|:---------|:----------|:--------------|
| Introduction méthodologique | `00.1-methodologie-de-base.md` | Executive summary 2 pages |
| Analyse risques par phase | `11.6-dictionnaire-risques-cycle-vie.md` | Checklist 1 page |
| Cas sectoriels | `11.7-dictionnaire-risques-par-metier.md` | 12 fiches A4 |
| Conformité réglementaire | `11.5-mapping-ai-act.md` | Matrice 1 page |

### 2. Formation Certifiante

| Niveau | Contenu | Source |
|:-------|:--------|:-------|
| Fondamentaux | 1 jour | V2 uniquement |
| Avancé | 2 jours | V2 + extraits V1 |
| Expert | 3 jours | V2 + V1 complète |

### 3. Offre Consulting

| Offre | V1 | V2 | Prix |
|:------|:---|:---|:-----|
| Express | — | ✅ | €3-5K |
| Standard | Référence | ✅ | €8-12K |
| Premium | ✅ Analyse | ✅ Implémentation | €25-40K |
| Audit | ✅ Complet | ✅ Synthèse | €15-25K |

---

## 🔄 Maintenance Parallèle

### V1 — Mode "Référence Stable"

```yaml
update_policy:
  frequency: "Annual"
  type: "Corrections only"
  trigger:
    - "Changement réglementaire majeur (AI Act amendement)"
    - "Nouvelle norme ISO (42002, etc.)"
    - "Retour critique terrain"
```

### V2 — Mode "Itératif Agile"

```yaml
update_policy:
  frequency: "Monthly"
  type: "Features + fixes"
  trigger:
    - "Retour bêta-testeurs"
    - "Nouveau cas client"
    - "Amélioration outils"
```

---

## 🎨 Communication Client

### Message Clé

> **"V1 = la thèse, V2 = le kit de survie"**
> 
> — Vous avez besoin des deux, mais pas en même temps.

### Analogie

| V1 | V2 |
|:---|:---|
| Encyclopédie médicale | Trousse de premiers secours |
| Code civil complet | Guide du droit du travail |
| Manuel technique 500 pages | Quick start guide |

---

## 📊 Métriques de Succès

| Métrique | V1 | V2 |
|:---------|:---|:---|
| Téléchargements | Référence académique | Utilisation active |
| Citations | Publications, mémoires | Rapports clients |
| Contributions | Experts, régulateurs | Consultants, praticiens |
| Longévité | Archive pérenne | Version courante |

---

## ✅ Recommandation

**Ne pas fusionner V1 et V2** — les garder comme deux produits distincts :

```
┌─────────────────────────────────────────┐
│           EBIOS-RM IA                   │
│           (Marque globale)              │
├─────────────────────┬───────────────────┤
│      V1 REFERENCE   │    V2 OPERATIONEL │
│                     │                   │
│  • Riche (200p)     │  • Concis (20p)   │
│  • Français         │  • FR/EN          │
│  • Expert           │  • Praticien      │
│  • Stable           │  • Agile          │
│                     │                   │
│  Usage: Justifier   │  Usage: Faire     │
│  Convaincre         │  Délivrer         │
└─────────────────────┴───────────────────┘
```

---

*Stratégie V1+V2 — Capitaliser sur la richesse française* 😄
