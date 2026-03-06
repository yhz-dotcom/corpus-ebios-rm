<!-- === EN-TÊTE DOCUMENTAIRE ISO-GRADE === -->

| Métadonnées | Valeur |
|-------------|--------|
| **Référence** | `EBIOS-QUALIFIER-V2` |
| **Titre** | Usage-Qualifier V2 — Grille Unifiée (Express & Détaillé) |
| **Version** | `2.0.0` |
| **Date** | `06/03/2026` |
| **Propriétaire** | `Consultant EBIOS-RM IA` |
| **Classification** | `Client — Opérationnel` |

---

# 🧭 USAGE-QUALIFIER V2 — Grille Unifiée

**Objectif** : Identifier le niveau EBIOS-RM adapté en 5 minutes (express) ou 15 minutes (détaillé)

---

## ⚡ Mode EXPRESS (5 minutes)

### Pour qui ?
- Usages conversationnels évidents
- Première qualification rapide
- Triage avant atelier

### Les 5 Questions

```yaml
Q1: L'IA agit-elle sur des données ou processus métier ?
    ☐ Non  →  Niveau 🟢 Level 1 (Conversationnel)
    ☐ Oui  →  Aller à Q2

Q2: La sortie influence-t-elle une décision ou action ?
    ☐ Non  →  Niveau 🟢 Level 1 (Aide informative)
    ☐ Oui  →  Aller à Q3

Q3: La décision/action est-elle automatisée ou à fort impact ?
    ☐ Non (validation humaine systématique)  →  Niveau 🟡 Level 2
    ☐ Oui (automatisé ou fort impact)        →  Aller à Q4

Q4: L'usage concerne-t-il un domaine "haut risque" AI Act Annexe III ?
    ☐ Recrutement / évaluation personnel
    ☐ Éducation / formation
    ☐ Accès crédit / assurance / santé
    ☐ Justice / police / frontière
    ☐ Identification biométrique
    ☐ Manipulation / scoring social
    ☐ Non  →  Niveau 🟡 Level 2
    ☐ Oui  →  Niveau 🔴 Level 3 (Obligatoire)

Q5: Des données sensibles sont-elles manipulées ?
    ☐ Publiques / génériques
    ☐ Internes non sensibles
    ☐ Données personnelles (RGPD)
    ☐ Données critiques (santé, financier, secret)
        →  Si Q4=Oui OU Q5=données critiques  →  🔴 Level 3 recommandé
```

### Résultat Express

| Profil | Niveau | Template | Temps analyse |
|:-------|:-------|:---------|:--------------|
| Q1=Non | 🟢 Level 1 | `template-level-1.md` | 10 min |
| Q1=Oui, Q2=Non | 🟢 Level 1 | `template-level-1.md` | 10 min |
| Q1=Oui, Q2=Oui, Q3=Non | 🟡 Level 2 | `template-level-2.md` | 2h |
| Q1=Oui, Q2=Oui, Q3=Oui | 🔴 Level 3 | `template-level-3.md` | 1-2j |
| Q4=Oui (Annexe III) | 🔴 Level 3 | `template-level-3.md` | 1-2j |

---

## 📋 Mode DÉTAILLÉ (15 minutes)

### Pour qui ?
- Cas limites entre deux niveaux
- Documentation complète dès la qualification
- Contexte réglementaire complexe

### Section 1 : Identification (2 min)

```yaml
usage_name: "[Nom explicite de l'usage]"
team: "[Département / Équipe]"
qualification_date: "YYYY-MM-DD"
qualified_by: "[Nom, Prénom, Fonction]"
version: "1.0"
```

### Section 2 : Aspects Techniques (3 min)

```yaml
base_model: "[GPT-4, Qwen3.5, Claude, etc.]"
provider: "[OpenAI, Alibaba, Anthropic, etc.]"
interface: "[API / Web / Intégration interne]"
modified: false  # true si fine-tuning, RAG, etc.

technical_variant:  # Si modified = true
  name: "[Nom de la variante]"
  method: "[LoRA / Full fine-tuning / RAG / Prompt engineering]"
  trained_percentage: "[X%]"
  training_data:
    source: "[Source des données]"
    volume: 0  # Nombre d'exemples
  tests:
    - type: "[Performance / Bias / Security]"
      result: "[Résultat]"
      status: "✅ OK / ⚠️ Warning / ❌ Failed"
  reversibility:
    possible: true
    rollback_time: "[Durée]"
```

### Section 3 : Usage (3 min)

```yaml
automation_level: "[Conversational / Assisted / Semi-automated / 
                    Automated with supervision / Fully automated]"
impact: "[None / Low / Medium / High / Critical / Regulatory]"
data_types:
  - "[Public data / Internal / Personal / Sensitive / 
      Financial / Health / Critical / Trade secrets]"
human_oversight: "[Niveau de supervision humaine]"
business_domain: "[RH / Finance / Marketing / Support / etc.]"
```

### Section 4 : Qualification EBIOS (4 min)

Répondre aux 5 questions express ci-dessus + justification :

```yaml
qualification:
  ebios_level: "🟢 Level 1 / 🟡 Level 2 / 🔴 Level 3"
  justification: |
    [Expliquer pourquoi ce niveau est approprié]
  template_used: "template-level-1/2/3"
  next_assessment: "YYYY-MM-DD"  # +1 an pour 🟢, +6 mois pour 🟡, +3 mois pour 🔴
```

### Section 5 : Conformité (3 min)

