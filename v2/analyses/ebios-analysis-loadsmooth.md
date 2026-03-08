# Analyse EBIOS-RM IA — LoadSmooth-7 / Régulation Tension Réseau Électrique

**Référence** : EBIOS-LOADSMOOTH-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL CRITIQUE — CREG + Elia + ENISA

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🔴 **HIGH-RISK CRITIQUE** (Annexe III point 2) |
| **Classification EBIOS** | 🔴 **Level 3 Renforcé** — infrastructure critique nationale |
| **Incident 1** | Quasi-blackout : oscillation IA (pompage) sur fluctuation solaire |
| **Incident 2** | Attaque empoisonnement données météo → décisions destructrices |
| **Conclusion** | **Plan de traitement critique** — red team + diversité scénarios |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | LoadSmooth-7 |
| **Entreprise** | ElectraNet Belgium (3 200 salariés, 1,2Md€ CA) |
| **Localisation** | Bruxelles, Wallonie, Flandre |
| **Clients** | Elia (GRT), fournisseurs énergie, industriels |
| **Technologie** | Deep Learning + Edge Computing + automates sous-stations |
| **Fonction** | Régulation prédictive tension, ajustement transformateurs/compensateurs |
| **Automatisation** | Full automation (humain trop lent en pratique) |
| **Objectifs** | +25% capacité renouvelables sans nouvelles lignes (Green Deal wallon) |
| **Financement** | BEI 50M€ avec clauses performance/résilience |
| **Pression** | Pénalités CREG + perte confiance politique si défaillance |

### 1.2 Classification AI Act — **🔴 HIGH-RISK CRITIQUE CONFIRMÉE**

| Article | Critère | Application LoadSmooth | Statut |
|:---|:---|:---|:---:|
| **Annexe III point 2** | Infrastructure critique énergie | ✅ Gestion réseau électrique national |
| **RGPD** | Données personnelles traitées = DPIA requise | 🔴 **OBLIGATOIRE** | 🔴 **HIGH-RISK** |
| **Safety component** | Modification état physique réseau | ✅ Transformateurs, compensateurs | 🔴 **CRITIQUE** |
| Classification interne | "High-risk de toute évidence" | ✅ Correcte | 🔴 **CONFIRMÉE** |

---

## 2. INCIDENT 1 — QUASI-BLACKOUT OSCILLATION

### 2.1 Déroulement

| Élément | Détail |
|:---|:---|
| **Déclencheur** | Passage nuageux rapide sur fermes solaires |
| **Fluctuation** | Production solaire chute brutalement |
| **Réaction IA** | Actions correctives automatiques |
| **Problème** | **Non entraînée sur ce scénario** |
| **Résultat** | **Oscillation (pompage)** — actions contradictoires |
| **Danger** | Sous-région sur le point de tomber |
| **Sauvetage** | Opérateur humain : passage manuel après **90 secondes** |

### 2.2 Analyse — Manque Diversité Scénarios

```
Boucle oscillation LoadSmooth-7:
    Passage nuageux → solaire ↓
    ↓
    IA détecte sous-tension → augmente compensation
    ↓
    Nuage passe → solaire ↑
    ↓
    IA détecte surtension → diminue compensation
    ↓
    Nouveau nuage → solaire ↓
    ↓
    [OSCILLATION RAPIDE = POMPAGE]
    ↓
    Instabilité critique
    ↓
    [QUASI-BLACKOUT]
```

**Root cause** : Dataset entraînement = scénarios historiques, pas **variations rapides météo**.

---

## 3. INCIDENT 2 — ATTAQUE EMPOISONNEMENT DONNÉES

### 3.1 Vulnérabilité Découverte

| Élément | Détail |
|:---|:---|
| **Chercheur** | Sécurité (responsible disclosure) |
| **Vecteur** | Flux "prévisions météo" |
| **Problème** | **Source non sécurisée** |
| **Attaque** | Injection fausses données météo |
| **Conséquence** | IA force décisions **destructrices** transformateurs |
| **Impact** | Coupures localisées possibles |

### 3.2 Analyse — Chaîne d'Approvisionnement Faible

