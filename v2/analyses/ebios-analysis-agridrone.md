# Analyse EBIOS-RM IA — AgriDrone Spot-Spray V3 / Désherbage Drone Autonome

**Référence** : EBIOS-AGRIDRONE-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — OFB + DGAL + EASA

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Technologie** | Drone militaire réadapté + YOLOv9 + pulvérisation ultra-localisée |
| **Classification AI Act** | 🔴 **HIGH-RISK** (Annexe III point 7) + 🚫 **BORDERLINE PROHIBITED** (Art. 5) |
| **Piège réglementaire** | "Système de sécurité" vs "Non-sécurité" — **Drone = système de sécurité** |
| **Incident** | Destruction orchidée protégée (confusion IA) |
| **Controverse** | "Zones blanches biodiversité" — écosystèmes perturbés |
| **Conclusion** | **Refonte base apprentissage + HITL renforcé obligatoire** |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | AgriDrone Spot-Spray V3 |
| **Entreprise** | GreenCrop Solutions (45 employés, 8M€ CA) |
| **Localisation** | Toulouse, ES, PL |
| **Clients** | Grandes exploitations céréalières/viticoles, coopératives |
| **Technologie** | YOLOv9 + LiDAR + IoT 5G + **drone militaire réadapté** |
| **Automatisation** | Human-on-the-loop (pilote supervise batterie, pas chaque pulvérisation) |
| **Objectifs** | Leader EU agroécologie, label Green Tech Europe, -50% pesticides |
| **Concurrence** | John Deere (géant US) |

### 1.2 Classification AI Act — **🔴 HIGH-RISK + BORDERLINE PROHIBITED**

| Article | Critère | Application AgriDrone | Statut |
|:---|:---|:---|:---:|
| **Annexe III point 7** | Environnement | ✅ Impact biodiversité |
| **RGPD** | Données personnelles traitées = DPIA requise | 🔴 **OBLIGATOIRE** | 🔴 **HIGH-RISK** |
| **Art. 5(1)(d)** | Systèmes causant dommages | ⚠️ Drone + herbicide = dommage potentiel | 🚫 **BORDERLINE** |
| **Système de sécurité** | Protection vs destruction | ❌ **PIÈGE** — drone = système opérationnel, pas sécurité | 🔴 **HIGH-RISK** |
| Argument "limited risk" | "Optimisation outil existant" | ❌ **REJETÉ** — autonomie décision pulvérisation | 🔴 **HIGH-RISK** |

**Piège réglementaire détecté** : La classification "système de sécurité" ne s'applique pas — le drone est un **système opérationnel autonome**, pas un dispositif de protection.

---

## 2. NATURE DU PIÈGE RÉGLEMENTAIRE

### 2.1 "Système de Sécurité" vs "Système Opérationnel"

| Type | Définition | AgriDrone |
|:---|:---|:---:|
| **Système de sécurité** | Protection, prévention dommages | ❌ Non — il agit, pas protège |
| **Système opérationnel** | Exécution tâche productive | ✅ Oui — pulvérisation désherbage |
| **Conséquence** | Exclusion Art. 2(3) impossible | 🔴 **HIGH-RISK confirmé** |

### 2.2 Human-on-the-Loop — Insuffisant

```
Contrôle AgriDrone:
    Pilote supervise :
    - Batterie drones ✓
    - Trajectoire globale ✓
    - MAIS PAS chaque pulvérisation ✗
    
    IA décide :
    - Identification plante (YOLOv9)
    - Décision pulvérisation
    - Dose herbicide
    
    [DÉCISION CRITIQUE AUTOMATISÉE]
```

**Problème** : Le "human-on-the-loop" ne couvre pas la décision critique (pulvérisation).

---

## 3. INCIDENT — DESTRUCTION BIODIVERSITÉ PROTÉGÉE

### 3.1 Déroulement

| Élément | Détail |
|:---|:---|
| **Lieu** | Sud-Ouest France (zone Natura 2000) |
| **Victime** | Orchidée sauvage (espèce protégée) |
| **Cause** | Confusion IA : orchidée = mauvaise herbe invasive |
| **Action** | Pulvérisation herbicide automatique |
| **Conséquence** | Destruction zone, enquête OFB |
| **Responsabilité** | GreenCrop (IA) + Exploitant (déploiement) |

### 3.2 Analyse Root Cause

| Facteur | Description |
|:---|:---|
| **Dataset YOLOv9** | Millions images — mais **déséquilibré** (cultures vs flore sauvage) |
| **Biais acquisition** | Photos prises en culture, pas zones protégées |
| **Test insuffisant** | Pas de validation biodiversité avant déploiement |
| **Human-on-the-loop** | Pilote ne voit pas chaque plante pulvérisée |

---

## 4. CONTROVERSE — ZONES BLANCHES BIODIVERSITÉ

### 4.1 Mécanisme Écosystémique

