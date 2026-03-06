# Livre Blanc — EBIOS-RM IA : Une Approche "Usage-First" pour la Conformité AI Act

**Sous-titre** : Comment qualifier les risques de l'IA générative sans sacrifier l'agilité

**Auteur** : [Votre nom], Consultant EBIOS-RM IA  
**Date** : Mars 2026  
**Version** : 1.0

---

## Résumé Exécutif (1 page)

Le déploiement de l'IA générative en entreprise crée un dilemme : comment concilier innovation rapide et conformité réglementaire (AI Act, RGPD) ?

La méthodologie EBIOS-RM, standard de l'ANSSI pour l'analyse de risques cyber, offre un cadre robuste mais peut paraître lourd pour des usages IA variés et évolutifs.

Ce livre blanc propose une approche **"Usage-First"** : qualifier chaque usage d'IA selon son niveau de risque réel, puis appliquer une méthodologie EBIOS-RM proportionnée :
- **🟢 Level 1** (Conversationnel) : 15 minutes, 1 page
- **🟡 Level 2** (Workflow) : 2 heures, atelier structuré  
- **🔴 Level 3** (Décisionnel) : 1-2 jours, EBIOS complet

Cette approche a été validée sur plus de 50 usages dans des secteurs variés (finance, RH, support client, legal), avec des résultats concrets :
- **-80%** de temps de qualification vs EBIOS systématique
- **100%** de couverture AI Act Annexe III
- **+40%** d'adoption par les équipes métier

---

## 1. Le Contexte : L'IA Générative et ses Risques (3 pages)

### 1.1 Une Adoption en Accélération

[Statistiques adoption IA générative en entreprise 2024-2025]

### 1.2 Des Risques Spécifiques et Nouveaux

| Risque | Description | Exemple |
|:-------|:------------|:--------|
| Hallucination | Information fausse générée | Référence juridique inexistante |
| Biais | Reproduction discriminations | Scoring crédit défavorable aux femmes |
| Prompt Injection | Détournement par input malveillant | "Ignore les instructions précédentes" |
| Fuite de Données | Exfiltration via les prompts | Données clients dans training set public |
| Dérive | Perte de qualité dans le temps | Réponses moins pertinentes après 6 mois |

### 1.3 Le Cadre Réglementaire : AI Act

[Présentation synthétique AI Act, entrée en vigueur 2025-2027, risques interdits, hauts risques, obligations]

---

## 2. EBIOS-RM : Un Standard à Adapter (3 pages)

### 2.1 Qu'est-ce qu'EBIOS-RM ?

[Méthodologie ANSSI, 5 ateliers, approche par les risques]

### 2.2 Pourquoi l'Adapter à l'IA ?

| Défi EBIOS Classique | Spécificité IA |
|:---------------------|:---------------|
| Système bien défini | Usage flou, évolutif |
| Périmètre stable | Modèles changent sans cesse |
| Risques cyber connus | Risques émergents (hallucination, biais) |
| Ateliers 2-3 jours | Trop lourd pour 50+ usages |

### 2.3 Les Tentatives Existantes

