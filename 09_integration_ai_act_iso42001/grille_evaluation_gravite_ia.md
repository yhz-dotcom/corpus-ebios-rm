# Grille d'Évaluation de Gravité Enrichie - Systèmes IA

**Référence**: 07_outils_templates/grille_evaluation_gravite_ia.md  
**Version**: 1.0  
**Date**: 2026-03-02

---

## 🎯 Vue d'ensemble

Cette grille enrichit l'évaluation de gravité EBIOS RM classique avec des critères spécifiques aux systèmes d'intelligence artificielle et alignés sur l'AI Act.

---

## 📊 Grille EBIOS RM Classique (Rappel)

**Formule** : Gravité = Impact × Vraisemblance

| Niveau | Valeur |
|:-------|:-------|
| 🔴 Critique | 16-25 |
| 🟠 Élevé | 9-15 |
| 🟡 Modéré | 4-8 |
| 🟢 Faible | 1-3 |

---

## 🆕 Critères d'Impact Spécifiques IA

### Échelle d'impact

| Niveau | Critères IA | Exemples |
|:-------|:------------|:---------|
| **🔴 Critique (5)** | Atteinte aux droits fondamentaux, discrimination systémique, impact sur santé/sécurité physique | Biais racial en recrutement, erreur diagnostic médical, accident véhicule autonome |
| **🟠 Élevé (4)** | Impact financier significatif, atteinte à la réputation, non-conformité réglementaire majeure | Fuite données clients, décision crédit erronée, sanction réglementaire |
| **🟡 Modéré (3)** | Perte d'efficacité opérationnelle, erreurs corrigeables a posteriori | Faux positif filtrage, recommandation inappropriée |
| **🟢 Faible (2)** | Impact négligeable, facilement détectable et réversible | Suggestion non pertinente, erreur mineure |
| **⚪️ Mineur (1)** | Aucun impact significatif | - |

### Questions d'évaluation IA

| # | Question | Si OUI |
|:-:|:---------|:-------|
| I1 | Le risque impacte-t-il des droits fondamentaux (non-discrimination, vie privée) ? | Impact ≥ 4 |
| I2 | Le risque concerne-t-il la santé ou sécurité physique de personnes ? | Impact = 5 |
| I3 | Le risque entraîne-t-il une non-conformité AI Act (haut risque) ? | Impact ≥ 4 |
| I4 | Le risque pourrait-il causer un préjudice financier > 100K€ ? | Impact ≥ 3 |
| I5 | Le risque affecte-t-il la réputation de l'organisation ? | Impact ≥ 3 |
| I6 | Le risque est-il difficile à détecter sans monitoring spécifique ? | Impact +1 |

---

## 🆕 Critères de Vraisemblance Spécifiques IA

### Facteurs de vraisemblance

| Facteur | Description | Impact sur Vraisemblance |
|:--------|:------------|:-------------------------|
| **Complexité du modèle** | Plus le modèle est opaque, plus la détection d'anomalie est difficile | +1 si boîte noire |
| **Exposition publique** | Un système accessible en ligne est plus vulnérable aux attaques | +1 si exposé |
| **Données sensibles** | La présence de données personnelles augmente l'attractivité pour les attaquants | +1 si données sensibles |
| **Maturité des garde-fous** | Des contrôles robustes réduisent la vraisemblance de succès d'une attaque | -1 si garde-fous testés |
| **Historique d'incidents** | Des incidents passés similaires augmentent la vraisemblance | +1 si antécédents |
| **Évolution rapide** | Les systèmes IA peuvent dériver rapidement | +1 si pas de monitoring |

### Questions d'évaluation

| # | Question | Si OUI |
|:-:|:---------|:-------|
| V1 | Le modèle est-il une "boîte noire" difficile à interpréter ? | Vraisemblance +1 |
| V2 | Le système est-il exposé publiquement (internet, API) ? | Vraisemblance +1 |
| V3 | Le système traite-t-il des données personnelles sensibles ? | Vraisemblance +1 |
| V4 | Les garde-fous ont-ils été testés et validés ? | Vraisemblance -1 |
| V5 | Existe-t-il des antécédents d'incidents similaires ? | Vraisemblance +1 |
| V6 | Le système fait-il l'objet d'un monitoring continu ? | Vraisemblance -1 |

