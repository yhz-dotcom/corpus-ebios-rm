# Changelog — Corpus EBIOS-RM IA v2.0

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère à [Semantic Versioning](https://semver.org/lang/fr/).

---

## [Unreleased]

### Added
- Structure v2.0 en construction parallèle à v1.0
- Schéma JSON de validation du registre (`registry/schema.json`)
- CLI Python (`tools/cli/sia-cli.py`) avec commandes qualify/validate/export/dashboard
- Quickstart 15 minutes (`docs/quickstart.md`)
- Template Level 1 harmonisé (`templates/template-level-1.md`)

### Changed
- N/A (v2.0 en construction)

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- N/A

---

## [1.0.0] - 2026-03-06

### Added (V1 stable, conservée dans racine)

#### Méthodologie
- `00.2-usage-first-qualifier.md` — Grille V1 (5 questions)
- `00.2-usage-first-qualifier-V2.md` — Grille V2 alternative (YAML)
- `01-EBIOS-LIGHT.md` — Template 🟢 conversationnel
- `02-EBIOS-STANDARD.md` — Template 🟡 workflow (5 ateliers)
- `03-EBIOS-RENFORCE.md` — Template 🔴 décisionnel (EBIOS complet)
- `04-arbre-decision.md` — Arbre de décision visuel

#### Déploiement
- `90-DEPLOYMENT/ROADMAP-30-60-90.md` — Roadmap détaillée 90 jours

#### Registre
- `99-REGISTRE/registre-sia.yaml` — Registre V1 standard
- `99-REGISTRE/registre-sia-V2.yaml` — Registre V2 enrichi
- `99-REGISTRE/scripts/export-registre.py` — Script d'export

#### Documentation SIA
- `11-SIA/11.2-sources-risque-ia.md` — Sources de risque IA
- `11-SIA/11.3-scenarios-ia.md` — Scénarios de risque
- `11-SIA/11.4-mesures-securite-ia.md` — Mesures de sécurité
- `11-SIA/11.5-mapping-ai-act.md` — Mapping EBIOS/AI Act/ISO 42001
- `11-SIA/11.6-dictionnaire-risques-cycle-vie.md` — Risques par phase
- `11-SIA/11.7-dictionnaire-risques-par-metier.md` — Risques sectoriels
- `11-SIA/11.8-guide-deployer-ai-act.md` — Guide Deployer

#### Review
- `99-ARCHIVE/REVIEW-CRITIQUE-V1.md` — Review critique complète

### Known Issues (V1)
- V1 et V2 coexistent sans stratégie de convergence
- Pas de schéma de validation formel
- Pas de tests automatisés
- Pas de cas réels anonymisés
- Fragmentation terminologique

---

## Types de Changements

- `Added` : Nouvelles fonctionnalités
- `Changed` : Modifications de fonctionnalités existantes
- `Deprecated` : Fonctionnalités obsolètes
- `Removed` : Fonctionnalités supprimées
- `Fixed` : Corrections de bugs
- `Security` : Corrections de sécurité

---

## Versioning Strategy

### V1.x (Stable)
- Conservée dans la racine du repository
- Bug fixes uniquement
- Pas de nouvelles fonctionnalités

### V2.0 (En construction)
- Développement dans `/v2/`
- Architecture refondue
- Migration path documentée

### Migration V1 → V2
- Guide disponible dans `v2/MIGRATION.md`
- Outil de migration CLI prévu
- Période de coexistence : 6 mois

---

*Dernière mise à jour : 06/03/2026*
