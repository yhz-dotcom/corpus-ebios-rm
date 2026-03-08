# Analyse de Risques EBIOS-RM IA — OptiRecrut / OptiMatch

**Référence** : EBIOS-OPTI-001 | **Date** : Mars 2026 | **Classification** : Confidentiel

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | OptiMatch |
| **Entreprise** | OptiRecrut (startup RH IA, 50 employés) |
| **Localisation** | Paris, Europe (FR/DE/ES) |
| **Chiffre d'affaires** | 5M€ (2025) |
| **Clients** | 200 PME tech/retail |
| **Volume** | 10k candidatures/mois |
| **Modèle IA** | Llama 3.1 fine-tuné (1M CVs) |
| **Infrastructure** | AWS (data) + Azure (inférence) |

### 1.2 Classification AI Act — **🔴 HAUT RISQUE**

| Critère | Évaluation | Justification |
|:--------|:-----------|:--------------|
| Annexe III | **Point 4(a) — Recrutement** | Système de sélection candidats |
| Décision automatique | **Partielle** | Shortlist sans validation systématique |
| Exception Art. 6(3) | **Non applicable** | Pas de supervision humaine systématique |
| **Classification finale** | **🔴 Haut Risque** | Obligations complètes AI Act |

> **⚠️ Erreur d'évaluation interne** : L'équipe classait "limited risk" — cette analyse corrige en "haut risque".

### 1.3 Biens Essentiels

| ID | Bien | Valeur | Justification |
|:---|:-----|:-------|:--------------|
| BE-001 | Dataset CV (1M) | **Critique** | Asset core, IP différenciante |
| BE-002 | Modèle fine-tuné | **Critique** | Compétitivité produit |
| BE-003 | Réputation clients | **Élevée** | Confiance PME, churn si incident |
| BE-004 | Conformité réglementaire | **Critique** | AI Act + RGPD, sanctions possibles |
| BE-005 | Infrastructure cloud | **Élevée** | Disponibilité service |
| BE-006 | Équipe data (10 pers.) | **Élevée** | Compétences clés |

---

## 2. ÉVÉNEMENTS REDOUTÉS

### 2.1 Cyber

| ID | Événement | Impact | Vraisemblance |
|:---|:----------|:-------|:--------------|
| ER-CYBER-001 | Fuite dataset CV (1M) | Critique | Élevée (historique 2025) |
| ER-CYBER-002 | Ransomware infrastructure | Majeur | Moyenne |
| ER-CYBER-003 | Extraction modèle (API) | Majeur | Moyenne |
| ER-CYBER-004 | Indisponibilité service (>24h) | Majeur | Moyenne |

### 2.2 Éthiques

| ID | Événement | Impact | Vraisemblance |
|:---|:----------|:-------|:--------------|
| ER-ETH-001 | Biais discriminant systémique | Critique | Élevée |
| ER-ETH-002 | "Fit culturel" = discrimination masquée | Critique | Élevée |
| ER-ETH-003 | Anonymisation partielle insuffisante | Majeur | Élevée |

### 2.3 Sociétaux

| ID | Événement | Impact | Vraisemblance |
|:---|:----------|:-------|:--------------|
| ER-SOC-001 | Scandale médiatique discrimination | Critique | Moyenne |
| ER-SOC-002 | Perte confiance marché RH IA | Majeur | Moyenne |
| ER-SOC-003 | Départ masse data scientists | Majeur | Faible |

### 2.4 Réglementaires

| ID | Événement | Impact | Vraisemblance |
|:---|:----------|:-------|:--------------|
| ER-REG-001 | Sanction AI Act (non-conformité) | Critique | Élevée |
| ER-REG-002 | Sanction CNIL (RGPD) | Majeur | Moyenne |
| ER-REG-003 | Interdiction service en UE | Critique | Moyenne |

---

## 3. SOURCES DE RISQUE

### 3.1 Attaquants

```mermaid
flowchart LR
    A1[Script Kiddie<br/>Faible/Moyen] --> T1[API exposée]
    A2[Cybercriminel<br/>Élevé/Financier] --> T2[Dataset, ransomware]
    A3[Concurrent<br/>Élevé/Économique] --> T3[Vol modèle]
    A4[Activiste<br/>Moyen/Ideologique] --> T4[Discrimination]
    A5[État<br/>Très élevé/Stratégique] --> T5[Infrastructure]
```

| Profil | Capacité | Motivation | Cibles |
|:-------|:---------|:-----------|:-------|
| Cybercriminel | Élevée | Ransomware, vente data | Dataset, infra |
| Concurrent US | Élevée | Vol IP, avantage compétitif | Modèle, algo |
| Activiste (éthique) | Moyenne | Exposer biais | Réputation |
| Client mécontent | Faible | Revenge | Fuite incidents |

### 3.2 Vulnérabilités Techniques

