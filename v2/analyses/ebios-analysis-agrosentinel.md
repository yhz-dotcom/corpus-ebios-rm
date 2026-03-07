# Analyse EBIOS-RM IA — AgroSentinel-Predict / Agriculture Précision et Risque Environnemental

**Référence** : EBIOS-AGROSENTINEL-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — DGAL + ANSES + Commission Européenne

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🔴 **HIGH-RISK** (Annexe III point 1 — sécurité alimentaire) / 🔴 **CRITIQUE** (impact environnemental/santé) |
| **Classification interne** | "Limited risk" — **REJETÉ** (agriculture = sécurité alimentaire + environnement) |
| **Fonction** | Prédiction risques phytosanitaires + recommandation traitements + prescription automatique |
| **Automatisation** | Human-on-the-loop allégé — taux blocage < 2% |
| **Enjeu** | Contrat Écophyto 2030 (9,2M€, 120 000 ha) + levée Série B 22M€ |
| **Conclusion** | **High-Risk critique** — conformité assessment obligatoire + validation agronome renforcée |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | AgroSentinel-Predict |
| **Entreprise** | VerdeLogic SAS (310 salariés, 47M€ CA) |
| **Localisation** | Toulouse, France + Valence (ES) + Poznań (PL) |
| **Clients** | Coopératives agricoles (Invivo, Axéréal, Limagrain), exploitations > 200 ha |
| **Contrat public** | **DGAL Plan Écophyto 2030** — 9,2M€, 120 000 ha |
| **Partenariats** | Airbus (Pléiades Neo), Planet Labs, Weenat, Sencrop |
| **Technologie** | XGBoost/LightGBM + SegFormer (vision) + LLaMA 3 (recommandations) |
| **Données** | 6 ans historique 4 200 exploitations |
| **Fonction 1** | Prédiction risques phytosanitaires (J+7/J+14) |
| **Fonction 2** | **Recommandation traitements (type, dose, fenêtre)** |
| **Fonction 3** | **Génération fiches prescription automatiques** |
| **Fonction 4** | Modélisation impact environnemental (lessivage, biodiversité) |
| **Automatisation** | Human-on-the-loop allégé — blocage < 2% en 30 min |

### 1.2 Classification AI Act — **🔴 HIGH-RISK SÉCURITÉ ALIMENTAIRE**

| Argument | Réalité | Statut |
|:---|:---|:---:|
| "Limited risk" (agriculture non listée) | ❌ **REJETÉ** — Impact sécurité alimentaire + environnement | 🔴 **HIGH-RISK** |
| **Annexe III point 1** | Sécurité alimentaire | ✅ **HIGH-RISK** |
| Impact santé publique | Pesticides = santé | 🔴 **HIGH-RISK** |
| Impact environnemental | Biodiversité, lessivage | 🔴 **CRITIQUE** |

**Piège** : Agriculture non listée ≠ absence risque (santé + environnement).

---

## 2. RISQUES CRITIQUES IDENTIFIÉS

### 2.1 Risque Environnemental — Biodiversité

| Risque | Mécanisme | Impact |
|:---|:---|:---|
| **Sur-traitement** | Prédiction erronée = traitement inutile | Pollution sols/eaux |
| **Sous-traitement** | Prédiction erronée = absence traitement nécessaire | Perte récolte + propagation ravageurs |
| **Lessivage** | Dose mal calculée = contamination nappes | Santé publique |
| **Pollinisateurs** | Traitement mal calibré = mortalité abeilles | Écosystème |

### 2.2 Risque Sanitaire — Pesticides

| Risque | Mécanisme | Impact |
|:---|:---|:---|
| **Résidus** | Dose excès = résidus dans aliments | Santé consommateurs |
| **Exposition** | Fenêtre application mal calculée = exposition travailleurs | Santé agriculteurs |
| **Résistance** | Traitement répété = résistance ravageurs | Efficacité phytosanitaires |

---

## 3. INCIDENTS POTENTIELS

### 3.1 Scénario 1 — Sur-Traitement et Pollution

```
Erreur AgroSentinel:
    Modèle prédit :
    - Risque septoriose blé = ÉLEVÉ (faux positif)
    ↓
    Recommandation :
    - Fongicide systémique, dose maximale
    - Fenêtre : immédiat
    ↓
    Prescription auto (blocage < 2%) :
    - Fiche envoyée distributeur
    - Traitement appliqué
    ↓
    Réalité :
    - Aucun risque réel
    - Traitement inutile
    ↓
    [SUR-TRAITEMENT]
    ↓
    [POLLUTION SOLS/EAUX]
    ↓
    [PERTE BIODIVERSITÉ]
```