```
Chaîne LoadSmooth-7:
    Source météo externe (non sécurisée)
    ↓
    [POINT D'ENTRÉE ATTAQUANT]
    ↓
    LoadSmooth-7 (fait confiance données)
    ↓
    Décisions transformateurs
    ↓
    [DOMMAGES PHYSIQUES RÉSEAU]
```

**Vulnérabilité critique** : Source externe non vérifiée → décisions physiques.

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 4.1 Opérationnels

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-OP-001 | **Blackout national** (oscillation non contrôlée) | ⚫ Belgique | 🔴 Élevée |
| ER-OP-002 | **Destruction transformateurs** (attaque) | 🔴 Infrastructure | 🔴 Élevée (démontrée) |
| ER-OP-003 | **Perte confiance renouvelables** | 🔴 Green Deal | 🔴 Élevée |

### 4.2 Cyber

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-CYBER-001 | **Attaque empoisonnement météo** | 🔴 Coupures | 🔴 Élevée (démontrée) |
| ER-CYBER-002 | **Attaque chaîne approvisionnement** | ⚫ Blackout | 🔴 Élevée |
| ER-CYBER-003 | **Ransomware + IA** | ⚫ Double crise | 🔴 Élevée |

---

## 5. SCÉNARIO CATASTROPHIQUE : Blackout Belgique

```mermaid
flowchart TB
    C1[Passage nuageux + attaque météo<br/>LoadSmooth-7 en action]
    --
    O1[Oscillation IA + données fausses<br/>Déséquilibre critique]
    --
    B1[BLACKOUT BELGIQUE<br/>Hôpitaux, transports, industries]
    --
    M1[Scandale "Green Deal a tué réseau"<br/>+ Enquête parlementaire<br/>+ Poursuites dirigeants]
    --
    S1[Pénalités CREG<br/>Perte BEI 50M€<br/>Faillite ElectraNet]
    --
    F1[Retour énergies fossiles<br/>Retard décennie renouvelables<br/>Climat UE compromise]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style O1 fill:#fff3e0,stroke:#ef6c00
    style B1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style M1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style S1 fill:#b71c1c,stroke:#000,color:#fff
    style F1 fill:#7f0000,stroke:#000,color:#fff
```

---

## 6. PLAN DE TRAITEMENT CRITIQUE

### 6.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Zéro oscillation | Diversité scénarios extrêmes | 100% couvert |
| Sécurité données | Chaîne approvisionnement vérifiée | 0 source non sécurisée |
| Résilience cyber | Red team exercices | Trimestriel |

### 6.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Sécurisation flux météo** | 300k€ | Source vérifiée/cryptée |
| **Scénarios oscillation** | 200k€ | Dataset complémentaire |
| **Circuit breaker manuel** | 100k€ | Arrêt IA < 30 secondes |

### 6.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Red team cyber | 500k€ | Vulnérabilités identifiées |
| Simulation extrêmes météo | 400k€ | Modèle robuste |
| Conformité BEI | 300k€ | Clauses résilience |

### 6.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Certification ENISA | 400k€ | Infrastructure critique |
| Diversité algorithmique | 300k€ | Multi-modèles |

**Budget total** : **2,5M€** (0,2% CA)

---

## 7. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Sécurisation + diversité scénarios | ✅ **CHOISIR** |
| PIVOT | Régulation moins automatisée | ⚠️ Possible mais retard Green Deal |
| KILL | Arrêt LoadSmooth-7 | ❌ Impossible (renouvelables dépendent) |

---

## 8. CONCLUSION — INFRASTRUCTURE CRITIQUE VULNÉRABLE

**LoadSmooth-7 est HIGH-RISK CRITIQUE avec :**
- Oscillation IA confirmée (manque diversité scénarios)
- Attaque empoisonnement données démontrée
- Chaîne approvisionnement faible
- Green Deal wallon dépendant

**Gérable avec sécurisation cyber et diversité algorithmique.**

---

*Analyse EBIOS-RM IA — LoadSmooth-7 | Conclusion : HIGH-RISK CRITIQUE — Sécurisation + Diversité | Mars 2026*
