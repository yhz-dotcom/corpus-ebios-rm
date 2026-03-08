# Analyse EBIOS-RM IA — MedRisk Adaptive Pricing / Assurance Santé et Tarification Dynamique

**Référence** : EBIOS-MEDRISK-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — ACPR + CAA + Commission Européenne

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🔴 **HIGH-RISK** (Annexe III point 2 — assurance) / 🚫 **PROHIBITED** (Art. 5 si social scoring) |
| **Classification interne** | "Limited risk" (optimisation actuarielle) — **REJETÉ** |
| **Fonction** | Calcul dynamique primes + évaluation risque médical + programmes prévention + ajustement franchises |
| **Incident 1** | **Primes plus élevées** groupes socio-économiques corrélés santé |
| **Incident 2** | **Fuite** : variables indirectes infèrent conditions médicales sensibles |
| **Enjeu** | 1,9 Md€ CA + partenariat grand groupe assurance + mutuelles entreprise |
| **Conclusion** | **High-Risk** — gouvernance données + explicabilité + supervision humaine + audits équité |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | MedRisk Adaptive Pricing |
| **Entreprise** | VitaSure Insurance Group (2 400 salariés, 1,9 Md€ CA) |
| **Localisation** | Luxembourg, Luxembourg |
| **Clients** | Particuliers et entreprises, assurances santé complémentaires multi-pays |
| **Partenariats** | Fournisseurs données santé numériques (wellness apps, wearables) + startup analyse génomique |
| **Équipe IA** | 90 spécialistes data/IA |
| **Technologie** | Gradient boosting + deep learning tabulaire + prédiction maladies |
| **Données** | Dossiers médicaux anonymisés, wearables, données socio-économiques, télémédecine |
| **Fonction 1** | **Calcul dynamique primes individuelles** |
| **Fonction 2** | Évaluation risque médical futur (chroniques, hospitalisations) |
| **Fonction 3** | Recommandations programmes prévention personnalisés |
| **Fonction 4** | Ajustement automatique franchises/bonus santé |
| **Automatisation** | Calcul automatisé score risque — validation humaine limitée (fortes valeurs) |

### 1.2 Classification AI Act — **🔴 HIGH-RISK / 🚫 PROHIBITED**

| Argument | Réalité | Statut |
|:---|:---|:---:|
| "Limited risk" (actuariel) | ❌ **REJETÉ** — Influence accès assurance | 🔴 **HIGH-RISK** |
| **Annexe III point 2** | Assurance | ✅ **HIGH-RISK** |
| **Art. 5(1)(c)** | Scoring social comportement | 🚫 **PROHIBITED** |
| **Convention AERAS** | Droit à l'oubli maladies graves | 🔴 **OBLIGATOIRE** |
| **RGPD Art. 35** | DPIA données santé + scoring auto | 🔴 **DPIA REQUISE** |

**Piège** : Optimisation actuarielle ≠ exemption — accès assurance = high-risk.

---

## 2. INCIDENTS CONFIRMÉS

### 2.1 Incident 1 — Discrimination Socio-Économique

| Élément | Détail |
|:---|:---|
| **Source** | Association de consommateurs |
| **Révélation** | **Primes plus élevées** certains groupes socio-économiques |
| **Corrélation** | Facteurs socio-éco corrélés à santé |
| **Mécanisme** | Code postal, revenu, éducation = proxies santé |

#### Analyse — Biais Actuariel Discriminatoire

```
Biais MedRisk:
    Variables modèle :
    - Code postal = zone géographique
    - Niveau éducation = diplôme
    - Revenu estimé = capacité financière
    ↓
    Corrélations santé :
    - Zone défavorisée = plus maladies chroniques
    - Faible éducation = moins prévention
    - Faible revenu = moins accès soins
    ↓
    Scoring actuariel :
    - Zone défavorisée = prime élevée
    - Faible éducation = prime élevée
    - Faible revenu = prime élevée
    ↓
    [DISCRIMINATION INDIRECTE]
    ↓
    [INÉGALITÉ ACCÈS ASSURANCE]
```

### 2.2 Incident 2 — Inférence Données Sensibles

| Élément | Détail |
|:---|:---|
| **Source** | Fuite interne |
| **Problème** | **Variables indirectes** infèrent conditions médicales sensibles |
| **Exclusion** | Malgré exclusion explicite données sensibles |
| **Mécanisme** | Corrélations indirectes = reconstruction maladies |

#### Analyse — Reconstruction Algorithmique

```
Inférence MedRisk:
    Variables "anodines" :
    - Fréquence achats pharmacie = traitement chronique
    - Recherche Google santé = symptômes préoccupants
    - Désactivation localisation = consultation spécialiste
    - Achats alimentaires spécifiques = régime médical
    ↓
    Modèle corrèle :
    - Pattern achats = maladie X probable
    - Pattern recherche = condition Y suspectée
    - Pattern localisation = traitement Z en cours
    ↓
    Inférence implicite :
    - Données sensibles reconstruites
    - Sans consentement explicite
    - Sans base légale RGPD
    ↓
    [VIOLATION RGPD ART. 9]
    ↓
    [DONNÉES SANTÉ SENSIBLES]
```

---

## 3. DÉPENDANCE DÉCISIONNELLE ACTUAIRES

### 3.1 Mécanisme

| Aspect | Problème |
|:---|:---|
| **Confiance aveugle** | Actuaires suivent score IA sans questionnement |
| **Opacité modèle** | Difficulté expliquer décisions tarifaires |
| **Déresponsabilisation** | "C'est l'IA qui décide" |

### 3.2 Risque

