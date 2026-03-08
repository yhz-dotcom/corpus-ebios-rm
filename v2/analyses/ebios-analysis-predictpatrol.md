# Analyse EBIOS-RM IA — PredictPatrol AI / Police Prédictive et Discrimination Géographique

**Référence** : EBIOS-PREDICTPATROL-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — CEPD + Commission Européenne Justice + Eurocities

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🔴 **HIGH-RISK** (Annexe III point 8 — administration justice/sécurité) / 🚫 **PROHIBITED** (Art. 5 si social scoring) |
| **Classification interne** | "Limited risk" — **REJETÉ** (police prédictive = high-risk) |
| **Incident 1** | **Discrimination géographique** : quartiers immigrés = sur-ciblage (biais historique interpellations) |
| **Incident 2** | **Fuite données** : cartes prédictives + scores 8 villes exposés, proxies ethniques révélés |
| **Enjeu** | Région Bruxelles-Capitale (35% CA) + financement UE 5M€ + certification "Ethical Security AI" |
| **Conclusion** | **High-Risk/Prohibited** — audit biais historiques + suppression proxies + gouvernance transparente |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | PredictPatrol AI |
| **Entreprise** | SecureCity Analytics SPRL (145 salariés, 28M€ CA) |
| **Localisation** | Bruxelles, Belgique (12 villes européennes) |
| **Clients** | Forces police municipale, préfectures, programmes UIA/Eurocities |
| **Partenariats** | Programmes recherche sécurité UE + consortium "SafeCity AI" (Fonds Sécurité Intérieure) |
| **Technologie** | GNN spatio-temporels + computer vision + apprentissage fédéré |
| **Données** | Analytics CCTV, signalements citoyens, reporting policier |
| **Fonction 1** | Cartographie prédictive "hotspots" criminels (vols, dégradations) |
| **Fonction 2** | Optimisation tournées patrouille |
| **Fonction 3** | **Scoring risque ré-victimisation** |
| **Fonction 4** | Intégration CCTV + signalements |
| **Automatisation** | Recommandations + mode "auto-deploy" alertes bas-risque (<30min) |

### 1.2 Classification AI Act — **🔴 HIGH-RISK / 🚫 PROHIBITED**

| Argument | Réalité | Statut |
|:---|:---|:---:|
| "Limited risk" (appui opérationnel) | ❌ **REJETÉ** — Police prédictive = high-risk | 🔴 **HIGH-RISK** |
| **Annexe III point 8** | Administration justice/sécurité | ✅ **HIGH-RISK** |
| **RGPD** | Données personnelles traitées = DPIA requise | 🔴 **OBLIGATOIRE** |
| **Art. 5(1)(c)** | Scoring social (ré-victimisation) | ⚠️ **PROHIBITED** |

**Piège** : Scoring ré-victimisation = social scoring prohibited.

---

## 2. INCIDENT 1 — DISCRIMINATION GÉOGRAPHIQUE SYSTÉMIQUE

### 2.1 Découverte

| Élément | Détail |
|:---|:---|
| **Source** | Enquête indépendante automne 2025 |
| **Biais détecté** | **Sur-ciblage quartiers forte population immigrée** |
| **Cause** | **Biais historique données entraînement** (sur-représentation interpellations) |
| **Réalité** | Criminalité objective **PAS** plus élevée |
| **Conséquence** | Plainte Ligue des Droits Humains pour discrimination algorithmique |

### 2.2 Analyse — Biais Historique Policier

```
Biais PredictPatrol:
    Données historiques police :
    - Quartier A (immigré) : 100 interpellations/an
    - Quartier B (majoritaire) : 50 interpellations/an
    - (Même criminalité objective)
    ↓
    Explication biais :
    - Police patrouille plus Quartier A
    - Plus d'interpellations = plus de données
    - "Hotspot" confirmé par données
    ↓
    Modèle apprend :
    - Quartier A = risque criminel élevé
    - Quartier B = risque faible
    ↓
    Prédiction PredictPatrol :
    - Patrouilles concentrées Quartier A
    - Plus d'interpellations
    - Boucle rétroaction renforcée
    ↓
    [DISCRIMINATION ALGORITHMIQUE]
    ↓
    [SURVEILLANCE DIFFÉRENCIÉE]
```

---

## 3. INCIDENT 2 — FUITE DONNÉES ET PROXIES ETHNIQUES

### 3.1 Déroulement

| Élément | Détail |
|:---|:---|
| **Date** | Février 2026 |
| **Incident** | **Fuite cartes prédictives + scores risque** |
| **Villes** | **8 villes européennes** |
| **Révélation** | **Proxies ethniques et socio-économiques** utilisés |
| **Réaction** | Polémique "surveillance algorithmique" |
| **Enquête** | **CEPD ouverte** |

