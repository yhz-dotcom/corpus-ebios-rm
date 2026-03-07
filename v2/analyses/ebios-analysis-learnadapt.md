# Analyse EBIOS-RM IA — LearnAdapt Pro / Éducation Adaptative et Biais Linguistique

**Référence** : EBIOS-LEARNADAPT-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — CNIL + France Compétences + Horizon Europe

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🔴 **HIGH-RISK** (Annexe III point 3 — éducation/formation professionnelle) |
| **Classification interne** | "Limited risk" — **REJETÉ** (formation professionnelle = high-risk) |
| **Incident 1** | **Biais linguistique** : non-francophones natifs = scores -18% (même production) |
| **Incident 2** | **Fuite données** : 45 000 profils engagement exposés (concentration, émotions) |
| **Enjeu** | Accord France Compétences (20% CA) + subvention Horizon Europe 6M€ |
| **Conclusion** | **High-Risk gérable** — corpus multilingue équilibré + DPIA renforcée |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | LearnAdapt Pro |
| **Entreprise** | EduFlow Technologies SAS (210 salariés, 38M€ CA) |
| **Localisation** | Nantes, France (8 pays UE via partenaires EdTech) |
| **Clients** | OPCO français, grands groupes upskilling, plateformes certification EU |
| **Partenariats** | Inria + consortium européen "SkillsAI" (Horizon Europe) |
| **Technologie** | LLMs fine-tunés pédagogiques + DKT/AKT + analyse multimodale (webcam/micro) |
| **Fonction 1** | Parcours apprentissage adaptatif temps réel |
| **Fonction 2** | Évaluation automatique productions complexes (rapports, code, oraux) |
| **Fonction 3** | Détection décrochage par signaux comportementaux |
| **Fonction 4** | Recommandation interventions pédagogiques |
| **Automatisation** | HITL certifications finales — **MAIS** recommandations automatiques |
| **Intégration** | LTI Moodle, Canvas |

### 1.2 Classification AI Act — **🔴 HIGH-RISK ÉDUCATION**

| Article | Critère | Application LearnAdapt | Statut |
|:---|:---|:---|:---:|
| **Annexe III point 3** | Éducation/formation professionnelle | ✅ Certification professionnelle continue | 🔴 **HIGH-RISK** |
| Argument "limited risk" | "Outil accompagnement, pas décision orientation" | ❌ **REJETÉ** — Formation professionnelle = high-risk | 🔴 **HIGH-RISK** |

---

## 2. INCIDENT 1 — BIAIS LINGUISTIQUE SYSTÉMIQUE

### 2.1 Découverte

| Élément | Détail |
|:---|:---|
| **Source** | Étude indépendante automne 2025 |
| **Biais détecté** | Non-francophones natifs = scores **-18%** en moyenne |
| **Condition** | **Production équivalente** |
| **Cause** | Corpus entraînement majoritairement **francophone "standard"** |
| **Conséquence** | Plainte fédération organismes formation |

### 2.2 Analyse — Discrimination Linguistique

```
Biais LearnAdapt:
    Corpus entraînement :
    - 85% productions francophones natifs
    - 15% productions non-natifs (sous-représenté)
    ↓
    LLM évaluation écrite :
    - Apprend style "standard" = correct
    - Style non-natif = incorrect (même contenu)
    ↓
    Exemple :
    Production A (natif) : "L'analyse démontre que..."
    → Score : 85/100
    
    Production B (non-natif) : "L'analyse montre que..."
    → Score : 67/100 (même contenu, style différent)
    ↓
    [BIAS LINGUISTIQUE SYSTÉMIQUE]
    ↓
    [DISCRIMINATION APPRENANTS NON-FRANCOPHONES]
```

---

## 3. INCIDENT 2 — FUITE DONNÉES ENGAGEMENT

### 3.1 Déroulement

| Élément | Détail |
|:---|:---|
| **Date** | Printemps 2026 |
| **Cause** | **API mal configurée** |
| **Données exposées** | 45 000 profils engagement détaillés |
| **Données sensibles** | Temps concentration, moments décrochage, **réactions émotionnelles détectées** |
| **Conséquence** | CNIL ouvre enquête : minimisation + défaut DPIA |

### 3.2 Analyse — Violation Privacy

