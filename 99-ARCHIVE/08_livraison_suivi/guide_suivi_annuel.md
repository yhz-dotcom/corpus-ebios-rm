# Guide de Suivi Annuel EBIOS RM

## Maintenir la pertinence de l'analyse des risques

---

## 1. OBJECTIF DU SUIVI

L'analyse des risques EBIOS RM n'est pas un exercice ponctuel. Elle doit évoluer avec :
- Les changements de l'organisation
- Les nouvelles menaces
- Les incidents survenus
- Les évolutions réglementaires

---

## 2. FRÉQUENCE DE MISE À JOUR

### Mise à jour annuelle (obligatoire)

| Élément | Fréquence | Déclencheur |
|---------|-----------|-------------|
| Revue complète | Annuelle | Date anniversaire |
| Atelier de mise à jour | Annuelle | Tous les 12 mois |
| Validation direction | Annuelle | Comité sécurité |

### Mise à jour ponctuelle (si événement)

| Événement | Délai mise à jour | Ateliers concernés |
|-----------|-------------------|-------------------|
| Incident majeur | 1 mois | 2, 3, 4 |
| Changement organisationnel | 3 mois | 1, 2, 3 |
| Nouvelle réglementation | 3 mois | 1, 4 |
| Fusion/acquisition | 3 mois | Tous |
| Nouveau système critique | 1 mois | 1, 3, 4 |

---

## 3. PROCESSUS DE MISE À JOUR ANNUELLE

### Étape 1 : Préparation (2 semaines avant)

**Collecte d'informations** :
- [ ] Incidents de l'année écoulée
- [ ] Avancement feuille de route
- [ ] Nouveaux systèmes déployés
- [ ] Changements organisationnels
- [ ] Évolution menaces (veille)

**Participants à convier** :
- RSSI
- MOA
- RSI
- Pilotes des chantiers sécurité

---

### Étape 2 : Atelier de mise à jour (4h)

#### Partie A : Bilan (1h)

**1.1 Bilan des incidents**
| Incident | Date | Impact | Leçons apprises | Risque associé |
|----------|------|--------|-----------------|----------------|
| [Description] | [Date] | [Impact] | [Leçons] | [SR-XXX] |

**1.2 Avancement feuille de route**
| Action | Prévu | Réalisé | Écart | Cause |
|--------|-------|---------|-------|-------|
| [FR-001] | [Date] | [Date] | [Retard/avance] | [Cause] |

**1.3 Nouveaux éléments**
- Nouveaux biens essentiels
- Nouveaux systèmes
- Nouvelles menaces identifiées

---

#### Partie B : Mise à jour des risques (2h)

**2.1 Réévaluation des risques existants**

Pour chaque risque critique ou élevé :
- Le risque est-il toujours pertinent ?
- L'impact a-t-il changé ?
- La vraisemblance a-t-elle évolué ?

| ID Risque | Gravité avant | Gravité après | Évolution | Justification |
|-----------|---------------|---------------|-----------|---------------|
| SR-001 | 12 | 9 | ↓ | Mesures déployées |

**2.2 Identification nouveaux risques**

Brainstorming :
- Nouvelles cyberattaques dans le secteur
- Nouvelles vulnérabilités
- Changements de contexte

**2.3 Risques à archiver**

Risques devenus obsolètes :
- Système décommissionné
- Mesure définitive
- Contexte changé

---

#### Partie C : Ajustement feuille de route (1h)

**3.1 Bilan actions**
- Actions terminées ✅
- Actions en retard ⚠️
- Actions à ajouter ➕

**3.2 Nouvelles priorités**
| Nouveau risque | Action proposée | Échéance | Budget |
|----------------|-----------------|----------|--------|
| [SR-XXX] | [Description] | [Date] | [€] |

**3.3 Feuille de route année N+1**
- Priorités pour l'année à venir
- Budget prévisionnel
- Ressources nécessaires

---

### Étape 3 : Documentation (1 semaine après)

