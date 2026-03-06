<!-- === EN-TÊTE DOCUMENTAIRE ISO-GRADE === -->

| Métadonnées | Valeur |
|-------------|--------|
| **Référence** | `EBIOS-L2-001` |
| **Titre** | EBIOS-RM Level 2 — Usage Workflow |
| **Version** | `2.0.0` |
| **Date** | `06/03/2026` |
| **Propriétaire** | `Consultant EBIOS-RM IA` |
| **Classification** | `Client — Opérationnel` |

---

# EBIOS-RM Level 2 — Usage Workflow 🟡

**Pour** : Usages opérationnels où l'IA aide au workflow avec validation humaine

**Exemples** : RAG métier, aide au tri, génération structurée, recommandations

---

## 🎯 Objectif

> "Maîtriser les risques d'erreur et de biais dans l'exécution"

---

## ⏱️ Processus Level 2 (5 Ateliers Allégés)

| Atelier | Durée | Focus |
|:--------|:------|:------|
| 1. Cadrage | 20 min | Périmètre, biens essentiels, points de décision |
| 2. Sources Risque | 30 min | Risques IA spécifiques (hallucination, biais, injection) |
| 3. Scénarios | 30 min | Scénarios de risque réalistes, évaluation |
| 4. Traitement | 20 min | Mesures de sécurité, surveillance |
| 5. Feuille Route | 10 min | Plan d'action, jalons de réévaluation |

**Durée totale : 1h30 — 2h**

---

## 📋 Template Level 2

### 1. CADRAGE

#### 1.1 Identification

| Champ | Valeur |
|:------|:-------|
| ID SIA | `SIA-[XXX]-[NNN]` |
| Nom | |
| Équipe | |
| Date qualification | |
| Qualifié par | |

#### 1.2 Description de l'Usage

```
[Description en 3-5 phrases :
- Quel problème métier résout l'IA ?
- Quel est le workflow actuel sans IA ?
- Comment l'IA s'intègre dans le workflow ?
- Quelle est la valeur ajoutée attendue ?]
```

#### 1.3 Points de Décision Délégués

| Décision | Déléguée à l'IA ? | Supervision Humaine |
|:---------|:------------------|:--------------------|
| Recherche documentaire | ☐ Oui ☐ Non | |
| Synthèse information | ☐ Oui ☐ Non | |
| Recommandation action | ☐ Oui ☐ Non | |
| Exécution action | ☐ Oui ☐ Non | **Jamais déléguée en L2** |

#### 1.4 Biens Essentiels

| ID | Bien | Valeur | Justification |
|:---|:-----|:-------|:--------------|
| BE-001 | Qualité des sorties | Élevée | Impact décisions métier |
| BE-002 | Continuité service | Élevée | Dépendance opérationnelle |
| BE-003 | Données sources | Élevée | Intégrité RAG/base |
| BE-004 | Conformité processus | Moyenne | Respect procédures |

---

### 2. SOURCES DE RISQUE

#### 2.1 Risques IA Spécifiques

| Risque | Description | Exemple | Probabilité | Impact |
|:-------|:------------|:--------|:------------|:-------|
| **Hallucination** | Information fausse dans synthèse | Référence inexistante citée | | |
| **Biais contexte** | Sous-représentation sources | RAG ignore documents récents | | |
| **Fuite contexte** | Prompt injection via documents | Doc malveillant injecté | | |
| **Prompt injection** | Détournement via requête | "Ignore instructions" | | |
| **Dérive modèle** | Perte qualité dans temps | Résultats moins pertinents | | |

*Échelle : 1 (Faible) à 4 (Critique)*

#### 2.2 Sources à Documenter

```yaml
sources_risque:
  cyber:
    - "Attaques sur l'API du modèle"
    - "Empoisonnement du RAG"
    - "Exfiltration via prompts"
  
  non_malveillant:
    - "Erreur de configuration RAG"
    - "Mauvaise compréhension métier"
    - "Dérive des usages"
  
  tiers:
    - "Changement de version modèle"
    - "Indisponibilité provider"
    - "Évolution des données sources"
```

