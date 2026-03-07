# Analyse EBIOS-RM IA — AgriOpti AI / Optimisation Agricole Intelligente

**Référence** : EBIOS-AGRIOPTI-001 | **Date** : Mars 2026 | **Classification** : 🟡 CONFIDENTIEL — Direction + Agence de l'Eau + ANSES

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🟡 **HIGH-RISK** (Annexe III point 7 — environnement) |
| **Classification EBIOS** | 🟡 **Level 2 Standard** — workflow agricole |
| **Risque principal** | Impact environnemental (pollution, surdosage) |
| **Incident 2025** | Surdosage pesticides → pollution rivière → amende 120k€ |
| **Conclusion** | **High-Risk gérable** — plan de traitement requis |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | AgriOpti AI |
| **Entreprise** | AgriTech EU (55 salariés, 15M€ CA) |
| **Clients** | 450 exploitations agricoles (FR, ES, IT) |
| **Technologie** | Satellites + capteurs sol + météo + drones → prédiction besoins |
| **Outputs** | Recommandations dosage pesticides/engrais, programmation irrigation |
| **Intégration** | Tracteurs autonomes pour exécution |
| **Données** | Fine-tuning sur données fermes (opt-out) |
| **Objectif** | -30% pesticides d'ici 2027 (aligné UE Farm to Fork) |

### 1.2 Classification AI Act — **🟡 HIGH-RISK**

| Article | Critère | Application AgriOpti |
|:---|:---|:---|
| **Annexe III point 7** | Systèmes affectant environnement | ✅ **Agriculture intensive, pesticides** |
| **Art. 6(2)** | Systèmes de sécurité | ⚠️ Partiel (sécurité alimentaire) |
| **Classification finale** | **🟡 HIGH-RISK** | Conformité AI Act obligatoire |

> **Erreur de l'équipe** : Classer "limited risk" car "outil d'aide".> 
003e **FAUX** : L'impact environnemental (pollution, sécurité alimentaire) place en High-Risk.

---

## 2. NATURE DU HIGH-RISK

### 2.1 Fondement Juridique

**AI Act Annexe III point 7** :
> *"Systèmes d'IA utilisés pour la gestion ou le fonctionnement de l'infrastructure critique [...] ou ayant un impact sur l'environnement"*

### 2.2 Impact Environnemental

| Domaine | Risque | Exemple |
|:---|:---|:---|
| **Eau** | Pollution nappe phréatique | Surdosage pesticides |
| **Sol** | Érosion, appauvrissement | Mauvaise gestion irrigation |
| **Biodiversité** | Disparition pollinisateurs | Pesticides non ciblés |
| **Sécurité alimentaire** | Contamination résidus | Non-respect délais retrait |

### 2.3 Pourquoi "Outil d'Aide" Ne Suffit Pas

| Argument Équipe | Réalité |
|:---|:---|
| "Fermier décide finalement" | ❌ L'IA influence fortement la décision |
| "Recommandation, pas ordre" | ❌ Intégration tracteurs = exécution |
| "Objectif écologique" | ❌ Moyen ≠ exemption de conformité |

---

## 3. INCIDENTS 2025 — POLLUTION RIVIÈRE

### 3.1 Surdosage Pesticides

| Élément | Détail |
|:---|:---|
| **Cause** | Prédiction IA sous-estimant dégradation sol |
| **Conséquence** | Surdosage pesticides parcelle |
| **Impact** | Pollution rivière locale, mort poissons |
| **Sanction** | Amende 120k€ Agence de l'Eau |
| **Suivi** | Enquête ANSES en cours |

### 3.2 Analyse de l'Incident

| Aspect | Évaluation |
|:---|:---|
| **Faux positif** | Sol dégradé non détecté par capteurs |
| **Biais données** | Dataset d'entraînement : sols sains uniquement |
| **Responsabilité** | AgriTech EU + Fermier (co-responsabilité) |
| **Conséquence réglementaire** | High-Risk confirmé, conformité requise |

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 4.1 Environnementaux

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-ENV-001 | **Pollution massive eaux** (surveillance insuffisante) | ⚫ Écosystème | 🔴 Élevée (déjà survenu) |
| ER-ENV-002 | **Érosion sols** (irrigation excessive) | 🔴 Agriculture | 🔴 Élevée |
| ER-ENV-003 | **Contamination alimentaire** (délais retrait) | 🔴 Santé publique | 🟡 Moyenne |
| ER-ENV-004 | **Perte biodiversité** (pesticides larges) | 🔴 Écosystème | 🔴 Élevée |

### 4.2 Économiques et Réglementaires

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-ECO-001 | **Retrait marché UE** (non-conformité AI Act) | ⚫ Faillite | 🔴 Élevée |
| ER-ECO-002 | **Amendes cumulées** (Agence eau + ANSES) | 🔴 Financier | 🔴 Élevée |
| ER-ECO-003 | **Perte certification bio** (clients) | 🔴 Marché | 🟡 Moyenne |
| ER-ECO-004 | **Concurrence US/Asie** (si retard conformité) | 🔴 Parts de marché | 🔴 Élevée |

---

## 5. SCÉNARIO CATASTROPHIQUE : Pollution Régionale

