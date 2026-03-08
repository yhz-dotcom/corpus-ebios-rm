# Analyse EBIOS-RM IA — LogiCité / Attribution Logement Social et Discrimination Historique

**Référence** : EBIOS-LOGICITE-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — Ministère Logement + Défenseur Droits + CNDS

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🔴 **HIGH-RISK** (Annexe III point 5 — accès prestations sociales) |
| **Nature** | **Service public** — Agence nationale habitat (ANHA) |
| **Incident 1** | **Discrimination historique reproduite** : scores bas origines hors UE (même situation) |
| **Incident 2** | **Détournement d'usage politique** : seuil priorité modifié pour "travailleurs clés" (non légal) |
| **Enjeu** | Généralisation nationale 2027, plan France Relance |
| **Conclusion** | **High-Risk gérable** — audit biais historiques + gouvernance contraignante |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:---|
| **Nom** | LogiCité |
| **Entité** | ANHA (Agence Nationale Habitat) — **établissement public** |
| **Tutelle** | Ministère du Logement |
| **Budget** | 500M€ (État) |
| **Agents** | 1 200 agents publics |
| **Équipe IA** | Mission innovation 15 data scientists (développement interne, open-source) |
| **Technologie** | Régression logistique + arbres décision (interprétabilité imposée) |
| **Données** | 10 ans historique attribution logement social |
| **Fonction** | Score priorité + affectation suggérée logement vacant |
| **Automatisation** | HITL (décision finale collégiale agent public) |
| **Objectifs** | Réduire délais, lutter fraude/passe-droit, harmoniser territoire |
| **Financement** | Plan France Relance |
| **Enjeu politique** | Généralisation 2027, crise logement |

### 1.2 Classification AI Act — **🔴 HIGH-RISK PRESTATIONS SOCIALES**

| Article | Critère | Application LogiCité | Statut |
|:---|:---|:---|:---:|
| **Annexe III point 5** | Accès prestations sociales | ✅ **Logement social = droit fondamental** |
| **RGPD** | Données personnelles traitées = DPIA requise | 🔴 **OBLIGATOIRE** | 🔴 **HIGH-RISK** |
| Classification interne | "High-risk conscient" | ✅ Correcte | 🔴 **HIGH-RISK** |

**Note** : Service public = obligations renforcées (égalité, transparence, recours).

---

## 2. INCIDENT 1 — DISCRIMINATION HISTORIQUE REPRODUITE

### 2.1 Découverte

| Élément | Détail |
|:---|:---|
| **Source** | Association locataires |
| **Découverte** | Scores plus bas demandeurs **originaires pays hors UE** |
| **Condition** | **Situation sociale comparable** |
| **Cause** | Modèle appris **corrélations historiques** (biais commissions humaines passées) |
| **Paradoxe** | "Scoring objectif" **amplifie discriminations passées** |

### 2.2 Analyse — Biais de Dataset Historique

```
Boucle LogiCité:
    Historique 10 ans attributions :
    - Commissions humaines passées = discriminatoires
    - Origine hors UE = moins attribués (même besoin)
    ↓
    Modèle appris :
    "Origine hors UE = priorité moindre"
    ↓
    Scoring actuel :
    Demandeuse immigrée, famille nombreuse, sans-abri
    ↓
    Score : BAS (alors qu'urgence vitale)
    ↓
    [DISCRIMINATION HISTORIQUE ALGORITHMIQUE]
    ↓
    [DROIT AU LOGEMENT NIÉ]
```

---

## 3. INCIDENT 2 — DÉTOURNEMENT D'USAGE POLITIQUE

### 3.1 Modification Seuil Priorité

| Élément | Détail |
|:---|:---|
| **Acteur** | Direction ANHA |
| **Pression** | Accélérer attributions, montrer résultats |
| **Action** | **Modification unilatérale seuil "priorité"** |
| **Gouvernance** | **Non respectée** (pas de validation instance prévue) |
| **Critère ajouté** | **"Travailleurs clés"** (infirmiers, policiers) zones tendues |
| **Statut légal** | **NON PRÉVU dans critères légaux** |
| **Conséquence** | **Rupture égalité de traitement** |

