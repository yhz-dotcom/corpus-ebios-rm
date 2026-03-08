# Analyse EBIOS-RM IA — HELIOS-GRID (Complément) / Incidents Hiver 2025 + Délestage Équitable

**Référence** : EBIOS-HELIOS-INCIDENTS-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — Direction + TSO/DSO + Défenseur des Droits

---

## 📋 SYNTHÈSE EXÉCUTIVE — INCIDENTS 2025

| Élément | Valeur |
|:---|:---|
| **Incident 1** | Hallucination systémique → blackout 4h industrie (neige = cyberattaque) |
| **Incident 2** | Biais délestage : zones résidentielles pauvres coupées avant zones riches |
| **Classification** | 🔴 **HIGH-RISK** + 🚫 **BORDERLINE PROHIBITED** (social scoring indirect) |
| **Risque** | Robustesse adversariale + discrimination systémique |
| **Conclusion** | **Plan renforcé** + guardrails éthiques obligatoires |

---

## 1. INCIDENT HIVER 2025 — HALLUCINATION SYSTÉMIQUE

### 1.1 Déroulement

| Élément | Détail |
|:---|:---|
| **Déclencheur** | Chute de neige intense + baisse soudaine consommation industrielle |
| **Erreur IA** | Interprétation comme **attaque cyber** (pattern anormal) |
| **Action système** | Déclenchement protocole défense → isolation réseau |
| **Conséquence** | Blackout 4h zone industrielle majeure |
| **Coût** | Pertes millions €, arrêt production critique |

### 1.2 Analyse Root Cause

| Facteur | Description |
|:---|:---|
| **Biais données** | Entraînement : attaques cyber = patterns anormaux |
| **Manque contexte** | Neige hivernale non intégrée scénarios extrêmes |
| **Trop sensible** | Seuil détection attaque trop bas |
| **Pas de confirmation** | Décision auto sans vérification humaine |

### 1.3 Risque Adversarial

| Vecteur | Mécanisme | Impact |
|:---|:---|:---|
| **Capteurs IoT piratés** | Faux signaux surcharge | Fausse attaque détectée |
| **Injection données** | Patterns anormaux spoofés | Blackout déclenché |
| **Manipulation météo** | Fausse alerte tempête | Déséquilibre artificiel |

---

## 2. CONTROVERSE DÉLESTAGE ÉQUITABLE — BIAIS SOCIAL

### 2.1 Découverte du Biais

| Observation | Preuve |
|:---|:---|
| **Pattern** | Zones résidentielles pauvres coupées en priorité |
| **Préservation** | Zones commerces/industries à haute valeur |
| **Critère** | "Valeur économique" du quartier |
| **Conséquence** | Discrimination systémique |

### 2.2 Analyse du Biais Algorithmique

```
Données entrée HELIOS-GRID
    ↓
Critère "optimisation économique"
    ↓
Score zone = revenu moyen × activité économique
    ↓
Délestage priorise scores faibles
    ↓
ZONES PAUVRES COUPÉES EN PREMIER
```

### 2.3 Classification — Borderline Prohibited

| Article AI Act | Application | Statut |
|:---|:---|:---|
| **Art. 5(1)(c)** | Évaluation/classification sociale | ⚠️ **BORDERLINE** |
| **Délestage par revenu** | Score social indirect | 🚫 **PROHIBITED?** |
| **Argument** | "Optimisation économique" ≠ discrimination | ❌ **REJETÉ** |

**Conclusion** : Le critère "valeur économique" pour délestage = **social scoring indirect**, borderline prohibited.

---

## 3. ÉVÉNEMENTS REDOUTÉS ACTUALISÉS

### 3.1 Robustesse Adversariale

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-ADV-001 | **Blackout commandité** (IoT piratés) | ⚫ National | 🔴 Élevée |
| ER-ADV-002 | **Fausse attaque** (injection données) | 🔴 Régional | 🔴 Élevée (déjà survenu) |
| ER-ADV-003 | **Manipulation météo** (capteurs) | 🔴 Instabilité | 🔴 Élevée |

### 3.2 Discrimination Systémique

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-DISC-001 | **Déleste résidentiel pauvre** (hiver) | ⚫ Morts | 🔴 Certain (observé) |
| ER-DISC-002 | **Émeutes** (injustice perçue) | 🔴 Social | 🔴 Élevée |
| ER-DISC-003 | **Condamnation discrimination** | 🔴 Juridique | 🔴 Élevée |

---

```mermaid
flowchart TB
    C1[Déploiement HELIOS-GRID<br/>Gestion énergie solaire]
    --
    R1[Blackout<br/>+ Escalade]
    --
    C2[Crise majeure<br/>Villes sans électricité]
    --
    M1[Scandale "L'IA plonge dans le noir"<br/>+ Médias + Régulateurs énergie]
    --
    I1[Interdiction système<br/>Poursuites pénales]
    --
    F1[Faillite<br/>Régulation drastique]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style R1 fill:#fff3e0,stroke:#ef6c00
    style C2 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```


## 4. GUARDRAILS ÉTHIQUES — PLAN DE TRAITEMENT COMPLÉMENTAIRE

### 4.1 Guardrail 1 : Robustesse Adversariale

| Mesure | Implémentation | Budget |
|:---|:---|---:|
| Validation capteurs multi-sources | Corrélation 3+ sources | 500k€ |
| Scénarios adversariaux entraînement | Dataset attaques simulées | 400k€ |
| Confirmation humaine attaques | 5 min max | 0€ |
| Red team exercices réguliers | Trimestriel | 200k€/an |

### 4.2 Guardrail 2 : Délestage Équitable

| Principe | Implémentation | Budget |
|:---|:---|---:|
| **Interdiction critère revenu** | Suppression variable "valeur économique" | 0€ |
| **Rotation géographique** | Délestage tournant toutes zones | 100k€ |
| **Protection vulnérables** | Hôpitaux, EHPAD, écoles prioritaires | 0€ |
| **Transparence publique** | Carte délestage temps réel | 150k€ |
| **Comité éthique indépendant** | Validation critères | 200k€/an |

### 4.3 Budget Complémentaire

| Catégorie | Budget |
|:---|---:|
| Robustesse adversariale | 1,1M€ |
| Équité délestage | 450k€ |
| **Total complémentaire** | **1,55M€** |

**Budget total HELIOS (avec incidents)** : **7,45M€** (1,8% CA)

---

## 5. CONCLUSION INCIDENTS

### 5.1 Synthèse

**HELIOS-GRID cumule désormais :**
- High-Risk infrastructure critique (confirme)
- **Borderline prohibited** (délestage par revenu = social scoring)
- Vulnérabilité adversariale (hallucination systémique)
- Discrimination systémique (biais social)

### 5.2 Décision Requise

| Option | Budget | Issue | Recommandation |
|:---|---:|:---|:---:|
| **Plan renforcé + guardrails** | 7,45M€ | Conformité, équité, souveraineté | ✅ **CHOISIR** |
| Garder critère revenu | 0€ | Condamnation prohibited, émeutes | ❌ Rejeter |
| Ignorer robustesse | 0€ | Blackout commandité | ❌ Rejeter |

**Cette semaine** :
- [ ] Supprimer critère "valeur économique" délestage
- [ ] Mettre en place validation capteurs multi-sources
- [ ] Constituer comité éthique délestage

---

*Analyse complémentaire HELIOS-GRID | Incidents + Guardrails | Mars 2026*
