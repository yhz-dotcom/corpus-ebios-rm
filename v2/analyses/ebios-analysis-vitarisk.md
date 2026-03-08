# Analyse EBIOS-RM IA — VitaRisk Predict & Prevent / Assurance Santé Prédictive

**Référence** : EBIOS-VITARISK-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — ACPR + CNIL + Commission Européenne

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🔴 **HIGH-RISK** (Annexe III point 2 — assurance) / 🚫 **PROHIBITED** (Art. 5 si social scoring) |
| **Classification interne** | "High-Risk" (reconnu) — mais tarification "juste" contestable |
| **Fonction** | Prédiction maladies chroniques + segmentation tarification + obligations prévention |
| **Incident** | Refus prise en charge opération non liée (tracker nuit) + proxies socio-économiques |
| **Enjeu** | 500M€ encaissements + Convention AERAS + expansion UE |
| **Conclusion** | **High-Risk/Prohibited** — refus obligations prévention coercitives + suppression proxies |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | VitaRisk Predict & Prevent |
| **Entreprise** | SantéPlus Vie (200 employés, 500M€ encaissements) |
| **Localisation** | Paris, France (opérations UE) |
| **Clients** | Particuliers complémentaires santé et prévoyance |
| **Partenariats** | Grand laboratoire analyses médicales européen (data-sharing) |
| **Technologie** | XGBoost sur données médicales anonymisées + remboursements + objets connectés |
| **Fonction 1** | **Prédiction maladies chroniques** (diabète, cardio) à 5 ans |
| **Fonction 2** | **Segmentation 3 pools tarification** |
| **Fonction 3** | **Obligations prévention coercitives** (capteur, sport) |
| **Fonction 4** | Refus/surprise majeure si risque élevé non résolu |
| **Automatisation** | **Automated Decision Making** — recours humain long/complexe |

### 1.2 Classification AI Act — **🔴 HIGH-RISK / 🚫 PROHIBITED**

| Argument | Réalité | Statut |
|:---|:---|:---:|
| "High-Risk reconnu" | ✅ Assurance santé | 🔴 **HIGH-RISK** |
| **Annexe III point 2** | Assurance | ✅ **HIGH-RISK** |
| **RGPD Art. 35** | Données santé + comportement = DPIA obligatoire | 🔴 **OBLIGATOIRE** |
| **Art. 5(1)(c)** | Scoring social comportement | 🚫 **PROHIBITED** |
| Tarification "juste" | ❌ Proxies socio-économiques | 🚫 **DISCRIMINATION** |

**Piège** : Obligations prévention = scoring social prohibited.

---

## 2. INCIDENTS CONFIRMÉS

### 2.1 Incident 1 — Refus Prise en Charge par Non-Observance

| Élément | Détail |
|:---|:---|
| **Situation** | Opération non liée état santé prédictif |
| **Motif refus** | Score "comportement de prévention" trop faible |
| **Détail** | **Ne porte pas tracker la nuit** |
| **Inférence IA** | "Non-observance théorique" généralisée |
| **Problème** | Refus soin non lié au risque initial |

#### Analyse — Scoring Social Sanitaire

```
Scoring VitaRisk:
    Données tracker :
    - Pas de tracker nuit = "non-observant"
    ↓
    Inférence algorithmique :
    - Non-observant nuit = non-observant général
    - Non-observant = risque élevé
    ↓
    Décision :
    - Refus prise en charge opération
    - (Opération non liée au risque initial)
    ↓
    [SCORING SOCIAL]
    ↓
    [REFUS SOIN ARBITRAIRE]
```

### 2.2 Incident 2 — Proxies Socio-Économiques

| Élément | Détail |
|:---|:---|
| **Source** | Enquête |
| **Proxies** | **Code postal + revenu** fortement corrélés prédiction santé |
| **Impact** | **Pénalisation classes populaires** |
| **Cause** | Moins accès prévention qualité (bio, sport club) |
| **Conséquence** | Discrimination indirecte systémique |

#### Analyse — Discrimination Socio-Économique

```
Biais VitaRisk:
    Variables modèle :
    - Code postal = zone géographique
    - Revenu déclaré = capacité financière
    ↓
    Corrélation santé :
    - Zone riche = meilleure santé (prévention accessible)
    - Zone pauvre = moins bonne santé (prévention inaccessible)
    ↓
    Tarification :
    - Riche = tarif standard (prévention facile)
    - Pauvre = tarif majoré/refus (prévention difficile)
    ↓
    [DISCRIMINATION SOCIO-ÉCONOMIQUE]
    ↓
    [INÉGALITÉ ACCÈS SOINS]
```

