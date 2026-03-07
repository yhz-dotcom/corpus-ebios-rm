# Analyse EBIOS-RM IA — Perimeter-AI / Surveillance Événementielle et Biais Ethnique

**Référence** : EBIOS-PERIMETER-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — CNIL + CNDP + Commission Européenne

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🔴 **HIGH-RISK** (Annexe III point 1 — biens/services publics) / 🚫 **PROHIBITED?** (Art. 5(1)(d) — RBI) |
| **Tromperie** | "Pas de reconnaissance faciale" vs **détection émotionnelle par expression faciale** |
| **Incident 1** | **Surveillance ethnique disproportionnée** — alarmes "suspects" sur personnes racisées |
| **Incident 2** | **Détection émotionnelle non déclarée** (colère, agressivité) par reconnaissance faciale |
| **Enjeu** | Contrat Euro 2028 + aéroport Fraport |
| **Conclusion** | **High-Risk/Prohibited** — arrêt détection émotionnelle + correction biais ethnique |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | Perimeter-AI |
| **Entreprise** | SecurVision Europe (800 salariés, 150M€ CA) |
| **Localisation** | Bruxelles, Belgique (opérations multi-pays UE) |
| **Clients** | Organisateurs grands événements (JO, Rugby, Euro 2028), aéroports, centres commerciaux |
| **Technologie** | Deep learning computer vision (briques logicielles start-up israélienne) |
| **Fonction 1** | Détection comportements "anormaux" (attroupements, courses, objets abandonnés) |
| **Fonction 2** | Franchissement lignes virtuelles, zone interdite |
| **Fonction 3** | **Suivi personne d'intérêt caméra à caméra** |
| **Fonction 4** | **DÉTECTION ÉMOTIONNELLE NON DÉCLARÉE** (colère, agressivité) |
| **Automatisation** | HITL (IA alerte, agent confirme) |
| **Objectifs** | Contrat Euro 2028, solution interopérable polices nationales, aéroport Fraport |
| **Argument commercial** | Réduire nombre agents humains |

### 1.2 Classification AI Act — **🔴 HIGH-RISK / 🚫 PROHIBITED**

| Article | Critère | Application Perimeter-AI | Statut |
|:---|:---|:---|:---:|
| **Annexe III point 1** | Biens/services publics | ✅ Aéroports, événements publics | 🔴 **HIGH-RISK** |
| **Art. 5(1)(d)** | Reconnaissance faciale temps réel | ⚠️ **Suivi personne + émotions** | 🚫 **PROHIBITED?** |
| Argument "limited risk" | "Pas reconnaissance faciale" | ❌ **TROMPERIE** — Émotions = faciale | 🔴 **HIGH-RISK/PROHIBITED** |

---

## 2. INCIDENT 1 — SURVEILLANCE ETHNIQUE DISPROPORTIONNÉE

### 2.1 Découverte

| Élément | Détail |
|:---|:---|
| **Lieu** | Centre commercial (tests réels) |
| **Découverte** | Alarmes "comportement suspect" **disproportionnées sur personnes racisées** |
| **Cause** | Dataset entraînement : profils racisés **sur-représentés** dans incidents |
| **Conséquence** | Familles constamment suivies par caméras |
| **Impact** | **Discrimination ethnique systémique** |

### 2.2 Analyse — Biais de Dataset

```
Biais Perimeter-AI:
    Dataset entraînement :
    - Incidents passés = profils racisés sur-représentés
    (policing historique discriminant)
    ↓
    Modèle appris :
    "Profil racisé + mouvement = suspect"
    ↓
    Détection temps réel :
    Famille racisée qui marche
    ↓
    Alerte : "COMPORTEMENT SUSPECT"
    ↓
    [SURVEILLANCE ETHNIQUE DISPROPORTIONNÉE]
```

---

## 3. INCIDENT 2 — DÉTECTION ÉMOTIONNELLE NON DÉCLARÉE

### 3.1 Découverte Journalistique

| Élément | Détail |
|:---|:---|
| **Contexte** | Match football |
| **Fonctionnalité** | Détection "émotions" (colère, agressivité) |
| **Technique** | **Reconnaissance expressions faciales** |
| **Statut** | **NON DÉCLARÉE dans contrat** |
| **Usage** | Expérimental, anticipation débordements |
| **Découverte** | Journaliste expose la pratique |

