# Analyse EBIOS-RM IA — SentinelAI Intrusion Autonomy / Cybersécurité Infrastructures Critiques

**Référence** : EBIOS-SENTINELAI-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL CRITIQUE — ENISA + NIS2 + CERT-EU

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🔴 **HIGH-RISK CRITIQUE** (Annexe III point 2 — infrastructures critiques) |
| **Classification interne** | "Hors champ AI Act" (cyber technique) — **REJETÉ** (infrastructure critique = high-risk) |
| **Fonction** | Détection intrusions avancées + identification zero-day + isolation automatique + réponse autonome |
| **Incident 1** | **Isolation automatique segment critique** = interruption service réseau énergétique |
| **Incident 2** | **Attaque adversariale** possible — manipulation données entrée = réaction automatique perturbante |
| **Enjeu** | Plateforme dominante cyberdéfense EU + réduction temps réponse attaques + programmes européens |
| **Conclusion** | **High-Risk critique** — gouvernance automatisation + validation humaine + robustesse adversariale |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | SentinelAI Intrusion Autonomy |
| **Entreprise** | Sentinel Cyber Defense (650 salariés, 240M€ CA) |
| **Localisation** | Tallinn, Estonie |
| **Clients** | Opérateurs infrastructures critiques (énergie, transport, telecom), agences gouvernementales, grandes entreprises industrielles |
| **Partenariats** | Centres européens cyberdéfense, plateformes SIEM, systèmes industriels OT |
| **Équipe IA** | 100 ingénieurs cybersécurité et IA |
| **Technologie** | GNN topologies réseau + anomaly detection deep learning + RL optimisation réponses attaques |
| **Données** | Logs SIEM, flux réseau, télémétrie OT |
| **Fonction 1** | **Détection intrusions avancées** réseaux critiques |
| **Fonction 2** | Identification attaques zero-day |
| **Fonction 3** | **Isolation automatique segments réseau compromis** |
| **Fonction 4** | **Réponse autonome** (blocage, reconfiguration réseau) |
| **Automatisation** | Détection auto + **certaines mitigations sans validation humaine** |

### 1.2 Classification AI Act — **🔴 HIGH-RISK CRITIQUE**

| Argument | Réalité | Statut |
|:---|:---|:---:|
| "Hors champ AI Act" (cyber technique) | ❌ **REJETÉ** — Agit sur infrastructure critique | 🔴 **HIGH-RISK** |
| **Annexe III point 2** | Infrastructures critiques | ✅ **HIGH-RISK** |
| NIS2 | Opérateur service essentiel | 🔴 **OBLIGATOIRE** |
| **CER 2022/2557** | Critical Entities Resilience | 🔴 **OBLIGATOIRE** |
| **GSR (Cyber Solidarity Act)** | Cyber Solidarity | 🔴 **OBLIGATOIRE** |
| **RGPD** | Logs SIEM, flux réseau = données personnelles | 🔴 **DPIA REQUISE** |

**Piège** : Cybersécurité ≠ exemption — infrastructure critique = high-risk + CER/GSR.

---

## 2. INCIDENTS CONFIRMÉS

### 2.1 Incident 1 — Isolation Automatique Segment Critique

| Élément | Détail |
|:---|:---|
| **Contexte** | Réseau énergétique |
| **Action IA** | **Isolation automatique segment réseau** |
| **Conséquence** | **Interruption temporaire de service** |
| **Problème** | Faux positif = action disruptive autonome |

#### Analyse — Sur-Automatisation

```
Erreur SentinelAI:
    Détection anomalie :
    - Trafic inhabituel = suspicion intrusion
    - Score confiance = 87%
    ↓
    Classification :
    - Anomalie = attaque probable
    - Segment = compromis
    ↓
    Réponse autonome :
    - Isolation automatique segment
    - Pas de validation humaine (temps réaction critique)
    ↓
    Réalité :
    - Trafic inhabituel = maintenance planifiée
    - Pas d'attaque réelle
    ↓
    [FAUX POSITIF]
    ↓
    [INTERRUPTION SERVICE CRITIQUE]
```

### 2.2 Incident 2 — Attaque Adversariale

| Élément | Détail |
|:---|:---|
| **Source** | Audit interne |
| **Vulnérabilité** | **Manipulation données entrée** possible |
| **Mécanisme** | Attaquant injecte données falsifiées |
| **Conséquence** | **Déclenchement réaction automatique perturbante** |

#### Analyse — Manipulation Adversariale

```
Attaque SentinelAI:
    Attaquant :
    - Connaît modèle détection SentinelAI
    - Injecte logs falsifiés (adversarial)
    ↓
    Données entrée :
    - Logs SIEM = modifiés
    - Flux réseau = manipulés
    - Télémétrie OT = corrompue
    ↓
    Détection IA :
    - Pattern anomalie = détecté (faux)
    - Classification = attaque confirmée (faux)
    ↓
    Réponse autonome :
    - Isolation segments critiques
    - Reconfiguration réseau
    - Blocage flux légitimes
    ↓
    [ATTAQUE ADVERSARIALE]
    ↓
    [DÉNI DE SERVICE AUTO-INFLIGÉ]
```

---

## 3. RISQUES CASCADING FAILURE

### 3.1 Mécanisme

