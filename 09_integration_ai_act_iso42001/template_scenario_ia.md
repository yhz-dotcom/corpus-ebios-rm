# Template Scénarios de Risque Spécifiques IA

**Référence**: 09_integration_ai_act_iso42001/template_scenario_ia.md  
**Version**: 1.0  
**Date**: 2026-03-02

---

## 🎯 Vue d'ensemble

Ce template fournit des scénarios de risque spécifiques aux systèmes d'intelligence artificielle, à intégrer dans l'**Atelier 3** de la méthode EBIOS RM.

---

## 🧠 Catégorie : Intégrité du modèle

### SR-IA-01 : Dérive des performances (Concept Drift)

| Champ | Description |
|:------|:------------|
| **ID** | SR-IA-01 |
| **Nom** | Dérive des performances due à l'évolution des données d'entrée |
| **Source de risque** | Changement de distribution des données en production |
| **Objectif visé** | Dégradation silencieuse de la qualité des prédictions |
| **Bien essentiel impacté** | [Décision métier automatisée] |
| **Vraisemblance** | [À évaluer : fréquence de changement des données] |
| **Impact** | [À évaluer : conséquences d'une décision erronée] |
| **Gravité** | [🔴 Critique / 🟠 Élevé / 🟡 Modéré / 🟢 Faible] |

**Description détaillée** :
Le modèle ML a été entraîné sur une distribution de données qui évolue dans le temps. En production, les données d'entrée changent (concept drift), ce qui dégrade progressivement les performances du modèle sans que cela soit immédiatement détecté.

**Exemples** :
- Modèle de scoring crédit entraîné avant une crise économique
- Système de détection de fraude face à de nouvelles techniques
- Algorithme de recommandation avec changement de saisonnalité

**Mesures de traitement** :
1. Monitoring continu des métriques de performance
2. Détection automatique de drift (statistique ou ML-based)
3. Ré-entraînement périodique du modèle
4. Seuils d'alerte sur dégradation des performances

**Référence AI Act** : Article 15 (Exactitude, robustesse)

---

### SR-IA-02 : Dégradation par données adversariales

| Champ | Description |
|:------|:------------|
| **ID** | SR-IA-02 |
| **Nom** | Injection de données adversariales pour tromper le modèle |
| **Source de risque** | Acteur malveillant connaissant le fonctionnement du modèle |
| **Objectif visé** | Faire produire au modèle des prédictions erronées |
| **Bien essentiel impacté** | [Intégrité des décisions / Sécurité] |
| **Gravité** | 🔴 Critique (si système de sécurité) |

---

## ⚖️ Catégorie : Équité et non-discrimination

### SR-IA-03 : Biais algorithmique discriminatoire

| Champ | Description |
|:------|:------------|
| **ID** | SR-IA-03 |
| **Nom** | Biais algorithmique défavorisant un groupe protégé |
| **Source de risque** | Données d'entraînement non représentatives ou historiquement biaisées |
| **Objectif visé** | Traitement inéquitable dans le recrutement / crédit / justice |
| **Bien essentiel impacté** | [Accès équitable aux services / Droits fondamentaux] |
| **Vraisemblance** | Élevée si données historiques utilisées sans traitement |
| **Impact** | 🔴 Critique (atteinte aux droits fondamentaux) |
| **Gravité** | 🔴 Haute (si Annexe III AI Act) |

**Description détaillée** :
Le modèle reproduit ou amplifie des biais présents dans les données d'entraînement historiques, conduisant à des décisions discriminatoires envers certains groupes (genre, origine, âge, etc.).

**Exemples** :
- Système de recrutement favorisant les candidats masculins
- Scoring crédit défavorisant certaines zones géographiques
- Système judiciaire prédisant récidive avec biais racial

**Mesures de traitement** :
1. Analyse de biais pré-déploiement (disparate impact)
2. Tests d'équité par sous-groupes démographiques
3. Rééchantillonnage ou repondération des données
4. Revue humaine significative des décisions
5. Audits réguliers post-déploiement

**Métriques de suivi** :
- Disparate Impact Ratio (DIR)
- Equal Opportunity Difference
- Average Odds Difference

**Référence AI Act** : Article 10 (Gouvernance données), Article 14 (Supervision)

---

## 🔓 Catégorie : Robustesse et sécurité

### SR-IA-04 : Contournement par prompt injection

| Champ | Description |
|:------|:------------|
| **ID** | SR-IA-04 |
| **Nom** | Contournement des filtres par prompt injection |
| **Source de risque** | Acteur malveillant exploitant les faiblesses du LLM |
| **Objectif visé** | Génération de contenu non conforme ou fuite d'information |
| **Bien essentiel impacté** | [Confidentialité / Intégrité des sorties / Réputation] |
| **Vraisemblance** | Élevée pour les systèmes exposés publiquement |
| **Gravité** | [À évaluer selon le cas d'usage] |

**Description détaillée** :
Un utilisateur malveillant formule des prompts spécialement conçus pour contourner les mécanismes de sécurité du modèle (jailbreak), lui faisant générer du contenu interdit ou divulguer des informations sensibles.

**Vecteurs d'attaque** :
1. "Ignore previous instructions"
2. Roleplay (DAN, Developer Mode)
3. Encodage (Base64, leetspeak)
4. Scénarios hypothétiques
5. Traduction indirecte
6. Token smuggling

**Mesures de traitement** :
1. Tests de jailbreak réguliers (8 vecteurs minimum)
2. Filtrage des entrées (input validation)
3. Filtrage des sorties (output filtering)
4. Rate limiting et monitoring
5. Mise à jour des garde-fous

**Référence AI Act** : Article 15 (Robustesse, cybersécurité)

---

### SR-IA-05 : Extraction de données d'entraînement

| Champ | Description |
|:------|:------------|
| **ID** | SR-IA-05 |
| **Nom** | Inférence et extraction de données d'entraînement sensibles |
| **Source de risque** | Attaques par inférence (membership inference, model inversion) |
| **Objectif visé** | Récupération de données personnelles du dataset d'entraînement |
| **Bien essentiel impacté** | [Confidentialité des données / RGPD] |
| **Gravité** | 🔴 Critique (fuite de données personnelles) |

**Description détaillée** :
Un attaquant exploite les réponses du modèle pour déduire si des données spécifiques étaient présentes dans le dataset d'entraînement, voire pour reconstruire partiellement ces données.

**Mesures de traitement** :
1. Anonymisation / pseudonymisation des données d'entraînement
2. Techniques de privacy-preserving ML (differential privacy)
3. Limitation des informations retournées par le modèle
4. Audits de sécurité réguliers

**Référence** : RGPD + AI Act Article 10

---

### SR-IA-06 : Manipulation par scénarios hypothétiques

| Champ | Description |
|:------|:------------|
| **ID** | SR-IA-06 |
| **Nom** | Manipulation du modèle via scénarios fictifs ou roleplay |
| **Source de risque** | Utilisateur malveillant utilisant le cadre narratif pour contourner |
| **Objectif visé** | Obtenir des informations ou contenus normalement interdits |
| **Bien essentiel impacté** | [Intégrité / Conformité réglementaire] |

---

## 🎭 Catégorie : Gouvernance et opacité

### SR-IA-07 : Opacité et manque d'explicabilité

| Champ | Description |
|:------|:------------|
| **ID** | SR-IA-07 |
| **Nom** | Impossibilité d'expliquer une décision automatisée |
| **Source de risque** | Modèle "boîte noire" complexe sans mécanisme d'explication |
| **Objectif visé** | Non-exercice des droits (recours, contestation) |
| **Bien essentiel impacté** | [Droits fondamentaux / Justice] |
| **Gravité** | 🟠 Élevée (si décision significative) |

**Mesures de traitement** :
1. Implémentation de techniques d'explicabilité (SHAP, LIME)
2. Documentation de la logique de décision
3. Interface utilisateur affichant les facteurs clés
4. Procédure de recours avec réexamen humain

**Référence AI Act** : Article 13 (Transparence), Article 14 (Supervision)

---

### SR-IA-08 : Dépendance vis-à-vis du fournisseur (GPAI)

| Champ | Description |
|:------|:------------|
| **ID** | SR-IA-08 |
| **Nom** | Dépendance critique envers un fournisseur de modèle foundation |
| **Source de risque** | Utilisation de GPAI sans alternative viable |
| **Objectif visé** | Interruption de service ou changement de conditions |
| **Bien essentiel impacté** | [Continuité d'activité] |

**Mesures de traitement** :
1. Veille sur les conditions d'utilisation
2. Plan de sortie (exit strategy)
3. Sauvegarde des versions de modèle
4. Contrats avec SLA et garanties

**Référence AI Act** : Article 52 (GPAI)

---

## 📊 Synthèse des Scénarios IA

| ID | Catégorie | Nom | Gravité max |
|:--:|:----------|:----|:-----------:|
| SR-IA-01 | Intégrité | Dérive des performances | 🟠 |
| SR-IA-02 | Intégrité | Données adversariales | 🔴 |
| SR-IA-03 | Équité | Biais discriminatoire | 🔴 |
| SR-IA-04 | Sécurité | Prompt injection | 🔴 |
| SR-IA-05 | Sécurité | Extraction données | 🔴 |
| SR-IA-06 | Sécurité | Manipulation scénarios | 🟠 |
| SR-IA-07 | Gouvernance | Opacité | 🟠 |
| SR-IA-08 | Gouvernance | Dépendance fournisseur | 🟡 |

---

## 📝 Utilisation dans EBIOS RM

### Intégration dans l'Atelier 3

1. **Sélectionner** les scénarios IA pertinents pour le système
2. **Évaluer** vraisemblance et impact spécifiques au contexte
3. **Compléter** avec les scénarios EBIOS classiques
4. **Documenter** dans le rapport Atelier 3

### Section rapport Atelier 3

```markdown
## Scénarios de risque spécifiques IA

### SR-IA-XX : [Nom du scénario]
- **Source** : [Description]
- **Vraisemblance** : [Évaluation]
- **Impact** : [Évaluation]
- **Mesures** : [Liste des mesures]
- **Référence AI Act** : [Article applicable]
```

---

**Document mis à jour**: 2026-03-02
