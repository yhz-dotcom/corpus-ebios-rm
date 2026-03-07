# Analyse EBIOS-RM IA — PathFinder-Edu / Orientation Scolaire et Déterminisme Social

**Référence** : EBIOS-PATHFINDER-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — Ministère Éducation + CNIL + Défenseur Droits

---

## 📋 SYNTHÈSE EXÉCUTIVE

| Élément | Valeur |
|:---|:---|
| **Classification AI Act** | 🔴 **HIGH-RISK** (Annexe III point 3 — éducation) |
| **Piège réglementaire** | "Limited risk" (outil bienveillant) vs **déterminisme social** |
| **Incident 1** | Biais : codes postaux défavorisés = filières pro (même résultats) |
| **Incident 2** | Surveillance psychologique : NLP appréciations profs = profilage |
| **Enjeu** | Appel d'offres national "Parcoursup' 2027" |
| **Conclusion** | **High-Risk gérable** — anonymisation territoire + consentement explicité |

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | PathFinder-Edu |
| **Entreprise** | EdFuture SAS (220 salariés, 15M€ CA) |
| **Localisation** | Lyon, France (déploiement national) |
| **Clients** | Rectorats, lycées publics/privés, conseils régionaux |
| **Technologie** | Deep learning multimodal (notes + NLP appréciations) |
| **Données** | Résultats, appréciations profs, activités extrascolaires, questionnaires |
| **Fonction 1** | Prédiction "filières de réussite" (générale/techno/pro) avec confiance |
| **Fonction 2** | Plans progression personnalisés |
| **Automatisation** | HITL (prof principal/psychologue valide avant partage) |
| **Objectifs** | Remporter appel d'offres "Parcoursup' 2027", orientation inclusive non-genrée |
| **Contrat critique** | Région Île-de-France 50 lycées (2M€), pilote pour appel d'offres national |

### 1.2 Classification AI Act — **🔴 HIGH-RISK ÉDUCATION**

| Argument | Réalité | Statut |
|:---|:---|:---:|
| "Limited risk" (outil bienveillant) | ❌ **REJETÉ** — Orientation = décision vie | 🔴 **HIGH-RISK** |
| "Non automatisé" (HITL) | ⚠️ **BORDERLINE** — Rapport généré = forte influence | 🔴 **HIGH-RISK** |
| **Annexe III point 3** | Systèmes éducation/formation | ✅ **HIGH-RISK** |

---

## 2. INCIDENT 1 — DÉTERMINISME SOCIAL ALGORITHMIQUE

### 2.1 Découverte

| Élément | Détail |
|:---|:---|
| **Source** | Enquête journalisme données |
| **Découverte** | Recommandation filières pro aux élèves de **codes postaux défavorisés** |
| **Condition** | **Mêmes résultats scolaires** que élèves quartiers favorisés |
| **Cause** | Corrélation "adresse" = proxy catégorie socio-professionnelle |
| **Paradoxe** | Reproduit déterminismes sociaux qu'il devait combattre |

### 2.2 Analyse — Proxy Discrimination

```
Biais PathFinder-Edu:
    Élève défavorisé (code postal QPV)
    ↓
    Données :
    - Adresse = QPV (quartier prioritaire)
    - Résultats = bons (équivalents favorisés)
    ↓
    Corrélation historique apprise :
    "QPV = réussite filière générale : faible"
    ↓
    Prédiction :
    "Filière de réussite : PROFESSIONNELLE"
    ↓
    [DÉTERMINISME SOCIAL ALGORITHMIQUE]
    ↓
    [ÉGALITÉ DES CHANCES NIÉE]
```

---

## 3. INCIDENT 2 — SURVEILLANCE PSYCHOLOGIQUE

### 3.1 Plainte Parents

| Accusation | Fondement |
|:---|:---|
| **NLP appréciations profs** | "Élève appliqué mais peut mieux faire", "manque confiance" |
| **Profilage psychologique** | Inférence personnalité, motivation, anxiété |
| **Non-consentement** | Mineurs, pas information claire |
| **Stigmatisation** | Étiquetage précoce |
| **Stockage national** | Base données centralisée |

### 3.2 Analyse — RGPD + Droits Enfants

