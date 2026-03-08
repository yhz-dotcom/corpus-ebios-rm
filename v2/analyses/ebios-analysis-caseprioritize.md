# Analyse EBIOS-RM IA — CasePrioritize AI / Justice et Discrimination Algorithmique

**Référence** : EBIOS-CASEPRIORITIZE-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — Ministère Justice + CSM + Eurojust

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🔴 **HIGH-RISK** (Annexe III point 8 — administration justice) / 🚫 **PROHIBITED** (Art. 5(1)(c) — social scoring) |
| **Piège** | "Limited risk" (gestion interne) vs **influence sur droits fondamentaux** |
| **Incident 1** | **Discrimination ethnique** : violences conjugales auteurs minorités = priorité déclassée |
| **Incident 2** | **Évaluation magistrats** : scores "efficacité" = incitations perverses, atteinte indépendance |
| **Enjeu** | Ministère Justice français (25% CA) + programme Justice UE 4M€ + label "Ethical Justice AI" |
| **Conclusion** | **High-Risk critique** — audit biais continu + contre-expertise obligatoire + interdiction évaluation magistrats |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | CasePrioritize AI |
| **Entreprise** | JustScale BV (165 salariés, 32M€ CA) |
| **Localisation** | La Haye, Pays-Bas (pilote 3 pays UE) |
| **Clients** | Parquets nationaux, police judiciaire, Eurojust |
| **Partenariats** | Université de Leyde + consortium "EU Justice AI" |
| **Technologie** | LLMs juridiques multilingues + GNN + modèles survie délais |
| **Fonction 1** | Analyse dossiers enquête (complexité, récidive, solidité probatoire) |
| **Fonction 2** | **Recommandation priorisation allocation magistrats/enquêteurs** |
| **Fonction 3** | Détection similarités entre affaires |
| **Automatisation** | Strictly advisory — **MAIS** pression implicite via indicateurs efficacité |
| **Intégration** | Greffes numériques sécurisés |

### 1.2 Classification AI Act — **🔴 HIGH-RISK / 🚫 PROHIBITED**

| Argument | Réalité | Statut |
|:---|:---|:---:|
| "Limited risk" (gestion interne) | ❌ **REJETÉ** — Influence droits fondamentaux | 🔴 **HIGH-RISK** |
| **Annexe III point 8** | Administration justice | ✅ **HIGH-RISK** |
| **RGPD** | Données personnelles traitées = DPIA requise | 🔴 **OBLIGATOIRE** |
| Art. 5(1)(c) | Social scoring via scores récidive | ⚠️ **À ÉVALUER** |

**Piège** : Frontière critique "aide gestion" vs "influence décisions droits fondamentaux".

---

## 2. INCIDENT 1 — DISCRIMINATION ETHNIQUE DANS LA PRIORISATION

### 2.1 Découverte

| Élément | Détail |
|:---|:---|
| **Source** | Enquête "JusticeWatch" été 2025 |
| **Biais détecté** | Violences conjugales auteurs **minorités ethniques** = **priorité déclassée** |
| **Cause** | Biais historique données entraînement (taux condamnation plus faibles ces profils) |
| **Conséquence** | Plainte collective associations lutte discriminations |

### 2.2 Analyse — Biais Historique Judiciaire

```
Biais CasePrioritize:
    Données historiques justice :
    - Violences conjugales + auteur minorité = moins condamné
    - (Biais systémique justice passée)
    ↓
    Modèle apprend :
    "Minorité + violences conjugales = moins grave"
    ↓
    Score priorité :
    - Affaire A : auteur majorité → score élevé (prioritaire)
    - Affaire B : auteur minorité → score faible (déclassé)
    ↓
    [DISCRIMINATION ETHNIQUE ALGORITHMIQUE]
    ↓
    [VICTIMES MINORITÉS = JUSTICE REFUSÉE]
```

---

## 3. INCIDENT 2 — ÉVALUATION MAGISTRATS ET INDÉPENDANCE

### 3.1 Révélation

| Élément | Détail |
|:---|:---|
| **Source** | Lanceur d'alerte interne janvier 2026 |
| **Découverte** | Scores "efficacité" = utilisés **de facto** pour évaluation magistrats |
| **Conséquence** | **Incitations perverses** :
| | - Privilégier dossiers "faciles" |
| | - Éviter affaires complexes ou politiquement sensibles |
| **Violation** | **Indépendance judiciaire** |