**Mise à jour des documents** :
- [ ] Fiches de risques modifiées
- [ ] Nouvelles fiches créées
- [ ] Feuille de route actualisée
- [ ] Rapport de mise à jour rédigé

**Rapport de mise à jour** :
```
RAPPORT MISE À JOUR EBIOS RM
Date : [Date]
Version : V[X].0

1. BILAN ANNÉE ÉCOULÉE
   - Incidents majeurs
   - Avancement feuille de route
   - Écarts analysés

2. ÉVOLUTIONS RISQUES
   - Risques réévalués
   - Nouveaux risques
   - Risques archivés

3. NOUVELLE FEUILLE DE ROUTE
   - Priorités N+1
   - Budget
   - Planning

4. ANNEXES
   - Fiches mises à jour
   - Nouvelles fiches
```

---

## 4. INDICATEURS DE SUIVI

### KPI EBIOS

| Indicateur | Cible | Fréquence |
|------------|-------|-----------|
| % risques critiques traités | 100% | Mensuelle |
| % mesures déployées (feuille route) | 80% | Trimestrielle |
| Temps depuis dernière mise à jour EBIOS | < 12 mois | Annuelle |
| Nombre incidents vs risques identifiés | [Référence] | Annuelle |

### Tableau de bord

```
┌─────────────────────────────────────────────────────────┐
│  DASHBOARD SÉCURITÉ - MISE À JOUR EBIOS                │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  RISQUES           MESURES          INCIDENTS           │
│  ┌─────┐          ┌─────┐          ┌─────┐             │
│  │ 🔴 3│          │ ✅ 12│          │ ⚠️ 2 │             │
│  │ 🟠 5│          │ 🔄 8 │          │     │             │
│  │ 🟡 8│          │ ⏳ 5 │          │     │             │
│  └─────┘          └─────┘          └─────┘             │
│                                                          │
│  Dernière mise à jour EBIOS : [Date]                   │
│  Prochaine révision : [Date]                           │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 5. GOUVERNANCE

### Comité de pilotage sécurité

| Élément | Description |
|---------|-------------|
| Fréquence | Trimestrielle |
| Participants | RSSI, MOA, Pilotes, Direction |
| Ordre du jour | Avancement EBIOS, incidents, ajustements |
| Livrable | Compte-rendu + indicateurs |

### Revue annuelle

| Élément | Description |
|---------|-------------|
| Fréquence | Annuelle |
| Participants | Direction, RSSI, MOA |
| Contenu | Bilan risques, validation feuille route, budget N+1 |
| Livrable | Présentation direction, feuille route validée |

---

## 6. TRIGGERS DE MISE À JOUR URGENTE

### Déclencheurs immédiats

- [ ] **Incident majeur** : Ransomware, fuite massive, indisponibilité critique
- [ ] **Nouvelle menace** : Vulnérabilité critique (Log4j, etc.)
- [ ] **Changement réglementaire** : Nouvelle loi, sanction importante
- [ ] **Changement stratégique** : Fusion, acquisition, cession

### Processus d'urgence

1. **Jour J** : Incident détecté
2. **J+1** : Réunion crise, évaluation impact
3. **J+7** : Analyse risque, identification écarts EBIOS
4. **J+30** : Mise à jour fiches concernées
5. **J+90** : Atelier de mise à jour complet si nécessaire

---

## 7. ARCHIVAGE DES VERSIONS

### Gestion des versions

| Version | Date | Nature | Archivage |
|---------|------|--------|-----------|
| V1.0 | [Date] | Version initiale | 5 ans |
| V1.1 | [Date] | Mise à jour ponctuelle | 5 ans |
| V2.0 | [Date] | Révision annuelle | 5 ans |

### Conservation

- **Dossier EBIOS courant** : Accessible, à jour
- **Versions archivées** : Stockage sécurisé, consultable
- **Durée légale** : 5 ans minimum

---

*Guide pour maintenir la pertinence de l'analyse EBIOS RM dans le temps*
