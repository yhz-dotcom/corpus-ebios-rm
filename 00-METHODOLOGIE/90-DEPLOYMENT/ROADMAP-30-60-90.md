<!-- === EN-TÊTE DOCUMENTAIRE ISO-GRADE === -->

| Métadonnées | Valeur |
|-------------|--------|
| **Référence** | `EBIOS-DEPLOY-001` |
| **Titre** | Guide de Déploiement Progressif — Roadmap 30-60-90 jours |
| **Version** | `1.0` |
| **Date** | `06/03/2026` |
| **Propriétaire** | `Direction Conformité / AI Officer` |
| **Classification** | `Interne` |

---

# 🚀 Guide de Déploiement Progressif — EBIOS-RM IA "Usage-First"

**Référence** : EBIOS-DEPLOY-001 | Roadmap 30-60-90 jours

---

## 📋 Pré-requis & Facteurs de Succès

### Avant de commencer

| Pré-requis | Description |
|:-----------|:------------|
| **Sponsor exécutif** | Un dirigeant qui porte la démarche (RSSI, DPO, DSI ou DRH) |
| **Équipe pilote** | 3-5 personnes : métier + technique + conformité |
| **Périmètre initial** | Un domaine métier limité (ex: RH, Support, Marketing) |
| **Outils minimaux** | Git + Markdown + un tableur pour le registre (au début) |

### Facteurs Clés de Succès

✅ **Commencer petit** : Mieux vaut 3 usages bien qualifiés que 30 mal documentés  
✅ **Impliquer les utilisateurs finaux** dès la qualification : ils voient les risques réels  
✅ **Documenter les choix d'allègement** : La proportionnalité doit être justifiée  
✅ **Itérer, ne pas parfaire** : Livrer une v1 utile, améliorer en v2  
✅ **Capitaliser sur l'existant** : Réutiliser AIPD, audits, retours d'incident

### Pièges à Éviter

❌ **Vouloir tout qualifier en mode 🔴** dès le départ → surcharge et rejet  
❌ **Dissocier qualification technique de métier** → incohérences  
❌ **Oublier de planifier les révisions** → registre obsolète  
❌ **Négliger la communication** → perçu comme une contrainte

---

## 🗓 PHASE 1 : Jours 1-30 — Fondation & Pilote

> 🎯 **Objectif** : Valider l'approche sur 3-5 usages concrets, produire les premiers livrables, ajuster les templates.

### Semaine 1 : Cadrage & Outillage

#### Livrables

- [ ] Valider le sponsor et l'équipe pilote (3-5 personnes)
- [ ] Cloner/adapater le corpus `11-SIA/` dans votre dépôt interne
- [ ] Configurer le registre minimal (`registre-sia.yaml` ou tableur temporaire)
- [ ] Former l'équipe pilote à la grille `USAGE-QUALIFIER` (1h)

#### Réunion de Cadrage

| Durée | Ordre du jour |
|:------|:--------------|
| 15 min | Présentation de l'approche "Usage-First" |
| 15 min | Démonstration : qualification d'un usage exemple |
| 30 min | Sélection des 3-5 usages pilotes |
| 30 min | Planning des ateliers de qualification |

#### Critères de Sélection des Pilotes

| Niveau | Exemple | Pourquoi |
|:-------|:--------|:---------|
| 🟢 **Conversationnel** | Rédaction assistée | Simple, rapide à qualifier |
| 🟡 **Workflow** | RAG documentaire | Moyen, teste les processus |
| 🔴 **Borderline** | Tri semi-auto | Complexe, valide la méthode |

> ⚠️ **Éviter** : usages trop critiques ou trop flous pour le pilote

---

### Semaines 2-3 : Qualification & Analyse Pilote

#### Pour chaque usage pilote

```yaml
étape_1_qualification:
  - "Animer la grille USAGE-QUALIFIER (30 min max)"
  - "Documenter la justification du niveau choisi"
  - "Ajouter l'entrée au registre (statut: 'En qualification')"

étape_2_analyse:
  - "Télécharger le template correspondant (🟢/🟡/🔴)"
  - "Animer l'atelier EBIOS-RM adapté (timeboxé)"
  - "Produire la fiche/dossier avec les risques prioritaires"
  - "Lier la fiche au registre (champ fiche_reference)"

étape_3_validation:
  - "Revue croisée : métier + technique + conformité"
  - "Ajustements mineurs si besoin"
  - "Changer statut registre: 'Actif'"
  - "Planifier la prochaine revue (3/6/12 mois selon niveau)"
```

#### Output Phase 1

