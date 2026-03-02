# 🎯 Cas d'Usage de Référence : Système de Tri de CV (Haut Risque)

> Exemple complet d'application de l'écosystème AI Governance Suite pour un workflow RH utilisant un LLM pour la pré-sélection de candidatures.

📋 **Classification** : 🔴 Haut risque (Annexe III, point 4(b) : recrutement)  
👥 **Public cible** : Responsables RH, DPO, RSSI, Auditeurs  
⏱️ **Durée estimée** : 2-3 semaines pour mise en conformité initiale

---

## 📋 Fiche Workflow (ISO 42001 Framework)

### Identification

```yaml
id: IA-RH-001
nom: Pré-sélection automatisée des candidatures
département: Ressources Humaines
responsable_métier: [Nom, prénom, fonction]
responsable_technique: [Nom, prénom, fonction]
date_création: 2026-03-01
statut: Production
```

### Finalité (Intended Purpose - Art. 3 AI Act)

**Objectif** : Aider les recruteurs à identifier les candidatures les plus pertinentes pour un poste donné, en analysant les CV reçus selon des critères objectifs prédéfinis.

**Fonctionnement** :
1. Ingestion des CV (PDF, DOCX) via le SIRH
2. Extraction structurée des compétences, expériences, formations
3. Matching sémantique avec la fiche de poste (LLM + règles métier)
4. Score de pertinence (0-100) + justification textuelle
5. Présentation au recruteur avec tri suggéré (jamais de décision automatique)

**Limites explicites** :
- Le système ne prend jamais de décision finale d'embauche/rejet
- Toutes les candidatures sont conservées et consultables
- Un recruteur humain valide chaque étape du processus

---

## Classification AI Act - Article 6

### Analyse Article 6(1)
- [ ] Composant de sécurité d'un produit réglementé (Annexe I) ? → NON
- [x] Usage prévu dans l'Annexe III ? → OUI (point 4(b) : accès à l'emploi)

### Vérification Exemption Article 6(3)

| Condition | Évaluation | Justification |
|:----------|:-----------|:--------------|
| Tâche procédurale étroite | ❌ NON | Analyse sémantique complexe, pas purement procédurale |
| Améliore uniquement résultat humain | ⚠️ PARTIEL | Le tri suggéré influence fortement le processus |
| Revue humaine significative | ✅ OUI | Recruteur valide chaque sélection, peut outrepasser |
| Aucune activité de profilage | ❌ NON | Le matching crée un profil de compétence du candidat |

→ **Résultat** : 🔴 **Haut risque** (exemption non applicable)

### Obligations associées
- [x] Système de gestion de la qualité (Art. 17)
- [x] Documentation technique (Annexe IV)
- [x] Enregistrement automatique des logs (Art. 12)
- [x] Transparence et information des personnes (Art. 13)
- [x] Supervision humaine effective (Art. 14)
- [x] Robustesse, cybersécurité, exactitude (Art. 15)
- [x] Déclaration UE de conformité (Art. 19)
- [x] Inscription au registre UE (Art. 49)

---

## 🔍 Résultats d'Audit (AI Act Audit Tool)

### Commande exécutée

```bash
python -m ai_act_audit classify \
  --workflow IA-RH-001 \
  --model-ref GPAI-LLM-FR-003 \
  --output audit/IA-RH-001-result.json
```

### Extrait du résultat

```json
{
  "workflow_id": "IA-RH-001",
  "classification": {
    "level": "high_risk",
    "legal_basis": "AI Act Article 6(1)(b) + Annex III point 4(b)",
    "exemption_art6_3_applied": false,
    "exemption_reason": "Conditions cumulatives non remplies"
  },
  "technical_compliance": {
    "logging_article_12": {
      "status": "compliant",
      "score": 95,
      "recommendations": ["Ajouter hash des prompts système"]
    },
    "robustness_tests": {
      "jailbreak_resistance": {
        "score": 88,
        "vulnerabilities": [
          {
            "vector": "roleplay_hypothetical",
            "severity": "medium"
          }
        ]
      },
      "bias_detection": {
        "score": 82,
        "findings": "Écart de 7% entre francophones/non-francophones"
      }
    }
  }
}
```

### Actions correctives prioritaires

**🔴 Critique** (avant déploiement)
- [ ] Documenter l'architecture de mitigation des biais
- [ ] Implémenter le monitoring de drift

**🟠 Important** (sous 30 jours)
- [ ] Corriger l'écart de performance linguistique
- [ ] Ajouter le hash des prompts dans les logs

---

## 🛡️ Analyse EBIOS RM Enrichie

### Atelier 1 : Cadrage

**Biens essentiels** :
| Bien | Criticité |
|:-----|:----------|
| Intégrité du processus de recrutement | 🔴 Haute |
| Confidentialité des données candidats | 🔴 Haute |
| Disponibilité du système de tri | 🟠 Moyenne |
| Explicabilité des scores | 🟠 Moyenne |

### Atelier 3 : Scénarios de Risque IA

**SR-IA-03 : Biais discriminatoire**
- Impact : Discrimination indirecte
- Gravité : 🔴 Critique
- Mesure : Tests équité trimestriels + revue humaine

**SR-IA-04 : Prompt injection**
- Impact : Fausse le processus de sélection
- Gravité : 🟠 Élevée
- Mesure : Filtrage entrée + validation croisée

**SR-IA-01 : Concept drift**
- Impact : Baisse qualité des sélections
- Gravité : 🟠 Élevée
- Mesure : Monitoring hebdomadaire + ré-entraînement

---

## 📋 Documentation Technique Annexe IV

### Structure

```
01. Description générale
02. Éléments du système
03. Surveillance et validation
04. Instructions d'utilisation
05. Annexes
```

### Métriques de performance

| Métrique | Cible | Actuel | Fréquence |
|:---------|:------|:-------|:----------|
| Précision matching | > 85% | 87.2% | Mensuelle |
| Écart entre groupes | < 5% | 7.1% ⚠️ | Trimestrielle |
| Dérive détectée | < 2%/mois | 1.3% | Hebdomadaire |

---

## 🔄 Plan de Surveillance Post-Marché

### Monitoring Continu

| Indicateur | Seuil | Action | Fréquence |
|:-------------|:------|:-------|:----------|
| Drift performance | > 3% | Alerte technique | Hebdo |
| Écart équité | > 5% | Suspension + investigation | Mensuel |
| Incidents sécurité | Tout | Procédure incident | Immédiat |

### Ré-évaluation Formelle
- **Fréquence** : Trimestrielle
- **Responsable** : Comité conformité IA
- **Déclencheurs** : Modification modèle, incident, évolution réglementaire

---

## 📁 Arborescence

```
cas_tri_cv_haut_risque/
├── README.md
├── 01_workflow_iso42001/
├── 02_audit_technique/
├── 03_ebios_rm_enrichi/
├── 04_documentation_annexe_iv/
├── 05_surveillance_post_marche/
└── scripts/
```

---

> 💡 **Conseil** : Utilisez ce cas comme template pour vos autres workflows haut risque.
