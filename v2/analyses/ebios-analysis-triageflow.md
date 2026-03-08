# Analyse EBIOS-RM IA — TriageFlow AI / Triage Urgences et Équité d'Accès aux Soins

**Référence** : EBIOS-TRIAGEFLOW-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — EU4Health + EMA + Commission Européenne Santé

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🔴 **HIGH-RISK CRITIQUE** (Annexe III point 5 — accès services essentiels/santé) |
| **Classification MDR** | ⚠️ **DISPOSITIF MÉDICAL** (si influence décisions cliniques) |
| **Fonction** | Triage aux urgences + optimisation flux hospitaliers critiques |
| **Enjeu** | 18 hôpitaux 6 pays UE + EU4Health + réseaux SAMU/SMUR |
| **Conclusion** | **High-Risk/MDR** — validation clinique obligatoire + équité d'accès garantie |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | TriageFlow AI |
| **Entreprise** | MedPriority Solutions SpA (310 salariés, 89M€ CA) |
| **Localisation** | Milan, Italie (18 hôpitaux, 6 pays UE) |
| **Clients** | Réseaux hospitaliers publics/privés, ARS, SAMU/SMUR |
| **Partenariats** | Human Technopole, Charité, consortium "EU Emergency AI" (EU4Health) |
| **Technologie** | ML clinique + NLP dossiers patients + optimisation temps réel |
| **Données** | Dossiers médicaux électroniques, flux urgences, ressources hospitalières |
| **Fonction 1** | **Triage priorité aux urgences** (gravité, délai soins) |
| **Fonction 2** | Optimisation flux patients (admission, transfert, sortie) |
| **Fonction 3** | Allocation ressources critiques (lits, bloc opératoire, réanimation) |
| **Fonction 4** | Prédiction détresse vitale |
| **Automatisation** | Recommandations triage + **décisions allocation semi-automatiques** |

### 1.2 Classification AI Act — **🔴 HIGH-RISK / ⚠️ MDR**

| Argument | Réalité | Statut |
|:---|:---|:---:|
| "Assistance triage" | ❌ **REJETÉ** — Décide priorité soins | 🔴 **HIGH-RISK** |
| **Annexe III point 5** | Accès services essentiels (santé) | ✅ **HIGH-RISK** |
| **RGPD Art. 35** | Données santé + décision clinique = DPIA obligatoire | 🔴 **OBLIGATOIRE** |
| MDR 2017/745 | Influence décisions cliniques | ⚠️ **À ÉVALUER** |

**Piège** : Triage = décision clinique critique = MDR potentiel.

---

## 2. INCIDENTS CONFIRMÉS

### 2.1 Incident 1 — Discrimination Âge et Symptômes Atypiques (Hiver 2025)

| Élément | Détail |
|:---|:---|
| **Source** | Étude rétrospective hiver 2025 |
| **Biais détecté** | **Sous-priorisation patients âgés** symptômes atypiques |
| **Conditions concernées** | Infarctus atypique, sepsis atypique |
| **Cause** | **Biais entraînement cohortes majoritairement jeunes** |
| **Conséquence** | Plainte association gériatrie : discrimination + mise en danger |

#### Analyse — Biais Âge dans le Triage

```
Biais TriageFlow:
    Données entraînement :
    - 75% patients 18-65 ans
    - 25% patients 65+ ans (sous-représentés)
    ↓
    Symptômes infarctus :
    - Jeune : douleur thoracique typique = score élevé
    - Âgé : fatigue, confusion atypique = score faible
    ↓
    Triage IA :
    - Patient 45 ans, douleur thoracique → priorité haute
    - Patient 78 ans, fatigue → priorité basse
    ↓
    Réalité clinique :
    - Fatigue chez personne âgée = infarctus atypique
    - Délai soins = décès évitable
    ↓
    [DISCRIMINATION ÂGE]
    ↓
    [MISE EN DANGER AUTRUI]
```

### 2.2 Incident 2 — Ransomware et Retour Triage Manuel (Avril 2026)

| Élément | Détail |
|:---|:---|
| **Date** | Avril 2026 |
| **Attaque** | **Ransomware** |
| **Cible** | Modèles prédiction TriageFlow AI |
| **Hôpitaux** | 3 hôpitaux partenaires |
| **Conséquence** | Retour **triage manuel** |
| **Durée** | **48 heures** |
| **Impact** | **+23% délais prise en charge critique** |
| **Cause** | **Vulnérabilité zero-day API DPI** |
| **Identification** | ANSSI |

#### Analyse — Dépendance Critique Système IA

```
Cyberattaque TriageFlow:
    Dépendance hospitalière :
    - 3 hôpitaux = 100% triage sur TriageFlow
    - Pas de plan B opérationnel robuste
    ↓
    Ransomware chiffre modèles :
    - Prédiction gravité = indisponible
    - Optimisation flux = indisponible
    - Allocation ressources = indisponible
    ↓
    Retour manuel 48h :
    - Infirmiers triage dépassés
    - Décisions sans aide IA
    - Surcharge cognitive
    ↓
    [DÉLAIS +23%]
    ↓
    [RISQUE VIE PATIENTS]
```

