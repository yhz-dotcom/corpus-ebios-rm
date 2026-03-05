# Module d'Intégration AI Act / ISO 42001

**Référence**: 09_integration_ai_act_iso42001/README.md  
**Version**: 1.0  
**Date**: 2026-03-02

---

## 🎯 Objectif

Enrichir la méthode EBIOS RM pour l'analyse de risques des systèmes d'intelligence artificielle, en assurant la conformité avec l'AI Act et l'ISO 42001.

---

## 📁 Contenu du Module

| Fichier | Usage | Public cible |
|:--------|:------|:-------------|
| `mapping_ebios_aiact.md` | Correspondance méthodologique EBIOS ↔ AI Act ↔ ISO 42001 | RSSI, DPO, Auditeurs |
| `checklist_art6_ebios.md` | Classification Article 6 dans l'Atelier 1 | Consultants, RSSI |
| `template_scenario_ia.md` | 8 scénarios de risque IA pour l'Atelier 3 | Auditeurs cyber |
| `mesures_traitement_aiact.md` | Mesures AI Act à intégrer dans l'Atelier 4 | RSSI, Équipes sécurité |
| `articulation_livrables.md` | Production documentation technique Annexe IV | DPO, Consultants |
| `livrables_combines.md` | Structuration du dossier final conformité | Tous |
| `grille_evaluation_gravite_ia.md` | Critères spécifiques IA pour l'évaluation impact | Auditeurs |
| `guide_suivi_adapte.md` | Fréquences de ré-évaluation adaptées | RSSI, Pilotes conformité |

---

## ⚡️ Quick Start

### Étape 1 : Classification
Utiliser `checklist_art6_ebios.md` pour classifier le système selon l'Article 6 AI Act.

```bash
# Résultat attendu
Classification: [🔴 Haut risque / 🟡 Risque limité / 🟢 Risque minimal]
Annexe applicable: [I / III / Aucune]
Exemption Art 6(3): [Oui / Non applicable]
```

### Étape 2 : Scénarios
Sélectionner les scénarios pertinents dans `template_scenario_ia.md` selon la classification.

| Classification | Scénarios recommandés |
|:---------------|:----------------------|
| 🔴 Haut risque | SR-IA-01 à SR-IA-08 (tous) |
| 🟡 Risque limité | SR-IA-01, SR-IA-04, SR-IA-07 |
| 🟢 Risque minimal | SR-IA-01 (optionnel) |

### Étape 3 : Mesures
Intégrer les mesures AI Act via `mesures_traitement_aiact.md` dans le plan de traitement EBIOS.

### Étape 4 : Livrables
Produire les livrables combinés selon `articulation_livrables.md` et `livrables_combines.md`.

---

## 🔗 Intégration avec l'Écosystème

Ce module s'inscrit dans l'écosystème AI Governance :

```
┌─────────────────────────────────────────────────────────┐
│              AI GOVERNANCE ECOSYSTEM                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ai-act-iso42001-framework  ──►  Cartographie workflows │
│           │                                             │
│           ▼                                             │
│  ai-act-audit-tool  ──►  Classification + Tests         │
│           │                                             │
│           ▼                                             │
│  corpus-ebios-rm  ──►  Analyse risques cyber            │
│           │                                             │
│           └──►  09_integration_ai_act_iso42001/         │
│                 (Ce module)                             │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 📚 Ressources Complémentaires

- [Guide EBIOS RM ANSSI](https://www.ssi.gouv.fr/ebios-rm/)
- [AI Act (UE 2024/1689)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
- [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html)

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Voir [CONTRIBUTING.md](../CONTRIBUTING.md)

---

**Version**: 1.0  
**Mise à jour**: 2026-03-02