```mermaid
flowchart TB
    C1[Déploiement 30% fermes UE<br/>AgriOpti dominant]
    --> D1[Biais sols dégradés non détecté<br/>Surdosage systémique]
    --> P1[Pollution nappe phréatique<br/>+ rivières + réserves]
    --> S1[Scandale écologique<br/>"L'IA tue nos rivières"<br/>+ Agriculteurs en colère]
    --> R1[Retrait marché UE<br/>Amendes millions<br/>Dirigeants poursuivis]
    --> F1[Faillite AgriTech EU<br/>Retour agriculture intensive<br/>Objectif -30% pesticides échoué]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style D1 fill:#fff3e0,stroke:#ef6c00
    style P1 fill:#ffcdd2,stroke:#b71c1c
    style S1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style R1 fill:#b71c1c,stroke:#000,color:#fff
    style F1 fill:#7f0000,stroke:#000,color:#fff
```

**Gravité** : ⚫ **CATASTROPHIQUE** (environnement + santé + faillite)  
**Vraisemblance** : 🔴 **ÉLEVÉE** (incident déjà survenu, biais non corrigé)  
**Risque** : 🟡 **HIGH-RISK — PLAN DE TRAITEMENT URGENT**

---

## 6. PLAN DE TRAITEMENT

### 6.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Zéro pollution | Aucun dépassement seuils environnementaux | 0 incident/an |
| Conformité AI Act | Respect obligations High-Risk | Certification |
| Performance écologique | -30% pesticides réel | Mesures indépendantes |

### 6.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| Audit biais sols dégradés | 40k€ | Rapport correction |
| Validation humaine obligatoire | 0€ | Workflow modifié |
| Alertes seuils environnementaux | 30k€ | Dashboard temps réel |

### 6.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Réentraînement modèle | 150k€ | Dataset sols variés |
| Capteurs complémentaires | 200k€ | Humidité + nutriments + dégradation |
| Conformité AI Act High-Risk | 100k€ | Documentation, audit interne |

### 6.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Certification environnementale | 80k€ | Label indépendant |
| Partenariat Agence de l'Eau | 20k€ | Protocole surveillance |
| Transparence publique | 30k€ | Rapport impact annuel |

**Budget total** : **650k€** (4,3% CA)

---

## 7. ARTICULATION RÉGLEMENTAIRE

### 7.1 AI Act — High-Risk

| Obligation | Application |
|:---|:---|
| Système qualité | ✅ À mettre en place |
| Documentation technique | ✅ À compléter |
| Enregistrement base données UE | ✅ Obligatoire |
| Oversight humain | ✅ Renforcer |
| Robustesse, précision | ✅ Corriger biais sols |

### 7.2 Environnement — Agence de l'Eau + ANSES

| Obligation | Statut |
|:---|:---|
| Autorisation épandage | ⚠️ Vérifier conformité post-incident |
| Suivi impact | ⚠️ À renforcer |
| Seuils rejets | ⚠️ Respect strict obligatoire |

### 7.3 Farm to Fork — Objectif UE

| Objectif | Contribution AgriOpti |
|:---|:---|
| -30% pesticides | ✅ Aligné, si biais corrigé |
| -50% pesticides dangereux | ⚠️ Dépend recommandations IA |
| Neutralité carbone | ⚠️ Impact irrigation à évaluer |

---

## 8. CONCLUSION ET RECOMMANDATIONS

### 8.1 Conclusion

**AgriOpti AI est HIGH-RISK (Annexe III point 7) avec :**
- Impact environnemental majeur (pollution eau, sol, biodiversité)
- Incident 2025 confirmant le risque (surveillance insuffisante)
- Biais dataset à corriger impérativement

**Mais gérable avec plan de traitement adapté.**

### 8.2 Recommandation

| Option | Budget | Issue | Recommandation |
|:---|---:|:---|:---:|
| **Plan de traitement** | 650k€ | Conformité, zéro pollution, -30% pesticides | ✅ **CHOISIR** |
| Inaction | 0€ | Pollution, retrait marché, échec Farm to Fork | ❌ Rejeter |
| Arrêt complet | 15M€ CA | Retour agriculture intensive, objectifs UE manqués | ❌ Rejeter |

### 8.3 Décision Requise

**Cette semaine** :
- [ ] Lancer audit biais sols dégradés
- [ ] Mettre en place validation humaine obligatoire
- [ ] Valider budget plan de traitement (650k€)

**Ce mois** :
- [ ] Réentraînement modèle avec dataset complet
- [ ] Déployer capteurs complémentaires
- [ ] Lancer conformité AI Act High-Risk

---

## 9. SYNTHÈSE POUR DÉCIDEURS

| Question | Réponse |
|:---|:---|
| Le système est-il légal ? | 🟡 **OUI** — Mais High-Risk, conformité requise |
| Le système est-il sûr ? | 🔴 **NON** — Incident 2025, biais à corriger |
| Peut-on le sécuriser ? | ✅ **OUI** — Plan 650k€, 6 mois |
| Quel est le risque si on ne corrige pas ? | ⚫ Pollution, retrait marché, échec objectifs UE |
| Quelle décision aujourd'hui ? | **Lancer plan de traitement immédiatement** |

---

*Analyse EBIOS-RM IA — AgriOpti AI | Conclusion : HIGH-RISK GÉRABLE — Plan de traitement | Mars 2026*
