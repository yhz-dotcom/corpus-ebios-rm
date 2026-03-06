# Guide AI Act — Deployer vs Provider (et exceptions)

**Référence** : Art. 2, 25, 6(3) AI Act | **Usage** : Détermination du rôle et obligations

---

## 🎯 Vue d'Ensemble

```
┌─────────────────────────────────────────────────────────────┐
│                    CHAÎNE DE VALEUR IA                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │   PROVIDER  │───▶│   SYSTEM    │───▶│   DEPLOYER  │     │
│  │  (Créateur) │    │   (SIA)     │    │  (Utilisateur)│    │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
│         │                  │                  │             │
│         ▼                  ▼                  ▼             │
│    • Développe        • Modèle           • Intégration     │
│    • Entraînement     • Fine-tuning      • Usage final      │
│    • Mise marché      • Inférence        • Supervision      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 Définitions AI Act

### Provider (Fournisseur)

> *"Toute personne physique ou morale, autorité publique, agence ou autre organisme qui développe un système d'IA ou un modèle d'IA à usage général [...] et le met sur le marché ou le met en service sous son propre nom ou sa propre marque"*

**Obligations** : Toutes (Art. 8-15 pour haut risque)

### Deployer (Déployeur)

> *"Toute personne physique ou morale, autorité publique, agence ou autre organisme qui utilise un système d'IA à usage de ses propres systèmes"*

**Obligations** : Allégées (Art. 26 pour haut risque)

---

## 🔍 Comment Déterminer son Rôle ?

### Arbre de Décision

```
Vous utilisez un système d'IA ?
    │
    ├──► Vous l'avez développé ET mis sur le marché ?
    │       │
    │       ├──► OUI ──▶ PROVIDER
    │       │
    │       └──► NON ──▶ Vous l'utilisez pour vous ?
    │               │
    │               ├──► OUI ──▶ PROVIDER (for own use)
    │               │
    │               └──► NON ──▶ DEPLOYER
    │
    └──► Vous utilisez un système existant ?
            │
            ├──► Sans modification ──▶ DEPLOYER
            │
            └──► Avec modification substantielle ?
                    │
                    ├──► OUI ──▶ PROVIDER
                    │
                    └──► NON (prompt engineering, etc.) ──▶ DEPLOYER