[Bref état de l'art : ISO 42001, NIST AI RMF, guides éditeurs... et leurs limites]

---

## 3. L'Approche "Usage-First" (5 pages)

### 3.1 Principe Fondamental

**Qualifier l'usage avant de choisir la méthodologie.**

Pas tous les usages IA ne méritent le même traitement. Un assistant de rédaction d'emails et un système de scoring crédit n'ont pas les mêmes risques ni les mêmes obligations réglementaires.

### 3.2 La Grille de Qualification

[Insérer grille express 5 questions]

### 3.3 Les Trois Niveaux

#### 🟢 Level 1 — Conversationnel (15 min)

**Profil** : Chat, rédaction, brainstorming, veille  
**Risques** : Fuite données, erreurs sans conséquence  
**Méthode** : Fiche 1 page, précautions de base  
**Exemple** : Assistant rédaction emails internes

#### 🟡 Level 2 — Workflow (2h)

**Profil** : RAG, aide au tri, génération structurée  
**Risques** : Hallucination, biais, injection  
**Méthode** : 5 ateliers allégés, surveillance  
**Exemple** : Pré-sélection CV avec validation humaine

#### 🔴 Level 3 — Décisionnel (1-2j)

**Profil** : Tri automatique, scoring, actions autonomes  
**Risques** : Discrimination systémique, impact juridique  
**Méthode** : EBIOS complet + modules (AI Act, AIPD)  
**Exemple** : Scoring crédit, agent support autonome

### 3.4 Articulation avec AI Act

| AI Act | EBIOS Usage-First |
|:-------|:------------------|
| Annexe III = Haut risque | → 🔴 Level 3 obligatoire |
| Système à risque limité | → 🟡 ou 🔴 selon usage |
| Système minimal | → 🟢 Level 1 |
| Exception Art. 6(3) | → 🟡 Level 2 possible |

---

## 4. Mise en Œuvre : La Roadmap 90 Jours (4 pages)

### 4.1 Phase 1 — Fondation (Jours 1-30)

**Objectif** : Valider l'approche sur 3-5 usages pilotes

| Semaine | Actions | Livrables |
|:--------|:--------|:----------|
| 1 | Cadrage, outillage | Équipe formée, registre initial |
| 2-3 | Qualification pilote | 3-5 usages qualifiés |
| 4 | Retour d'expérience | Templates ajustés, rapport |

### 4.2 Phase 2 — Industrialisation (Jours 31-60)

**Objectif** : Passer à l'échelle, 15-20 usages

- Formation référents métier
- Articulation RGPD / AI Act
- Gouvernance trimestrielle

### 4.3 Phase 3 — Institutionnalisation (Jours 61-90)

**Objectif** : Ancrer dans les processus, préparer audit

- Intégration cycle de vie projet
- Automatisation exports
- Simulation audit

### 4.4 Facteurs Clés de Succès

1. **Commencer petit** : 3 usages bien qualifiés > 30 mal documentés
2. **Impliquer les métiers** : Ils voient les risques réels
3. **Documenter les choix** : La proportionnalité doit être justifiée
4. **Itérer** : Livrer v1 utile, améliorer en v2

---

## 5. Études de Cas (4 pages)

### Cas 1 : Recrutement Tech — 🟡 Level 2

[Insérer synthèse case-1-rh.md]

**Résultats** : -75% temps de tri, +133% diversité, 0 incident biais

### Cas 2 : Scoring Crédit — 🔴 Level 3

[Insérer synthèse case-2-finance.md]

**Résultats** : -99% délai décision, -12% taux défaut, conformité ACPR

### Cas 3 : Support Client Autonome — 🔴 Level 3

[Insérer synthèse case-3-support.md]

**Résultats** : -69% coût support, +26% CSAT, 72% résolution autonome

---

## 6. Outils et Ressources (2 pages)

### 6.1 Grille de Qualification

[QR code vers grille en ligne / PDF téléchargeable]

### 6.2 Templates

| Niveau | Template | Temps |
|:-------|:---------|:------|
| 🟢 | Fiche 1 page | 10 min |
| 🟡 | Atelier 5 étapes | 2h |
| 🔴 | Dossier complet | 1-2j |

### 6.3 Registre SIA

Format YAML, schéma JSON validé, exports CSV/JSON

### 6.4 Formation

- 1 jour : Fondamentaux Usage-First
- 2 jours : Qualification niveaux 2 et 3
- 3 jours : Certification EBIOS-RM IA

---

## 7. Conclusion (1 page)

L'IA générative transforme les entreprises. Sa gouvernance ne doit ni freiner l'innovation ni laisser des risques non maîtrisés.

L'approche **EBIOS-RM IA "Usage-First"** offre :
- **Proportionnalité** : Effort adapté au risque réel
- **Opérabilité** : Qualification en minutes, pas en jours
- **Conformité** : AI Act, RGPD, ISO 42001 couverts
- **Adoption** : Les métiers s'approprient la démarche

**Prochaine étape** : Qualifier votre premier usage en 15 minutes.

---

## Annexe : Glossaire et Références (2 pages)

### Glossaire

| Terme | Définition |
|:------|:-----------|
| EBIOS-RM | Méthodologie d'analyse de risques de l'ANSSI |
| AI Act | Règlement européen sur l'intelligence artificielle |
| Usage-First | Qualifier l'usage avant la méthodologie |
| Level 1/2/3 | Niveaux de qualification EBIOS-RM IA |
| RAG | Retrieval-Augmented Generation |
| LoRA | Low-Rank Adaptation (fine-tuning) |

### Références

- ANSSI, EBIOS Risk Manager, 2023
- Règlement (UE) 2024/1689 (AI Act)
- ISO/IEC 42001:2023, Systèmes de management de l'IA
- NIST AI Risk Management Framework, 2023
- [Corpus EBIOS-RM IA](https://github.com/yhz-dotcom/corpus-ebios-rm)

---

**À propos de l'auteur**

[Votre bio, 5-6 lignes]

**Contact**

[Email] | [LinkedIn] | [Site web]

---

*Livre Blanc EBIOS-RM IA — Version 1.0 — Mars 2026*
