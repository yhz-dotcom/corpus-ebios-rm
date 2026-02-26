# Plan Détaillé - Pense-bête de l'Auditeur EBIOS RM

## Objectif
Créer un guide complet pour accompagner un auditeur dans la réalisation d'une analyse des risques EBIOS RM avec un client, de la préparation à la livraison.

---

## Structure du Pense-bête

### PARTIE 1 : PRÉPARATION (Avant les ateliers)

#### 1.1 Checklist de préparation
- [ ] Vérification du périmètre avec le client
- [ ] Identification des parties prenantes (MOA, RSSI, métier, technique)
- [ ] Planification des 5 ateliers (dates, durées, participants)
- [ ] Préparation des supports (templates, outils, accès salle)
- [ ] Revue des documents existants (politique sécurité, architecture, audits précédents)

#### 1.2 Documents à demander au client
- Organigramme et organigramme de sécurité
- Périmètre technique (schémas réseau, inventaire)
- Registre des traitements RGPD
- Rapports d'audit précédents
- PCA/PRA existants
- Cartographie des flux

#### 1.3 Outils à préparer
- Fichier EBIOS RM (fichier .ebios ou équivalent)
- Tableur pour le suivi
- Outil de visio avec tableau blanc (Miro, Mural, ou physique)
- Template de compte-rendu

---

### PARTIE 2 : LES 5 ATELIERS EBIOS RM

#### ATELIER 1 - Cadrage et Socle de Sécurité

**Objectif** : Définir le périmètre, les biens essentiels et le socle de sécurité existant

**Livrables** :
- Périmètre de l'étude (contexte, cartographie)
- Biens essentiels identifiés et évalués (valeur métier)
- Socle de sécurité (mesures existantes)

**Pense-bête pour l'auditeur** :
- Questions à poser pour identifier les biens essentiels
- Grille d'évaluation de la valeur métier (VM)
- Checklist du socle de sécurité (ISO 27002, ANSSI)
- Pièges à éviter (périmètre trop large/trop étroit)
- Comment faciliter l'atelier (icebreaker, prise de parole)

---

#### ATELIER 2 - Sources de Risque

**Objectif** : Identifier les sources de risque (acteurs, cyberattaques, non-malveillant)

**Livrables** :
- Acteurs du risque (attaquants, menaces internes)
- Scénarios de cyberattaques (ANSSI, MITRE ATT&CK)
- Scénarios non-malveillants (pannes, erreurs)

**Pense-bête pour l'auditeur** :
- Liste des sources de risque courantes par secteur
- Mapping avec MITRE ATT&CK
- Comment éviter les biais (trop technique, trop générique)
- Techniques de facilitation (brainstorming, post-its)

---

#### ATELIER 3 - Scénarios de Risque

**Objectif** : Construire les scénarios de risque et évaluer leur gravité

**Livrables** :
- Scénarios de risque (source de risque → objectif visé → biens essentiels)
- Évaluation de la gravité (impact × vraisemblance)
- Cartographie des risques

**Pense-bête pour l'auditeur** :
- Méthode d'évaluation de l'impact (échelle 1-4)
- Méthode d'évaluation de la vraisemblance (échelle 1-4)
- Matrice de gravité (risques majeurs, critiques)
- Comment gérer les désaccords sur les évaluations
- Validation des scénarios avec le client

---

#### ATELIER 4 - Traitement du Risque

**Objectif** : Définir les mesures de traitement et calculer le risque résiduel

**Livrables** :
- Mesures de sécurité recommandées
- Plan de traitement des risques
- Risque résiduel évalué

**Pense-bête pour l'auditeur** :
- Référentiels de mesures (ISO 27002, ANSSI, guides sectoriels)
- Priorisation des mesures (quick wins, stratégiques)
- Estimation des coûts et délais
- Acceptation des risques résiduels (décision métier)

---

#### ATELIER 5 - Feuille de Route

**Objectif** : Construire la feuille de route et finaliser le dossier

**Livrables** :
- Feuille de route (plan d'action)
- Synthèse pour la direction
- Dossier EBIOS RM complet

**Pense-bête pour l'auditeur** :
- Construction de la roadmap (court/moyen/long terme)
- Indicateurs de suivi (KPI sécurité)
- Présentation aux décideurs (synthèse exécutive)
- Gouvernance de suivi (qui fait quoi, quand)

---

### PARTIE 3 : OUTILS ET TEMPLATES

#### 3.1 Templates pour chaque atelier
- Template de compte-rendu d'atelier
- Grille d'évaluation EBIOS RM
- Fiche de scénario de risque
- Fiche de mesure de sécurité
- Template de feuille de route

#### 3.2 Outils de facilitation
- Checklist de l'animateur (début, pendant, fin d'atelier)
- Techniques de gestion des conflits
- Comment gérer les participants difficiles
- Comment maintenir l'énergie du groupe

#### 3.3 Outils de documentation
- Structure du dossier EBIOS RM
- Liste des annexes obligatoires
- Format de la synthèse direction

---

### PARTIE 4 : LIVRAISON ET SUIVI

#### 4.1 Livrables finaux
- Dossier EBIOS RM complet (5 ateliers + synthèse)
- Feuille de route détaillée
- Présentation direction
- Annexes techniques

#### 4.2 Suivi post-mission
- Revue annuelle des risques
- Mise à jour sur événement
- Indicateurs de performance

---

## Plan de Production

### Phase 1 : Structure (1 commit)
- Créer l'arborescence des dossiers
- README général

### Phase 2 : Partie 1 - Préparation (1 commit)
- Checklist de préparation
- Liste des documents à demander
- Outils indispensables

### Phase 3 : Partie 2 - Les 5 ateliers (5 commits ou 1 commit)
- Atelier 1 : Cadrage et socle
- Atelier 2 : Sources de risque
- Atelier 3 : Scénarios de risque
- Atelier 4 : Traitement
- Atelier 5 : Feuille de route

### Phase 4 : Partie 3 - Outils et templates (1 commit)
- Templates pour chaque atelier
- Outils de facilitation
- Outils de documentation

### Phase 5 : Partie 4 - Livraison et suivi (1 commit)
- Checklist des livrables
- Guide de suivi

### Phase 6 : Finalisation (1 commit)
- Revue complète
- Liens entre documents
- Index et navigation

---

## Estimation

- **Nombre de fichiers** : ~15-20 documents
- **Temps de production** : 1-2 heures
- **Nombre de commits** : 6-8 commits

---

Valide ce plan ou veux-tu des modifications avant que je commence la production ?