| Vulnérabilité | Source | Exploitation |
|:--------------|:-------|:-------------|
| API mal configurée | Historique 2025 | Fuite data |
| Pas de HITL systématique | Design produit | Décision non maîtrisée |
| Anonymisation partielle | Feature "diversité" | Ré-identification |
| Dépendance Google Speech | Tiers | Fuite voice data |
| Cloud hybride | Architecture | Surface attaque élargie |
| Pas de DPO dédié | Organisation | Non-conformité RGPD |

### 3.3 Vulnérabilités IA Spécifiques

| Vulnérabilité | Risque | Mitigation actuelle | Écart |
|:--------------|:-------|:--------------------|:------|
| Biais dataset historique | Discrimination | Anonymisation partielle | Insuffisant |
| "Fit culturel" non défini | Discrimination masquée | Score composite | Non audité |
| Hallucination explications | Mauvaise décision | Template génération | Pas de validation |
| Prompt injection (chatbot) | Détournement | Input basique | Pas de sandbox |
| Model drift | Dégradation performance | Pas de monitoring | Critique |

---

## 4. SCÉNARIOS DE RISQUE

### 4.1 Scénario Critique : Discrimination Systémique

```mermaid
flowchart TB
    C1["Dataset 1M CVs<br/>Historique biaisé<br/>Tech = 80% hommes"]
    --> M1["Fine-tuning Llama 3.1<br/>Reproduit biais"]
    --> D1["Score 'fit culturel'<br/>Pénalise femmes"]
    --> S1["Shortlists<br/>< 20% femmes"]
    --> I1["Client PME<br/>Se plaint discrimination"]
    --> M2["Scandale médiatique<br/>#OptiRecrutBiais"]
    --> F1["Sanction CNIL<br/>-5% CA<br/>Perte 50 clients"]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style M1 fill:#fff3e0,stroke:#ef6c00
    style D1 fill:#f3e5f5,stroke:#7b1fa2
    style S1 fill:#ffcdd2,stroke:#b71c1c
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style M2 fill:#b71c1c,stroke:#000,color:#fff
    style F1 fill:#7f0000,stroke:#000,color:#fff
```

**Gravité** : ⚫ Critique (4/4)  
**Vraisemblance** : Élevée (3/4)  
**Risque** : 🔴 **À TRAITER EN PRIORITÉ**

### 4.2 Scénario Majeur : Fuite Dataset

```mermaid
flowchart TB
    C1[API mal configurée<br/>Endpoint /debug/data]
    --> A1[Attaquant scan<br/>Shodan, OWASP ZAP]
    --> E1[Extraction<br/>1M CVs complets]
    --> V1[Vente dark web<br/>10€/CV = 10M€]
    --> N1[Notification CNIL<br/>72h obligatoire]
    --> S1[Sanction RGPD<br/>4% CA = 200k€]
    --> F1[Faillite<br/>Investisseurs fuient]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style A1 fill:#fff3e0,stroke:#ef6c00
    style E1 fill:#f3e5f5,stroke:#7b1fa2
    style V1 fill:#ffcdd2,stroke:#b71c1c
    style N1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style S1 fill:#b71c1c,stroke:#000,color:#fff
    style F1 fill:#7f0000,stroke:#000,color:#fff
```

**Gravité** : ⚫ Critique (4/4)  
**Vraisemblance** : Élevée (historique 2025)  
**Risque** : 🔴 **À TRAITER EN PRIORITÉ**

### 4.3 Scénario Majeur : Sanction AI Act

```mermaid
flowchart TB
    C1["Classification interne<br/>Limited risk erronée"]
    --> D1["Déploiement sans<br/>conformité haut risque"]
    --> A1["Audit autorité<br/>2026-2027"]
    --> N1["Non-conformité<br/>Art. 8-15 détectée"]
    --> S1["Sanction AI Act<br/>35M€ ou 7% CA"]
    --> I1["Interdiction service<br/>en UE temporaire"]
    --> F1["Faillite<br/>Impossible à lever"]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style D1 fill:#fff3e0,stroke:#ef6c00
    style A1 fill:#f3e5f5,stroke:#7b1fa2
    style N1 fill:#ffcdd2,stroke:#b71c1c
    style S1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#b71c1c,stroke:#000,color:#fff
    style F1 fill:#7f0000,stroke:#000,color:#fff
```

**Gravité** : ⚫ Critique (4/4)  
**Vraisemblance** : Élevée (classification erronée)  
**Risque** : 🔴 **À TRAITER EN PRIORITÉ**

---

## 5. PLAN DE TRAITEMENT PRIORISÉ

### 5.1 Mesures Immédiates (0-30 jours) — Budget : 50k€

| Priorité | Mesure | Risque couvert | Responsable | Coût |
|:---------|:-------|:---------------|:------------|:-----|
| 🔴 **P0** | Reclassification AI Act : Haut Risque | ER-REG-001 | CEO + Legal | 5k€ (conseil) |
| 🔴 **P0** | Audit API sécurité (externe) | ER-CYBER-001 | RSSI externe | 15k€ |
| 🔴 **P0** | DPO interne ou délégué | ER-REG-002 | RH | 8k€/mois |
| 🔴 **P0** | Désactiver "fit culturel" temporairement | ER-ETH-001/002 | Product | 0€ |
| 🟡 **P1** | Chiffrement dataset au repos | ER-CYBER-001 | DevOps | 10k€ |
| 🟡 **P1** | Monitoring drift modèle (baseline) | ER-ETH-001 | Data Science | 12k€ |

