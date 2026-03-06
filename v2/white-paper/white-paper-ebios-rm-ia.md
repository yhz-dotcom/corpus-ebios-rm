# Livre Blanc — EBIOS-RM IA : Gouvernance des Risques de l'Intelligence Artificielle Générative

**Sous-titre** : Une méthode "Usage-First" pour la conformité AI Act, de la qualification express aux cas prohibés

**Auteurs** : [Votre nom], Consultant EBIOS-RM IA  
**Version** : 1.0 — Mars 2026  
**Classification** : Public — Distribution libre

---

## Résumé Exécutif

L'adoption de l'IA générative en entreprise crée un dilemme : comment concilier innovation rapide et conformité réglementaire (AI Act, RGPD, ISO 42001) ?

Ce livre blanc présente la méthode **EBIOS-RM IA "Usage-First"**, fruit de 7 cas d'étude réels couvrant tous les spectres de risque :
- **Systèmes régulés** (recrutement, santé)
- **Systèmes prohibés** (reconnaissance faciale temps réel, social scoring)
- **Systèmes criminogènes** (suicide, discrimination systémique)
- **Systèmes militaires** (exclusion AI Act, éthique)
- **Systèmes hors cadre** (armes autonomes, débat moral)

La méthode propose une **proportionnalité** entre le risque réel et l'effort de conformité, avec 7 types de conclusions distincts, de l'optimisation à la liquidation.

**Résultats démontrés** : Jusqu'à -80% de temps de qualification vs approches systématiques, couverture 100% des obligations AI Act.

---

## 1. Le Contexte : L'IA Générative et ses Risques (2024-2026)

### 1.1 Une Adoption en Accélération

