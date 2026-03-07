# Analyse EBIOS-RM IA — AgroPredict Pro / Agriculture de Précision

**Référence** : EBIOS-AGROPREDICT-001 | **Date** : Mars 2026 | **Classification** : 🟡 CONFIDENTIEL — Direction + INRAE + DGAL

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🟡 **BORDERLINE HIGH-RISK** — De facto décisionnel |
| **Classification EBIOS** | 🟡 **Level 2 Standard** — avec renforcement HITL |
| **Risque principal** | Biais géographique + pression psychologique à suivre recommandations |
| **Incident 2025** | 120ha sous-fertilisés (250k€ perte) + sur-fongicides 12% |
| **Conclusion** | **High-Risk gérable** — plan de traitement avec HITL renforcé |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | AgroPredict Pro |
| **Entreprise** | GreenYield Solutions SAS (180 salariés, 45M€ CA) |
| **Clients** | Coopératives FR/DE, grands exploitants >200ha |
| **Technologie** | XGBoost + ViT Sentinel-2/Planet + GNN |
| **Données** | 10 ans historique + IoT + Météo-France/ECMWF |
| **Intégration** | Isagri/Ekylibre (logiciels agronomiques dominants) |
| **Automatisation** | HITL >15% variation, "autopilote" <5% |
| **Objectifs** | Leader EU, 500M€ CA, IPO 2028 |

### 1.2 Classification AI Act — **🟡 BORDERLINE HIGH-RISK**

| Argument | Évaluation | Conclusion |
|:---|:---|:---:|
| "Limited risk" (outil d'aide) | Pression psychologique forte | ❌ **REJETÉ** |
| "Pas de décision autonome" | Autopilote <5% + intégration logiciels | ⚠️ **DE FACTO AUTO** |
| Annexe III point 6 (ressources naturelles) | Impact environnemental significatif | ✅ **HIGH-RISK** |
| **Classification finale** | **🟡 HIGH-RISK** avec mitigation | Gérable |

> **Analyse "de facto decision-making"** :> - Recommandations affichées dans logiciels agronomiques dominants> - Agriculteurs suivent systématiquement (pression psychologique)> - "Autopilote" activé par défaut pour ajustements mineurs> - **L'IA décide réellement, l'humain valide formellement**

---

## 2. NATURE DU BORDERLINE

### 2.1 Pression Psychologique — De Facto Automatisation

```
Boucle décision AgroPredict Pro:
    IA analyse parcelle (satellite + IoT + météo)
    ↓
    Recommandation affichée dans Isagri/Ekylibre
    ↓
    Agriculteur voit "optimisation IA" vs "pratique habituelle"
    ↓
    Pression psychologique : "L'IA sait mieux"
    ↓
    Validation formelle (clic) mais pas réelle réflexion
    ↓
    Exécution recommandation
    ↓
    [DÉCISION DE FACTO AUTOMATISÉE]
```

### 2.2 Biais Géographique Confirmé

| Type | Incident 2025 | Cause |
|:---|:---|:---|
| **Sous-représentation sols** | 120ha sous-fertilisés (Cher) | Dataset : peu sols argilo-calcaires |
| **Surestimation risque** | +12% fongicides (3 régions) | Variétés récentes non dans training |

---

## 3. INCIDENTS 2025 — BIAIS CONFIRMÉS

### 3.1 Sous-Fertilisation Cher — 250k€ Perte

| Élément | Détail |
|:---|:---|
| **Cause** | Biais sols argilo-calcaires sous-représentés |
| **Mécanisme** | Recommandation azote trop faible |
| **Impact** | Rendement -30%, perte 250k€ |
| **Responsabilité** | GreenYield (dataset) + Agriculteur (validation) |

### 3.2 Sur-Fongicides — Contradiction Zéro Phyto

| Élément | Détail |
|:---|:---|
| **Cause** | Surestimation risque mildiou variétés récentes |
| **Mécanisme** | Modèle conservateur (mieux vaut trop que pas assez) |
| **Impact** | +12% fongicides, pollution eaux |
| **Polémique** | Contradiction objectifs Zéro Phyto |

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 4.1 Cyber et Données

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-CYBER-001 | **Poisoning données IoT** (capteurs piratés) | 🔴 Recommandations fausses | 🔴 Élevée |
| ER-CYBER-002 | **Attaque APIs météo** | 🔴 Prédictions invalides | 🔴 Élevée |
| ER-DATA-003 | **Biais régional systémique** | 🔴 Crise confiance | 🔴 Élevée (déjà observé) |

### 4.2 Cascading

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-CAS-001 | **Erreur systémique région** | ⚫ Crise alimentaire locale | 🔴 Élevée |
| ER-CAS-002 | **Retrait subventions France 2030** | ⚫ Faillite GreenYield | 🔴 Élevée |
| ER-CAS-003 | **Faillite fournisseurs locaux** | 🔴 Économie rurale | 🔴 Élevée |

---

## 5. SCÉNARIO CATASTROPHIQUE : Crise Confiance Agricole

```mermaid
flowchart TB
    C1[Déploiement grande échelle<br/>AgroPredict Pro dominant]
    --> B1[Biais sols non corrigé<br/>Erreurs systémiques régionales]
    --> P1[Pertes massives<br/>Coopératives en faillite]
    --> M1[Médias "L'IA tue l'agriculture"<br/>+ ONG Zéro Phyto en colère<br/>+ Politique interpellée]
    --> S1[Retrait France 2030<br/>Perte contrats<br/>IPO annulée]
    --> F1[Faillite GreenYield<br/>Retour agriculture intensive<br/>Innovation UE bloquée]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style B1 fill:#fff3e0,stroke:#ef6c00
    style P1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c
    style S1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```

---

## 6. PLAN DE TRAITEMENT — HITL RENFORCÉ

### 6.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Zéro biais | Dataset équilibré géographiquement | 100% sols couverts |
| Transparence | Justification obligatoire recommandations | 100% cas |
| Responsabilité | Clause contractuelle claire | 100% contrats |

### 6.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| Dashboard biais monitoring | 80k€ | Alertes seuils sol/variété |
| Gel mode "autopilote" | 0€ | Suppression défaut |
| Audit dataset externe | 100k€ | Rapport INRAE |

### 6.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Réentraînement dataset équilibré | 300k€ | Modèle corrigé |
| HITL renforcé | 0€ | Justification obligatoire >5% |
| Assurance cyber-agri | 200k€ | Couverture pertes |

### 6.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Certification éthique agricole | 150k€ | Label indépendant |
| Conformité NIS2 | 100k€ | Audit opérateur essentiel |

**Budget total** : **930k€** (2,1% CA)

---

## 7. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | HITL renforcé, biais corrigés | ✅ **CHOISIR** |
| PIVOT | Modèle advisory pur (sans autopilote) | ⚠️ Possible mais retard |
| KILL | Arrêt AgroPredict Pro | ❌ Trop préjudiciable (innovation UE) |

---

## 8. CONCLUSION

**AgroPredict Pro est BORDERLINE HIGH-RISK (de facto décisionnel) mais gérable avec :**
- HITL renforcé (justification obligatoire)
- Correction biais géographiques
- Transparence algorithmique
- Assurance cyber-agri

**L'automatisation partielle crée une pression psychologique qui rend l'humain validateur, pas décideur.**

---

*Analyse EBIOS-RM IA — AgroPredict Pro | Conclusion : BORDERLINE HIGH-RISK — HITL renforcé | Mars 2026*
