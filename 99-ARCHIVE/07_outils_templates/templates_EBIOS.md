# Outils et Templates pour EBIOS RM

## Collection de templates prêts à l'emploi

---

## 1. TEMPLATES PAR ATELIER

### Atelier 1 - Fiche Bien Essentiel

```markdown
# FICHE BIEN ESSENTIEL

## Identification
| Champ | Valeur |
|-------|--------|
| ID | BE-XXX |
| Nom | [Nom du bien] |
| Catégorie | [Processus / Application / Donnée / Infrastructure / Personnel] |
| Description | [Description détaillée] |

## Valeur Métier
| Critère | Évaluation | Justification |
|---------|------------|---------------|
| Impact financier | [€ / heure d'indisponibilité] | [Justification] |
| Impact réglementaire | [Oui/Non - Préciser] | [Justification] |
| Impact réputation | [Critique/Majeur/Mineur] | [Justification] |
| Impact opérationnel | [Description] | [Justification] |

**Valeur Métier retenue** : VM [1/2/3/4]

## Responsable
| Rôle | Nom | Contact |
|------|-----|---------|
| Owner | [Nom] | [Contact] |
| RSSI | [Nom] | [Contact] |

## Commentaires
[Notes complémentaires]
```

---

### Atelier 2 - Fiche Acteur du Risque

```markdown
# FICHE ACTEUR DU RISQUE

## Identification
| Champ | Valeur |
|-------|--------|
| ID | AR-XXX |
| Nom | [Nom de l'acteur] |
| Type | [Externe / Interne] |
| Catégorie | [Cybercriminel / Étatique / Hacktiviste / Interne malveillant / Interne négligent] |

## Caractérisation
| Élément | Description |
|---------|-------------|
| Description | [Qui est cet acteur ?] |
| Motivation | [Pourquoi attaquer ?] |
| Capacités | [Niveau technique, ressources] |
| Opportunités | [Comment accéder au SI ?] |

## Objectifs visés
| Objectif | Description | Cibles privilégiées |
|----------|-------------|---------------------|
| [Objectif 1] | [Description] | [Biens visés] |
| [Objectif 2] | [Description] | [Biens visés] |

## Scénarios associés
- [Référence scénario 1]
- [Référence scénario 2]
```

---

### Atelier 3 - Fiche Scénario de Risque

```markdown
# FICHE SCÉNARIO DE RISQUE

## Identification
| Champ | Valeur |
|-------|--------|
| ID | SR-XXX |
| Nom | [Nom du scénario] |

## Construction
| Élément | Description |
|---------|-------------|
| Source de risque | [Référence acteur] |
| Objectif visé | [Ce qu'il cherche à faire] |
| Bien essentiel visé | [Référence bien] |

**Scénario complet** :
> [Source] cherche à [objectif] sur [bien essentiel] en utilisant [modus operandi]

## Évaluation de l'impact
| Dimension | Niveau | Justification |
|-----------|--------|---------------|
| Financier | [1-4] | [Justification] |
| Opérationnel | [1-4] | [Justification] |
| Réputation | [1-4] | [Justification] |
| Réglementaire | [1-4] | [Justification] |
| **Impact maximum** | **I[1-4]** | |

## Évaluation de la vraisemblance
| Facteur | Évaluation | Justification |
|---------|------------|---------------|
| Menace | [Faible/Moyenne/Élevée] | [Justification] |
| Vulnérabilité | [Faible/Moyenne/Élevée] | [Justification] |
| Opportunité | [Faible/Moyenne/Élevée] | [Justification] |
| **Vraisemblance** | **V[1-4]** | |

## Gravité
| Calcul | Valeur |
|--------|--------|
| Impact × Vraisemblance | I[X] × V[Y] = **[Score]** |
| Niveau | [Critique/Élevé/Moyen/Faible] |

## Mesures de traitement
- [Référence mesure 1]
- [Référence mesure 2]
```

---

### Atelier 4 - Fiche Mesure de Sécurité

