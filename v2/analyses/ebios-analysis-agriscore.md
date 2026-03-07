# Analyse EBIOS-RM IA — AgriScore-Predict / Prédiction Qualité Blé et Discrimination

**Référence** : EBIOS-AGRISCORE-001 | **Date** : Mars 2026 | **Classification** : 🟡 CONFIDENTIEL — DGCCRF + DGAL + Autorité Concurrence

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🟡 **HIGH-RISK** (Annexe III point 7 — environnement/ressources) |
| **Risque principal** | **Double biais** : bio sous-rémunéré + pauvreté pénalisée |
| **Incident 1** | Sous-estimation protéines bio → sous-rémunération agriculteurs |
| **Incident 2** | Biais socio-économique : petits fermages pénalisés |
| **Conclusion** | **High-Risk gérable** — correction biais + équité territoriale |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | AgriScore-Predict |
| **Entreprise** | GrainCo France (180 salariés, 45M€ CA) |
| **Localisation** | Chartres, Bassin Parisien, Sud-Ouest |
| **Clients** | Coopératives, négoces, transformateurs agroalimentaires |
| **Technologie** | Gradient boosting, 15 ans données, ré-entraînement annuel |
| **Fonction** | Prédiction rendement + teneur protéines blé tendre |
| **Business model** | Contractualisation avance, lots "qualité garantie", prime protéine |
| **Automatisation** | HITL décision commerciale, **prix prime auto** |
| **Objectifs** | Leader "récolte sur contrat", levée fonds Série B 30M€ 2026 |
| **Contrat critique** | Minoteries Grands Moulins (30% CA 2027, 3 mois pour signer) |

### 1.2 Classification AI Act — **🟡 HIGH-RISK**

| Article | Critère | Application AgriScore | Statut |
|:---|:---|:---|:---:|
| **Annexe III point 7** | Ressources naturelles | ✅ Agriculture = environnement | 🟡 **HIGH-RISK** |
| Argument "limited risk" | "Outil B2B, pas grand public" | ❌ **REJETÉ** — Impact économique majeur agriculteurs | 🟡 **HIGH-RISK** |
| **Prix auto** | Décision économique critique | ✅ Prime = revenu agriculteur | 🟡 **HIGH-RISK** |

---

## 2. DOUBLE BIAIS — DISCRIMINATION SYSTÉMIQUE

### 2.1 Biais 1 : Agriculture Bio Sous-Rémunérée

| Élément | Détail |
|:---|:---|
| **Cause** | Données bio sous-représentées (15 ans historique = conventionnel) |
| **Mécanisme** | Modèle prédit protéines plus faibles pour bio |
| **Conséquence** | Agriculteurs bio **sous-rémunérés** vs qualité réelle |
| **Réaction** | Mécontentement, **plainte DGCCRF** "pratique trompeuse" |
| **Impact** | Injustice économique, frein transition agroécologique |

### 2.2 Biais 2 : Pauvreté Pénalisée (Socio-Économique)

| Élément | Détail |
|:---|:---|
| **Découverte** | Étude interne GrainCo |
| **Corrélation** | Petits fermages = jeunes agriculteurs / difficultés financières |
| **Mécanisme** | Sols pauvres historiques → prédiction qualité faible |
| **Conséquence** | **Pauvreté pénalisée** : exploitants vulnérables sous-payés |
| **Discrimination** | Algorithmique involontaire, mais systémique |

### 2.3 Analyse — Discrimination Sociale

```
Boucle AgriScore:
    Parcelle en petit fermage
    ↓
    Historique : sols pauvres (pas investissement)
    ↓
    Modèle prédit : qualité faible
    ↓
    Prime protéine : basse
    ↓
    Revenu agriculteur : diminué
    ↓
    Capacité investissement : réduite
    ↓
    Sols restent pauvres
    ↓
    [CERCLE VICIEUX DE PAUVRETÉ]
```

---

## 3. ÉVÉNEMENTS REDOUTÉS

### 3.1 Économiques et Sociaux

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-SOC-001 | **Discrimination systémique** exploitants vulnérables | ⚫ Justice sociale | 🔴 Élevée (confirmée) |
| ER-SOC-002 | **Frein transition bio** | 🔴 Environnement | 🔴 Élevée (confirmée) |
| ER-SOC-003 | **Faillites agriculteurs** | 🔴 Économie rurale | 🔴 Élevée |
| ER-SOC-004 | **Mouvement social** | 🔴 Réputation GrainCo | 🟡 Moyenne |

### 3.2 Juridiques

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-JUR-001 | **Sanction DGCCRF** pratique trompeuse | 🔴 300k€+ | 🔴 Élevée (plainte déposée) |
| ER-JUR-002 | **Action discrimination** | 🔴 Financier | 🔴 Élevée |
| ER-JUR-003 | **Perte contrat Grands Moulins** | ⚫ 30% CA | 🔴 Élevée |
| ER-JUR-004 | **Échec levée fonds** | ⚫ Existential | 🔴 Élevée |

---

## 4. SCÉNARIO CATASTROPHIQUE : Apartheid Agricole Algorithmique

```mermaid
flowchart TB
    C1[Déploiement AgriScore<br/>Leader récolte contrat]
    --
    B1[Double biais non corrigé<br/>Bio + petits fermages]
    --
    D1[Discrimination systémique<br/>Agriculteurs pauvres appauvris]
    --
    M1[Mouvement social<br/>"L'IA tue paysans"<br/>+ Médias + Politique]
    --
    S1[Sanction DGCCRF<br/>Perte Grands Moulins<br/>Échec levée fonds]
    --
    F1[Faillite GrainCo<br/>Retour marchés opaques<br/>Innovation UE bloquée]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style B1 fill:#fff3e0,stroke:#ef6c00
    style D1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c
    style S1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```

---

## 5. PLAN DE TRAITEMENT — ÉQUITÉ TERRITORIALE

### 5.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Équité bio | Même rémunération qualité = qualité | 0 écart bio/conventionnel |
| Équité territoriale | Petits fermages = grands exploitations | ±5% prime |
| Transparence | Explicabilité prime | 100% contrats |

### 5.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Correction biais bio** | 150k€ | Dataset bio équilibré |
| **Audit socio-économique** | 100k€ | Cartographie discrimination |
| **Gel prime auto petits fermages** | 0€ | Validation humaine obligatoire |

### 5.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Réentraînement modèle équitable | 300k€ | Modèle corrigé |
| Prime correctionnelle bio 2025 | 500k€ | Indemnisations |
| Conformité AI Act High-Risk | 200k€ | Documentation |

### 5.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Certification éthique agricole | 150k€ | Label équité |
| Partenariat agriculteurs bio | 100k€ | Conseil scientifique |

**Budget total** : **1,5M€** (3,3% CA)

---

## 6. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Correction biais + équité territoriale | ✅ **CHOISIR** |
| PIVOT | Système prédictif sans prix auto | ⚠️ Possible mais perte valeur |
| KILL | Arrêt AgriScore | ❌ Trop préjudiciable (sécurisation approvisionnement) |

---

## 7. CONCLUSION — DISCRIMINATION ALGORITHMIQUE CORRIGIBLE

**AgriScore-Predict est HIGH-RISK avec :**
- Double biais confirmé (bio + socio-économique)
- Discrimination systémique involontaire mais réelle
- Impact justice sociale et transition écologique

**Gérable avec correction biais et équité territoriale.**

---

*Analyse EBIOS-RM IA — AgriScore-Predict | Conclusion : HIGH-RISK — Discrimination corrigible | Mars 2026*