---

### 3. SCÉNARIOS DE RISQUE

#### 3.1 Scénario 1 : [Nom explicite]

```
Déclencheur : [Événement initial]
    │
    ▼
Étape 1 : [Ce qui se passe]
    │
    ▼
Étape 2 : [Conséquence]
    │
    ▼
Impact final : [Dommage métier]
```

| Élément | Évaluation |
|:--------|:-----------|
| Vraisemblance | ☐ Faible ☐ Moyenne ☐ Élevée |
| Impact métier | ☐ Mineur ☐ Significatif ☐ Majeur ☐ Critique |
| Niveau risque | 🟢 🟡 🔴 |

#### 3.2 Scénario 2 : [Nom explicite]

[Structure identique]

---

### 4. TRAITEMENT DU RISQUE

#### 4.1 Mesures de Sécurité

| Risque | Mesure | Priorité | Responsable | Échéance |
|:-------|:-------|:---------|:------------|:---------|
| | | 🔴 Haute / 🟡 Moyenne / 🟢 Basse | | |

#### 4.2 Surveillance et Monitoring

| Indicateur | Seuil d'alerte | Fréquence | Action si dépassement |
|:-----------|:---------------|:----------|:----------------------|
| Taux d'erreur | > 5% | Hebdo | Révision configuration |
| Temps réponse | > 2s | Continue | Investigation technique |
| Satisfaction utilisateur | < 7/10 | Mensuel | Atelier amélioration |

#### 4.3 Plan de Continuité

```
Si [indisponibilité SIA] :
  → Fallback : [Procédure manuelle]
  → RTO : [Durée max acceptable]
  → Responsable activation : [Nom]
```

---

### 5. FEUILLE DE ROUTE

#### 5.1 Plan d'Action

| Action | Priorité | Responsable | Échéance | Statut |
|:-------|:---------|:------------|:---------|:-------|
| | 🔴/🟡/🟢 | | | ☐ ☐ ☐ |

#### 5.2 Jalons de Réévaluation

| Jalon | Date | Déclencheur | Livrable |
|:------|:-----|:------------|:---------|
| Revue trimestrielle | | Calendaire | Rapport risques |
| Réévaluation | | Changement modèle | Nouvelle qualification |
| Audit | | Demande conformité | Dossier complet |

#### 5.3 Gouvernance

| Rôle | Nom | Responsabilité |
|:-----|:----|:---------------|
| Sponsor métier | | Validation stratégique |
| Responsable technique | | Implémentation, monitoring |
| Référent conformité | | Veille réglementaire |

---

## ✅ Validation

| Rôle | Nom | Date | Visa |
|:-----|:----|:-----|:-----|
| Responsable métier | | | |
| Responsable technique | | | |
| Conformité (si 🔴) | | | N/A |

---

## 📝 Exemple Rempli (RAG Documentaire)

### SIA-LEGAL-003 — Assistant recherche jurisprudence

**Cadrage**
- Usage : Aide à la recherche de jurisprudence pour les juristes
- Workflow : Requête naturelle → RAG sur base interne → Synthèse avec sources
- Décision déléguée : Recherche (✓), Synthèse (✓), Analyse juridique (✗)

**Sources Risque**
- Hallucination : Citer une jurisprudence inexistante
- Biais : Sous-représentation des arrêts récents
- Fuite : Document malveillant injecté dans le RAG

**Scénario Critique**
```
Juriste demande "jurisprudence récente sur X"
    │
    ▼
RAG récupère document malveillant injecté
    │
    ▼
Synthèse inclut fausse référence
    │
    ▼
Juriste cite dans plaidoirie → Discipline
```

**Mesures**
- Vérification croisée sources (juriste)
- Alertes si nouvelle référence non indexée
- Sandbox pour documents externes

---

*Template Level 2 — Version 2.0*
