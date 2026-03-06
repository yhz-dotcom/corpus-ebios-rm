# Programme Formation Certifiante EBIOS-RM IA — 3 Jours

**Référence** : EBIOS-CERT-3DAYS-001 | **Version** : 1.0 | **Date** : Mars 2026

---

## 🎯 Objectif Global

Former des **Experts EBIOS-RM IA** capables de conduire des analyses complètes, de la qualification express à la recommandation stratégique, sur tous types de systèmes (régulés, prohibited, criminels, militaires).

---

## 📋 Architecture du Programme

```
JOUR 1 — FONDAMENTAUX (7h)
├── Qualification et 3 Levels
├── Grille express et arbre de décision
├── Registry SIA et CLI
└── Certification Practitioner

JOUR 2 — APPROFONDISSEMENT (7h)
├── 5 Ateliers EBIOS complets
├── Cas réels sectoriels
├── Articulation réglementaire
└── Certification Professional

JOUR 3 — EXPERTISE (7h)
├── 7 Types de conclusions
├── Cas prohibited et criminels
├── Cas militaires et hors cadre
├── Synthèse et Certification Expert
```

---

## JOUR 1 — FONDAMENTAUX

### 9h00 — 9h30 : Introduction et Contexte (30 min)

- Enjeux réglementaires 2026 (AI Act, RGPD, ISO 42001)
- Méthode "Usage-First" : philosophie et proportionnalité
- Parcours 3 jours et certifications

### 9h30 — 11h00 : Module 1 — Qualification Express (1h30)

**Grille 5 questions** :
```yaml
Q1: Données/processus métier ? → Level 1 ou suite
Q2: Influence décision ? → Level 1 ou suite
Q3: Automatisé/fort impact ? → Level 2 ou 3
Q4: Annexe III AI Act ? → Level 3 si oui
Q5: Données sensibles ? → Level 3 si critiques
```

**Exercice** : 10 cas, classification en 15 min

### 11h00 — 11h15 : Pause

### 11h15 — 12h30 : Module 2 — Les 3 Levels (1h15)

| Level | Temps | Template | Processus |
|:---|:---|:---|:---|
| 🟢 Level 1 | 15 min | 1 page | Fiche light |
| 🟡 Level 2 | 2h | 3 pages | 5 ateliers allégés |
| 🔴 Level 3 | 1-2j | 10+ pages | EBIOS complet |

**Démonstration** : Remplissage template Level 1 en live

### 12h30 — 13h30 : Déjeuner

### 13h30 — 15h00 : Module 3 — Registry SIA et CLI (1h30)

**Structure YAML** :
```yaml
metadata:
  version: "2.0.0"
  last_update: "2026-03-06"

sia_entries:
  - sia_id: "SIA-XXX-001"
    identification: {...}
    technical: {...}
    usage: {...}
    assessment: {...}
```

**CLI** :
```bash
sia-cli qualify --mode express
sia-cli validate registry.yaml
sia-cli export --format csv
sia-cli dashboard
```

**Atelier pratique** : Créer 3 entrées registry, valider, exporter

### 15h00 — 15h15 : Pause

### 15h15 — 16h30 : Module 4 — Cas Pratiques Jour 1 (1h15)

**3 cas progressifs** :
1. Assistant rédaction (Level 1) — 20 min
2. Pré-sélection CV (Level 2) — 40 min
3. Scoring crédit (Level 3) — 40 min

### 16h30 — 17h00 : Certification Practitioner (30 min)

**QCM 30 questions** (20 min) :
- 10 qualification
- 10 levels
- 10 registry/CLI

**Barème** : 24/30 pour certification

---

## JOUR 2 — APPROFONDISSEMENT

### 9h00 — 9h15 : Bilan Jour 1 et Objectifs Jour 2 (15 min)

### 9h15 — 11h00 : Module 5 — Atelier 1 Cadrage (1h45)

**Objectif** : Définir périmètre et biens essentiels

| Élément | Méthode | Livrable |
|:---|:---|:---|
| Problème métier | Interview | Description |
| Décision déléguée | Matrice | Tableau décisions |
| Biens essentiels | Brainstorm | Liste priorisée |

**Cas pratique** : Cadrage système RAG documentaire

### 11h00 — 11h15 : Pause

### 11h15 — 13h00 : Module 6 — Ateliers 2 et 3 (1h45)

**Atelier 2 — Sources de Risque** :
- Risques IA spécifiques (hallucination, biais, injection, drift)
- Profils attaquants
- Vulnérabilités techniques

**Atelier 3 — Scénarios** :
- Structure : Déclencheur → Propagation → Impact
- Flowchart Mermaid
- Évaluation gravité/vraisemblance

**Exercice** : Scénario complet sur cas fourni

### 13h00 — 14h00 : Déjeuner

### 14h00 — 15h30 : Module 7 — Ateliers 4 et 5 (1h30)

**Atelier 4 — Traitement** :
- Mesures préventives, détectives, correctives
- HITL (Human-in-the-Loop)
- Monitoring et KPIs

