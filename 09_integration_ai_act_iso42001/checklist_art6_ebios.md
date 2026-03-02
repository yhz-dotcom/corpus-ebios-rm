# Checklist Classification Article 6 - Intégration Atelier 1 EBIOS

**Référence**: 09_integration_ai_act_iso42001/checklist_art6_ebios.md  
**Version**: 1.0  
**Date**: 2026-03-02

---

## 🎯 Objectif

Cette checklist permet d'intégrer la classification AI Act (Article 6) dans l'**Atelier 1** de la méthode EBIOS RM.

---

## 📋 Checklist Classification

### Étape 1 : Vérification Article 5 (Pratiques Interdites)

| # | Question | Réponse | Action si OUI |
|:-:|:---------|:-------:|:--------------|
| 1.1 | Le système utilise-t-il des techniques de manipulation subliminale ? | ☐ Oui ☐ Non | 🚫 Arrêt immédiat |
| 1.2 | Exploite-t-il les vulnérabilités de groupes spécifiques (enfants, personnes handicapées) ? | ☐ Oui ☐ Non | 🚫 Arrêt immédiat |
| 1.3 | Réalise-t-il un scoring social à l'échelle de la société ? | ☐ Oui ☐ Non | 🚫 Arrêt immédiat |
| 1.4 | Utilise-t-il de la biométrie à distance en temps réel dans des espaces publics ? | ☐ Oui ☐ Non | 🚫 Arrêt immédiat |
| 1.5 | Détecte-t-il les émotions dans des écoles ou lieux de travail ? | ☐ Oui ☐ Non | 🚫 Arrêt immédiat |

**Résultat Étape 1** : ☐ Interdit ☐ Continuer

---

### Étape 2 : Vérification Annexe I (Composants Sécurité)

| # | Question | Réponse | Action si OUI |
|:-:|:---------|:-------:|:--------------|
| 2.1 | Le système est-il un composant de sécurité d'un produit réglementé ? | ☐ Oui ☐ Non | 🔴 Haut risque |
| 2.2 | Produit concerné : machines, jouets, équipements médicaux, véhicules ? | ☐ Oui ☐ Non | 🔴 Haut risque |

**Résultat Étape 2** : ☐ Haut risque (Annexe I) ☐ Continuer

---

### Étape 3 : Vérification Annexe III (Secteurs Haut Risque)

| # | Secteur | Applicable ? | Référence |
|:-:|:--------|:------------:|:----------|
| 3.1 | **Biométrie** - Identification/validation biométrique | ☐ | Annexe III.1 |
| 3.2 | **Éducation** - Notation, évaluation, orientation | ☐ | Annexe III.2 |
| 3.3 | **Emploi** - Recrutement, sélection, évaluation | ☐ | Annexe III.3 |
| 3.4 | **Services publics** - Aide aux bénéficiaires | ☐ | Annexe III.4 |
| 3.5 | **Services essentiels** - Crédit, assurance, évaluation risque | ☐ | Annexe III.5 |
| 3.6 | **Justice** - Aide aux juges, évaluation preuves | ☐ | Annexe III.6 |
| 3.7 | **Migration/Asile** - Évaluation demandes | ☐ | Annexe III.7 |
| 3.8 | **Application loi** - Profilage, évaluation récidive | ☐ | Annexe III.8 |
| 3.9 | **Démocratie** - Diffusion contenu électoral | ☐ | Annexe III.9 |

**Résultat Étape 3** : ☐ Au moins 1 case cochée ☐ Aucune

---

### Étape 4 : Vérification Exemption Article 6(3)

**Si au moins une case 3.x cochée, vérifier les conditions cumulatives** :

| # | Condition | Réponse |
|:-:|:----------|:-------:|
| 4.1 | **Tâche procédurale étroite** - La tâche est-elle clairement définie et circonscrite ? | ☐ Oui ☐ Non |
| 4.2 | **Amélioration résultat humain** - Le système améliore-t-il uniquement un résultat humain préexistant ? | ☐ Oui ☐ Non |
| 4.3 | **Supervision humaine** - Une revue humaine significative est-elle intégrée au workflow ? | ☐ Oui ☐ Non |
| 4.4 | **Pas de profilage** - Aucune activité de profilage de personnes physiques n'est-elle réalisée ? | ☐ Oui ☐ Non |

**Résultat Étape 4** :
- ☐ Toutes les conditions remplies → 🟡 Risque limité (exemption)
- ☐ Au moins 1 condition non remplie → 🔴 Haut risque

---

### Étape 5 : Vérification Article 50 (Transparence)

| # | Question | Réponse |
|:-:|:---------|:-------:|
| 5.1 | Le système est-il un chatbot ou agent conversationnel ? | ☐ Oui ☐ Non |
| 5.2 | Génère-t-il du contenu synthétique (deepfake, texte, image) ? | ☐ Oui ☐ Non |
| 5.3 | Analyse-t-il ou traite-t-il des émotions ? | ☐ Oui ☐ Non |

**Résultat Étape 5** :
- ☐ Au moins 1 case cochée → 🟡 Risque limité (transparence)
- ☐ Aucune → 🟢 Risque minimal

---

## 🎯 Résultat Final

### Classification

| Résultat | Obligations | Prochaines étapes EBIOS |
|:---------|:------------|:------------------------|
| 🚫 **INTERDIT** | Arrêt immédiat | Fin du processus |
| 🔴 **HAUT RISQUE** | Régime complet AI Act | Ateliers 2-5 complets |
| 🟡 **RISQUE LIMITÉ** | Transparence | Ateliers allégés |
| 🟢 **RISQUE MINIMAL** | Bonnes pratiques | Atelier 1 suffisant |

### Documentation à Produire

| Classification | Documents obligatoires |
|:---------------|:-----------------------|
| 🔴 Haut risque | Documentation technique (Annexe IV), FRIA, Déclaration UE |
| 🟡 Risque limité | Notice utilisateur, marquage contenu synthétique |
| 🟢 Risque minimal | Aucun document réglementaire obligatoire |

---

## 📝 Intégration dans l'Atelier 1 EBIOS

### Section à ajouter dans le rapport Atelier 1

```markdown
## Annexe : Classification AI Act

### Résultat de la classification
- **Niveau de risque** : [🔴 Haut / 🟡 Limité / 🟢 Minimal]
- **Fondement juridique** : [Article 6.1(a) / Article 6.3 / Article 50]
- **Annexe applicable** : [I / III / Aucune]
- **Exemption** : [Oui / Non]

### Justification
[Explication détaillée de la classification]

### Impact sur l'analyse EBIOS
- [ ] Scénarios de risque spécifiques IA à inclure
- [ ] Mesures de traitement AI Act à intégrer
- [ ] Plan de surveillance post-marché à établir
```

---

**Document mis à jour**: 2026-03-02
