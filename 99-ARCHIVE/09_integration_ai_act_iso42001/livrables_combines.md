# Livrables Combinés EBIOS RM + AI Act

**Référence**: 09_integration_ai_act_iso42001/livrables_combines.md  
**Version**: 1.0  
**Date**: 2026-03-02

---

## 🎯 Vue d'ensemble

Ce document décrit comment produire un dossier de conformité combinant les livrables EBIOS RM et les documents requis par l'AI Act.

---

## 📁 Structure du Dossier Combiné

```
DOSSIER-CONFORMITE-IA/
├── 00-Synthese/
│   ├── resume-executif.md
│   └── mapping-reglementaire.md
│
├── 01-EBIOS-RM/
│   ├── A1-Cadre-Périmetre/
│   │   ├── atelier1-rapport.md
│   │   └── [+] classification-ai-act.md
│   │
│   ├── A2-Sources-Menace/
│   │   ├── atelier2-rapport.md
│   │   └── [+] sources-menace-ia.md
│   │
│   ├── A3-Scenarios-Risque/
│   │   ├── atelier3-rapport.md
│   │   └── [+] scenarios-ia-specifiques.md
│   │
│   ├── A4-Traitement-Risque/
│   │   ├── atelier4-rapport.md
│   │   └── [+] mesures-ai-act.md
│   │
│   └── A5-Feuille-Route/
│       ├── atelier5-rapport.md
│       └── [+] plan-surveillance-post-marché.md
│
├── 02-AI-Act/
│   ├── classification/
│   │   ├── justification-haut-risque.md
│   │   └── grille-exemption-art63.md
│   │
│   ├── documentation-technique/
│   │   └── annexe-iv-checklist.md
│   │
│   ├── conformite/
│   │   ├── declaration-ue-conformite.md
│   │   ├── registre-ue-systeme.md
│   │   └── politique-qualite.md
│   │
│   └── surveillance/
│       ├── plan-surveillance-post-marché.md
│       └── procedure-signalement-incidents.md
│
└── 03-ISO-42001 (optionnel)/
    ├── contexte-organisation/
    ├── leadership/
    ├── planification/
    ├── support/
    ├── fonctionnement/
    ├── evaluation-performances/
    └── amelioration/
```

---

## 📝 Livrables par Niveau de Risque

### 🔴 Système Haut Risque (Annexe III)

| Document | Source | Obligatoire |
|:---------|:-------|:-----------:|
| Rapport EBIOS Atelier 1-5 | EBIOS RM | ✅ |
| Classification AI Act | AI Act Art. 6 | ✅ |
| Documentation technique (Annexe IV) | AI Act Art. 11 | ✅ |
| Système management qualité | AI Act Art. 17 | ✅ |
| Évaluation risques | AI Act Art. 9 | ✅ |
| Gouvernance données | AI Act Art. 10 | ✅ |
| Logs traçabilité | AI Act Art. 12 | ✅ |
| Supervision humaine | AI Act Art. 14 | ✅ |
| Tests robustesse | AI Act Art. 15 | ✅ |
| Évaluation conformité | AI Act Art. 43 | ✅ |
| Déclaration UE conformité | AI Act Art. 47-48 | ✅ |
| Enregistrement base UE | AI Act Art. 49 | ✅ |
| Plan surveillance post-marché | AI Act Art. 72 | ✅ |

### 🟡 Système Risque Limité

| Document | Source | Obligatoire |
|:---------|:-------|:-----------:|
| Rapport EBIOS Atelier 1 (allégé) | EBIOS RM | Recommandé |
| Classification AI Act | AI Act Art. 6 | ✅ |
| Notice utilisateur | AI Act Art. 50 | ✅ |
| Marquage contenu synthétique | AI Act Art. 50 | ✅ |

### 🟢 Système Risque Minimal

| Document | Source | Obligatoire |
|:---------|:-------|:-----------:|
| Classification AI Act | AI Act Art. 6 | Recommandé |
| Code de conduite (volontaire) | AI Act | Optionnel |

---

## 🔗 Correspondance Livrables

### EBIOS RM → AI Act

