# Guide de Migration — V1 → V2

**Objectif** : Migrer votre corpus EBIOS-RM IA de la V1 à la V2 sans perte de données.

---

## 🎯 Vue d'Ensemble

| Aspect V1 | Changement V2 | Impact |
|:----------|:--------------|:-------|
| `00-METHODOLOGIE/` | `v2/methodology/` | Restructuration |
| `99-REGISTRE/*.yaml` | `v2/registry/registry.yaml` | Schéma JSON + validation |
| Qualifier V1/V2 | Mode Express/Détaillé unique | Unification |
| Templates disparates | Templates harmonisés | Cohérence |
| Script Python basique | CLI complet | Fonctionnalités étendues |

---

## 📋 Prérequis

- [ ] Sauvegarde complète du repository V1
- [ ] Python 3.9+ installé
- [ ] Accès en écriture au repository

---

## 🚀 Migration Étape par Étape

### Étape 1 : Préparation (15 min)

```bash
# 1. Cloner le repository (si pas déjà fait)
git clone https://github.com/yhz-dotcom/corpus-ebios-rm.git
cd corpus-ebios-rm

# 2. Créer une branche de migration
git checkout -b migration-v1-to-v2

# 3. Vérifier la structure V2 existe
ls -la v2/
# Doit afficher : docs/ methodology/ registry/ templates/ tools/ training/ references/
```

### Étape 2 : Migration du Registre (30 min)

#### 2.1 Identifier vos entrées V1

```bash
# Compter les entrées existantes
grep -c "sia_id:" 99-REGISTRE/registre-sia.yaml
grep -c "sia_id:" 99-REGISTRE/registre-sia-V2.yaml 2>/dev/null || echo "0 (pas de V2)"
```

#### 2.2 Exporter les entrées V1

```bash
# Utiliser le script V1 pour exporter en JSON
python 99-REGISTRE/scripts/export-registre.py --format json --output v1-export.json
```

#### 2.3 Convertir au format V2

```bash
# Utiliser le convertisseur V2
python v2/tools/cli/sia-cli.py migrate v1-export.json --output v2/registry/migrated-entries.yaml
```

#### 2.4 Valider la conversion

```bash
# Valider chaque entrée migrée
python v2/tools/cli/sia-cli.py validate v2/registry/migrated-entries.yaml
```

#### 2.5 Fusionner dans le registre V2

```bash
# Ajouter au registre principal
cat v2/registry/migrated-entries.yaml >> v2/registry/registry.yaml

# Valider le registre complet
python v2/tools/cli/sia-cli.py validate v2/registry/registry.yaml
```

### Étape 3 : Migration des Fiches (1-2h)

#### 3.1 Identifier les fiches existantes

```bash
find 11-SIA/20-OUTILS/archives/ -name "*.md" -type f
```

#### 3.2 Mapper vers les templates V2

| Template V1 | Template V2 | Action |
|:------------|:------------|:-------|
| `fiche-light.md` | `template-level-1.md` | Copier + adapter en-tête |
| `fiche-workflow.md` | `template-level-2.md` | Migrer section par section |
| `dossier-decisionnel.md` | `template-level-3.md` | Réorganisation complète |

#### 3.3 Script de migration automatique

```bash
# Créer un script de migration pour les fiches
python v2/tools/cli/sia-cli.py migrate-template \
    --from 11-SIA/20-OUTILS/archives/fiche-*.md \
    --to v2/templates/migrated/
```

### Étape 4 : Mise à Jour des Processus (30 min)

#### 4.1 Former l'équipe

```bash
# Lire le quickstart V2
cat v2/docs/quickstart.md

# Tester la qualification V2
python v2/tools/cli/sia-cli.py qualify --mode express
```

#### 4.2 Mettre à jour la documentation interne

Remplacer les références :
- `00.2-usage-first-qualifier.md` → `v2/methodology/qualifier/index.md`
- `01-EBIOS-LIGHT.md` → `v2/methodology/levels/level-1-conversational.md`
- `99-REGISTRE/registre-sia.yaml` → `v2/registry/registry.yaml`

### Étape 5 : Validation Finale (30 min)

```bash
# 1. Valider le registre complet
python v2/tools/cli/sia-cli.py validate v2/registry/registry.yaml

# 2. Tester l'export
python v2/tools/cli/sia-cli.py export v2/registry/registry.yaml --format csv

# 3. Vérifier le dashboard
python v2/tools/cli/sia-cli.py dashboard v2/registry/registry.yaml

# 4. Comparer les statistiques V1/V2
echo "=== V1 ==="
grep -c "sia_id:" 99-REGISTRE/registre-sia.yaml
echo "=== V2 ==="
grep -c "sia_id:" v2/registry/registry.yaml
```

---

## 🔄 Coexistence V1/V2

Pendant la période de transition (recommandé : 3-6 mois) :

```
corpus-ebios-rm/
├── 00-METHODOLOGIE/        ← V1 (lecture seule)
├── 11-SIA/                 ← V1 (lecture seule)
├── 99-REGISTRE/            ← V1 (lecture seule)
├── v2/                     ← V2 (actif)
│   ├── registry/
│   └── ...
└── README.md               ← Pointe vers V2
```

### Workflow de coexistence

1. **Nouveaux usages** : Qualifier directement en V2
2. **Usages existants** : Migrer à la prochaine revue annuelle
3. **Modifications** : Faire en V2, archiver la V1

---

## ⚠️ Points d'Attention

### Changements Breaking

| V1 | V2 | Action requise |
|:---|:---|:---------------|
| `niveau_ebios: "🟢 Light"` | `ebios_level: "🟢 Level 1"` | Renommer |
| `fiche_reference` | `reference_file` | Renommer |
| `rgpd.concerne` | `gdpr.applies` | Renommer |
| `ai_act.annex_iii: true` | `ai_act.annex_iii: true` | Identique ✓ |

### Données Non Migrées Automatiquement

- Historique des versions des fiches
- Commentaires et notes libres
- Pièces jointes externes

### Validation Requise Manuellement

- [ ] Tous les `sia_id` sont uniques
- [ ] Les `reference_file` pointent vers des fichiers existants
- [ ] Les dates sont au format `YYYY-MM-DD`
- [ ] Les enums sont valides (levels, statuses, etc.)

---

## 🆘 Dépannage

### Erreur : "Champ requis manquant"

**Cause** : Le schéma V2 est plus strict
**Solution** : Compléter les champs manquants ou utiliser `--strict=false`

### Erreur : "sia_id déjà existant"

**Cause** : Conflit ID entre V1 et V2
**Solution** : Renommer l'entrée V1 ou V2

### Erreur : "Template non trouvé"

**Cause** : Le champ `template_used` référence un template V1
**Solution** : Mettre à jour vers `template-level-1/2/3`

---

## ✅ Checklist Migration

- [ ] Sauvegarde V1 effectuée
- [ ] Branche migration créée
- [ ] Registre migré et validé
- [ ] Fiches migrées (ou plan de migration défini)
- [ ] Équipe formée à la V2
- [ ] Documentation interne mise à jour
- [ ] Tests de validation passés
- [ ] Dashboard V2 opérationnel
- [ ] Plan de désactivation V1 défini (dans 6 mois)

---

## 📞 Support

En cas de problème :
1. Consulter `v2/docs/faq.md`
2. Vérifier `v2/CHANGELOG.md`
3. Ouvrir une issue sur GitHub

---

*Guide de Migration V1 → V2 — Version 1.0*