| Livrable | Description |
|:---------|:------------|
| **3-5 usages qualifiés** | Analysés et documentés |
| **Registre SIA peuplé** | Avec entrées réelles |
| **Retours d'expérience** | Sur les templates (ce qui marche/coince) |
| **Templates v1.1** | Version ajustée intégrée au corpus |

---

### Semaine 4 : Retour d'Expérience & Ajustements

#### Atelier de REX

| Durée | Activité |
|:------|:---------|
| 30 min | Retour sur les 3-5 qualifications réalisées |
| 30 min | Identification des points de friction |
| 30 min | Propositions d'amélioration des templates |
| 30 min | Priorisation des ajustements pour Phase 2 |

#### Questions Clés

- La grille USAGE-QUALIFIER est-elle claire ? (temps réel, résultat)
- Les templates sont-ils adaptés à notre contexte ?
- Quels sont les blocages récurrents ?
- Quelle communication pour généraliser ?

---

## 🗓 PHASE 2 : Jours 31-60 — Industrialisation

> 🎯 **Objectif** : Passer à l'échelle sur un domaine métier complet, former des référents locaux, automatiser les exports.

### Semaines 5-6 : Formation des Référents

#### Programme de Formation (1/2 journée)

| Module | Durée | Contenu |
|:-------|:------|:--------|
| Contexte réglementaire | 30 min | AI Act, RGPD, responsabilités |
| Méthode Usage-First | 45 min | Grille, niveaux, proportionnalité |
| Atelier pratique | 60 min | Qualification d'un usage réel |
| Outils | 45 min | Registre, templates, exports |

#### Cible : 5-10 référents métier

- 1 par équipe/direction
- Profil : à l'aise avec l'outil informatique, compréhension métier
- Rôle : qualifier les usages de leur périmètre, remonter les cas limites

---

### Semaines 7-8 : Qualification à l'Échelle

#### Objectif : 15-20 usages qualifiés

| Activité | Fréquence | Qui |
|:---------|:----------|:----|
| Sessions de qualification | 2x/semaine | Référents + support conformité |
| Revue des cas limites | Hebdo | Équipe pilote |
| Mise à jour registre | Continue | Référents |
| Support technique | Quotidien | Équipe pilote (1h/jour) |

#### Automatisation

- [ ] Script d'export CSV opérationnel
- [ ] Dashboard simple (Google Sheets ou interne)
- [ ] Alertes revues à venir (≤ 30 jours)

---

### Fin Phase 2 : Bilan à 60 jours

#### KPIs

| Métrique | Objectif |
|:---------|:---------|
| Usages qualifiés | ≥ 15 |
| Référents formés | ≥ 5 |
| Temps moyen qualification | 🟢: 15min, 🟡: 2h, 🔴: 1j |
| Satisfaction référents | ≥ 7/10 |

---

## 🗓 PHASE 3 : Jours 61-90 — Optimisation & Gouvernance

> 🎯 **Objectif** : Intégrer dans la gouvernance, optimiser les processus, préparer la pérennisation.

### Semaines 9-10 : Intégration Gouvernance

#### Points à Formaliser

| Élément | Description |
|:--------|:------------|
| **Comité IA** | Réunion trimestrielle : revue registre, cas limites, évolutions |
| **Processus de qualification** | Workflow validé : qui qualifie, qui valide, délais |
| **Critères d'escalade** | Quand passer de 🟡 à 🔴 ? Quand impliquer le Comité ? |
| **Communication interne** | Newsletter, FAQ, supports de formation |

#### Documentation

- [ ] Procédure qualité "Qualification des usages IA"
- [ ] Guide référent (20 pages max)
- [ ] FAQ usagers (10 questions)
- [ ] Présentation direction (10 slides)

---

### Semaines 11-12 : Optimisation & Pérennisation

#### Améliorations Processus

| Amélioration | Description |
|:-------------|:------------|
| **Templates v2.0** | Intégration des retours des 90 jours |
| **Registre avancé** | V2 avec vues filtrées, exports automatisés |
| **Intégration CI/CD** | Qualification automatique des nouveaux déploiements IA |
| **KPIs temps réel** | Dashboard avec alertes |

#### Revue à 90 Jours

**Participants** : Sponsor, équipe pilote, référents, direction  
**Ordre du jour** :
1. Bilan quantitatif (usages, temps, satisfaction)
2. Retour d'expérience qualitatif
3. Identification des usages à requalifier
4. Planification Phase 4 (90-180 jours)

---

## 📊 Tableau de Bord de Suivi

### Vue d'Ensemble

