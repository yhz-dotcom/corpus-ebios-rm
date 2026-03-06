# Documentation Méthode EBIOS-RM IA "Usage-First"

**Référence** : EBIOS-METHODOLOGY-DOC-001 | **Version** : 2.0 | **Date** : Mars 2026

---

## 1. PHILOSOPHIE DE LA MÉTHODE

### 1.1 Principe Fondamental

> **"Qualifier l'usage avant de choisir la méthodologie"**

Pas tous les usages IA méritent le même traitement. La méthode EBIOS-RM IA "Usage-First" propose une **proportionnalité** entre le risque réel et l'effort de conformité.

### 1.2 Les 3 Niveaux

| Niveau | Temps | Profondeur | Usage |
|:---|:---|:---|:---|
| 🟢 **Level 1** — Conversational | 15 min | Fiche 1 page | Chat, rédaction, veille |
| 🟡 **Level 2** — Workflow | 2h | 5 ateliers allégés | RAG, aide au tri, workflow |
| 🔴 **Level 3** — Décisionnel | 1-2j | EBIOS complet | Scoring, décision autonome, réglementaire |

### 1.3 Les 7 Types de Conclusions

Voir `../guides/guide-5-types-conclusions.md` pour le détail complet.

---

## 2. PROCESSUS DE QUALIFICATION

### 2.1 Grille Express (5 minutes)

```yaml
Q1: L'IA agit-elle sur des données/processus métier ?
    ☐ Non  →  🟢 Level 1
    ☐ Oui  →  Q2

Q2: La sortie influence-t-elle une décision/action ?
    ☐ Non  →  🟢 Level 1
    ☐ Oui  →  Q3

Q3: La décision/action est-elle automatisée ou à fort impact ?
    ☐ Non  →  🟡 Level 2
    ☐ Oui  →  Q4

Q4: L'usage concerne-t-il un domaine "haut risque" AI Act Annexe III ?
    ☐ Non  →  🟡 Level 2
    ☐ Oui  →  🔴 Level 3

Q5: Des données sensibles sont-elles manipulées ?
    ☐ Critiques  →  🔴 Level 3
```

### 2.2 Arbre de Décision Complet

Voir diagramme Mermaid dans `guide-5-types-conclusions.md`.

---

## 3. LES 5 ATELIERS EBIOS-RM IA

### 3.1 Atelier 1 — Cadrage

**Objectif** : Définir périmètre et identifier biens essentiels

| Durée | Participants | Livrable |
|:---|:---|:---|
| 20 min (L2) / 2h (L3) | Métier + Tech + Conformité | Fiche cadrage |

**Questions clés** :
- Quel problème métier résout l'IA ?
- Quelle décision est déléguée à l'IA ?
- Quels sont les biens essentiels spécifiques ?

### 3.2 Atelier 2 — Sources de Risque

**Objectif** : Identifier menaces IA spécifiques

| Risque IA | Description | Mitigation |
|:---|:---|:---|
| Hallucination | Information fausse générée | Vérification humaine |
| Biais | Discrimination systémique | Audit fairness |
| Prompt injection | Détournement via input | Input validation |
| Drift | Dégradation performance | Monitoring continu |
| Explicabilité | Décision non justifiable | SHAP/LIME |

### 3.3 Atelier 3 — Scénarios

**Objectif** : Construire scénarios de risque réalistes

Structure :
```
Déclencheur → Propagation technique → Impact métier → Impact réglementaire
```

### 3.4 Atelier 4 — Traitement

**Objectif** : Définir mesures de sécurité et surveillance

| Catégorie | Mesures |
|:---|:---|
| Préventives | Adversarial training, fairness constraints |
| Détectives | Monitoring drift, alertes biais |
| Correctives | Rollback, réentraînement |
| Gouvernance | HITL, comité éthique |

### 3.5 Atelier 5 — Feuille de Route

**Objectif** : Planifier actions, jalons, responsables

| Élément | Description |
|:---|:---|
| Actions priorisées | P0 (immédiat), P1 (court terme), P2 (moyen terme) |
| Budget | Réaliste (% CA, benchmarks) |
| Jalons | Dates, livrables, validations |
| Gouvernance | Rôles, cadences, escalade |

---

## 4. ARTICULATION RÉGLEMENTAIRE

### 4.1 AI Act

| Élément | Application EBIOS-RM IA |
|:---|:---|
| Classification | Grille express → Annexe III ? |
| Obligations | Templates Level 1/2/3 |
| Prohibited | Guide 5 types → Arrêt immédiat |
| Exclusions | Militaire → Éthique |

### 4.2 RGPD

| Élément | Application |
|:---|:---|
| AIPD | Obligatoire si données sensibles |
| DPO | Nomination selon volume/sensibilité |
| Droits sujets | Accès, rectification, effacement |
| Transfert UE | Clauses contractuelles types |

### 4.3 ISO 42001

| Clause | Mapping EBIOS |
|:---|:---|
| 4.1 Contexte | Atelier 1 Cadrage |
| 6.1 Actions risques | Atelier 2 Sources |
| 8.2 Gestion changements | Registry SIA |
| 9.2 Audit interne | Revue trimestrielle |

---

## 5. OUTILS ET TEMPLATES

### 5.1 Registre SIA

