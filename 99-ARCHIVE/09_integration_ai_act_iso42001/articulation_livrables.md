# Articulation des Livrables EBIOS RM ↔️ AI Act

**Référence**: 08_livraison_suivi/articulation_livrables.md  
**Version**: 1.0  
**Date**: 2026-03-02

---

## 🎯 Vue d'ensemble

Ce document précise comment les livrables EBIOS RM s'articulent avec les documents requis par l'AI Act.

---

## 📊 Tableau de correspondance

| Livrable EBIOS RM | Correspondance AI Act | Action requise |
|:------------------|:----------------------|:---------------|
| **Périmètre + Biens essentiels** (Atelier 1) | Intended purpose (Art. 6) | Vérifier classification risque |
| **Sources de menace** (Atelier 2) | Gouvernance données (Art. 10) | Ajouter menaces IA |
| **Scénarios de risque** (Atelier 3) | Analyse risque (Annexe IV.2) | Enrichir menaces IA spécifiques |
| **Plan de traitement** (Atelier 4) | Mesures conformité (Art. 15-17) | Mapper exigences AI Act |
| **Feuille de route** (Atelier 5) | Surveillance post-marché (Art. 72) | Inclure indicateurs IA |
| **Dossier complet** | Documentation technique (Annexe IV) | Structurer format UE |

---

## 🔗 Détail par Atelier

### Atelier 1 → Classification AI Act

**Livrable EBIOS** : Rapport de cadrage, périmètre, biens essentiels

**Correspondance AI Act** :
- **Article 6** : Classification du système
- **Annexe III** : Détermination haut risque
- **Annexe IV.1** : Informations générales système

**Actions** :
1. Vérifier si le système relève de l'Annexe III
2. Documenter la classification dans le rapport Atelier 1
3. Justifier l'exemption Article 6(3) si applicable

---

### Atelier 2 → Gouvernance Données

**Menaces IA à ajouter** :
- Biais dans données training (Art. 10)
- Données non représentatives
- Manque de traçabilité

---

### Atelier 3 → Analyse Risque (Annexe IV.2)

**Scénarios IA à intégrer** :
- SR-IA-01 : Dérive des performances
- SR-IA-02 : Biais discriminatoire
- SR-IA-03 : Prompt injection
- SR-IA-04 : Extraction données
- SR-IA-05 : Manipulation scénarios

---

### Atelier 4 → Mesures Conformité

| Mesure EBIOS | Article AI Act |
|:-------------|:---------------|
| Tests sécurité | Art. 15 (Robustesse) |
| Supervision humaine | Art. 14 |
| Documentation | Art. 11 |
| Journalisation | Art. 12 |
| Transparence | Art. 13 |

---

### Atelier 5 → Surveillance Post-Marché

**Adaptation fréquences** :

| Classification | Fréquence adaptée IA |
|:---------------|:---------------------|
| 🔴 Haut risque | **Trimestrielle** |
| 🟡 Risque limité | **Semestrielle** |
| 🟢 Risque minimal | Annuelle |

---

## 📁 Structure Dossier Combiné

```
DOSSIER-CONFORMITE/
├── 01-EBIOS-RM/
│   ├── A1-Cadrage/
│   ├── A2-Sources-Menace/
│   ├── A3-Scenarios/
│   ├── A4-Traitement/
│   └── A5-Feuille-Route/
├── 02-AI-ACT/
│   ├── classification/
│   ├── documentation-technique/
│   ├── conformite/
│   └── surveillance/
└── 03-SYNTHESE/
    ├── mapping-ebios-aiact.md
    └── resume-executif.md
```

---

**Document mis à jour**: 2026-03-02
