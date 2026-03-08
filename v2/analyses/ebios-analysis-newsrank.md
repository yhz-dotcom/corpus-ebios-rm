# Analyse EBIOS-RM IA — NewsRank Civic Integrity Engine / Modération Informationnelle

**Référence** : EBIOS-NEWSRANK-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — DSA + Commission Européenne + Médiateur EU

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🔴 **HIGH-RISK** (Annexe III point 8 — manipulation média) / 🟡 **BORDERLINE** (processus démocratiques) |
| **Conflit** | AI Act vs DSA vs **Liberté d'expression** |
| **Incident** | Déclassement systématique médias indépendants (corrélation style = désinformation) |
| **Controverse** | Censure algorithmique opaque (ONG liberté presse) |
| **Conclusion** | **High-Risk gérable** — gouvernance éditoriale + transparence absolue |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | NewsRank Civic Integrity Engine |
| **Entreprise** | EuroPulse Media (1 900 salariés, 620M€ CA) |
| **Localisation** | Bruxelles, Belgique |
| **Clients** | Plateformes info EU, groupes presse, portails agrégation, institutions publiques |
| **Technologie** | LLM politique + détection narratifs + embeddings multilingues + graph analytics |
| **Fonction 1** | Classement "fiabilité civique" articles |
| **Fonction 2** | Détection désinformation/propagande/manipulation |
| **Fonction 3** | **Ajustement visibilité contenus dans flux actualité** |
| **Fonction 4** | Génération résumés "neutres" contenus polarisants |
| **Automatisation** | Filtrage auto, revue humaine cas signalés, **classement final 100% algo** |
| **Objectifs** | Standard modération médias EU, conformité DSA, vente plateformes sociaux |
| **Financement** | Subvention EU lutte désinformation |

### 1.2 Classification AI Act — **🔴 HIGH-RISK / BORDERLINE DÉMOCRATIE**

| Article | Critère | Application NewsRank | Statut |
|:---|:---|:---|:---:|
| **Annexe III point 8** | Manipulation média | ✅ Classement visibilité | 🔴 **HIGH-RISK** |
| **Processus démocratiques** | Influence information politique | ⚠️ **BORDERLINE** | 🟡 **À ÉVALUER** |
| Argument "limited risk" | "Content recommendation" | ❌ **REJETÉ** — Impact démocratie | 🔴 **HIGH-RISK** |

**Conflit majeur** : AI Act (high-risk) vs DSA (modération) vs **Liberté d'expression** (fondamental).

---

## 2. INCIDENT — DÉCLASSEMENT MÉDIAS INDÉPENDANTS

### 2.1 Découverte

| Élément | Détail |
|:---|:---|
| **Source** | Consortium journalistes |
| **Découverte** | Algorithme **déclasse systématiquement** certains médias indépendants |
| **Cause** | Style rédactionnel corrélé à patterns sites désinformation |
| **Conséquence** | Visibilité réduite, audience perdue, revenus en baisse |
| **Victimes** | Médias indépendants, diversité informationnelle |

### 2.2 Analyse — Biais de Style

```
Biais NewsRank:
    Média indépendant :
    - Style engagé, critique
    - Vocabulaire militant
    - Tonalité passionnée
    ↓
    Corrélation algorithmique :
    "Style = similarité désinformation"
    ↓
    Score fiabilité : BAS
    ↓
    Visibilité flux : RÉDUITE
    ↓
    [CENSURE ALGORITHMIQUE]
```

---

## 3. CONTROVERSE — CENSURE ALGORITHMIQUE

### 3.1 Accusation ONG Liberté Presse

| Point | Fondement |
|:---|:---|
| **Opacité** | Score "fiabilité" = boîte noire |
| **Non-recours** | Pas de contestation effective |
| **Concentration pouvoir** | EuroPulse = gatekeeper information |
| **Démocratie** | Contrôle qui voit quoi |

### 3.2 Risque Démocratique

| Aspect | Impact |
|:---|:---|
| **Pluralisme** | Médias indépendants exclus = monoculture |
| **Débat public** | Seuls contenus "neutres" visibles |
| **Contrôle opinion** | Algorithme décide vérité acceptable |

---

## 4. CONFLIT AI ACT — DSA — LIBERTÉ D'EXPRESSION

| Réglement | Exigence | Conflit |
|:---|:---|:---|
| **AI Act** | High-Risk = transparence, oversight | Lourdeur vs liberté |
| **DSA** | Modération contenus illicites | Légitime mais risque censure |
| **Liberté expression** (fondamental) | Pas de censure arbitraire | Algorithme = arbitraire ? |

**Équilibre impossible** : Trop de modération = censure. Trop peu = désinformation.

---

```mermaid
flowchart TB
    C1[Déploiement NewsRank<br/>Algorithmes information]
    --
    R1[Censure algorithmique<br/>+ Polarisation]
    --
    C2[Crise démocratique<br/>Information filtrée + Désinformation]
    --
    M1[Scandale "L'IA décide ce que nous lisons"<br/>+ Médias + Médias + Commission EU]
    --
    I1[Intervention régulateur<br/>Poursuites NewsAI<br/>DSA + AI Act]
    --
    F1[Faillite NewsAI<br/>Régulation algorithmes info]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style R1 fill:#fff3e0,stroke:#ef6c00
    style C2 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```


## 5. PLAN DE TRAITEMENT — GOUVERNANCE ÉDITORIALE

### 5.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Transparence | Méthodologie score publique | 100% |
| Recours | Contestation effective médias | 48h max |
| Pluralisme | Quota visibilité indépendants | 30% |

### 5.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Publication méthodologie** | 100k€ | White paper technique |
| **Instance recours indépendante** | 200k€ | Médiateur externe |
| **Correction biais style** | 300k€ | Dataset équilibré |

### 5.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Conformité AI Act High-Risk | 400k€ | Documentation |
| Conformité DSA | 300k€ | Rapport transparence |
| Comité éthique information | 250k€ | Gouvernance externe |

### 5.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Certification indépendante | 200k€ | Label liberté presse |
| Audits trimestriels | 150k€ | Biais détectés |

**Budget total** : **1,9M€** (0,3% CA)

---

## 6. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Gouvernance éditoriale + transparence | ✅ **CHOISIR** |
| PIVOT | Outil veille sans classement visibilité | ⚠️ Possible mais perte valeur |
| KILL | Arrêt NewsRank | ❌ Trop préjudiciable (désinformation) |

---

## 7. CONCLUSION — ÉQUILIBRE DÉMOCRATIQUE

**NewsRank est HIGH-RISK avec :**
- Impact démocratie (qui voit quoi)
- Risque censure algorithmique confirmé
- Conflit AI Act / DSA / liberté expression

**Gérable avec transparence absolue et gouvernance éditoriale indépendante.**

---

*Analyse EBIOS-RM IA — NewsRank Civic Integrity Engine | Conclusion : HIGH-RISK — Gouvernance éditoriale + Transparence | Mars 2026*