```markdown
# FICHE MESURE DE SÉCURITÉ

## Identification
| Champ | Valeur |
|-------|--------|
| ID | MS-XXX |
| Nom | [Nom de la mesure] |
| Référence | [ISO 27002 / ANSSI / Autre] |

## Description
| Élément | Description |
|---------|-------------|
| Description | [Ce qu'il faut faire] |
| Objectif | [Quel risque traite-t-elle ?] |
| Bénéfice attendu | [Réduction de risque] |

## Mise en œuvre
| Élément | Description |
|---------|-------------|
| Mise en œuvre | [Comment déployer ?] |
| Prérequis | [Dépendances] |
| Complexité | [Faible/Moyenne/Élevée] |

## Planning et budget
| Élément | Valeur |
|---------|--------|
| Horizon | [Court/Moyen/Long terme] |
| Date début | [Date] |
| Date fin | [Date] |
| Budget | [Montant] |

## Responsabilités
| Rôle | Nom |
|------|-----|
| Pilote | [Nom] |
| Contributeurs | [Noms] |

## Suivi
| Indicateur | Cible |
|------------|-------|
| [KPI] | [Cible] |
```

---

### Atelier 5 - Template Feuille de Route

```markdown
# FEUILLE DE ROUTE SÉCURITÉ

## Informations générales
| Élément | Valeur |
|---------|--------|
| Organisation | [Nom] |
| Date de création | [Date] |
| Période couverte | [Date début] - [Date fin] |
| Responsable | [Nom] |
| Version | [Numéro] |

## Actions planifiées

### Court terme (0-6 mois)
| ID | Action | Début | Fin | Budget | Resp. | Statut |
|----|--------|-------|-----|--------|-------|--------|
| FR-001 | [Action] | [Date] | [Date] | [€] | [Nom] | [Statut] |

### Moyen terme (6-18 mois)
| ID | Action | Début | Fin | Budget | Resp. | Statut |
|----|--------|-------|-----|--------|-------|--------|
| FR-010 | [Action] | [Date] | [Date] | [€] | [Nom] | [Statut] |

### Long terme (18-36 mois)
| ID | Action | Début | Fin | Budget | Resp. | Statut |
|----|--------|-------|-----|--------|-------|--------|
| FR-020 | [Action] | [Date] | [Date] | [€] | [Nom] | [Statut] |

## Budget global
| Horizon | Budget prévu | Budget engagé | Écart |
|---------|--------------|---------------|-------|
| Court | [€] | [€] | [€] |
| Moyen | [€] | [€] | [€] |
| Long | [€] | [€] | [€] |
| **Total** | **[€]** | **[€]** | **[€]** |

## Gouvernance
| Élément | Description |
|---------|-------------|
| Comité de pilotage | [Fréquence, participants] |
| Revue annuelle | [Date prévue] |
| Déclencheur mise à jour | [Incidents, changements majeurs] |
```

---

## 2. GRILLES D'ÉVALUATION

### Grille d'évaluation de la Valeur Métier

| Critère | VM1 Mineur | VM2 Utile | VM3 Important | VM4 Vital |
|---------|------------|-----------|---------------|-----------|
| **Impact financier** | < 100K€ | 100K-1M€ | 1-10M€ | > 10M€ |
| **Impact opérationnel** | Dégradation légère | Perturbation notable | Arrêt partiel | Arrêt total |
| **Impact réputation** | Aucun | Rumeur locale | Média national | Crise majeure |
| **Impact réglementaire** | Aucun | Observation | Mise en demeure | Sanction, condamnation |

### Grille d'évaluation de l'Impact

| Niveau | Description | Exemples |
|--------|-------------|----------|
| **I4** | Catastrophique | Arrêt activité, menace survie, sanction régulateur |
| **I3** | Majeur | Dégradation grave, impact durable, clients impactés |
| **I2** | Significatif | Dégradation notable, gérable avec effort |
| **I1** | Mineur | Impact limité, rapidement géré |

### Grille d'évaluation de la Vraisemblance

| Niveau | Description | Fréquence |
|--------|-------------|-----------|
| **V4** | Quasi-certain | > 1 fois / an |
| **V3** | Probable | 1 fois / 1-3 ans |
| **V2** | Possible | 1 fois / 3-10 ans |
| **V1** | Peu probable | < 1 fois / 10 ans |

### Matrice de Gravité

| V \ I | I1 | I2 | I3 | I4 |
|-------|----|----|----|----|
| **V4** | 4 | 8 | 12 | 16 |
| **V3** | 3 | 6 | 9 | 12 |
| **V2** | 2 | 4 | 6 | 8 |
| **V1** | 1 | 2 | 3 | 4 |

**Légende** :
- 🟢 1-3 : Faible
- 🟡 4-6 : Moyen
- 🟠 8-9 : Élevé
- 🔴 12-16 : Critique

---

*Templates à adapter selon le contexte de l'organisation*
