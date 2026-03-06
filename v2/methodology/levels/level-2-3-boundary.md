# Guide Cas Limites — Frontière Level 2 / Level 3

**Pour** : Qualifier les usages ambigus entre 🟡 et 🔴

---

## 🎯 Objectif

Aider à décider quand un usage dépasse le seuil 🟡 Level 2 pour passer en 🔴 Level 3.

---

## 🧭 Matrice de Décision

### Axe 1 : Niveau d'Automatisation

| Niveau | Description | Niveau EBIOS |
|:-------|:------------|:-------------|
| **A1** — Validation systématique | Humain valide chaque sortie | 🟢 ou 🟡 |
| **A2** — Validation échantillon | Humain vérifie % représentatif | 🟡 |
| **A3** — Supervision alerte | Humain intervient sur alerte | 🟡 ou 🔴 |
| **A4** — Supervision temps réel | Humain surveille en continu | 🔴 |
| **A5** — Totalement autonome | Pas de supervision en temps réel | 🔴 |

### Axe 2 : Impact Potentiel

| Niveau | Exemples | Niveau EBIOS |
|:-------|:---------|:-------------|
| **I1** — Aucun | Brainstorming, brouillon | 🟢 |
| **I2** — Faible | Recommandation ignorée | 🟢 ou 🟡 |
| **I3** — Moyen | Retard, inefficacité | 🟡 |
| **I4** — Élevé | Perte financière, insatisfaction | 🟡 ou 🔴 |
| **I5** — Critique | Santé, sécurité, discrim. systémique | 🔴 |

### Matrice Croisée

| Automatisation \ Impact | I1 | I2 | I3 | I4 | I5 |
|:------------------------|:--:|:--:|:--:|:--:|:--:|
| **A1** Validation syst. | 🟢 | 🟢 | 🟡 | 🟡 | 🟡 |
| **A2** Échantillon | — | 🟡 | 🟡 | 🟡 | 🔴 |
| **A3** Alerte | — | 🟡 | 🟡 | 🔴 | 🔴 |
| **A4** Temps réel | — | — | 🔴 | 🔴 | 🔴 |
| **A5** Autonome | — | — | 🔴 | 🔴 | 🔴 |

---

## 📋 Cas Limites Typiques

### Cas 1 : Pré-sélection avec échantillonnage

**Situation** : IA pré-sélectionne 100 candidats, recruteur en vérifie 20

| Critère | Évaluation | Niveau |
|:--------|:-----------|:-------|
| Automatisation | A2 (échantillon) | |
| Impact | I4 (décision RH) | |
| **Résultat** | | **🟡 Level 2** |

**Justification** : Supervision humaine significative (20%), mais pas systématique.

**Mesures renforcées** :
- Échantillon aléatoire (pas choisi par l'IA)
- Métriques fairness sur les 100 (pas seulement 20 sélectionnés)
- Audit trimestriel des non-sélectionnés

---

### Cas 2 : Scoring avec alertes

**Situation** : IA score risque client, humain alerté si score > 80

| Critère | Évaluation | Niveau |
|:--------|:-----------|:-------|
| Automatisation | A3 (alerte) | |
| Impact | I4 (crédit refusé) | |
| **Résultat** | | **🔴 Level 3** |

**Justification** : Impact élevé + supervision réactive (pas préventive).

**Mesures renforcées** :
- HITL obligatoire pour scores > 80
- Justification explicable pour chaque décision
- Recours client formalisé

---

### Cas 3 : Support avec autonomie limitée

**Situation** : Agent autonome mais whitelist actions (FAQ, redirection, création ticket)

| Critère | Évaluation | Niveau |
|:--------|:-----------|:-------|
| Automatisation | A5 (autonome) mais limité | |
| Impact | I2 (recommandation) ou I3 (retard) | |
| **Résultat** | | **🟡 Level 2** ou **🔴 Level 3** |

**Justification** : Dépend de l'impact des actions whitelistées.

| Si action whitelist... | Niveau |
|:-----------------------|:-------|
| Information, FAQ | 🟡 |
| Création ticket, rendez-vous | 🟡 |
| Modification compte, commande | 🔴 |
| Paiement, résiliation | 🔴 |

---

### Cas 4 : Annexe III avec exception

**Situation** : Usage Annexe III mais exception Art. 6(3) applicable

| Critère | Évaluation | Niveau |
|:--------|:-----------|:-------|
| Annexe III | Oui | |
| Exception 6(3) | Validation humaine systématique | |
| **Résultat** | | **🟡 Level 2** |

**Justification** : Exception reconnue, mais prudence nécessaire.

**Conditions obligatoires** :
- [ ] Validation humaine **systématique** (pas échantillon)
- [ ] Documentation de la supervision
- [ ] Pas de décision définitive automatique
- [ ] Revue plus fréquente (semestrielle)

---

## 🎲 Règles de Décision

### Règle 1 : Doute = Monter

> En cas d'hésitation entre deux niveaux, **choisir le niveau supérieur** pour la première qualification.

On peut redescendre après analyse approfondie et documentation.

### Règle 2 : Premier Usage = Prudence

> Pour le **premier usage** dans un domaine métier, appliquer un niveau au-dessus.

Objectif : établir la référence avec marge de sécurité.

### Règle 3 : Contexte Client

| Contexte client | Ajustement |
|:----------------|:-----------|
| Régulé (banque, santé) | +1 niveau |
| Historique incidents | +1 niveau |
| Forte visibilité médiatique | +1 niveau |
| Maturité IA élevée | -1 niveau possible |

### Règle 4 : Évolution dans le Temps

| Évolution | Action |
|:----------|:-------|
| Automatisation augmente | Réévaluer niveau |
| Impact augmente | Réévaluer niveau |
| Incident survenu | +1 niveau temporaire |
| Maturité acquise | -1 niveau possible |

---

## ✅ Checklist Décision 🟡 vs 🔴

- [ ] Niveau d'automatisation clairement identifié (A1-A5)
- [ ] Impact potentiel évalué (I1-I5)
- [ ] Matrice croisée consultée
- [ ] Cas limites similaires recherchés
- [ ] Contexte client pris en compte
- [ ] Règles de décision appliquées
- [ ] Justification documentée
- [ ] Date de réévaluation planifiée

---

## 📝 Exemples de Justification

### 🟡 Level 2 (justifié)

> "Usage 🟡 car validation humaine par échantillonnage représentatif (30%).
> Impact élevé mais supervision significative.
> Mesures renforcées : échantillon aléatoire, métriques globales."

### 🔴 Level 3 (justifié)

> "Usage 🔴 car supervision réactive sur alerte uniquement.
> Impact élevé (décision financière) + automatisation A3.
> Précaution : premier usage dans ce domaine."

### 🔴 Level 3 → 🟡 Level 2 (après analyse)

> "Usage initialement 🔴, redescendu 🟡 après 6 mois.
> Justification : 0 incident, métriques stables, supervision A2 validée.
> Documentation : rapport mensuel + audit externe."

---

## 🆘 Escalade

Quand consulter un expert ?

- [ ] Cas non couvert par la matrice
- [ ] Conflit entre critères
- [ ] Enjeu réglementaire majeur
- [ ] Première fois dans le secteur
- [ ] Décision client stratégique

**Contact** : [AI Officer / Consultant EBIOS-RM IA]

---

*Guide Cas Limites — Version 2.0*
