# Quickstart — Qualifier votre premier usage IA en 15 minutes

**Objectif** : Qualifier un usage IA et l'ajouter au registre en 15 minutes chrono.

---

## ⚡ Mode Express (5 min)

Pour les usages conversationnels simples (rédaction, brainstorming, veille).

### Étape 1 : Répondre aux 5 questions (2 min)

```bash
python tools/cli/qualifier.py --mode express
```

**Questions** :
1. L'IA agit-elle sur des données/processus métier ?
2. La sortie influence-t-elle une décision/action ?
3. La décision est-elle automatisée ou à fort impact ?
4. L'usage concerne-t-il un domaine "haut risque" (Annexe III) ?
5. Des données sensibles sont-elles manipulées ?

### Étape 2 : Récupérer votre niveau (1 min)

| Réponses | Niveau | Prochaine étape |
|:---------|:-------|:----------------|
| Q1=Non | 🟢 Level 1 | Template 1 page, 10 min |
| Q1=Oui, Q2=Non | 🟢 Level 1 | Template 1 page, 10 min |
| Q1=Oui, Q2=Oui, Q3=Non | 🟡 Level 2 | Template 2-3 pages, 2h |
| Q1=Oui, Q2=Oui, Q3=Oui | 🔴 Level 3 | Template complet, 1-2j |
| Q4=Oui | 🔴 Level 3 | Obligatoire (Annexe III) |

### Étape 3 : Compléter le template (10 min pour 🟢)

```bash
# Copier le template
cp templates/template-level-1.md sia-my-first-usage.md

# Éditer avec vos informations
$EDITOR sia-my-first-usage.md
```

### Étape 4 : Ajouter au registre (2 min)

```bash
# Générer l'entrée registre
python tools/cli/qualifier.py --mode express --output registry/my-entry.yaml

# Valider
python tools/cli/validator.py registry/my-entry.yaml

# Ajouter au registre principal
cat registry/my-entry.yaml >> registry/registry.yaml
```

---

## 📋 Mode Détaillé (15 min)

Pour les usages où vous voulez documenter plus de contexte dès la qualification.

```bash
python tools/cli/qualifier.py --mode detailed
```

**Champs supplémentaires** :
- Description technique (modèle, provider, interface)
- Données manipulées (types, sensibilité)
- Supervision humaine (niveau, fréquence)
- Conformité (RGPD, AI Act anticipé)

---

## 🎯 Exemple Complet

### Scénario : Assistant de rédaction d'emails

```bash
# 1. Qualification express
$ python tools/cli/qualifier.py --mode express

🤖 EBIOS-RM IA Qualifier (Express Mode)

Q1: L'IA agit-elle sur des données/processus métier ?
   → Non (conversationnel uniquement)

✅ Niveau recommandé : 🟢 Level 1 — Conversational

Temps estimé : 10 minutes
Template : templates/template-level-1.md
```

### Fiche complétée

```markdown
# SIA-COM-001 — Assistant rédaction emails

## Identification
- **Nom** : Assistant rédaction emails internes
- **Équipe** : Communication
- **Qualifié par** : Marie Dupont
- **Date** : 2026-03-06

## Justification Level 1
- [x] Conversationnel : copier/coller, humain décide tout
- [x] Impact informel : pas de conséquence si erreur
- [x] Données internes non sensibles
- [x] Sortie toujours revue avant envoi

## Précautions
- [x] Pas de données clients dans les prompts
- [x] Vérification systématique avant envoi
- [x] Formation utilisateurs effectuée

## Risques
| Risque | Mitigation |
|:-------|:-----------|
| Fuite données sensibles | Consignes claires, DLP activé |
| Hallucination | Revue obligatoire avant envoi |

## Validation
- **Responsable** : Marie Dupont — 06/03/2026
```

### Entrée registre générée

```yaml
sia_id: "SIA-COM-001"
identification:
  name: "Assistant rédaction emails internes"
  team: "Communication"
  qualification_date: "2026-03-06"
  qualified_by: ["Marie Dupont"]
technical:
  base_model: "GPT-4"
  provider: "OpenAI"
  interface: "ChatGPT Enterprise"
  modified: false
usage:
  automation_level: "Conversational only"
  impact: "None"
  data_types: ["Internal non-sensitive"]
  human_oversight: "Systematic review"
assessment:
  ebios_level: "🟢 Level 1"
  template_used: "template-level-1"
governance:
  status: "Active"
  next_review: "2027-03-06"
tags: ["communication", "writing-assistant", "internal"]
```

---

## ✅ Checklist Qualification

- [ ] Grille qualificatrice complétée
- [ ] Niveau EBIOS déterminé
- [ ] Template rempli et validé
- [ ] Entrée registre créée
- [ ] Entrée validée (CLI)
- [ ] Prochaine revue planifiée

---

## 🆘 Besoin d'Aide ?

| Problème | Solution |
|:---------|:---------|
| Frontière 🟡/🔴 floue | Voir `methodology/levels/level-2-3-boundary.md` |
| Cas Annexe III incertain | Voir `references/mapping-ai-act.md` |
| Template trop complexe | Passer en mode express |
| Erreur validation registre | Voir message CLI + `docs/faq.md` |

---

## 📚 Prochaines Étapes

1. **Animer un atelier** : Voir `methodology/deployment/playbooks/`
2. **Former une équipe** : Voir `training/slides/`
3. **Intégrer au CI/CD** : Voir `tools/integrations/`

---

*Quickstart v2.0 — 15 minutes pour qualifier votre premier usage IA*