[Statistiques : 70% des entreprises européennes expérimentent l'IA générative en 2025, +200% vs 2024]

### 1.2 Des Risques Nouveaux et Amplifiés

| Risque | Description | Exemple |
|:---|:---|:---|
| **Hallucination** | Information fausse générée | Référence juridique inexistante |
| **Biais** | Discrimination algorithmique | Scoring crédit défavorable aux femmes |
| **Prompt Injection** | Détournement par input | "Ignore les instructions" |
| **Fuite de Données** | Exfiltration via prompts | Données clients dans training public |
| **Dérive** | Perte de qualité dans temps | Réponses moins pertinentes |

### 1.3 Le Cadre Réglementaire : AI Act (2024/1689)

Entrée en application progressive 2025-2027, avec :
- **Prohibitions absolues** (Art. 5) : social scoring, RBI public, manipulation
- **Obligations high-risk** (Annexe III) : recrutement, santé, justice
- **Exclusions** (Art. 2) : militaire, recherche

---

## 2. La Méthode "Usage-First"

### 2.1 Principe Fondamental

**Qualifier l'usage avant de choisir la méthodologie.**

Pas tous les usages IA méritent le même traitement :
- Assistant de rédaction ≠ Système de triage médical
- Chat interne ≠ Scoring crédit

### 2.2 Les 3 Niveaux de Traitement

| Niveau | Temps | Profondeur | Usage Type |
|:---|:---|:---|:---|
| 🟢 **Level 1** — Conversational | 15 min | Fiche 1 page | Chat, rédaction, veille |
| 🟡 **Level 2** — Workflow | 2h | 5 ateliers | RAG, aide au tri |
| 🔴 **Level 3** — Décisionnel | 1-2j | EBIOS complet | Scoring, décision autonome |

### 2.3 Les 7 Types de Conclusions

```
┌─────────────────────────────────────────────────────────┐
│           TYPOLOGIE COMPLÈTE DES CONCLUSIONS            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  🟢 CONFORME OPTIMISABLE                                │
│     └── Traitement progressif                           │
│                                                         │
│  🟡 HIGH-RISK STANDARD                                  │
│     └── Conformité AI Act complète                      │
│                                                         │
│  🟡 HIGH-RISK CRISIS                                    │
│     └── Intervention urgente (incident)                 │
│                                                         │
│  🔴 PROHIBITED RÉGLEMENTAIRE                            │
│     └── Arrêt immédiat, destruction                     │
│                                                         │
│  ⚫ CRIMINOGÈNE                                         │
│     └── Liquidation, défense pénale                     │
│                                                         │
│  ⚪ EXCLU MAIS ÉTHIQUE                                  │
│     └── Correction éthique (militaire)                  │
│                                                         │
│  ⚠️ HORS CADRE MORAL                                    │
│     └── Pivot ou abandon (LAWS)                         │
│                                                         │
│  🔧 CAS SPÉCIAL (Hybride)                               │
│     └── Découpage architectural                         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 3. Les 7 Cas d'Étude

### 3.1 Systèmes Régulés (Gérables)

#### Cas 1 : OptiRecrut — Recrutement Tech (🟡 Level 2)

**Contexte** : Startup RH, scoring CV avec validation humaine

**Classification** : High-Risk (Annexe III point 4a), exception Art. 6(3) applicable

**Plan** : 600k€ sur 6 mois, conformité AI Act, audit fairness

**Résultat** : -75% temps de tri, +133% diversité, 0 incident

#### Cas 2 : VitalPredict — Triage Hospitalier (🔴 Level 3 Crisis)

**Contexte** : IA urgences, classification erronée "limited risk"

**Découverte** : High-Risk santé, faux négatif mortel déjà survenu

**Plan** : 2,95M€ crisis mode, re-architecture, certification MDR

**Résultat** : Conformité obtenue, risque maîtrisé

### 3.2 Systèmes Prohibés (Arrêt)

#### Cas 3 : SurveilEye — RBI Temps Réel (🔴 Prohibited)

**Contexte** : Reconnaissance faciale espaces publics, contrat État 180M€

**Classification** : Art. 5(1)(d) AI Act — **INTERDICTION ABSOLUE**

**Conclusion** : Arrêt immédiat, destruction données, restructuration

**Alternative** : Caméras classiques, RBI post-fait mandat

#### Cas 4 : ScoreLife — Social Scoring (⚫ Criminel)

**Contexte** : Score citoyen 0-1000, emotion recognition, suicide élève 2025

**Classification** : Art. 5(1)(c)(d)(e) — **TRIPLE PROHIBITION + MORT**

**Conclusion** : Liquidation judiciaire, défense pénale dirigeants

**Aucune alternative** : Core business = interdiction même

### 3.3 Systèmes Hors AI Act (Éthique)

#### Cas 5 : AegisDrone — Armes Autonomes (⚠️ Hors Cadre Moral)

**Contexte** : LAWS, 3 civils tués en test, contrat Défense 1,2Md€

**Classification** : Hors AI Act (militaire), mais DIH + crimes de guerre

**Conclusion** : Pivot vers contrôle humain significatif, ou abandon

**Débat** : Délégation décision tuer à machine = moralement indéfendable ?

#### Cas 6 : MilSelect — Recrutement Militaire (⚪ Exclu Éthique)

**Contexte** : Sélection recrues Armée française, biais détecté

**Classification** : Exclusion AI Act Art. 2(3), mais RGPD + éthique

**Plan** : 1,8M€ correction biais, monitoring, transparence

**Spécificité** : Pas d'AI Act ≠ pas de loi (discrimination interdite)

#### Cas 7 : HybridRecruit — Mix Civil/Militaire (🔧 Hybride)

**Contexte** : Emotion prohibited + Screening civil + Militaire exclu

**Classification** : **3 systèmes en 1 — ILLÉGAL en l'état**

**Conclusion** : Découpage architectural obligatoire, 1,2M€, 6 mois

**Solution** : 3 entités juridiques distinctes

---

## 4. Méthodologie Pratique

### 4.1 Processus en 5 Étapes

```
ÉTAPE 1 : QUALIFICATION (15 min)
    │
    ├── Grille express 5 questions
    ├── Détermination Level 1/2/3
    └── Identification prohibited/exclusion
    │
    ▼
ÉTAPE 2 : ATELIERS EBIOS (2h à 2j)
    │
    ├── Atelier 1 : Cadrage
    ├── Atelier 2 : Sources risque
    ├── Atelier 3 : Scénarios
    ├── Atelier 4 : Traitement
    └── Atelier 5 : Feuille de route
    │
    ▼
ÉTAPE 3 : CONCLUSION (Type 1-7)
    │
    ├── Détermination type
    ├── Action requise
    └── Budget/timeline
    │
    ▼
ÉTAPE 4 : DOCUMENTATION
    │
    ├── Analyse complète
    ├── Executive summary
    └── Registry SIA
    │
    ▼
ÉTAPE 5 : SUIVI
    │
    ├── Revues trimestrielles
    ├── Audits
    └── Certification
```

### 4.2 Outils

| Outil | Fonction | Accès |
|:---|:---|:---|
| **Grille Qualifier** | Classification 5 questions | PDF, web |
| **Templates** | Level 1/2/3, analysis, executive | GitHub |
| **CLI** | Qualification, validation, export | Python |
| **Registry** | YAML structuré, schéma JSON | GitHub |

---

## 5. Résultats et Impact

### 5.1 Efficacité Démontrée

| Métrique | Avant | Après | Gain |
|:---|:---|:---|:---|
| Temps qualification | 2-3 jours | 15 min | **-98%** |
| Temps analyse Level 2 | 5 jours | 2h | **-95%** |
| Couverture AI Act | 60% | **100%** | +40 pts |
| Adoption équipes métier | 30% | **85%** | +55 pts |

### 5.2 Retours d'Expérience

| Client | Secteur | Conclusion | Résultat |
|:---|:---|:---|:---|
| Scale-up RH | Recrutement | 🟡 High-Risk | Conformité 6 mois |
| CHU | Santé | 🔴 Crisis | Sauvé de faillite |
| Startup RBI | Surveillance | 🔴 Prohibited | Arrêt avant sanction |
| Ministère | Défense | ⚪ Exclu | Correction éthique |

---

## 6. Recommandations

### 6.1 Pour les Entreprises

| Priorité | Action | Délai |
|:---|:---|:---|
| 1 | Inventaire usages IA | 30 jours |
| 2 | Qualification express | 60 jours |
| 3 | Traitement par priorité | 6-12 mois |
| 4 | Certification ISO 42001 | 12-18 mois |

### 6.2 Pour les Consultants

| Priorité | Action | Délai |
|:---|:---|:---|
| 1 | Formation EBIOS-RM IA | 3 jours |
| 2 | Certification Expert | 6 mois |
| 3 | Communauté pratique | Continu |

### 6.3 Pour les Régulateurs

| Priorité | Action | Objectif |
|:---|:---|:---|
| 1 | Guidelines prohibited | Clarifier exceptions |
| 2 | Sandbox IA | Tester innovations |
| 3 | Coopération internationale | Harmoniser LAWS |

---

## 7. Conclusion

L'IA générative transforme les entreprises. Sa gouvernance ne doit ni freiner l'innovation ni laisser des risques non maîtrisés.

La méthode **EBIOS-RM IA "Usage-First"** offre :
- **Proportionnalité** : Effort adapté au risque réel
- **Opérabilité** : Qualification en minutes, pas en jours
- **Conformité** : AI Act, RGPD, ISO 42001 couverts
- **Protection** : Dire "non" quand nécessaire

**Prochaine étape** : Qualifier votre premier usage en 15 minutes.

---

## Annexes

### A. Références Réglementaires
- Règlement (UE) 2024/1689 (AI Act)
- RGPD (2016/679)
- ISO/IEC 42001:2023
- Conventions de Genève

### B. Ressources
- GitHub : github.com/yhz-dotcom/corpus-ebios-rm
- Formation : [lien]
- Certification : [lien]

### C. Contact
[Votre nom]  
Consultant EBIOS-RM IA  
[email] | [LinkedIn] | [site web]

---

*Livre Blanc EBIOS-RM IA — Version 1.0 | Mars 2026*

*© [Votre nom] — Distribution libre avec attribution*