```
Fuite LearnAdapt:
    Données collectées (analyse multimodale) :
    - Webcam : attention visuelle, expressions faciales
    - Micro : tonalité, hésitations, engagement oral
    ↓
    Inférences algorithmiques :
    - "Réaction émotionnelle : frustration"
    - "Moment décrochage : 14h23"
    - "Temps concentration moyen : 12 min"
    ↓
    API mal configurée :
    - Endpoint /api/v2/learner-profiles exposé
    - Pas d'authentification requise
    ↓
    [45 000 PROFILS PSYCHOMÉTRIQUES EXPOSÉS]
    ↓
    [VIOLATION PRIVACY FONDAMENTALE]
```

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 4.1 Équité

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-EQU-001 | **Ségrégation pédagogique** | ⚫ Accès formation | 🔴 Élevée (confirmée) |
| ER-EQU-002 | **Exclusion non-francophones** | ⚫ Justice sociale | 🔴 Élevée |
| ER-EQU-003 | **Invalidation certifications** | 🔴 France Compétences | 🔴 Élevée |

### 4.2 Réglementaires

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-REG-001 | **Sanction CNIL** | 🔴 4% CA | 🔴 Élevée |
| ER-REG-002 | **Perte subvention Horizon Europe** | 🔴 6M€ | 🔴 Élevée |
| ER-REG-003 | **Rupture accord France Compétences** | 🔴 20% CA | 🔴 Élevée |

---

## 5. SCÉNARIO CATASTROPHIQUE : Apartheid Pédagogique

```mermaid
flowchart TB
    C1[Déploiement LearnAdapt<br/>8 pays UE]
    --
    B1[Biais linguistique non corrigé<br/>+ Fuite données récurrente]
    --
    D1[Ségrégation pédagogique<br/>Non-francophones = échec systémique<br/>+ Scandale privacy 45k apprenants]
    --
    M1[Scandale "L'IA discrimine dans l'éducation"<br/>+ Médias + CNIL + France Compétences<br/>+ Commission européenne]
    --
    I1[Perte subvention Horizon Europe<br/>Rupture France Compétences<br/>Sanction CNIL record]
    --
    F1[Faillite EduFlow<br/>Retard certification IA Europe<br/>Perte confiance EdTech]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style B1 fill:#fff3e0,stroke:#ef6c00
    style D1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```

---

## 6. PLAN DE TRAITEMENT — ÉQUITÉ ET PRIVACY

### 6.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Équité linguistique | Scores équivalents natifs/non-natifs | Δ < 5% |
| Privacy by design | Minimisation données engagement | 100% |
| Conformité | DPIA validée + France Compétences | 100% |

### 6.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Rééquilibrage corpus multilingue** | 300k€ | Dataset 50/50 |
| **Sécurisation API** | 100k€ | Audit sécurité |
| **DPIA renforcée** | 200k€ | Validation CNIL |

### 6.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Réentraînement modèle équitable | 500k€ | LLM multilingue |
| Conformité AI Act High-Risk | 300k€ | Documentation |
| Certification France Compétences | 400k€ | Label qualité |

### 6.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Audit biais annuel indépendant | 200k€ | Certification |
| Transparence algorithmique | 150k€ | Explicabilité |

**Budget total** : **2,15M€** (5,7% CA)

---

## 7. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Corpus équilibré + privacy renforcée | ✅ **CHOISIR** |
| PIVOT | Évaluation humaine sans IA | ⚠️ Possible mais perte efficacité |
| KILL | Arrêt LearnAdapt | ❌ Trop préjudiciable (certification IA) |

---

## 8. CONCLUSION — ÉQUITÉ PÉDAGOGIQUE ET PRIVACY

**LearnAdapt Pro est HIGH-RISK ÉDUCATION avec :**
- Biais linguistique systémique (-18% non-francophones)
- Fuite données psychométriques (45 000 apprenants)
- Enjeu stratégique majeur (France Compétences + Horizon Europe)
- Risque réglementaire critique (CNIL, Commission EU)

**Gérable avec corpus multilingue équilibré et privacy by design renforcée.**

---

*Analyse EBIOS-RM IA — LearnAdapt Pro | Conclusion : HIGH-RISK — Équité linguistique + Privacy | Mars 2026*