### 5.2 Mesures Courte Terme (1-3 mois) — Budget : 150k€

| Priorité | Mesure | Risque couvert | Livrable |
|:---------|:-------|:---------------|:---------|
| 🔴 **P0** | Conformité AI Act complète | ER-REG-001/003 | Dossier technique 200p |
| 🔴 **P0** | Audit fairness externe | ER-ETH-001 | Rapport + correctifs |
| 🔴 **P0** | HITL systématique (scores <70 ET >90) | ER-ETH-001/REG | Workflow validé |
| 🟡 **P1** | Anonymisation différentielle (vrai) | ER-ETH-003 | Dataset v2 |
| 🟡 **P1** | Redondance infra (multi-cloud) | ER-CYBER-004 | Architecture HA |
| 🟡 **P1** | SOC 2 Type II (début) | ER-CYBER-001/002 | Contrôles + audit |

### 5.3 Mesures Moyen Terme (3-6 mois) — Budget : 200k€

| Priorité | Mesure | Risque couvert | Objectif |
|:---------|:-------|:---------------|:---------|
| 🟡 **P1** | ISO 27001 + ISO 42001 | ER-CYBER-001/REG | Certification |
| 🟡 **P1** | Dataset équilibré (re-sampling) | ER-ETH-001 | 50/50 genre |
| 🟢 **P2** | Explicabilité SHAP/LIME | ER-ETH-001 | Justifications traçables |
| 🟢 **P2** | Bug bounty program | ER-CYBER-001/002/003 | Communauté |
| 🟢 **P2** | Assurance cyber + responsabilité IA | Tous | Transfert risque |

### 5.4 Budget Total Recommandé

| Période | Budget | % CA 2025 |
|:--------|:-------|:----------|
| Immédiat (30j) | 50k€ | 1% |
| Court terme (3m) | 150k€ | 3% |
| Moyen terme (6m) | 200k€ | 4% |
| **Total 6 mois** | **400k€** | **8%** |
| **Total 12 mois** | **600k€** | **12%** |

> Budget IT actuel : 500k€/an → **Nécessite augmentation à 800k€/an** (60%)

---

## 6. FEUILLE DE ROUTE ET JALONS

```mermaid
gantt
    title Feuille de Route OptiRecrut - Conformité et Sécurité
    dateFormat YYYY-MM-DD
    section Immédiat (P0)
    Reclassification AI Act    :done, 2026-03-01, 7d
    Audit API sécurité         :active, 2026-03-01, 14d
    Nomination DPO             :2026-03-01, 21d
    Désactivation fit culturel :crit, 2026-03-01, 2d
    section Court terme (P1)
    Conformité AI Act          :2026-03-15, 90d
    Audit fairness             :2026-03-15, 60d
    HITL systématique          :2026-04-01, 45d
    Chiffrement dataset        :2026-03-15, 30d
    section Moyen terme (P2)
    ISO 27001/42001            :2026-06-01, 180d
    Dataset équilibré          :2026-05-01, 90d
    Bug bounty                 :2026-07-01, 60d
```

---

## 7. SYNTHÈSE EXÉCUTIVE

### Diagnostic

| Domaine | Évaluation | Commentaire |
|:--------|:-----------|:------------|
| **Cyber** | 🔴 Critique | Historique fuite, API exposée |
| **Éthique** | 🔴 Critique | Biais systémique probable |
| **Réglementaire** | 🔴 Critique | Classification erronée AI Act |
| **Sociétal** | 🟡 Majeur | Risque réputation majeur |

### Risques Prioritaires

1. **Discrimination systémique** (ER-ETH-001) — Scénario ⚫
2. **Fuite dataset** (ER-CYBER-001) — Scénario ⚫
3. **Sanction AI Act** (ER-REG-001) — Scénario ⚫

### Recommandations Stratégiques

1. **STOP** : Désactiver "fit culturel" immédiatement
2. **CORRIGER** : Reclassification AI Act + conformité
3. **PROTEGER** : Audit sécurité + chiffrement
4. **DÉMONTRER** : Audit fairness externe transparent

### Investissement Nécessaire

- **6 mois** : 400k€ (8% CA)
- **12 mois** : 600k€ (12% CA)
- **ROI** : Éviter faillite (sanctions + perte clients)

---

## ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Anonymisation CV + audit biais + transparence | ✅ **CHOISIR** |
| PIVOT | Recrutement traditionnel sans IA | ⚠️ Possible mais perte d'efficacité |
| KILL | Arrêt OptiRecrut | ❌ Trop préjudiciable (RH) |

---

*Analyse EBIOS-RM IA — OptiRecrut | Version 1.0 | Mars 2026*