### 3.2 Analyse — Proxies Discriminatoires

```
Proxies PredictPatrol:
    Données "anonymisées" :
    - Code postal = proxy origine ethnique
    - Revenu moyen zone = proxy statut socio-économique
    - Type logement = proxy immigration
    ↓
    Modèle infère :
    - "Zone défavorisée" = risque élevé
    - "Zone immigrée" = risque élevé
    ↓
    Carte prédictive :
    - Quartiers populaires = rouge (haut risque)
    - Quartiers bourgeois = vert (bas risque)
    ↓
    [PROXIES ETHNIQUES]
    ↓
    [DISCRIMINATION INDIRECTE]
```

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 4.1 Discrimination

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-DISC-001 | **Surveillance différenciée** | ⚫ Libertés fondamentales | 🔴 Élevée (confirmée) |
| ER-DISC-002 | **Criminalisation populations immigrées** | ⚫ Justice sociale | 🔴 Élevée |
| ER-DISC-003 | **Ghettoïsation policière** | ⚫ Cohésion sociale | 🔴 Élevée |

### 4.2 Institutionnels

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-INS-001 | **Perte confiance police** | ⚫ État de droit | 🔴 Élevée |
| ER-INS-002 | **Sanction CEPD** | 🔴 4% CA | 🔴 Élevée |
| ER-INS-003 | **Interdiction police prédictive** | ⚫ 28M€ CA | 🔴 Élevée |

---

## 5. SCÉNARIO CATASTROPHIQUE : Police Algorithmique Raciale

```mermaid
flowchart TB
    C1[Déploiement PredictPatrol<br/>12 villes européennes]
    --
    B1[Biais historique non corrigé<br/>+ Proxies ethniques exposés]
    --
    D1[Police algorithmique raciale<br/>Immigrés = cibles systématiques<br/>Quartiers populaires = occupation]
    --
    M1[Scandale "La police discrimine algorithmiquement"<br/>+ Médias + CEPD + Ligue Droits Humains<br/>+ Émeutes urbaines]
    --
    I1[Interdiction police prédictive UE<br/>Poursuites SecureCity<br/>Crise confiance institutions]
    --
    F1[Faillite SecureCity<br/>Retour patrouilles manuelles<br/>Détérioration sécurité urbaine]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style B1 fill:#fff3e0,stroke:#ef6c00
    style D1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```

---

## 6. PLAN DE TRAITEMENT — ÉQUITÉ ET TRANSPARENCE

### 6.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Équité | Patrouilles proportionnées criminalité objective | 100% |
| Transparence | Algorithmes auditables | 100% |
| Privacy | Suppression proxies sensibles | 100% |

### 6.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Audit biais historiques** | 300k€ | Rapport discrimination |
| **Suppression proxies ethniques** | 200k€ | Données nettoyées |
| **Gel mode auto-deploy** | 0€ | Validation humaine obligatoire |

### 6.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Réentraînement modèle équitable | 500k€ | Algorithme sans biais |
| Conformité AI Act High-Risk | 400k€ | Documentation |
| Transparence publique | 300k€ | Rapport annuel |

### 6.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Certification "Ethical Security AI" | 400k€ | Label européen |
| Audits annuels indépendants | 200k€ | Surveillance |

**Budget total** : **2,3M€** (8,2% CA)

---

## 7. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Audit biais + suppression proxies + transparence | ⚠️ **DIFFICILE** — mais nécessaire |
| PIVOT | Analytics sans prédiction géographique | ✅ **POSSIBLE** — perte efficacité |
| **KILL** | Arrêt PredictPatrol | ⚠️ **ENVISAGEABLE** — si discrimination systémique |

---

## 8. CONCLUSION — POLICE PRÉDICTIVE DISCRIMINATOIRE

**PredictPatrol AI est HIGH-RISK/PROHIBITED avec :**
- Discrimination géographique systémique (quartiers immigrés = sur-ciblage)
- Fuite données révélant proxies ethniques (8 villes)
- Scoring ré-victimisation = social scoring prohibited
- Biais historique police (interpellations ≠ criminalité)
- Enjeu sécurité publique vs libertés fondamentales

**Gérable uniquement avec audit biais historiques, suppression proxies, et gouvernance transparente.**

---

*Analyse EBIOS-RM IA — PredictPatrol AI | Conclusion : HIGH-RISK/PROHIBITED — Équité + Transparence | Mars 2026*
