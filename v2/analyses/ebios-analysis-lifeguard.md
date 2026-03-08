# Analyse EBIOS-RM IA — LifeGuard Dynamic Profiler / Scoring Social et Discrimination par Proxy

**Référence** : EBIOS-LIFEGUARD-001 | **Date** : Mars 2026 | **Classification** : 🚫 CONFIDENTIEL URGENT — ACPR + CNIL + Commission Européenne

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🚫 **PROHIBITED** (Art. 5(1)(c) — scoring social) / 🔴 **HIGH-RISK** (Annexe III point 2 — assurance) |
| **Technique** | **Scoring social caché** : likes bars à vin + GPS quartiers = "risque comportemental" |
| **Incident** | Refus couverture + prime ×4 (400%) — "likes" bars à vin + GPS quartiers pauvres |
| **Controverse** | **Proxies discrimination** : origine/ethnie/santé inférés indirectement |
| **Conclusion** | **PROHIBITED** — arrêt scoring comportemental + tarification actuarielle standard |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | LifeGuard Dynamic Profiler |
| **Entreprise** | AssurFuture Corp (200 employés, 120M€ CA) |
| **Localisation** | Dublin, Irlande (QEAD) — distribution FR/IT |
| **Équipe IA** | Data Science externalisée Ukraine (sous-traitant) + CDO Dublin |
| **Technologie** | Graph Neural Networks (relations sociales) + NLP posts publics |
| **Données** | Transactions, navigation (cookies), réseau social, GPS |
| **Fonction 1** | Tarification dynamique prime assurance |
| **Fonction 2** | **Détection "risque comportemental"** |
| **Fonction 3** | **Refus si score risque trop élevé** |
| **Automatisation** | **Full-Automated** — tarif sans intervention humaine |
| **Objectifs** | "Zero Loss" (éradiquer fraude), pricing n=1, levée fonds VC |
| **Pression** | Marges brutes élevées pour investisseurs, montée fraudes post-COVID |

### 1.2 Classification AI Act — **🚫 PROHIBITED + 🔴 HIGH-RISK**

| Article | Critère | Application LifeGuard | Statut |
|:---|:---|:---|:---:|
| **Art. 5(1)(c)** | **Scoring social** | ✅ **Évaluation fiabilité via comportement social** | 🚫 **PROHIBITED** |
| **Annexe III point 2** | Assurance/crédit | ✅ Tarification/refus |
| **RGPD Art. 35** | Données santé inférées + scoring = DPIA obligatoire | 🔴 **OBLIGATOIRE** | 🔴 **HIGH-RISK** |
| Argument "limited risk" | "Données standard, consentement GDPR" | ❌ **REJETÉ** — Scoring social = prohibited | 🚫 **PROHIBITED** |

---

## 2. INCIDENT — SCORING COMPORTEMENTAL ABUSIF

### 2.1 Déroulement

| Élément | Détail |
|:---|:---|
| **Client** | Refus augmentation couverture santé |
| **Augmentation** | **Prime ×4 (400%)** |
| **Explication** | Vague : "risque comportemental" |
| **Découverte** | Client analyse son dossier |
| **Pénalités IA** | Likes pages bars à vin + GPS quartiers faible espérance vie |

### 2.2 Analyse — Proxies Discriminatoires

```
Scoring LifeGuard:
    Données collectées :
    - Likes Facebook : bars à vin
    - GPS fréquent : quartiers défavorisés
    - Réseau social : relations analysées (GNN)
    ↓
    Inférences algorithmiques :
    - Bars à vin = consommation alcool = risque santé
    - Quartiers pauvres = risque socio-économique = mortalité
    - Réseau = comportement de groupe = fiabilité
    ↓
    Score "risque comportemental" : ÉLEVÉ
    ↓
    Décision : REFUS couverture + prime ×4
    ↓
    [SCORING SOCIAL DISCRIMINATOIRE]
```

---

## 3. CONTROVERSE — PROXIES DISCRIMINATION INTERDITE

### 3.1 Enquête Journalistique

| Découverte | Mécanisme |
|:---|:---|
| **Origine ethnique** | Proxy : nom, quartier, réseau |
| **État de santé** | Proxy : activités détectées (parachutisme), likes (tabagisme) |
| **Situation socio-économique** | Proxy : code postal, fréquentation lieux |