### 3.2 Scénario 2 — Sous-Traitement et Perte Récolte

```
Erreur AgroSentinel:
    Modèle prédit :
    - Risque puceron = FAIBLE (faux négatif)
    ↓
    Recommandation :
    - Aucun traitement
    ↓
    Réalité :
    - Infestation massive
    - Prolifération rapide
    ↓
    [SOUS-TRAITEMENT]
    ↓
    [PERTE RÉCOLTE 40%]
    ↓
[CRISÉCONOMIQUE AGRICULTEUR]
```

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 4.1 Environnementaux

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-ENV-001 | **Pollution nappes phréatiques** | ⚫ Santé publique | 🔴 Élevée |
| ER-ENV-002 | **Effondrement biodiversité** | ⚫ Écosystème | 🔴 Élevée |
| ER-ENV-003 | **Résistance ravageurs** | 🔴 Sécurité alimentaire | 🔴 Élevée |

### 4.2 Sanitaires

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-SAN-001 | **Résidus pesticides aliments** | ⚫ Santé consommateurs | 🔴 Élevée |
| ER-SAN-002 | **Exposition travailleurs agricoles** | 🔴 Santé publique | 🔴 Élevée |
| ER-SAN-003 | **Crise alimentaire régionale** | ⚫ Sécurité alimentaire | 🔴 Élevée |

### 4.3 Réglementaires

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-REG-001 | **Retrait contrat Écophyto 2030** | 🔴 9,2M€ + réputation | 🔴 Élevée |
| ER-REG-002 | **Interdiction système** | ⚫ 47M€ CA | 🔴 Élevée |
| ER-REG-003 | **Sanction ANSES** | 🔴 Pénal | 🔴 Élevée |

---

## 5. SCÉNARIO CATASTROPHIQUE : Crise Agro-Environnementale

```mermaid
flowchart TB
    C1[Déploiement AgroSentinel<br/>800 000 ha Europe]
    --
    E1[Erreurs prédiction non détectées<br/>Sur-traitement + sous-traitement]
    --
    P1[Pollution massive nappes<br/>+ Perte récoltes 40%<br/>+ Effondrement abeilles]
    --
    M1[Scandale "L'IA empoisonne l'agriculture"<br/>+ Médias + DGAL + ANSES<br/>+ Tribunal européen environnement]
    --
    I1[Retrait contrat Écophyto 2030<br/>Interdiction AgroSentinel<br/>Poursuites VerdeLogic]
    --
    F1[Faillite VerdeLogic<br/>Crise confiance agriculture IA<br/>Retard transition écologique]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style E1 fill:#fff3e0,stroke:#ef6c00
    style P1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```

---

## 6. PLAN DE TRAITEMENT — SÉCURITÉ ALIMENTAIRE ET ENVIRONNEMENT

### 6.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Précision | Faux positifs/négatifs < 5% | 95% |
| Validation | Agronome valide chaque prescription | 100% |
| Traçabilité | Chaque décision traçable | 100% |
| Environnement | Impact négatif = 0 | 0% |

### 6.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Conformité assessment AI Act** | 400k€ | Documentation High-Risk |
| **Validation agronome obligatoire** | 0€ | Workflow modifié |
| **Audit modèles précision** | 300k€ | Rapport performance |

### 6.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Réentraînement modèles | 600k€ | Précision > 95% |
| Monitoring environnemental | 400k€ | Capteurs terrain |
| Conformité ANSES | 300k€ | Autorisation mise marché |

### 6.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Certification "Agriculture Durable IA" | 500k€ | Label européen |
| Audits annuels indépendants | 300k€ | Certification |

**Budget total** : **2,8M€** (6% CA)

---

## 7. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Conformité assessment + validation agronome renforcée | ✅ **CHOISIR** |
| PIVOT | Recommandation sans prescription automatique | ⚠️ Possible mais perte efficacité |
| KILL | Arrêt AgroSentinel | ❌ Trop préjudiciable (Écophyto 2030) |

---

## 8. CONCLUSION — SÉCURITÉ ALIMENTAIRE ET ENVIRONNEMENT

**AgroSentinel-Predict est HIGH-RISK avec :**
- Classification erronée "limited risk" (impact santé + environnement)
- Automatisation excessive (blocage < 2%)
- Risque environnemental critique (pollution, biodiversité)
- Risque sanitaire (pesticides, résidus)
- Enjeu stratégique majeur (Écophyto 2030, 9,2M€)

**Gérable avec conformité assessment obligatoire et validation agronome renforcée.**

---

*Analyse EBIOS-RM IA — AgroSentinel-Predict | Conclusion : HIGH-RISK — Sécurité alimentaire + Environnement | Mars 2026*