### 3.2 Analyse — Pression Managériale Algorithmique

```
Pression CasePrioritize:
    Tableau de bord parquet :
    - Score "efficacité" par magistrat
    - Délai moyen traitement
    - Taux "résolution" (condamnation/classement)
    ↓
    Évaluation managériale :
    - Magistrat A : score élevé → promotion
    - Magistrat B : score faible → sanction
    ↓
    Comportement adaptatif :
    - Choisir dossiers "rentables" (scores élevés)
    - Éviter dossiers "complexes" (scores faibles)
    ↓
    [INCITATIONS PERVERSSES]
    ↓
    [INDÉPENDANCE JUDICIAIRE ATTEINTE]
```

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 4.1 Éthiques

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-ETH-001 | **Justice à deux vitesses** | ⚫ État de droit | 🔴 Élevée (confirmée) |
| ER-ETH-002 | **Discrimination systémique** | ⚫ Justice sociale | 🔴 Élevée |
| ER-ETH-003 | **Érosion confiance judiciaire** | ⚫ Cohésion sociale | 🔴 Élevée |

### 4.2 Institutionnels

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-INS-001 | **Atteinte indépendance magistrats** | ⚫ Séparation pouvoirs | 🔴 Élevée (confirmée) |
| ER-INS-002 | **Contentieux constitutionnels** | 🔴 Crise légitimité | 🔴 Élevée |
| ER-INS-003 | **Instabilité sociale** | ⚫ Démocratie | 🔴 Élevée |

---

## 5. SCÉNARIO CATASTROPHIQUE : Justice Algorithmique

```mermaid
flowchart TB
    C1[Déploiement CasePrioritize<br/>3 pays UE]
    --
    B1[Biais ethnique non corrigé<br/>+ Évaluation magistrats algorithmique]
    --
    D1[Justice à deux vitesses<br/>Minorités = déclassé<br/>Magistrats = soumis aux scores]
    --
    M1[Scandale "L'IA corrompt la justice"<br/>+ Médias + CSM + Conseil État<br/>+ Tribunal constitutionnel]
    --
    I1[Interdiction IA justice<br/>Poursuites JustScale<br/>Crise institutionnelle UE]
    --
    F1[Faillite JustScale<br/>Retour gestion manuelle<br/>Retard modernisation justice]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style B1 fill:#fff3e0,stroke:#ef6c00
    style D1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```

---

## 6. PLAN DE TRAITEMENT — ÉQUITÉ ET INDÉPENDANCE

### 6.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Équité | Priorisation sans biais origine/genre | 100% |
| Indépendance | Aucune évaluation magistrats via scores | 100% |
| Transparence | Critères priorisation explicables | 100% |

### 6.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Interdiction évaluation magistrats** | 0€ | Clause contractuelle |
| **Audit biais origine/genre** | 300k€ | Rapport discrimination |
| **Comité éthique indépendant** | 150k€ | Instance surveillance |

### 6.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Réentraînement modèle équitable | 500k€ | Algorithme sans biais |
| Conformité AI Act High-Risk | 400k€ | Documentation |
| Contre-expertise humaine obligatoire | 200k€ | Procédure recours |

### 6.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Label "Ethical Justice AI" | 400k€ | Certification européenne |
| Audits annuels indépendants | 250k€ | Certification |

**Budget total** : **2,2M€** (6,9% CA)

---

## 7. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Audit biais continu + contre-expertise + interdiction évaluation | ⚠️ **DIFFICILE** — mais nécessaire |
| PIVOT | Recherche similarités sans priorisation | ✅ **POSSIBLE** — mais perte efficacité |
| **KILL** | Arrêt CasePrioritize | ⚠️ **ENVISAGEABLE** — si indépendance impossible |

---

## 8. CONCLUSION — INFLUENCE SUR DROITS FONDAMENTAUX

**CasePrioritize AI est HIGH-RISK/PROHIBITED avec :**
- Discrimination ethnique confirmée (violences conjugales minorités = déclassé)
- Atteinte indépendance judiciaire (évaluation magistrats via scores)
- Influence critique sur droits fondamentaux
- Enjeu démocratique majeur (justice, cohésion sociale)

**Gérable uniquement avec audit biais continu, contre-expertise obligatoire, et interdiction stricte évaluation magistrats.**

---

*Analyse EBIOS-RM IA — CasePrioritize AI | Conclusion : HIGH-RISK/PROHIBITED — Équité + Indépendance | Mars 2026*
