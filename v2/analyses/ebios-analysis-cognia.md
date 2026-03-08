# Analyse EBIOS-RM IA — Cognia Adaptive Learning Grid / Orientation Scolaire Algorithmique

**Référence** : EBIOS-COGNIA-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — Ministère Éducation + Protecteur Enfance + CNIL

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🔴 **HIGH-RISK** (Annexe III point 3 — éducation) |
| **Piège réglementaire** | "Limited risk" (outil apprentissage) vs **décision orientation** |
| **Incident** | Prédictions orientation **désavantagent élèves défavorisés** |
| **Controverse** | "Orientation algorithmique prématurée" influençant enseignants |
| **Conclusion** | **High-Risk gérable** — supervision humaine réelle + correction biais |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | Cognia Adaptive Learning Grid |
| **Entreprise** | Cognia Learning Systems (750 salariés, 210M€ CA) |
| **Localisation** | Helsinki, Finlande |
| **Clients** | Ministères éducation EU, universités, écoles privées internationales |
| **Technologie** | Knowledge tracing DL + LLM pédagogiques + trajectoire académique |
| **Fonction 1** | Adaptation contenu pédagogique selon performances |
| **Fonction 2** | **Scoring prédictif réussite académique** |
| **Fonction 3** | **Recommandation orientation académique** (scientifique, technique...) |
| **Fonction 4** | Génération exercices personnalisés |
| **Automatisation** | Enseignants peuvent modifier, **mais scores utilisés pour orientation** |
| **Objectifs** | Plateforme adaptative dominante EU, déploiement systèmes éducatifs nationaux |
| **Financement** | BEI + projets pilotes ministères |

### 1.2 Classification AI Act — **🔴 HIGH-RISK ÉDUCATION**

| Argument | Réalité | Statut |
|:---|:---|:---:|
| "Limited risk" (outil apprentissage) | ❌ **REJETÉ** — Orientation = décision critique | 🔴 **HIGH-RISK** |
| **Annexe III point 3** | Systèmes éducation/formation | ✅ **HIGH-RISK** |
| **Décision orientation** | Impact trajectoire vie | 🔴 **HIGH-RISK** |
| **RGPD Art. 8/35** | Données enfants + DPIA obligatoire | 🔴 **OBLIGATOIRE** |

**Piège détecté** : Vente "outil apprentissage", usage **décision orientation** = high-risk.

---

## 2. INCIDENT — BIAIS SOCIO-ÉCONOMIQUE ORIENTATION

### 2.1 Découverte

| Élément | Détail |
|:---|:---|
| **Source** | Étude académique |
| **Découverte** | Prédictions orientation **désavantagent élèves défavorisés** |
| **Mécanisme** | Corrélation milieu social / performances historiques |
| **Conséquence** | Orientation filières "moins valorisées" |
| **Impact** | **Destin scolaire déterminé par origine sociale** |

### 2.2 Analyse — Déterminisme Social Algorithmique

```
Boucle Cognia:
    Élève défavorisé :
    - Moins de ressources éducatives familiales
    - Performance historique : moyenne
    ↓
    Modèle prédit :
    "Réussite filière scientifique : faible"
    ↓
    Recommandation orientation :
    "Filière technique/professionnelle"
    ↓
    Enseignant (biais confirmation) :
    "L'IA confirme mon intuition"
    ↓
    Orientation réelle : filière pro
    ↓
    [DESTIN SCOLAIRE DÉTERMINÉ]
    ↓
    [MOBILITÉ SOCIALE BLOQUÉE]
```

---

## 3. CONTROVERSE — ORIENTATION ALGORITHMIQUE PRÉMATURÉE

### 3.1 Plainte Associations Parentales

| Accusation | Fondement |
|:---|:---|
| **Décision trop précoce** | Scores avant maturité |
| **Influence enseignants** | "L'IA le dit" = validation sans réflexion |
| **Absence recours** | Score = verdict |
| **Droit à l'erreur** | Pas de second chance |

### 3.2 Profilage Comportemental Enfants

| Donnée | Usage | Risque |
|:---|:---|:---|
| Temps réponse | Vitesse traitement | Stress, anxiété |
| Erreurs | Type difficultés | Étiquetage précoce |
| Engagement | Motivation | Personnalité jugée |
| **Total** | **Profil complet enfant** | **Droit à l'oubli ?** |

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 4.1 Éducatifs

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-EDU-001 | **Ghettoïsation filières** | ⚫ Mobilité sociale | 🔴 Élevée (confirmée) |
| ER-EDU-002 | **Abandon scolaire** | 🔴 Décrochage | 🔴 Élevée |
| ER-EDU-003 | **Dépression élèves** | ⚫ Santé mentale | 🔴 Élevée |

### 4.2 Sociétaux

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-SOC-001 | **Reproduction inégalités** | ⚫ Justice sociale | 🔴 Élevée |
| ER-SOC-002 | **Perte confiance école** | 🔴 Institution | 🔴 Élevée |

---

```mermaid
flowchart TB
    C1[Déploiement Cognia<br/>Systèmes éducatifs EU]
    --
    B1[Biais socio-économique<br/>+ Déterminisme social]
    --
    D1[Discrimination systémique<br/>Élèves défavorisés = désavantagés<br/>+ Orientation filières pro]
    --
    M1[Scandale "L'IA détermine l'avenir des enfants"<br/>+ Médias + Ministères + CNIL<br/>+ Manifestations]
    --
    I1[Interdiction système<br/>Poursuites Cognia<br/>Réforme éducation nationale]
    --
    F1[Faillite Cognia<br/>Retour orientation humaine<br/>Perte confiance éducation IA]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style B1 fill:#fff3e0,stroke:#ef6c00
    style D1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```


## 5. PLAN DE TRAITEMENT — SUPERVISION HUMAINE RÉELLE

### 5.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Équité | Même chances indépendamment origine | ±5% orientation |
| Supervision | Décision finale humaine | 100% |
| Recours | Contestation score possible | 48h max |

### 5.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Gel scores orientation** | 0€ | Moratoire |
| **Correction biais socio-économique** | 200k€ | Dataset équilibré |
| **Formation enseignants** | 150k€ | Culture critique IA |

### 5.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Réentraînement modèle équitable | 400k€ | Sans corrélation sociale |
| Conformité AI Act High-Risk | 300k€ | Documentation |
| Conformité RGPD enfants | 250k€ | Consentement parental |

### 5.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Comité éthique éducation | 200k€ | Gouvernance externe |
| Audits annuels équité | 150k€ | Biais détectés |

**Budget total** : **1,65M€** (0,8% CA)

---

## 6. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Supervision réelle + correction biais | ✅ **CHOISIR** |
| PIVOT | Apprentissage adaptatif sans orientation | ⚠️ Possible mais perte valeur |
| KILL | Arrêt Cognia | ❌ Trop préjudiciable (éducation) |

---

## 7. CONCLUSION — ORIENTATION = DÉCISION CRITIQUE

**Cognia est HIGH-RISK ÉDUCATION avec :**
- Orientation scolaire = décision vie entière
- Biais socio-économique confirmé
- Profilage comportemental enfants
- Dépendance décisionnelle enseignants

**Gérable avec supervision humaine RÉELLE et correction biais structurels.**

---

*Analyse EBIOS-RM IA — Cognia Adaptive Learning Grid | Conclusion : HIGH-RISK ÉDUCATION — Supervision réelle + Équité | Mars 2026*