```
Dépendance MedRisk:
    Scoring IA :
    - Score 85/100 = risque élevé
    - Prime = +40%
    ↓
    Actuaire :
    - "Modèle a appris sur millions de cas"
    - "Je ne peux pas contester"
    - Validation mécanique
    ↓
    Décision finale :
    - Prime majorée sans justification humaine
    - Client mécontent sans recours
    ↓
    [DÉRESPONSABILISATION]
    ↓
    [MANQUE SUPERVISION HUMAINE]
```

---

## 4. RISQUE CASCADING — IMPACT ACCÈS SOINS

### 4.1 Mécanisme

| Étape | Impact |
|:---|:---|
| Prime élevée | Refus/abandon assurance |
| Pas d'assurance | Pas d'accès soins complémentaires |
| Soins non couverts | Détérioration santé |
| Santé dégradée | Chômage, précarité |

### 4.2 Scénario

```
Cascading MedRisk:
    Tarification IA :
    - Zone défavorisée = prime +50%
    ↓
    Décision assuré :
    - Prime trop élevée = abandon contrat
    ↓
    Conséquence santé :
    - Pas de complémentaire = reste à charge élevé
    - Évite soins = maladie non traitée
    - Hospitalisation urgente = endettement
    ↓
    [EXCLUSION ASSURANTIELLE]
    ↓
    [EXCLUSION SOCIALE]
```

---

## 5. ÉVÉNEMENTS REDOUTÉS

### 5.1 Éthiques

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-ETH-001 | **Discrimination tarifaire** | ⚫ Justice sociale | 🔴 Élevée (confirmée) |
| ER-ETH-002 | **Exclusion assurantielle** | ⚫ Accès soins | 🔴 Élevée |
| ER-ETH-003 | **Inférence données sensibles** | ⚫ Vie privée | 🔴 Élevée |

### 5.2 Réglementaires

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-REG-001 | **Sanction ACPR/CAA** | 🔴 10% CA | 🔴 Élevée |
| ER-REG-002 | **Violation RGPD** | 🔴 4% CA | 🔴 Élevée |
| ER-REG-003 | **Interdiction tarification dynamique** | ⚫ Modèle éco | 🔴 Élevée |

---

## 6. SCÉNARIO CATASTROPHIQUE : Assurance à Deux Vitesses

```mermaid
flowchart TB
    C1[Déploiement MedRisk<br/>1,9 Md€ CA Europe]
    --
    D1[Discrimination socio-éco<br/>+ Inférence données sensibles<br/>+ Dépendance actuaires]
    --
    E1[Assurance à deux vitesses<br/>Riches = couverture<br/>Pauvres = exclusion<br/>+ Données santé exposées]
    --
    M1[Scandale "L'assurance discrimine les malades"<br/>+ Médias + ACPR + CNIL<br/>+ Tribunal européen]
    --
    I1[Interdiction tarification IA<br/>Poursuites VitaSure<br/>Réforme assurance santé]
    --
    F1[Faillite VitaSure<br/>Crise confiance assurance<br/>Retour tarification manuelle]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style D1 fill:#fff3e0,stroke:#ef6c00
    style E1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```

---

## 7. PLAN DE TRAITEMENT — GOUVERNANCE ET ÉQUITÉ

### 7.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Gouvernance | Contrôle données strict | 100% |
| Explicabilité | Scoring transparent | 100% |
| Supervision | Validation humaine obligatoire | 100% |
| Équité | Audits biais réguliers | 100% |

### 7.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Audit variables indirectes** | 500k€ | Suppression proxies |
| **Gel ajustement automatique franchises** | 0€ | Validation humaine |
| **Documentation explicabilité** | 300k€ | Rapport transparence |

### 7.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Réentraînement modèle équitable (échelle 1,9 Md€) | 2,5M€ | Algorithme sans biais |
| Conformité AI Act High-Risk | 800k€ | Documentation |
| **DPIA RGPD Art. 35** (données santé + scoring auto) | 400k€ | Évaluation impact protection |
| **Conformité Convention AERAS** (droit oubli) | 300k€ | Processus anonymisation |
| Supervision actuaires renforcée | 600k€ | Formation + procédures |

### 7.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Audits équité annuels indépendants | 500k€ | Certification |
| Registry UE systèmes high-risk | 200k€ | Enregistrement |

**Budget total** : **6,8M€** (0,36% CA) — *réalisme échelle 1,9 Md€*

---

## 8. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Gouvernance + explicabilité + supervision + audits | ✅ **CHOISIR** |
| PIVOT | Tarification traditionnelle sans IA | ⚠️ Possible mais perte compétitivité |
| KILL | Arrêt MedRisk | ❌ Trop préjudiciable (assurance) |

---

## 9. CONCLUSION — ASSURANCE ÉQUITABLE ET TRANSPARENTE

**MedRisk Adaptive Pricing est HIGH-RISK avec :**
- Discrimination socio-économique (primes corrélées revenu/éducation)
- Inférence données sensibles (variables indirectes)
- Dépendance décisionnelle actuaires (manque supervision)
- Risque cascading (exclusion assurantielle → exclusion sociale)
- **Non-conformité Convention AERAS** (droit à l'oubli maladies graves)
- **RGPD Art. 35** : DPIA requise pour données santé + scoring automatisé
- Enjeu majeur (1,9 Md€ CA, mutuelles entreprise)

**Gérable avec gouvernance données stricte, explicabilité scoring, supervision humaine renforcée, conformité AERAS, DPIA RGPD, et audits équité réguliers.**

---

*Analyse EBIOS-RM IA — MedRisk Adaptive Pricing | Conclusion : HIGH-RISK — Gouvernance + Équité + Transparence | Mars 2026*
