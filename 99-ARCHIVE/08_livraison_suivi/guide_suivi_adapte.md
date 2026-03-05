# Guide de Suivi Adapté aux Systèmes IA

**Référence**: 08_livraison_suivi/guide_suivi_adapte.md  
**Version**: 1.0  
**Date**: 2026-03-02

---

## 🎯 Vue d'ensemble

Ce guide adapte les fréquences de suivi EBIOS RM aux spécificités des systèmes d'IA et aux exigences de l'AI Act.

---

## 📊 Fréquences de Ré-évaluation

### Par Classification AI Act

| Classification | Fréquence EBIOS standard | Fréquence adaptée IA | Déclencheurs |
|:---------------|:-------------------------|:---------------------|:-------------|
| 🔴 **Haut risque** | Annuelle | **Trimestrielle** | Incident, changement données, mise à jour modèle |
| 🟡 **Risque limité** | Annuelle | **Semestrielle** | Retour utilisateur, évolution réglementaire |
| 🟢 **Risque minimal** | Annuelle | Annuelle | Modification substantielle du cas d'usage |

---

## 🔍 Monitoring Continu (Haut Risque)

### Indicateurs à surveiller

| Indicateur | Fréquence | Seuil d'alerte | Action |
|:-------------|:----------|:---------------|:-------|
| **Drift des prédictions** | Hebdomadaire | > 5% variation | Investigation |
| **Feedback utilisateurs** | Temps réel | Tout signalement | Analyse immédiate |
| **Biais par sous-groupe** | Mensuel | Écart > 10% | Correction |
| **Tests robustesse** | Mensuel | Nouvelle vulnérabilité | Patch sécurité |
| **Performance globale** | Trimestriel | Dégradation > 10% | Ré-entraînement |

---

## 📝 Journal de Suivi IA

### Template d'entrée

```markdown
## [Date] - Revue [Trimestrielle/Semestrielle/Annuelle]

### Métriques de performance
- Accuracy: [X]% (baseline: [Y]%)
- Drift détecté: [Oui/Non]
- Biais identifiés: [Liste]

### Incidents depuis dernière revue
- [ ] Aucun
- [ ] [Description incident]

### Actions correctives
- [ ] Aucune requise
- [ ] [Description action]

### Prochaine revue
Date: [JJ/MM/AAAA]
Type: [Trimestrielle/Semestrielle/Annuelle]
```

---

**Document mis à jour**: 2026-03-02