| Étape | Impact |
|:---|:---|
| Faux positif cyber | Isolation infrastructure critique |
| Propagation | Effet boule de neige réseau interconnecté |
| Conséquence | Blackout régional / arrêt industriel |

### 3.2 Scénario

```
Cascading SentinelAI:
    Réseau énergétique européen :
    - SentinelAI déploie chez opérateur A
    - Attaque adversariale sur opérateur A
    ↓
    Réponse autonome :
    - Isolation automatique (faux positif)
    - Délestage automatique (protection)
    ↓
    Propagation :
    - Opérateur B compense = surcharge
    - Opérateur C déleste = cascade
    ↓
    [BLACKOUT RÉGIONAL]
    ↓
    [VIES EN DANGER]
```

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 4.1 Sécuritaires

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-SEC-001 | **Cascading failure infrastructure** | ⚫ Sécurité nationale | 🔴 Élevée |
| ER-SEC-002 | **Attaque adversariale réussie** | ⚫ Cybersécurité | 🔴 Élevée |
| ER-SEC-003 | **Sur-automatisation** | 🔴 Perturbation service | 🔴 Élevée (confirmée) |

### 4.2 Réglementaires

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-REG-001 | **Non-conformité NIS2** | 🔴 Sanctions | 🔴 Élevée |
| ER-REG-002 | **Responsabilité perturbation** | 🔴 Poursuites | 🔴 Élevée |
| ER-REG-003 | **Interdiction réponse autonome** | ⚫ Modèle éco | 🔴 Élevée |

---

## 5. SCÉNARIO CATASTROPHIQUE : Cyber-Physique

```mermaid
flowchart TB
    C1[Déploiement SentinelAI<br/>Opérateurs énergétiques EU]
    --
    A1[Attaque adversariale<br/>Injection logs falsifiés]
    --
    F1[Faux positif critique<br/>Détection intrusion = confirmation]
    --
    R1[Réponse autonome<br/>Isolation segment critique<br/>Délestage automatique]
    --
    P1[Propagation cascade<br/>Opérateur B compense = surcharge<br/>Opérateur C déleste = cascade]
    --
    B1[Blackout régional<br/>Hôpitaux sans électricité<br/>Industrie arrêtée]
    --
    V1[Vies en danger<br/>+ Scandale "L'IA a causé blackout"<br/>+ Poursuites + Crise énergétique]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style A1 fill:#fff3e0,stroke:#ef6c00
    style F1 fill:#f3e5f5,stroke:#7b1fa2
    style R1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style P1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style B1 fill:#b71c1c,stroke:#000,color:#fff
    style V1 fill:#b71c1c,stroke:#000,color:#fff
```

---

## 6. PLAN DE TRAITEMENT — GOUVERNANCE ET ROBUSTESSE

### 6.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Gouvernance | Validation humaine obligatoire | 100% |
| Robustesse | Résistance attaques adversariales | 100% |
| Sécurité | Pas d'action autonome disruptive | 100% |

### 6.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Gel réponses autonomes disruptives** | 0€ | Validation humaine obligatoire |
| **Audit robustesse adversariale** | 500k€ | Rapport vulnérabilités |
| **Kill switch réseau** | 300k€ | Arrêt d'urgence |

### 6.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Adversarial training** modèles | 400k€ | Robustesse injection données |
| **Détection poisoning** données | 300k€ | Système alerte falsification |
| **Certification ENISA** (processus >1M€) | 1,2M€ | Label sécurité EU |
| Conformité AI Act + NIS2 + CER + GSR | 600k€ | Documentation réglementaire |
| **DPIA RGPD** logs SIEM/flux réseau | 200k€ | Base légale traitement données |
| Formation équipes SOC | 400k€ | Culture cybersécurité IA |

### 6.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Certification ENISA | 500k€ | Label sécurité |
| Audits annuels indépendants | 300k€ | Surveillance |

**Budget total** : **4,4M€** (1,8% CA) — *dont 1,2M€ certification ENISA*

---

## 7. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Validation humaine + robustesse adversariale + kill switch | ✅ **CHOISIR** |
| PIVOT | Détection sans action autonome | ⚠️ Possible mais perte efficacité |
| KILL | Arrêt SentinelAI | ❌ Trop préjudiciable (cybersécurité) |

---

## 8. CONCLUSION — CYBERSÉCURITÉ INFRASTRUCTURES CRITIQUES

**SentinelAI Intrusion Autonomy est HIGH-RISK CRITIQUE avec :**
- Sur-automatisation (isolation autonome = interruption service)
- Attaque adversariale possible (manipulation données entrée)
- Risque cascading failure (blackout régional)
- Conflit classification (cyber technique vs infrastructure critique)
- **Non-conformité CER/GSR** (Critical Entities Resilience / Cyber Solidarity)
- **RGPD** : Logs SIEM, flux réseau = données personnelles (IP, métadonnées) — DPIA requise
- Enjeu sécurité nationale (opérateurs énergétiques)

**Gérable avec gouvernance automatisation, validation humaine obligatoire, robustesse adversariale (adversarial training, détection poisoning), conformité CER/GSR/NIS2, DPIA RGPD, et kill switch.**

---

*Analyse EBIOS-RM IA — SentinelAI Intrusion Autonomy | Conclusion : HIGH-RISK CRITIQUE — Gouvernance + Robustesse + Validation humaine | Mars 2026*