| Livrable EBIOS | Correspondance AI Act | Utilisation |
|:---------------|:----------------------|:------------|
| Atelier 1 : Périmètre | Classification Art. 6 | Justification haut risque |
| Atelier 2 : Sources | Gouvernance données Art. 10 | Inventaire menaces IA |
| Atelier 3 : Scénarios | Évaluation risques Art. 9 | Scénarios IA spécifiques |
| Atelier 4 : Traitement | Mesures conformité | Plan de traitement |
| Atelier 5 : Feuille route | Surveillance Art. 72 | Plan post-marché |

### AI Act → EBIOS RM

| Document AI Act | Intégration EBIOS | Section |
|:----------------|:------------------|:--------|
| Classification | Atelier 1 | Annexe classification |
| Documentation technique | Atelier 4 | Mesures spécifiques |
| Plan surveillance | Atelier 5 | Suivi post-mission |

---

## 📊 Matrice de Production

| Phase | EBIOS | AI Act | ISO 42001 | Livrable combiné |
|:------|:------|:-------|:----------|:-----------------|
| 1. Cadrage | Atelier 1 | Classification | Clause 4 | Périmètre + classification |
| 2. Analyse | Ateliers 2-3 | Évaluation risques | Clause 6 | Scénarios enrichis IA |
| 3. Traitement | Atelier 4 | Mesures | Clause 8 | Plan traitement complet |
| 4. Suivi | Atelier 5 | Surveillance | Clause 9 | Plan surveillance |

---

## 🎓 Exemple : Dossier Complet

### Contexte
- **Système** : SIA de tri automatique de CV
- **Classification** : 🔴 Haut risque (Annexe III - Emploi)
- **Exemption Art 6(3)** : Non applicable

### Dossier produit

```
DOSSIER-RECRUTIA-CONFORMITE/
├── 00-Synthese/
│   ├── resume-executif.md
│   └── [✓] Classification: Haut risque - Annexe III point 4(a)
│
├── 01-EBIOS-RM/
│   ├── A1-Cadre-Périmetre/
│   │   ├── atelier1-rapport.md
│   │   └── [✓] classification-ai-act.md (justification détaillée)
│   │
│   ├── A2-Sources-Menace/
│   │   ├── atelier2-rapport.md
│   │   └── [✓] sources-menace-ia.md (biais, drift, jailbreak)
│   │
│   ├── A3-Scenarios-Risque/
│   │   ├── atelier3-rapport.md
│   │   └── [✓] scenarios-ia-specifiques.md (SR-IA-01 à SR-IA-08)
│   │
│   ├── A4-Traitement-Risque/
│   │   ├── atelier4-rapport.md
│   │   └── [✓] mesures-ai-act.md (M-10-03, M-14-01, etc.)
│   │
│   └── A5-Feuille-Route/
│       ├── atelier5-rapport.md
│       └── [✓] plan-surveillance-post-marché.md (Art. 72)
│
├── 02-AI-Act/
│   ├── classification/
│   │   ├── [✓] justification-haut-risque.md
│   │   └── [✓] grille-exemption-art63.md (non applicable)
│   │
│   ├── documentation-technique/
│   │   └── [✓] annexe-iv-checklist.md (98 points)
│   │
│   ├── conformite/
│   │   ├── [✓] declaration-ue-conformite.md
│   │   ├── [✓] registre-ue-systeme.md
│   │   └── [✓] politique-qualite.md
│   │
│   └── surveillance/
│       ├── [✓] plan-surveillance-post-marché.md
│       └── [✓] procedure-signalement-incidents.md
│
└── 03-ISO-42001/
    └── [optionnel - si certification visée]
```

---

## ✅ Checklist de Validation

Avant livraison du dossier :

- [ ] Classification AI Act documentée et justifiée
- [ ] Tous les ateliers EBIOS complétés
- [ ] Scénarios IA spécifiques inclus
- [ ] Mesures AI Act intégrées au plan de traitement
- [ ] Documentation technique Annexe IV complète
- [ ] Déclaration UE de conformité rédigée
- [ ] Plan de surveillance post-marché établi
- [ ] Registre UE préparé
- [ ] Revue qualité effectuée

---

**Document mis à jour**: 2026-03-02