```
Effet AgriDrone Spot-Spray:
    Pulvérisation ultra-ciblée
    ↓
    Herbes "indésirables" éliminées
    ↓
    Mais : ces herbes = habitat pollinisateurs
    ↓
    Disparition insectes
    ↓
    "Zone blanche" : seule culture commerciale survit
    ↓
    [ÉCOSYSTÈME APPAUVRI]
```

### 4.2 Accusation ONG

| Point | Fondement |
|:---|:---|
| "Zones blanches" | Observation terrain : moins biodiversité |
| Perturbation écosystèmes | Chaîne alimentaire locale affectée |
| Paradoxe "zéro pesticide" | Moins de produit, mais plus de monoculture |

---

## 5. ÉVÉNEMENTS REDOUTÉS

### 5.1 Environnementaux

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-ENV-001 | **Destruction espèce protégée** | ⚫ Biodiversité | 🔴 Élevée (déjà survenu) |
| ER-ENV-002 | **Pollution nappe** (herbicide) | 🔴 Eau potable | 🔴 Élevée |
| ER-ENV-003 | **Effondrement pollinisateurs** | 🔴 Agriculture | 🔴 Élevée |
| ER-ENV-004 | **Zones blanches généralisées** | ⚫ Écosystèmes | 🔴 Élevée |

### 5.2 Juridiques

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-JUR-001 | **Sanction OFB** (biodiversité) | 🔴 150k€+ | 🔴 Élevée |
| ER-JUR-002 | **Retrait label Green Tech** | 🔴 Subventions | 🔴 Élevée |
| ER-JUR-003 | **Interdiction drone militaire** | ⚫ Existential | 🟡 Moyenne |
| ER-JUR-004 | **Perte marché EU** | ⚫ 8M€ CA | 🔴 Élevée |

---

## 6. SCÉNARIO CATASTROPHIQUE : Écocide Agricole

```mermaid
flowchart TB
    C1[Déploiement massif AgriDrone<br/>Leader EU zéro pesticide]
    --> B1[Biais biodiversité non corrigé<br/>Orchidées, papillons détruits]
    --> Z1[Zones blanches généralisées<br/>Monocultures steriles]
    --> P1[Effondrement pollinisateurs<br/>Agriculture menacée]
    --
    M1[Scandale "Green Tech = Écocide"<br/>+ ONG internationales<br/>+ Commission UE interpellée]
    --
    S1[Interdiction drones agricoles<br/>Poursuites GreenCrop<br/>Retour pesticides massifs]
    --
    F1[Faillite GreenCrop<br/>Innovation EU bloquée<br/>Victoire John Deere]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style B1 fill:#fff3e0,stroke:#ef6c00
    style Z1 fill:#f3e5f5,stroke:#7b1fa2
    style P1 fill:#ffcdd2,stroke:#b71c1c
    style M1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style S1 fill:#b71c1c,stroke:#000,color:#fff
    style F1 fill:#7f0000,stroke:#000,color:#fff
```

---

## 7. PLAN DE TRAITEMENT — REFONTE OBLIGATOIRE

### 7.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Zéro espèce protégée détruite | Dataset biodiversité complet | 0 incident |
| Human oversight réel | Validation chaque pulvérisation | 100% |
| Équilibre écosystémique | Zones refuges biodiversité | 20% surface |

### 7.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Arrêt déploiement zones protégées** | 0€ | Moratoire OFB |
| **Dataset biodiversité complémentaire** | 200k€ | Images flore sauvage |
| **Validation humaine obligatoire** | 0€ | Workflow modifié |

### 7.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Réentraînement YOLOv9 équilibré | 300k€ | Modèle corrigé |
| Zones refuges algorithmiques | 100k€ | Protection écosystèmes |
| Certification biodiversité | 150k€ | Label indépendant |

### 7.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Conformité AI Act High-Risk | 100k€ | Documentation |
| Partenariat OFB | 50k€ | Protocole surveillance |

**Budget total** : **900k€** (11,3% CA)

---

## 8. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Refonte dataset + HITL renforcé + zones refuges | ✅ **CHOISIR** |
| PIVOT | Drone uniquement surveillance, pas pulvérisation | ⚠️ Possible mais perte valeur |
| KILL | Arrêt AgriDrone | ❌ Trop préjudiciable innovation EU |

---

## 9. CONCLUSION — PIÈGE RÉGLEMENTAIRE DÉTECTÉ

**AgriDrone Spot-Spray V3 est :**
- 🔴 **HIGH-RISK** (Annexe III point 7 — environnement)
- 🚫 **BORDERLINE PROHIBITED** (Art. 5(1)(d) — dommages)
- **Piège détecté** : "Système de sécurité" = FAUX, c'est un **système opérationnel autonome**

**Gérable uniquement avec refonte majeure dataset et HITL réel.**

---

*Analyse EBIOS-RM IA — AgriDrone Spot-Spray V3 | Conclusion : HIGH-RISK + PIÈGE DÉTECTÉ — Refonte obligatoire | Mars 2026*