---

## 3. RISQUE REDDITION ALGORITHMIQUE

### 3.1 Mécanisme

| Comportement | Impact |
|:---|:---|
| **Triche capteurs** | Données faussées |
| **Modèle corrompu** | Prédictions erronées |
| **Boucle perverse** | Plus de contrôle = plus de triche |

### 3.2 Scénario

```
Reddition VitaRisk:
    Obligation tracker :
    - Doit porter 24h/24 pour tarif standard
    ↓
    Comportement adaptatif :
    - Attache tracker au chien (pas de pas = pas de données)
    - Donne tracker à sportif ami (données fausses)
    - Achète données marché noir
    ↓
    Modèle apprend :
    - Données fausses = prédictions erronées
    - "Bons" clients = mauvais résultats santé
    ↓
    [MODÈLE CORROMPU]
    ↓
    [TARIFICATION INJUSTE]
```

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 4.1 Éthiques

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-ETH-001 | **Scoring social santé** | ⚫ Dignité humaine | 🔴 Élevée (confirmée) |
| ER-ETH-002 | **Discrimination socio-économique** | ⚫ Justice sociale | 🔴 Élevée |
| ER-ETH-003 | **Reddition algorithmique** | 🔴 Efficacité système | 🔴 Élevée |

### 4.2 Réglementaires

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-REG-001 | **Violation Convention AERAS** | 🔴 500M€ | 🔴 Élevée |
| ER-REG-002 | **Sanction ACPR** | 🔴 10% CA | 🔴 Élevée |
| ER-REG-003 | **Interdiction obligations prévention** | ⚫ Modèle éco | 🔴 Élevée |

---

## 5. SCÉNARIO CATASTROPHIQUE : Assurance Discriminatoire

```mermaid
flowchart TB
    C1[Déploiement VitaRisk<br/>500M€ encaissements]
    --
    S1[Scoring social + Proxies socio-éco<br/>+ Reddition algorithmique]
    --
    D1[Assurance santé discriminatoire<br/>Pauvres = refus<br/>Riches = couverture<br/>+ Données faussées]
    --
    M1[Scandale "L'assurance discrimine les pauvres"<br/>+ Médias + ACPR + CNIL<br/>+ Tribunal européen]
    --
    I1[Interdiction obligations prévention<br/>Poursuites SantéPlus Vie<br/>Réforme Convention AERAS]
    --
    F1[Faillite SantéPlus Vie<br/>Crise confiance assurance santé<br/>Régulation draconienne]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style S1 fill:#fff3e0,stroke:#ef6c00
    style D1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```

---

## 6. PLAN DE TRAITEMENT — ÉQUITÉ ET NON-DISCRIMINATION

### 6.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Équité | Tarification sans proxies socio-éco | 100% |
| Liberté | Pas d'obligations prévention coercitives | 100% |
| Efficacité | Prévention incitative, pas punitive | 100% |

### 6.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Suppression obligations prévention** | 0€ | Tarification libre |
| **Retrait proxies socio-économiques** | 200k€ | Modèle nettoyé |
| **Simplification recours humain** | 100k€ | Procédure accessible |

### 6.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Réentraînement modèle équitable | 600k€ | Prédiction sans biais |
| Conformité AI Act High-Risk | 400k€ | Documentation |
| Prévention incitative (bonus) | 300k€ | Programme volontaire |

### 6.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Certification ACPR équité | 400k€ | Label conformité |
| Audits annuels indépendants | 200k€ | Surveillance |

**Budget total** : **2,2M€** (0,4% encaissements)

---

## 7. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Suppression obligations + prévention incitative | ✅ **CHOISIR** |
| PIVOT | Assurance standard sans prévention | ⚠️ Possible mais perte différenciation |
| KILL | Arrêt VitaRisk | ❌ Trop préjudiciable (santé publique) |

---

## 8. CONCLUSION — ASSURANCE SANTÉ ÉQUITABLE

**VitaRisk Predict & Prevent est HIGH-RISK/PROHIBITED avec :**
- Scoring social (obligations prévention coercitives)
- Discrimination socio-économique (proxies code postal/revenu)
- Reddition algorithmique (triche capteurs)
- Refus soins arbitraires (non-observance théorique)
- Conflit Convention AERAS

**Gérable avec suppression obligations prévention coercitives, tarification équitable, et prévention incitative volontaire.**

---

*Analyse EBIOS-RM IA — VitaRisk Predict & Prevent | Conclusion : HIGH-RISK/PROHIBITED — Équité + Non-discrimination | Mars 2026*