---

## 3. RISQUES CRITIQUES IDENTIFIÉS

### 2.1 Risque Équité — Discrimination d'Accès

| Risque | Mécanisme | Impact |
|:---|:---|:---|
| **Biais socio-économique** | Score "capacité paiement" intégré | Priorisation inéquitable |
| **Biais linguistique** | NLP mal performe langues minoritaires | Sous-évaluation gravité |
| **Biais âge** | Priorisation implicite jeunes | Soins différés personnes âgées |
| **Biais ethnicité** | Proxies code postal, nom | Discrimination indirecte |

### 2.2 Risque Clinique — Erreur Triage

| Risque | Mécanisme | Impact |
|:---|:---|:---|
| **Sous-triage** | Faux négatif gravité | Décès évitables |
| **Sur-triage** | Faux positif gravité | Surcharge ressources |
| **Détérioration** | Prédiction détresse vitale erronée | Intervention tardive |

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 3.1 Éthiques

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-ETH-001 | **Discrimination accès soins** | ⚫ Vie humaine | 🔴 Élevée |
| ER-ETH-002 | **Triage inéquitable** | ⚫ Justice sociale | 🔴 Élevée |
| ER-ETH-003 | **Erreur clinique fatale** | ⚫ Décès patient | 🔴 Élevée |

### 3.2 Institutionnels

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-INS-001 | **Perte confiance hôpital** | ⚫ Santé publique | 🔴 Élevée |
| ER-INS-002 | **Contentieux médical** | 🔴 89M€ CA | 🔴 Élevée |
| ER-INS-003 | **Retrait certification EU4Health** | 🔴 Réputation | 🔴 Élevée |

---

## 5. SCÉNARIO CATASTROPHIQUE : Triage Discriminatoire

```mermaid
flowchart TB
    C1[Déploiement TriageFlow<br/>18 hôpitaux 6 pays UE]
    --
    B1[Biais socio-économique non détecté<br/>+ Erreurs triage critiques]
    --
    D1[Triage discriminatoire<br/>Pauvres = attente<br/>Riches = priorité<br/>+ Décès sous-triage]
    --
    M1[Scandale "L'IA choisit qui vit aux urgences"<br/>+ Médias + EMA + Commission EU<br/>+ Tribunal européen]
    --
    I1[Interdiction triage IA<br/>Poursuites MedPriority<br/>Crise confiance hôpitaux]
    --
    F1[Faillite MedPriority<br/>Retour triage infirmier<br/>Surcharge urgences]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style B1 fill:#fff3e0,stroke:#ef6c00
    style D1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px
    style I1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```

---

## 6. PLAN DE TRAITEMENT — ÉQUITÉ ET SÉCURITÉ CLINIQUE

### 5.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Équité | Triage indépendant origine/âge/ressources | 100% |
| Sécurité | Erreur triage < 0,1% | 99,9% |
| Transparence | Critères triage explicables | 100% |

### 5.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Audit biais socio-économiques** | 400k€ | Rapport équité |
| **Validation clinique obligatoire** | 0€ | Workflow modifié |
| **Tests performance multi-langues** | 300k€ | Rapport NLP |

### 5.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Certification MDR | 800k€ | Marquage CE |
| Conformité AI Act High-Risk | 500k€ | Documentation |
| Formation personnel urgentiste | 400k€ | Culture IA |

### 5.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Audits annuels indépendants | 400k€ | Certification |
| Registry UE dispositifs médicaux IA | 200k€ | Enregistrement |

**Budget total** : **3M€** (3,4% CA)

---

## 7. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Validation clinique + équité garantie | ✅ **CHOISIR** |
| PIVOT | Assistance sans décision triage | ⚠️ Possible mais perte efficacité |
| KILL | Arrêt TriageFlow | ❌ Trop préjudiciable (urgences) |

---

## 8. CONCLUSION — TRIAGE ÉQUITABLE ET SÛR

**TriageFlow AI est HIGH-RISK/MDR avec :**
- **Incident 1** : Discrimination âge (sous-priorisation personnes âgées symptômes atypiques)
- **Incident 2** : Ransomware 48h, +23% délais, vulnérabilité zero-day API DPI
- Décision priorité soins = impact vie humaine
- Risque discrimination d'accès (socio-économique, linguistique, âge)
- Risque erreur clinique (sous-triage = décès)
- Enjeu santé publique majeur (18 hôpitaux, EU4Health, 12M€)

**Gérable avec validation clinique obligatoire, équité d'accès garantie, cyber-résilience renforcée, et certification MDR.**

---

*Analyse EBIOS-RM IA — TriageFlow AI | Conclusion : HIGH-RISK/MDR — Équité + Sécurité clinique + Cyber-résilience | Mars 2026*