```
┌─────────────────────────────────────────────────────────────┐
│  ROADMAP EBIOS-RM IA - Suivi 30-60-90 jours                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PHASE 1 (J1-30)     ████████░░░░░░░░░░  [En cours]        │
│  ├─ Usages qualifiés: 3/5                                  │
│  ├─ Templates validés: ✅                                   │
│  └─ Prochaine étape: Formation référents                   │
│                                                             │
│  PHASE 2 (J31-60)    ░░░░░░░░░░░░░░░░░░  [À venir]         │
│  ├─ Objectif: 15 usages                                    │
│  ├─ Référents: 5 à former                                  │
│  └─ Automatisation: Export CSV                             │
│                                                             │
│  PHASE 3 (J61-90)    ░░░░░░░░░░░░░░░░░░  [À venir]         │
│  ├─ Gouvernance: Comité IA                                 │
│  ├─ Documentation: Procédure qualité                       │
│  └─ Optimisation: Templates v2                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### KPIs Clés

| KPI | J30 | J60 | J90 | Cible |
|:----|:----|:----|:----|:------|
| Usages qualifiés | 5 | 15 | 25 | 30+ |
| Référents actifs | 3 | 5 | 8 | 10 |
| Temps qualif. 🟡 | 4h | 2h | 1h30 | 1h30 |
| Satisfaction | - | 7/10 | 8/10 | 8/10 |

---

## 🎯 Checklist de Validation par Phase

### Phase 1 (J30) ✅

- [ ] Sponsor identifié et engagé
- [ ] Équipe pilote formée
- [ ] 3-5 usages qualifiés et documentés
- [ ] Registre initial peuplé
- [ ] Templates testés et ajustés
- [ ] REX réalisé et actions identifiées

### Phase 2 (J60) ✅

- [ ] 5-10 référents formés
- [ ] 15-20 usages qualifiés
- [ ] Processus de qualification fluide
- [ ] Exports automatisés opérationnels
- [ ] Support référents en place

### Phase 3 (J90) ✅

- [ ] Comité IA instauré
- [ ] Procédure qualité publiée
- [ ] 25+ usages qualifiés
- [ ] Documentation complète
- [ ] Plan 90-180 jours défini

---

## 📎 Ressources et Templates

### Documents à Préparer

| Document | Phase | Template |
|:---------|:------|:---------|
| Présentation sponsor | J1 | `templates/presentation-sponsor.pptx` |
| Formation équipe pilote | J1 | `templates/formation-pilote.md` |
| Guide référent | J60 | `templates/guide-referent.md` |
| Procédure qualité | J90 | `templates/procedure-qualite.md` |
| FAQ usagers | J90 | `templates/faq-usagers.md` |

### Outils Recommandés

| Usage | Outil | Alternative |
|:------|:------|:------------|
| Registre | YAML + Git | Excel → Notion → Airtable |
| Collaboration | Git + Markdown | Confluence, SharePoint |
| Dashboard | Python + Streamlit | Google Data Studio, Tableau |
| Formation | Markdown + Mermaid | PowerPoint, Miro |

---

## 💡 Conseils de Facilitation

### Pour Animer les Ateliers

1. **Timeboxer** : Respecter les durées annoncées
2. **Concret** : Toujours partir d'exemples réels
3. **Inclusif** : Faire parler métier ET technique
4. **Documenter** : Noter les décisions immédiatement
5. **Itérer** : Mieux vaut une v1 rapide qu'une v3 jamais finie

### Pour Gérer la Résistance

| Obstacle | Réponse |
|:---------|:--------|
| "Trop complexe" | Commencer par un usage 🟢 simple |
| "Pas le temps" | 15 min pour 🟢, on peut trouver 15 min |
| "On le fait déjà" | Super ! Documentons-le proprement |
| "L'IA change trop vite" | D'où l'intérêt des revues planifiées |
| "C'est du contrôle" | C'est de la protection (responsabilité, réputation) |

---

## 7. RÉVISION

| Version | Date | Auteur | Modifications |
|:--------|:-----|:-------|:--------------|
| 1.0 | 06/03/2026 | Direction Conformité | Création roadmap 30-60-90 |

---

**Document approuvé par :**
- [ ] Sponsor exécutif
- [ ] AI Officer
- [ ] RSSI

**Date d'approbation :** _______________

---

*Guide de Déploiement Progressif — Version 1.0 ISO-Grade*  
*Réf. EBIOS-DEPLOY-001*

---

> 📌 **Conclusion** : Ce guide transforme la méthodologie EBIOS-RM IA "Usage-First" en un **plan d'action concret et réalisable** en 90 jours. L'approche itérative permet de démontrer rapidement la valeur tout en construisant une gouvernance durable.