```

### Modification Substantielle (Seuil Provider)

| Modification | Provider ? | Justification |
|:-------------|:-----------|:--------------|
| Fine-tuning complet | ✅ Oui | Nouveau modèle créé |
| LoRA / Adapters | ✅ Oui | Comportement modifié |
| RAG sur base propriétaire | ⚠️ Cas par cas | Dépend de l'impact |
| Prompt engineering | ❌ Non | Usage standard |
| Configuration API | ❌ Non | Paramètres standard |

---

## 📊 Tableau Comparatif Obligations

### Pour Systèmes à Haut Risque (Annexe III)

| Obligation | Provider | Deployer |
|:-----------|:---------|:---------|
| **Art. 8** — Système qualité | ✅ | ❌ |
| **Art. 9** — Documentation technique | ✅ Complète | ❌ Référence |
| **Art. 10** — Gestion risques | ✅ | ⚠️ Utilisation conforme |
| **Art. 11** — Jeu de données | ✅ | ❌ |
| **Art. 12** — Traçabilité | ✅ | ✅ Registre Art. 60 |
| **Art. 13** — Transparence | ✅ Notice | ✅ Information utilisateurs |
| **Art. 14** — Supervision humaine | ✅ Conception | ✅ Mise en œuvre |
| **Art. 15** — Exactitude, robustesse | ✅ | ⚠️ Monitoring |
| **Art. 16** — Déclaration conformité | ✅ | ❌ |
| **Art. 17** — Marquage CE | ✅ | ❌ |
| **Art. 26** — Obligations Deployer | ❌ | ✅ |

### Art. 26 — Obligations Spécifiques Deployer

1. **Utilisation conforme** aux instructions du Provider
2. **Surveillance humaine** effective (personnes compétentes)
3. **Conservation logs** (min. 6 mois)
4. **Information** des personnes concernées
5. **Registre** des systèmes déployés (Art. 60)

---

## ⭐ Exception Art. 6(3) — "Provider for own use"

### Quand s'applique-t-elle ?

> *"Les systèmes d'IA à usage professionnel qui ne sont pas mis sur le marché mais utilisés par le fournisseur dans le cadre de ses propres activités"*

**Conditions cumulatives** :
1. Usage strictement **interne**
2. **Pas de mise sur le marché** (même gratuitement)
3. **Pas de fourniture à des tiers**

### Exemples

| Cas | Provider for own use ? | Justification |
|:----|:-----------------------|:--------------|
| Banque : scoring interne crédit | ✅ Oui | Usage interne, pas de vente |
| Assureur : évaluation risques | ✅ Oui | Propre portefeuille |
| ESN : outil interne recrutement | ✅ Oui | Pas pour clients |
| Éditeur : SaaS scoring | ❌ Non | Mis sur le marché |
| Consortium : outil partagé | ❌ Non | Fourniture à tiers |

### Conséquences

| Aspect | Provider for own use |
|:-------|:---------------------|
| Marquage CE | ❌ Non requis |
| Déclaration conformité | ❌ Non requise |
| Obligations techniques | ✅ Toutes (Art. 8-15) |
| Gouvernance | ✅ Interne |
| Audit | ✅ Possible par régulateur |

---

## 🎭 Cas Complexes

### Cas 1 : Fine-tuning sur modèle ouvert

**Situation** : Vous fine-tunez Llama 3 (open source) pour usage interne

| Élément | Évaluation |
|:--------|:-----------|
| Modèle de base | Open source (Meta = Provider initial) |
| Votre modification | Fine-tuning substantiel |
| Votre rôle | **Provider (for own use)** |
| Obligations | Art. 8-15, pas de CE |

### Cas 2 : API + RAG + Workflow métier

**Situation** : Vous utilisez GPT-4 (OpenAI) + RAG interne + workflow décisionnel

| Élément | Évaluation |
|:--------|:-----------|
| Modèle de base | GPT-4 (OpenAI = Provider) |
| Votre modification | RAG + workflow (pas modèle) |
| Votre rôle | **Deployer** |
| Obligations | Art. 26, registre, supervision |

### Cas 3 : Variante LoRA pour clients

**Situation** : Vous créez variante LoRA et la proposez à vos clients

| Élément | Évaluation |
|:--------|:-----------|
| Modèle de base | Qwen3.5 (Alibaba = Provider) |
| Votre modification | LoRA propriétaire |
| Votre action | Mise à disposition clients |
| Votre rôle | **Provider** (pas "for own use") |
| Obligations | Art. 8-17, CE obligatoire |

---

## 📝 Documentation Requise

### Provider (ou Provider for own use)

```
documentation-technique/
├── system-quality-management.md      # Art. 8
├── technical-documentation.md        # Art. 9
├── risk-management-system.md         # Art. 10
├── data-governance.md                # Art. 11
├── record-keeping.md                 # Art. 12
├── transparency-information.md       # Art. 13
├── human-oversight.md                # Art. 14
├── accuracy-robustness.md            # Art. 15
├── eu-declaration-of-conformity.md   # Art. 16 (sauf own use)
└── post-market-monitoring.md         # Art. 72
```

### Deployer

```
registre-deployer/
├── liste-systemes-deployes.md        # Art. 60
├── instructions-provider.md          # Art. 26(1)
├── human-oversight-implementation.md # Art. 26(2)
├── logs-retention-policy.md          # Art. 26(3)
└── information-subjects.md           # Art. 26(4)
```

---

## ✅ Checklist Détermination Rôle

- [ ] Qui a développé le système IA ?
- [ ] Y a-t-il eu modification substantielle ?
- [ ] Le système est-il mis sur le marché ?
- [ ] Fourni à des tiers (même internes) ?
- [ ] Usage strictement interne ?
- [ ] Obligations identifiées (Art. 8-15 ou 26) ?
- [ ] Documentation correspondante planifiée ?

---

## 🆘 Cas d'Éscalade

Consulter un expert si :

- [ ] Modèle open source + fine-tuning + usage flou
- [ ] Consortium / groupement / plateforme
- [ ] Frontière Provider/Deployer incertaine
- [ ] Exception Art. 6(3) contestable
- [ ] Sanctions réglementaires en jeu

---

## 📚 Références

| Référence | Contenu |
|:----------|:--------|
| Règlement (UE) 2024/1689 | AI Act complet |
| Art. 2 (Définitions) | Provider, Deployer, SIA |
| Art. 6(3) | Exception usage interne |
| Art. 25 | Obligations des Deployers |
| Art. 60 | Registre Deployers |
| Lignes directrices AI Office | Interprétation officielle |

---

*Guide AI Act — Deployer vs Provider | Version 2.0*