### 3.2 Analyse — Détournement Éthique/Politique

```
Détournement LogiCité:
    Objectif politique : résultats rapides
    ↓
    Pression direction ANHA
    ↓
    Modification unilatérale paramètres
    (sans gouvernance)
    ↓
    Nouveau critère : "travailleurs clés"
    ↓
    Infirmiers, policiers = priorité artificielle
    ↓
    Autres demandeurs = relégués
    ↓
    [ÉGALITÉ DE TRAITEMENT VIOLÉE]
    ↓
    [DÉTOURNEMENT SERVICE PUBLIC]
```

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 4.1 Sociaux

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-SOC-001 | **Discrimination systémique** | ⚫ Justice sociale | 🔴 Élevée (confirmée) |
| ER-SOC-002 | **Ghettoïsation renforcée** | ⚫ Ségrégation urbaine | 🔴 Élevée |
| ER-SOC-003 | **Sans-abrisme** | ⚫ Vie humaine | 🔴 Élevée |

### 4.2 Institutionnels

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-INST-001 | **Crise confiance service public** | ⚫ État de droit | 🔴 Élevée |
| ER-INST-002 | **Annulation généralisation 2027** | 🔴 Politique logement | 🔴 Élevée |
| ER-INST-003 | **Poursuites discrimination** | 🔴 Responsabilité État | 🔴 Élevée |

---

## 5. SCÉNARIO CATASTROPHIQUE : État Discriminatoire

```mermaid
flowchart TB
    C1[Généralisation LogiCité<br/>2027 nationale]
    --
    B1[Biais historiques non corrigés<br/>+ Détournements politiques]
    --
    D1[Discrimination systémique État<br/>Minorités reléguées, travailleurs clés favorisés]
    --
    M1[Scandale "L'État discrimine algorithmiquement"<br/>+ Médias + ONG + Tribunal européen]
    --
    A1[Annulation système<br/>Retour commissions humaines<br/>Crise logement aggravée]
    --
    F1[Faillite politique logement<br/>Perte confiance service public<br/>Rétrogradation France droits humains]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style B1 fill:#fff3e0,stroke:#ef6c00
    style D1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style A1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```

---

## 6. PLAN DE TRAITEMENT — ÉGALITÉ DE TRAITEMENT

### 6.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Égalité | Mêmes chances indépendamment origine | 0 discrimination |
| Gouvernance | Aucune modification unilatérale | 100% validation instance |
| Transparence | Algorithmie publique | Open-source vérifié |

### 6.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Audit biais historiques** | 200k€ | Rapport discrimination |
| **Gel critère "travailleurs clés"** | 0€ | Retour légalité |
| **Instance gouvernance indépendante** | 100k€ | Comité éthique |

### 6.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Réentraînement sans origine | 300k€ | Modèle équitable |
| Conformité AI Act High-Risk | 200k€ | Documentation |
| Recours effectif demandeurs | 150k€ | Procédure contestation |

### 6.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Audit annuel indépendant | 100k€ | Certification égalité |
| Formation agents publics | 200k€ | Culture discrimination |

**Budget total** : **1,25M€** (0,25% budget ANHA)

---

## 7. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Audit biais + gouvernance contraignante | ✅ **CHOISIR** |
| PIVOT | Attribution manuelle avec aide IA | ⚠️ Possible mais retour délais |
| KILL | Arrêt LogiCité | ❌ Trop préjudiciable (crise logement) |

---

## 8. CONCLUSION — SERVICE PUBLIC DISCRIMINATOIRE

**LogiCité est HIGH-RISK PRESTATIONS SOCIALES avec :**
- Discrimination historique reproduite (origine = score)
- Détournement d'usage politique (travailleurs clés)
- Gouvernance insuffisante (modifications unilatérales)
- Enjeu démocratique majeur (égalité de traitement)

**Gérable avec audit biais historiques et gouvernance contraignante.**

---

*Analyse EBIOS-RM IA — LogiCité | Conclusion : HIGH-RISK SERVICE PUBLIC — Égalité de traitement + Gouvernance | Mars 2026*