**Atelier 5 — Feuille de Route** :
- Priorisation P0/P1/P2
- Budget réaliste (% CA)
- Gantt et jalons

### 15h30 — 15h45 : Pause

### 15h45 — 16h30 : Module 8 — Articulation Réglementaire (45 min)

| Réglement | Mapping EBIOS | Obligations |
|:---|:---|:---|
| AI Act | Classification, conformité | Templates |
| RGPD | AIPD, DPO, droits | Processus |
| ISO 42001 | Management IA | Audit |

### 16h30 — 17h00 : Certification Professional (30 min)

**QCM 30 questions** + **Cas pratique 1h** :
- Analyse complète système Level 2
- 5 ateliers, registry, plan traitement

**Barème** : 24/30 QCM + cas validé

---

## JOUR 3 — EXPERTISE

### 9h00 — 9h15 : Bilan Jour 2 et Enjeux Jour 3 (15 min)

### 9h15 — 11h00 : Module 9 — Les 7 Types de Conclusions (1h45)

| Type | Définition | Action | Exemple |
|:---|:---|:---|:---|
| 🟢 Conforme | Régulé, optimisable | Traitement | Assistant rédaction |
| 🟡 High-Risk Std | Régulé, gérable | Conformité | Recrutement |
| 🟡 High-Risk Crisis | Régulé, critique | Crisis mode | Santé incident |
| 🔴 Prohibited | Interdit AI Act | Arrêt | RBI public |
| ⚫ Criminel | Interdit + mort | Liquidation | Social scoring |
| ⚪ Exclu éthique | Hors AI Act | Correction | Militaire |
| ⚠️ Hors cadre moral | Hors AI Act, moral | Pivot | LAWS |
| 🔧 Hybride | Mix | Découpage | Civil+militaire |

**Arbre de décision** : Application sur 5 cas complexes

### 11h00 — 11h15 : Pause

### 11h15 — 13h00 : Module 10 — Cas Prohibited et Criminels (1h45)

**SurveilEye** (RBI public) :
- Interdiction Art. 5(1)(d)
- Aucune exception
- Arrêt immédiat, destruction données

**ScoreLife** (Social scoring) :
- Triple prohibition
- Suicide survenu
- Liquidation, défense pénale

**Exercice** : Rédiger conclusion "arrêt" et "liquidation"

### 13h00 — 14h00 : Déjeuner

### 14h00 — 15h30 : Module 11 — Cas Militaires et Hors Cadre (1h30)

**MilSelect** (Militaire pur) :
- Exclusion AI Act Art. 2(3)
- Mais RGPD + pénal + éthique
- Correction biais, pas arrêt

**AegisDrone** (LAWS) :
- Hors AI Act (militaire)
- DIH, crimes de guerre
- Débat moral, pivot ou abandon

**HybridRecruit** (Mix) :
- Prohibited + High-Risk + Exclu
- Découpage architectural obligatoire

### 15h30 — 15h45 : Pause

### 15h45 — 16h30 : Module 12 — Synthèse et Bonnes Pratiques (45 min)

**Protection du consultant** :
- Documentation systématique
- Avis écrits
- Refus missions illégales

**Communication client** :
- Dire "non" avec fermeté
- Proposer alternatives
- Gérer pression board

### 16h30 — 17h30 : Certification Expert (1h)

**Épreuve 1 — QCM** (30 min, 40 questions) :
- 10 types conclusions
- 10 prohibited/exclusions
- 10 protections juridiques
- 10 cas pratiques

**Épreuve 2 — Cas complexe** (4h, dont 30 min préparation) :
- Analyse complète système hybride ou prohibited
- 5 ateliers, conclusion, recommandation
- Défense oral devant jury

**Barème Expert** :
- QCM : 32/40
- Cas : Analyse complète, conclusion appropriée, défense convaincante

---

## 🎓 Certifications

| Jour | Certification | Validité | Prérequis |
|:---|:---|:---|:---|
| 1 | EBIOS-RM IA Practitioner | 2 ans | 24/30 QCM |
| 2 | EBIOS-RM IA Professional | 2 ans | 24/30 + cas validé |
| 3 | EBIOS-RM IA Expert | 2 ans | 32/40 + cas + oral |

**Renouvellement** : Formation 1 jour ou preuve 3 missions/an

---

## 📚 Supports

### Pour Participants
- Syllabus 100 pages
- Templates (Level 1/2/3, analysis, executive)
- Guide 5 types conclusions
- Cas d'étude (7 complets)
- Arbre décision A4 plastifié
- Certificats (3 niveaux)

### Pour Formateur
- Guide animateur détaillé
- Slides 200 diapos
- Corrigés exercices
- Grilles évaluation

---

## 📊 Évaluation Formation

| Critère | Objectif | Mesure |
|:---|:---|:---|
| Satisfaction | > 4,5/5 | Questionnaire fin |
| Taux certification | > 80% | Résultats QCM |
| Application terrain | 3 missions/an | Suivi 12 mois |
| Recommandation | NPS > 50 | Enquête |

---

*Programme Formation Certifiante EBIOS-RM IA 3 Jours | Version 1.0 | Mars 2026*