---

## 🧮 Formule Enrichie

```
Gravité = (Impact_EBIOS + Impact_IA) × (Vraisemblance_EBIOS + Vraisemblance_IA)

Où:
- Impact_IA = +1 si au moins une question I1-I6 positive
- Vraisemblance_IA = Σ réponses V1-V6 (entre -2 et +4)
```

---

## 📋 Exemples d'Évaluation

### Exemple 1 : Biais discriminatoire (Recrutement)

| Critère | Évaluation | Score |
|:--------|:-----------|:------|
| Impact EBIOS | Atteinte réputation | 4 |
| Impact IA | I1 (droits fondamentaux) | +1 |
| **Impact total** | | **5** |
| Vraisemblance EBIOS | Données historiques biaisées | 4 |
| Vraisemblance IA | V1 (boîte noire) + V6 (pas monitoring) | +2 |
| **Vraisemblance totale** | | **6** |
| **Gravité** | 5 × 6 | **30** |
| **Niveau** | | 🔴 **CRITIQUE** |

### Exemple 2 : Prompt injection (Chatbot)

| Critère | Évaluation | Score |
|:--------|:-----------|:------|
| Impact EBIOS | Fuite information | 3 |
| Impact IA | I3 (non-conformité) | +1 |
| **Impact total** | | **4** |
| Vraisemblance EBIOS | Attaque connue | 3 |
| Vraisemblance IA | V2 (exposé) - V4 (garde-fous testés) | 0 |
| **Vraisemblance totale** | | **3** |
| **Gravité** | 4 × 3 | **12** |
| **Niveau** | | 🟠 **ÉLEVÉ** |

---

## 🎯 Seuils de Priorité

| Gravité | Priorité | Délai traitement |
|:--------|:---------|:-----------------|
| ≥ 20 | P1 - Critique | Immédiat (< 1 semaine) |
| 12-19 | P2 - Élevé | Court terme (< 1 mois) |
| 6-11 | P3 - Modéré | Moyen terme (< 3 mois) |
| ≤ 5 | P4 - Faible | Planifié |

---

## 📝 Intégration dans EBIOS RM

### Section à ajouter dans l'Atelier 3

```markdown
## Évaluation de la gravité - Enrichissement IA

### Scénario : [Nom]

#### Impact classique EBIOS
- [ ] Catastrophique (5)
- [ ] Majeur (4)
- [ ] Important (3)
- [ ] Mineur (2)
- [ ] Négligeable (1)

#### Impact IA complémentaire
- [ ] I1 - Droits fondamentaux
- [ ] I2 - Santé/sécurité physique
- [ ] I3 - Non-conformité AI Act
- [ ] I4 - Impact financier > 100K€
- [ ] I5 - Réputation
- [ ] I6 - Difficulté détection

#### Vraisemblance classique EBIOS
- [ ] Quasi-certain (5)
- [ ] Très probable (4)
- [ ] Possible (3)
- [ ] Peu probable (2)
- [ ] Exceptionnel (1)

#### Vraisemblance IA complémentaire
- [ ] V1 - Modèle boîte noire (+1)
- [ ] V2 - Exposition publique (+1)
- [ ] V3 - Données sensibles (+1)
- [ ] V4 - Garde-fous testés (-1)
- [ ] V5 - Antécédents (+1)
- [ ] V6 - Pas de monitoring (+1)

### Calcul final
- Impact EBIOS : [X]
- Impact IA : [Y]
- Vraisemblance EBIOS : [Z]
- Vraisemblance IA : [W]
- **Gravité totale** : (X+Y) × (Z+W) = **[Résultat]**
- **Niveau** : [🔴/🟠/🟡/🟢]
- **Priorité** : [P1/P2/P3/P4]
```

---

**Document mis à jour**: 2026-03-02