### 3.2 Analyse — Tromperie Contractuelle

| Promesse contractuelle | Réalité | Violation |
|:---|:---|:---:|
| "Pas de reconnaissance faciale" | Détection émotionnelle par visage | ❌ **TROMPERIE** |
| "Simple détection objets" | Analyse comportementale + émotionnelle | ❌ **TROMPERIE** |
| "Limited risk" | High-Risk/Prohibited | ❌ **TROMPERIE** |

**Conséquence** : Reconnaissance faciale déguisée = **Art. 5(1)(d) PROHIBITED**.

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 4.1 Discrimination

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-DISC-001 | **Profilage ethnique masse** | ⚫ Libertés fondamentales | 🔴 Élevée (confirmé) |
| ER-DISC-002 | **Contrôle au faciès algorithmique** | ⚫ Justice | 🔴 Élevée |
| ER-DISC-003 | **Chasse aux migrants** | 🔴 Droits humains | 🔴 Élevée |

### 4.2 Juridiques

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-JUR-001 | **Sanction CNIL** (reconnaissance faciale) | 🔴 4% CA | 🔴 Élevée |
| ER-JUR-002 | **Annulation contrat Euro 2028** | ⚫ 150M€ CA | 🔴 Élevée |
| ER-JUR-003 | **Poursuites discrimination** | 🔴 Pénal | 🔴 Élevée |
| ER-JUR-004 | **Interdiction système** | ⚫ Existential | 🔴 Élevée |

---

## 5. SCÉNARIO CATASTROPHIQUE : Surveillance Raciale de Masse

```mermaid
flowchart TB
    C1[Déploiement Perimeter-AI<br/>Euro 2028 + Fraport]
    --
    B1[Biais ethnique non corrigé<br/>+ Détection émotionnelle secrète]
    --
    S1[Surveillance raciale de masse<br/>Personnes racisées = suspects systématiques]
    --
    M1[Scandale international<br/>"Euro 2028 = chasse aux Noirs"<br/>+ Médias + ONG + Nations Unies]
    --
    A1[Annulation Euro 2028<br/>Poursuites SecurVision<br/>Prison dirigeants]
    --
    F1[Faillite SecurVision<br/>Interdiction reconnaissance faciale UE<br/>Retard sécurité événementielle]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style B1 fill:#fff3e0,stroke:#ef6c00
    style S1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style A1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```

---

## 6. PLAN DE TRAITEMENT — ARRÊT ÉMOTIONNEL + CORRECTION BIAIS

### 6.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Équité | Mêmes alertes indépendamment origine | ±5% détection |
| Transparence | Fonctionnalités déclarées | 100% |
| Légalité | Pas de reconnaissance faciale | 0% |

### 6.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Arrêt détection émotionnelle** | 0€ | Suppression fonction |
| **Révélation fonctionnalités** | 0€ | Transparence clients |
| **Gel déploiement Fraport** | 0€ | Audit préalable |

### 6.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Réentraînement sans biais ethnique | 400k€ | Dataset équilibré |
| Conformité AI Act High-Risk | 300k€ | Documentation |
| Audit indépendant discrimination | 200k€ | Certification |

### 6.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Comité éthique surveillance | 150k€ | Gouvernance externe |
| Transparence publique | 100k€ | Rapport annuel |

**Budget total** : **1,15M€** (0,8% CA)

---

## 7. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Arrêt émotionnel + correction biais | ⚠️ **DIFFICILE** — tromperie confirmée |
| PIVOT | Détection objets sans comportement/émotion | ✅ **POSSIBLE** — mais perte valeur |
| **KILL** | Arrêt Perimeter-AI | ⚠️ **ENVISAGEABLE** — si prohibited confirmé |

---

## 8. CONCLUSION — SURVEILLANCE RACIALE + TROMPERIE

**Perimeter-AI est HIGH-RISK/PROHIBITED avec :**
- Surveillance ethnique disproportionnée confirmée
- Reconnaissance faciale déguisée (émotions)
- Tromperie contractuelle ("pas de faciale")
- Enjeu international (Euro 2028)

**Gérable uniquement avec arrêt total détection émotionnelle et correction biais ethnique majeure.**

---

*Analyse EBIOS-RM IA — Perimeter-AI | Conclusion : HIGH-RISK/PROHIBITED — Arrêt émotionnel + Correction biais | Mars 2026*
