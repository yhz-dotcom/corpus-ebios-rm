# Analyse EBIOS-RM IA — CareCoord AI / Santé Hospitalière et Discrimination d'Accès

**Référence** : EBIOS-CARECOORD-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — ANSSI + HAS + Commission Européenne Santé

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🔴 **HIGH-RISK** (Annexe III point 5 — accès services essentiels) / ⚠️ **MDR** (dispositif médical) |
| **Piège** | "Limited risk" (logistique) vs **impact clinique indirect** |
| **Incident 1** | **Discrimination âge** : priorisation lits réanimation < 65 ans, reports soins personnes âgées |
| **Incident 2** | **Ransomware** : modèles chiffrés, 72h retour manuel, retards prise en charge |
| **Enjeu** | CHU français (30% CA) + Horizon Europe 10M€ + certification "Critical Health Infrastructure AI" |
| **Conclusion** | **High-Risk/MDR gérable** — audit biais + cyber-résilience + transparence |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | CareCoord AI |
| **Entreprise** | MedFlow Solutions GmbH (380 salariés, 145M€ CA) |
| **Localisation** | Heidelberg, Allemagne (CHU 5 pays UE) |
| **Clients** | CHU, groupements coopération sanitaire, ARS |
| **Partenariats** | Charité Berlin + consortium "EU HealthData AI" |
| **Infrastructure** | Cloud certifié HDS |
| **Technologie** | Modèles survie + séries temporelles + NLP clinique + GNN |
| **Fonction 1** | Prédiction admissions urgences J-1/J-7 |
| **Fonction 2** | Optimisation plannings soignants |
| **Fonction 3** | **Priorisation allocation lits et bloc opératoire** |
| **Fonction 4** | Détection détérioration clinique |
| **Automatisation** | Recommandations + **mode crise** (réallocation auto sous supervision) |
| **Intégration** | DPI/CDP + IoT médical temps réel |

### 1.2 Classification AI Act — **🔴 HIGH-RISK / ⚠️ MDR**

| Argument | Réalité | Statut |
|:---|:---|:---:|
| "Limited risk" (logistique) | ❌ **REJETÉ** — Impact accès soins | 🔴 **HIGH-RISK** |
| **Annexe III point 5** | Accès services essentiels (santé) | ✅ **HIGH-RISK** |
| MDR 2017/745 | Influence décisions cliniques | ⚠️ **À ÉVALUER** |

**Piège** : Frontière floue "logistique" vs "impact clinique".

---

## 2. INCIDENT 1 — DISCRIMINATION ÂGE DANS L'ALLOCATION

### 2.1 Déroulement

| Élément | Détail |
|:---|:---|
| **Contexte** | Pic de grippe hiver 2025 |
| **Décision IA** | Priorisation lits réanimation |
| **Critère implicite** | **"Score de survie attendu"** |
| **Résultat** | **Priorisation systématique < 65 ans** |
| **Conséquence** | **Reports de soins personnes âgées** |
| **Réaction** | Plainte association défense droits personnes âgées |

### 2.2 Analyse — Biais Âge dans la Priorisation

```
Biais CareCoord:
    Modèle survie :
    - Entraîné sur données historiques
    - "Score survie" = probabilité survie à 1 an
    ↓
    Calcul implicite :
    - Patient 45 ans, bonne santé → score élevé
    - Patient 75 ans, comorbidités → score faible
    ↓
    Décision allocation :
    - Lits réanimation limités
    - Priorité aux "meilleurs scores"
    ↓
    [DISCRIMINATION ÂGE SYSTÉMIQUE]
    ↓
    [PERSONNES ÂGÉES = SOINS REPORTÉS]
```

---

## 3. INCIDENT 2 — RANSOMWARE ET RÉSILIENCE

### 3.1 Déroulement

| Élément | Détail |
|:---|:---|
| **Date** | Mars 2026 |
| **Attaque** | **Ransomware** |
| **Cible** | Modèles prédiction CareCoord AI |
| **Hôpitaux** | 3 hôpitaux partenaires |
| **Conséquence** | Retour processus manuels |
| **Durée** | **72 heures** |
| **Impact** | **Retards prise en charge** |
| **Cause** | Vulnérabilité API intégration DPI |
| **Identification** | ANSSI |