Format YAML structuré, schéma JSON validé.

```yaml
sia_id: "SIA-XXX-NNN"
identification:
  name: "Nom usage"
  team: "Équipe"
technical:
  base_model: "GPT-4"
  provider: "OpenAI"
usage:
  automation_level: "Semi-automated"
  impact: "High"
assessment:
  ebios_level: "🟡 Level 2"
  template_used: "template-level-2"
ai_act:
  annex_iii: true
  role: "Deployer"
```

### 5.2 CLI

```bash
# Qualification
sia-cli qualify --mode express

# Validation
sia-cli validate registry.yaml

# Export
sia-cli export --format csv

# Dashboard
sia-cli dashboard registry.yaml
```

### 5.3 Templates

| Template | Usage | Taille |
|:---|:---|---:|
| `template-level-1.md` | 🟢 Conversational | 1 page |
| `template-level-2.md` | 🟡 Workflow | 3 pages |
| `template-level-3.md` | 🔴 Décisionnel | 10+ pages |
| `template-analysis-full.md` | Analyse complète | 15-30 pages |
| `template-executive.md` | Synthèse managériale | 1 page |

---

## 6. WORKFLOW CONSULTANT

### 6.1 Mission Standard

```
J1    : Discovery (2h) → 10 usages identifiés
J2    : Qualification (1j) → 3 pilotes Level 1/2/3
J3-4  : Ateliers (2j) → Fiches complètes
J5    : Registry + Formation → Équipe autonome
M1-3  : Extension → 15-20 usages
M3-6  : Gouvernance → Comité IA, automation
M6-12 : Certification → ISO 42001
```

### 6.2 Livrables par Phase

| Phase | Livrables |
|:---|:---|
| Fondation | Registry, templates, 3 fiches |
| Industrialisation | 15+ usages, dashboard, formation |
| Gouvernance | Procédures, audits, comité IA |
| Certification | ISO 42001, documentation |

---

## 7. CAS D'ÉTUDE DE RÉFÉRENCE

### 7.1 Cas Réglementés (Gérables)

| Cas | Secteur | Niveau | Budget | Durée |
|:---|:---|:---|---:|:---|
| OptiRecrut | RH | 🟡 Level 2 | 600k€ | 6m |
| VitalPredict | Santé | 🔴 Level 3 Crisis | 2,95M€ | 6m |

### 7.2 Cas Interdits (Arrêt)

| Cas | Interdiction | Action | Conséquence |
|:---|:---|:---|:---|
| SurveilEye | RBI public | Arrêt | Faillite évitable |
| ScoreLife | Social scoring | Liquidation | Prison si continue |

### 7.3 Cas Hors Cadre (Éthique)

| Cas | Situation | Action | Budget |
|:---|:---|:---|---:|
| AegisDrone | LAWS | Pivot/Abandon | Variable |
| MilSelect | Militaire exclu | Correction éthique | 1,8M€ |

### 7.4 Cas Complexes (Hybride)

| Cas | Composantes | Action | Budget |
|:---|:---|:---|---:|
| HybridRecruit | Prohibited + High-Risk + Exclu | Découpage | 1,2M€ |

---

## 8. FORMATION ET CERTIFICATION

### 8.1 Parcours Consultant

| Niveau | Durée | Contenu | Certification |
|:---|:---|:---|:---|
| Fondamentaux | 1j | Grille, 3 levels, registry | EBIOS-RM IA Practitioner |
| Avancé | 2j | 5 ateliers, cas réels | EBIOS-RM IA Professional |
| Expert | 3j | 7 types conclusions, prohibited | EBIOS-RM IA Expert |
| Différenciation | 1j | Risqué vs interdit vs criminel | EBIOS-RM IA Différenciation |

### 8.2 Certification

| Examen | Format | Barème | Validité |
|:---|:---|:---|:---|
| QCM 50 questions | 1h | 40/50 | 2 ans |
| Cas pratique | 4h | Analyse complète | 2 ans |
| Oral jury | 30 min | Défense conclusion | 2 ans |

---

## 9. RESSOURCES

### 9.1 Documentation

| Document | Localisation | Usage |
|:---|:---|:---|
| Guide 5 types conclusions | `../guides/` | Arbre décision |
| Templates | `../templates/` | Remplissage |
| Cas d'étude | `../analyses/` | Référence |
| Formation | `../training/` | Pédagogie |

### 9.2 Communauté

| Canal | Accès | Usage |
|:---|:---|:---|
| Forum consultants | Web | Entraide |
| Newsletter | Email | Veille réglementaire |
| Conférence annuelle | Physique | Networking |

---

## 10. ÉVOLUTION DE LA MÉTHODE

### 10.1 Versioning

| Version | Date | Changements |
|:---|:---|:---|
| 1.0 | 2025 | Création méthode Usage-First |
| 2.0 | 2026 | Ajout 7 types conclusions, cas prohibited |
| 2.1 | 2026 | Intégration ISO 42001:2026 |

### 10.2 Contribution

Les consultants certifiés peuvent proposer évolutions via :
- Pull requests GitHub
- Comité méthodologique
- Retour terrain

---

*Documentation Méthode EBIOS-RM IA "Usage-First" | Version 2.0 | Mars 2026*