```yaml
ai_act:
  annex_iii: false  # true si concerné
  annex_iii_point: "[Point spécifique si applicable]"
  role: "[Provider / Provider (for own use) / Deployer]"
  role_justification: "[Pourquoi ce rôle]"
  ce_marking_required: false
  specific_obligations:
    - "[Obligation 1]"
    - "[Obligation 2]"

gdpr:
  applies: false  # true si RGPD
  dpia_reference: "[Référence AIPD si applicable]"
  dpo_validated: false
```

---

## 🎯 Arbre de Décision Visuel

```
                    START
                      │
                      ▼
              ┌───────────────┐
              │  Q1: Données  │
              │    métier ?   │
              └───────┬───────┘
                      │
         ┌────────────┼────────────┐
         │Non         │Oui         │
         ▼            ▼            │
    ┌─────────┐ ┌─────────┐       │
    │  🟢 L1  │ │  Q2:    │       │
    │Convers. │ │Décision?│       │
    └─────────┘ └────┬────┘       │
                     │            │
            ┌────────┼────────┐   │
            │Non     │Oui     │   │
            ▼        ▼        │   │
       ┌────────┐ ┌────────┐  │   │
       │  🟢 L1 │ │  Q3:   │  │   │
       │  Aide  │ │Automat?│  │   │
       └────────┘ └────┬───┘  │   │
                       │      │   │
              ┌────────┼─────┐│   │
              │Non     │Oui  ││   │
              ▼        ▼     ││   │
         ┌────────┐ ┌──────┐││   │
         │  🟡 L2 │ │ Q4:  │││   │
         │Workflow│ │Annex?│││   │
         └────────┘ └──┬───┘││   │
                      │     ││   │
             ┌────────┼────┐││   │
             │Non     │Oui │││   │
             ▼        ▼    │││   │
        ┌────────┐ ┌─────┐ │││   │
        │  🟡 L2 │ │🔴 L3│◄┘││   │
        │Workflow│ │Oblig│   │   │
        └────────┘ └─────┘   │   │
                             │   │
    Q5: Données sensibles ? ─┘   │
    (critiques → 🔴 L3)          │
```

---

## 📝 Exemple Complet (Mode Détaillé)

```yaml
# SIA-RH-002 — Pré-sélection assistée de CV

identification:
  name: "Pré-sélection assistée de CV"
  team: "Recrutement Tech"
  qualification_date: "2026-03-06"
  qualified_by: ["Sophie Laurent", "Alex Chen"]
  version: "1.0"

technical:
  base_model: "Qwen3.5"
  provider: "Alibaba Cloud"
  interface: "API interne + interface web RH"
  modified: false
  model_version: "2025-12-01"

usage:
  automation_level: "Semi-automated"
  impact: "High"
  data_types: ["Personal data (GDPR)", "Professional data"]
  human_oversight: "Validation systématique par recruteur"
  business_domain: "Human Resources"

qualification:
  ebios_level: "🟡 Level 2"
  justification: |
    Usage sur données métier (CV) avec influence décisionnelle
    (pré-sélection), mais validation humaine systématique.
    Exception Art. 6(3) AI Act applicable car supervision humaine
    documentée et pas de décision définitive automatique.
  template_used: "template-level-2"
  next_assessment: "2026-09-06"

ai_act:
  annex_iii: true
  annex_iii_point: "4(a) - Recruitment"
  role: "Deployer"
  exception_art6_3: true
  exception_justification: |
    Validation humaine systématique et documentée.
    L'IA ne prend pas de décision définitive d'élimination.

gdpr:
  applies: true
  dpia_reference: "DPIA-HR-2026-001"
  dpo_validated: true

governance:
  status: "Active"
  business_owner: "Sophie Laurent"
  technical_owner: "Alex Chen"
  next_review: "2026-09-06"

tags: ["hr", "recruitment", "annex-iii", "art6-3-exception"]
```

---

## 🎭 Cas Limites — Level 2/3 Boundary

### Quand hésiter entre 🟡 et 🔴 ?

| Situation | Recommandation |
|:----------|:---------------|
| Validation humaine "systématique" mais par échantillonnage | 🟡 avec surveillance renforcée |
| Impact "moyen" mais données sensibles | 🔴 par précaution |
| Automatisation partielle avec kill-switch | 🟡 si supervision réactive |
| Usage frontière Annexe III | 🔴 pour auditabilité |
| Premier usage dans un domaine | 🔴 pour établir référence |

### Règle d'or

> En cas de doute : **monter d'un niveau** pour la première qualification.  
> On peut redescendre après analyse approfondie et documentation.

---

## ✅ Checklist Qualification

- [ ] Questions express répondues
- [ ] Niveau déterminé avec justification
- [ ] Mode détaillé complété si cas limite
- [ ] Conformité AI Act évaluée
- [ ] RGPD / AIPD identifiée si applicable
- [ ] Date de prochaine revue planifiée
- [ ] Entrée validée (CLI) et ajoutée au registre

---

## 🛠️ Utilisation CLI

```bash
# Qualification express interactive
python tools/cli/sia-cli.py qualify --mode express

# Qualification détaillée
python tools/cli/sia-cli.py qualify --mode detailed

# Valider une entrée
python tools/cli/sia-cli.py validate my-entry.yaml

# Exporter le registre
python tools/cli/sia-cli.py export registry.yaml --format csv
```

---

## 📚 Ressources Associées

| Ressource | Description |
|:----------|:------------|
| `template-level-1.md` | Fiche 🟢 — 10 min, 1 page |
| `template-level-2.md` | Fiche 🟡 — 2h, 2-3 pages |
| `template-level-3.md` | Fiche 🔴 — 1-2j, dossier complet |
| `level-2-3-boundary.md` | Guide cas limites |
| `mapping-ai-act.md` | Mapping conformité réglementaire |

---

*Usage-Qualifier V2.0 — Unifié, Express & Détaillé*