### 3.2 Violation AI Act

| Principe | Violation | Preuve |
|:---|:---|:---:|
| **Interdiction scoring social** | Évaluation fiabilité via comportement | ✅ Likes + GPS = score |
| **Interdiction discrimination** | Origine/ethnie/santé inférées | ✅ Proxies détectés |
| **Explicabilité** | Explication vague "risque comportemental" | ❌ Refus incompréhensible |

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 4.1 Discrimination

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-DISC-001 | **Ségrégation assurance** | ⚫ Accès soins | 🔴 Élevée (confirmée) |
| ER-DISC-002 | **Ghettoïsation tarifaire** | ⚫ Justice sociale | 🔴 Élevée |
| ER-DISC-003 | **Exclusion précaires** | ⚫ Vulnérables sans couverture | 🔴 Élevée |

### 4.2 Juridiques

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-JUR-001 | **Sanction ACPR** | 🔴 10% CA | 🔴 Élevée |
| ER-JUR-002 | **Interdiction système** | ⚫ 120M€ CA | 🔴 Élevée |
| ER-JUR-003 | **Poursuites discrimination** | 🔴 Pénal | 🔴 Élevée |

---

## 5. SCÉNARIO CATASTROPHIQUE : Apartheid Assurantiel

```mermaid
flowchart TB
    C1[Déploiement LifeGuard<br/>Zero Loss Europe]
    --
    S1[Scoring social masse<br/>Proxies discrimination systémique]
    --
    A1[Apartheid assurantiel<br/>Pauvres = primes ×10 ou refus<br/>Riches = couverture premium]
    --
    M1[Scandale "L'IA crée ghetto assurances"<br/>+ Médias + Tribunal européen<br/>+ Manifestations]
    --
    I1[Interdiction UE scoring comportemental<br/>Poursuites AssurFuture<br/>Prison dirigeants]
    --
    F1[Faillite AssurFuture<br/>Régulation draconienne assurance IA<br/>Retard innovation sectorielle]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style S1 fill:#fff3e0,stroke:#ef6c00
    style A1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```

---

## 6. PLAN DE TRAITEMENT — ARRÊT SCORING COMPORTEMENTAL

### 6.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Tarification actuarielle | Risque objectif uniquement (âge, historique sinistres) | 100% |
| Interdiction proxies | Pas d'inférence origine/santé/socio | 0% |
| Explicabilité | Refus justifié et contestable | 100% |

### 6.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Arrêt scoring comportemental** | 0€ | Suppression GNN + NLP social |
| **Gel refus automatiques** | 0€ | Validation humaine obligatoire |
| **Audit proxies discriminatoires** | 150k€ | Rapport discrimination |

### 6.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Retour tarification actuarielle standard | 400k€ | Modèle conforme |
| Conformité AI Act Prohibited/High-Risk | 300k€ | Documentation |
| Recours effectif assurés | 100k€ | Contestation scores |

### 6.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Certification ACPR équité | 200k€ | Label conformité |
| Transparence publique | 100k€ | Rapport annuel |

**Budget total** : **1,25M€** (1% CA)

---

## 7. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| FIX | Tarification actuarielle sans scoring social | ⚠️ **DIFFICILE** — business model détruit |
| **PIVOT** | Assurance standard sans IA comportementale | ✅ **POSSIBLE** — mais perte VC |
| **KILL** | Arrêt LifeGuard | ⚠️ **ENVISAGEABLE** — si prohibited confirmé |

---

## 8. CONCLUSION — SCORING SOCIAL INTERDIT

**LifeGuard Dynamic Profiler est PROHIBITED (Art. 5(1)(c)) avec :**
- Scoring social déguisé en "risque comportemental"
- Proxies discrimination (origine, santé, socio-économique)
- Tarification abusive (×4) sans explicabilité
- Business model = discrimination systémique

**Seule issue : arrêt total scoring comportemental, retour tarification actuarielle standard.**

---

*Analyse EBIOS-RM IA — LifeGuard Dynamic Profiler | Conclusion : PROHIBITED — Scoring social interdit | Mars 2026*
