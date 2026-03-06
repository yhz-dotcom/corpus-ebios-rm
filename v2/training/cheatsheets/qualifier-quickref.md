# Cheat Sheet — Qualification EBIOS-RM IA 🟢🟡🔴

**Format** : A4 recto-verso | **Temps** : Référence rapide

---

## RECTO — Grille Express (5 min)

### Les 5 Questions

| Q | Question | Si Non → | Si Oui → |
|:-:|:---------|:---------|:---------|
| 1 | IA sur données/processus métier ? | **🟢 L1** | Q2 |
| 2 | Sortie influence décision/action ? | **🟢 L1** | Q3 |
| 3 | Automatisé ou fort impact ? | **🟡 L2** | Q4 |
| 4 | Domaine haut risque (Annexe III) ? | **🟡 L2** | **🔴 L3** |
| 5 | Données sensibles/critiques ? | — | **🔴 L3** |

### Résultat

| Niveau | Template | Temps | Revue |
|:-------|:---------|:------|:------|
| 🟢 Level 1 | `template-level-1.md` | 10 min | Annuelle |
| 🟡 Level 2 | `template-level-2.md` | 2h | Semestrielle |
| 🔴 Level 3 | `template-level-3.md` | 1-2j | Trimestrielle |

---

## VERSO — Checklists et Commandes

### Checklist Avant Atelier

- [ ] Sponsor identifié
- [ ] Équipe 3-5 personnes (métier + tech + conformité)
- [ ] Usage concret sélectionné
- [ ] Salle 2h réservée
- [ ] Template imprimé / partagé

### Checklist Qualification

- [ ] Grille express complétée
- [ ] Niveau déterminé avec justification
- [ ] Template rempli
- [ ] Entrée registre créée
- [ ] CLI validation passée
- [ ] Date revue planifiée

### Commandes CLI Essentielles

```bash
# Qualification
python tools/cli/sia-cli.py qualify --mode express

# Validation
python tools/cli/sia-cli.py validate entry.yaml

# Export
python tools/cli/sia-cli.py export registry.yaml --format csv

# Dashboard
python tools/cli/sia-cli.py dashboard registry.yaml
```

### Contacts et Ressources

| Ressource | Lien |
|:----------|:-----|
| Quickstart | `v2/docs/quickstart.md` |
| Grille complète | `v2/methodology/qualifier/index.md` |
| Templates | `v2/templates/` |
| Cas réels | `v2/training/cases/` |

---

*Cheat Sheet EBIOS-RM IA V2.0 — À imprimer et laminer*