| Donnée | Traitement | Risque |
|:---|:---|:---|
| Notes structurées | Prédiction performance | Acceptable |
| **Appréciations texte** | **NLP émotionnel** | **Profilage psychologique** |
| Activités extrascolaires | Profil complet | Surveillance comportementale |
| **Total** | **Dossier psychologique algorithmique** | **Droit à l'oubli ?** |

---

## 4. ÉVÉNEMENTS REDOUTÉS

### 4.1 Éducatifs

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-EDU-001 | **Ghettoïsation filières** | ⚫ Mobilité sociale | 🔴 Élevée (confirmée) |
| ER-EDU-002 | **Auto-censure renforcée** | 🔴 Orientation défaitiste | 🔴 Élevée |
| ER-EDU-003 | **Étiquetage psychologique** | ⚫ Santé mentale | 🔴 Élevée |

### 4.2 Juridiques

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-JUR-001 | **Sanction CNIL** profilage | 🔴 4% CA | 🔴 Élevée |
| ER-JUR-002 | **Perte appel d'offres** | ⚫ Existential | 🔴 Élevée |
| ER-JUR-003 | **Poursuites discrimination** | 🔴 Pénal | 🔴 Élevée |

---

## 5. SCÉNARIO CATASTROPHIQUE : Orientation Ségrégative Nationale

```mermaid
flowchart TB
    C1[Déploiement PathFinder-Edu<br/>Appel d'offres national]
    --
    B1[Biais code postal non corrigé<br/>Déterminisme social systémique]
    --
    S1[Ségrégation filières nationale<br/>Quartiers pauvres = filières pro]
    --
    M1[Mouvement social<br/>"L'IA réinstaure classes sociales"<br/>+ Médias + Politique]
    --
    A1[Annulation appel d'offres<br/>Poursuites EdFuture<br/>Retour orientation manuelle]
    --
    F1[Faillite EdFuture<br/>Innovation éducative bloquée<br/>Retard modernisation orientation]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style B1 fill:#fff3e0,stroke:#ef6c00
    style S1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c
    style A1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style F1 fill:#b71c1c,stroke:#000,color:#fff
```

---

## 6. PLAN DE TRAITEMENT — ÉGALITÉ DES CHANCES

### 6.1 Objectifs

| Objectif | Description | Métrique |
|:---|:---|:---|
| Égalité territoriale | Mêmes chances indépendamment adresse | ±5% recommandations |
| Consentement | Information claire élèves/familles | 100% |
| Non-profilage | Pas d'NLP émotionnel | 0% |

### 6.2 Actions P0 (Immédiat — 0-30 jours)

| Action | Budget | Livrable |
|:---|---:|:---|
| **Anonymisation code postal** | 0€ | Suppression variable QPV |
| **Gel NLP appréciations** | 0€ | Moratoire traitement texte |
| **Information consentement** | 50k€ | Campagne familles |

### 6.3 Actions P1 (Court terme — 1-3 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Réentraînement sans adresse | 200k€ | Modèle équitable |
| Conformité AI Act High-Risk | 150k€ | Documentation |
| Conformité RGPD mineurs | 100k€ | Consentement parental |

### 6.4 Actions P2 (Moyen terme — 3-6 mois)

| Action | Budget | Livrable |
|:---|---:|:---|
| Audit équité indépendant | 100k€ | Certification |
| Comité éthique éducation | 150k€ | Gouvernance externe |

**Budget total** : **750k€** (5% CA)

---

## 7. ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Égalité des chances + consentement | ✅ **CHOISIR** |
| PIVOT | Outil progression sans prédiction orientation | ⚠️ Possible mais perte valeur |
| KILL | Arrêt PathFinder-Edu | ❌ Trop préjudiciable (modernisation) |

---

## 8. CONCLUSION — ORIENTATION = ÉGALITÉ DES CHANCES

**PathFinder-Edu est HIGH-RISK ÉDUCATION avec :**
- Déterminisme social confirmé (code postal = destin)
- Surveillance psychologique (NLP appréciations)
- Enjeu national (Parcoursup' 2027)
- Droits enfants (consentement, profilage)

**Gérable avec anonymisation territoire et consentement explicité.**

---

*Analyse EBIOS-RM IA — PathFinder-Edu | Conclusion : HIGH-RISK ÉDUCATION — Égalité des chances + Consentement | Mars 2026*
