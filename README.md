<!-- === EN-TÊTE DOCUMENTAIRE ISO-GRADE === -->

| Métadonnées | Valeur |
|-------------|--------|
| **Référence** | `CORPUS-EBIOS-RM-001` |
| **Titre** | Corpus EBIOS RM - Guide de l'Auditeur |
| **Version** | `2.0` |
| **Date** | `06/03/2026` |
| **Propriétaire** | `Direction Conformité / RSSI` |
| **Classification** | `Confidentiel` |

---

# Corpus EBIOS RM - Guide de l'Auditeur

**Référence** : CORPUS-EBIOS-RM-001 | ANSSI EBIOS RM v1.0 (2021)

---

## 1. PRÉSENTATION

Ce corpus fournit un guide complet et structuré pour accompagner les auditeurs et consultants dans la réalisation d'analyses de risques cyber selon la méthodologie **EBIOS RM** (Risk Manager) de l'ANSSI.

### 1.1 Conformité ISO 31000

EBIOS RM est conforme au cadre de l'**ISO 31000** (Management du risque — Principes et lignes directrices), assurant une reconnaissance internationale de la méthodologie.

---

## 2. STRUCTURE DU CORPUS

```
corpus-ebios-rm/
│
├── 📘 00-METHODOLOGIE/              ← CŒUR METHODOLOGIQUE (NEUTRE)
│   ├── 00.1-principes-iso-31000.md       ← Cadre normatif international
│   ├── 00.2-methodologie-ebios.md        ← Méthodologie de base
│   ├── 00.3-les-5-ateliers.md            ← Détail des ateliers
│   ├── 00.4-guides-pratiques/            ← Guides d'utilisation
│   │   ├── guide-auditeur.md
│   │   ├── guide-facilitation.md
│   │   └── guide-livraison.md
│   └── 00.5-glossaire-et-references.md   ← Glossaire et normes
│
├── 📗 11-SIA/                       ← APPLICATION SIA
│   ├── 11.1-risques-specifiques-ia.md
│   ├── 11.2-sources-risque-ia.md
│   ├── 11.3-scenarios-ia.md
│   ├── 11.4-mesures-securite-ia.md
│   └── 11.5-mapping-ai-act.md
│
├── 📙 20-OUTILS/                    ← TEMPLATES ET OUTILS
│   ├── templates/
│   │   ├── template-cadrage.md
│   │   ├── template-sources-risque.md
│   │   ├── template-scenarios.md
│   │   └── template-feuille-route.md
│   ├── checklists/
│   └── scripts/
│
├── 📕 40-EXEMPLES/                  ← SCÉNARIOS FICTIFS
│   ├── 40.1-exemple-sante-fictif.md
│   ├── 40.2-exemple-finance-fictif.md
│   └── 40.3-exemple-ia-fictif.md
│
└── 📦 99-ARCHIVE/                   ← ANCIENNES VERSIONS (CONSERVÉES)
    └── [anciens dossiers archivés]
```

---

## 3. CONVENTION DE NUMÉROTATION

| Préfixe | Contenu | Stabilité |
|:--------|:--------|:----------|
| **00** | Méthodologie de base | Stable - MàJ mineures |
| **11-19** | Applications sectorielles | Évolutif |
| **20-29** | Outils et templates | Évolutif |
| **40-49** | Exemples et cas pratiques | Évolutif |
| **99** | Archive | Figé - Conservation |

---

## 4. UTILISATION

### 4.1 Pour une Mission Standard

1. Lire `00-METHODOLOGIE/00.2-methodologie-ebios.md`
2. Utiliser les templates dans `20-OUTILS/templates/`
3. Suivre les guides dans `00-METHODOLOGIE/00.4-guides-pratiques/`

### 4.2 Pour une Mission SIA (Système d'IA)

1. Lire la méthodologie de base (00-METHODOLOGIE/)
2. Consulter `11-SIA/` pour les spécificités IA
3. Adapter les templates avec les éléments SIA

### 4.3 Pour se Former

1. Étudier `40-EXEMPLES/` - scénarios fictifs complets
2. Simuler une analyse sur un cas d'étude

---

## 5. RÔLES ET RESPONSABILITÉS

| Rôle | Responsabilité | Livrable |
|:-----|:---------------|:---------|
| **Auditeur EBIOS** | Animer les 5 ateliers | Dossier EBIOS RM |
| **RSSI Client** | Fournir informations techniques | Socle de sécurité |
| **Direction Client** | Arbitrer, valider scénarios | Décision traitement |
| **Référents Métier** | Participer aux ateliers | Cartographie biens |

---

## 6. RÉVISION

| Version | Date | Auteur | Modifications |
|:--------|:-----|:-------|:--------------|
| 2.0 | 06/03/2026 | Direction Conformité | Restructuration complète, séparation méthodo/applications |
| 1.0 | 05/03/2026 | Direction Conformité | Création initiale ISO-Grade |

---

**Document approuvé par :**
- [ ] RSSI
- [ ] Direction Conformité

**Date d'approbation :** _______________

---

*Corpus EBIOS RM — Version 2.0 ISO-Grade*  
*Réf. CORPUS-EBIOS-RM-001*

---

## ⚠️ NOTE IMPORTANTE

> Ce corpus est un guide d'accompagnement. Il ne remplace pas la 
> **formation officielle EBIOS RM de l'ANSSI**.
> 
> Pour toute certification ou mission critique, suivre la formation 
> officielle dispensée par l'ANSSI ou ses partenaires agréés.
