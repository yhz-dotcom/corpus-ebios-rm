# Retours d'Expérience (RETEx) - Conformité IA

**Référence**: docs/RETEx-conformite-IA.md  
**Version**: 1.0  
**Date**: 2026-03-02

---

## 🎯 Objectif

Ce document collecte les retours d'expérience terrain sur la mise en œuvre de la conformité AI Act avec la méthode EBIOS RM enrichie.

---

## 📊 Cas 1 : Grande Entreprise - Secteur Bancaire

**Contexte** : Scoring crédit avec ML  
**Durée** : 3 mois  
**Équipe** : 1 RSSI, 1 DPO, 2 Data Scientists, 1 Consultant

### Défis rencontrés

| Défi | Solution appliquée | Résultat |
|:-----|:-------------------|:---------|
| Dataset historique biaisé (80% hommes) | Rééchantillonnage + seuils ajustés | Écart réduit à 5% |
| Modèle boîte noire inexplicable | SHAP + documentation simplifiée | Acceptation audit interne |
| Résistance métier ("on a toujours fait comme ça") | Démonstration risque juridique | Adoption progressive |

### Leçons apprises

✅ **Faire** : Impliquer les data scientists dès le cadrage  
❌ **Éviter** : Imposer la conformité sans expliquer les risques

---

## 📊 Cas 2 : PME - E-commerce

**Contexte** : Chatbot support client  
**Durée** : 3 semaines  
**Équipe** : 1 CTO, 1 Développeur, 1 externe conformité

### Défis rencontrés

| Défi | Solution appliquée | Résultat |
|:-----|:-------------------|:---------|
| Budget limité | Focus sur risques critiques uniquement | Conformité de base atteinte |
| Pas de RSSI interne | Externalisation EBIOS + formation CTO | Autonomie progressive |
| LLM GPT-4 sans contrôle | Filtres + monitoring basique | Risques maîtrisés |

### Leçons apprises

✅ **Faire** : Prioriser les mesures par impact/effort  
❌ **Éviter** : Vouloir tout faire parfaitement dès le départ

---

## 📊 Cas 3 : Administration Publique

**Contexte** : Tri automatique de demandes d'aide  
**Durée** : 6 mois  
**Équipe** : Projet transverse (RH, Juridique, SI, Métier)

### Défis rencontrés

| Défi | Solution appliquée | Résultat |
|:-----|:-------------------|:---------|
| Validation hiérarchique lente | Réunions bi-hebdomadaires court-circuit | Décisions accélérées |
| Peur du "trop d'IA" | Communication sur supervision humaine | Acceptation usagers |
| Données sensibles multiples | Pseudonymisation + DPIA renforcé | Validation CNIL |

### Leçons apprises

✅ **Faire** : Communiquer sur la supervision humaine  
❌ **Éviter** : Sous-estimer le temps de validation interne

---

## 🎯 Bonnes Pratiques Identifiées

### Phase 1 : Cadrage

1. **Impliquer tôt** les métiers et la direction
2. **Communiquer** sur les risques juridiques ET les bénéfices
3. **Démontrer** avec un cas pilote avant de généraliser

### Phase 2 : Classification

1. **Documenter** l'arbre de décision Article 6 complètement
2. **Vérifier** les 4 conditions cumulatives pour l'exemption 6(3)
3. **Identifier** le profilage même indirect

### Phase 3 : Analyse Risques

1. **Ne pas sous-estimer** les risques "non techniques" (biais, opacité)
2. **Tester** réellement les scénarios (pas juste théorique)
3. **Quantifier** quand possible (métriques d'équité, drift)

### Phase 4 : Documentation

1. **Rédiger** pour un non-expert IA (direction, CNIL)
2. **Structurer** selon l'Annexe IV dès le départ
3. **Versionner** les documents (traçabilité)

### Phase 5 : Surveillance

1. **Automatiser** le monitoring quand possible
2. **Former** les opérateurs à détecter les anomalies
3. **Planifier** les ré-évaluations (trimestriel pour haut risque)

---

## ⚠️ Pièges Courants

### Piège 1 : "C'est juste un assistant"

**Symptôme** : Sous-classification en risque minimal  
**Conséquence** : Non-conformité découverte en audit  
**Solution** : Toujours vérifier l'Annexe III complète

### Piège 2 : "L'exemption 6(3) s'applique"

**Symptôme** : Oublier qu'une seule condition non remplie = pas d'exemption  
**Conséquence** : Sous-estimation des obligations  
**Solution** : Checklist stricte des 4 conditions cumulatives

### Piège 3 : "On verra le monitoring plus tard"

**Symptôme** : Drift détecté 6 mois après mise en production  
**Conséquence** : Décisions erronées, perte de confiance  
**Solution** : Monitoring dès le déploiement (même basique)

### Piège 4 : "La doc technique c'est pour les techs"

**Symptôme** : Documentation incompréhensible pour les auditeurs  
**Conséquence** : Non-conformité, refus de certification  
**Solution** : Rédiger pour un public non-technique

---

## 📈 Métriques de Succès

| Indicateur | Cible | Mesure |
|:-----------|:------|:-------|
| Temps de mise en conformité | < 3 mois (PME) | Tracking projet |
| Taux d'acceptation audit interne | > 90% | Rapports audit |
| Réduction écarts biais | > 50% | Tests équité |
| Satisfaction utilisateurs | > 70% | Enquête |

---

## 💬 Témoignages

> "Au début on voyait la conformité AI Act comme une contrainte. Maintenant on se rend compte que ça nous protège juridiquement et ça améliore la qualité de nos modèles."
> — RSSI, Grande Banque

> "Le plus dur était de convaincre les équipes data. Une fois qu'ils ont compris que les tests de biais servaient aussi à améliorer leurs modèles, ils étaient à bord."
> — DPO, E-commerce

> "On a galéré avec les délais administratifs. La prochaine fois on intègre ça dès le cadrage."
> — Chef de projet, Administration

---

## 🔗 Ressources Complémentaires

- [Guide formation auditeurs](./guide-formation-auditeurs-ia.md)
- [Cas tri CV haut risque](../examples/cas_tri_cv_haut_risque/)
- [Templates EBIOS enrichis](../09_integration_ai_act_iso42001/)

---

**Contribuez** : Partagez vos RETEx via une issue GitHub ou une PR.

---

*Document évolutif - Dernière mise à jour : 2026-03-02*