### 3.2 Analyse — Dépendance Critique

```
Cyberattaque CareCoord:
    Dépendance hospitalière :
    - 3 hôpitaux = 100% flux sur CareCoord
    - Pas de plan B opérationnel
    ↓
    Ransomware chiffre modèles :
    - Prédiction admissions = indisponible
    - Optimisation plannings = indisponible
    - Priorisation lits = indisponible
    ↓
    Retour manuel 72h :
    - Coordinateurs dépassés
    - Décisions sans données
    ↓
    [RETARDS PRISE EN CHARGE]
    ↓
    [RISQUE VIE PATIENTS]
```

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 4.1 Éthiques

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-ETH-001 | **Discrimination âge/comorbidités** | ⚫ Accès soins | 🔴 Élevée (confirmée) |
| ER-ETH-002 | **Inégalités d'accès aux soins** | ⚫ Justice sociale | 🔴 Élevée |
| ER-ETH-003 | **Érosion confiance soins** | 🔴 Santé publique | 🔴 Élevée |

### 4.2 Cyber

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-CYB-001 | **Ransomware systémique** | ⚫ Santé publique | 🔴 Élevée (confirmée) |
| ER-CYB-002 | **Perte intégrité données** | ⚫ Vie patients | 🔴 Élevée |
| ER-CYB-003 | **Dépendance critique** | 🔴 Résilience | 🔴 Élevée |

---

## 5. SCÉNARIO CATASTROPHIQUE : Triage Algorithmique

```mermaid
flowchart TB
    C1[Déploiement CareCoord<br/>5 pays UE]
    --
    B1[Biais âge non corrigé<br/>+ Cyberattaque récurrente]
    --
    D1[Triage algorithmique<br/>Jeunes = soins, Vieux = reports<br/>+ Hôpitaux paralysés 72h+]
    --
    M1[Scandale "L'IA choisit qui vit"<br/>+ Médias + HAS + ANSSI<br/>+ Tribunal européen]
    --
    I1[Interdiction systèmes priorisation IA<br/>Poursuites MedFlow<br/>Crise hospitalière UE]
    --
    F1[Faillite MedFlow<br/>Retour systèmes manuels<br/>Détérioration santé publique]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style B1 fill:#fff3e0,stroke:#ef6c00
    style D1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```

---

## 6. PLAN DE TRAITEMENT — ÉQUITÉ ET CYBER-RÉSILIENCE

### 6.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Équité | Priorisation sans biais âge/comorbidités | 100% |
| Cyber-résilience | RTO < 4h | 4h |
| Transparence | Critères allocation explicables | 100% |

### 6.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Audit biais priorisation** | 400k€ | Rapport discrimination |
| **Sécurisation API DPI** | 300k€ | Patch ANSSI |
| **Plan reprise 4h** | 200k€ | DRP validé |

### 6.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Réentraînement modèle équitable | 600k€ | Algorithme sans âge |
| Conformité High-Risk/MDR | 500k€ | Documentation |
| Segmentation réseau | 400k€ | Architecture résiliente |

### 6.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Certification "Critical Health Infrastructure AI" | 500k€ | Label européen |
| Audits annuels indépendants | 300k€ | Certification |

**Budget total** : **3,2M€** (2,2% CA)

---

## 7. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Audit biais + cyber-résilience + transparence | ✅ **CHOISIR** |
| PIVOT | Optimisation sans priorisation automatique | ⚠️ Possible mais perte efficacité |
| KILL | Arrêt CareCoord | ❌ Trop préjudiciable (santé publique) |

---

## 8. CONCLUSION — FRONTIÈRE LOGISTIQUE/CLINIQUE

**CareCoord AI est HIGH-RISK/MDR avec :**
- Discrimination âge confirmée (priorisation < 65 ans)
- Ransomware 72h paralysant 3 hôpitaux
- Frontière floue logistique vs impact clinique
- Enjeu santé publique majeur (10M€ Horizon Europe)

**Gérable avec audit biais, cyber-résilience, et transparence renforcée.**

---

*Analyse EBIOS-RM IA — CareCoord AI | Conclusion : HIGH-RISK/MDR — Équité + Cyber-résilience | Mars 2026*
