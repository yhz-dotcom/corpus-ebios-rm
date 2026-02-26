# Guide Atelier 2 - Sources de Risque

## Objectif
Identifier les sources de risque : acteurs du risque, cyberattaques et événements non-malveillants.

---

## 🎯 Livrables attendus

1. **Acteurs du risque** identifiés et caractérisés
2. **Scénarios de cyberattaques** (objectifs visés)
3. **Scénarios non-malveillants** (pannes, erreurs)

---

## ⏱️ Durée et participants

- **Durée** : 4 à 6 heures
- **Participants** :
  - RSSI / Responsable sécurité
  - Responsable technique (RSI/DSI)
  - Responsable métier
  - Responsable des opérations (exploitation)
  - RH (pour menaces internes)

---

## 📋 Déroulé de l'atelier

### Étape 1 : Rappel et introduction (20 min)

**Rappel Atelier 1** :
- Périmètre validé
- Biens essentiels (VM3 et VM4)
- Socle de sécurité

**Objectif Atelier 2** :
> "Qui ou quoi pourrait menacer nos biens essentiels ?"

---

### Étape 2 : Acteurs du risque (1h30)

**Objectif** : Identifier les attaquants potentiels et les menaces internes

**Méthode** : Brainstorming par catégories

#### Catégorie A : Attaquants externes

| Type | Description | Exemples |
|------|-------------|----------|
| **Cybercriminels** | Motivation financière | Ransomware, vol de données |
| **Hacktivistes** | Motivation idéologique | Défiguration, vol de données |
| **Étatiques** | Espionnage, sabotage | APT, infrastructure critique |
| **Concurrents** | Avantage économique | Espionnage industriel |
| **Script kiddies** | Opportunistes | Exploits automatisés |

**Questions pour identifier les acteurs** :
- Quelles sont les menaces sectorielles connues ?
- Avez-vous déjà été ciblés ?
- Quelles sont vos données les plus convoitées ?
- Qui pourrait vouloir vous nuire ?

#### Catégorie B : Menaces internes

| Type | Description | Exemples |
|------|-------------|----------|
| **Malveillant intentionnel** | Employé mécontent | Sabotage, vol de données |
| **Complice externe** | Corruption, extorsion | Aide à intrusion |
| **Negligence** | Erreur, manque de formation | Perte de données |
| **Détournement** | Usage non conforme | Fuites accidentelles |

**Questions** :
- Quels accès privilégiés existent ?
- Quel est le turnover ?
- Y a-t-il eu des tensions sociales ?

#### Fiche Acteur du Risque

Pour chaque acteur identifié :

| Champ | Description |
|-------|-------------|
| Nom | [Designation] |
| Description | [Qui c'est ?] |
| Motivation | [Pourquoi attaquer ?] |
| Capacités | [Quel niveau technique ?] |
| Opportunités | [Comment accéder ?] |
| Cibles privilégiées | [Quels biens viser ?] |

---

### Étape 3 : Scénarios de cyberattaques (2h)

**Objectif** : Identifier les tactiques d'attaque (inspiré MITRE ATT&CK)

**Méthode** : Pour chaque acteur, identifier les objectifs visés

#### Objectifs types d'attaques

| Objectif | Description | Exemples techniques |
|----------|-------------|---------------------|
| **Accès initial** | Pénétrer le SI | Phishing, exploit, compromission fournisseur |
| **Exécution** | Exécuter du code malveillant | Malware, script, commande à distance |
| **Persistance** | Maintenir l'accès | Backdoor, compte caché, tâche planifiée |
| **Élévation privilèges** | Avoir plus de droits | Exploit, credentials volés |
| **Déplacement latéral** | Se propager | Pass-the-hash, compromission compte |
| **Collecte** | Voler des données | Exfiltration, keylogger, screenshot |
| **Impact** | Perturber, détruire | Ransomware, destruction, modification |

**Exercice pratique** :
> "Si vous étiez un cybercriminel, comment attaqueriez-vous [système critique] ?"

#### Construction des scénarios

Format : **[Acteur] utilise [tactique] pour [objectif] sur [bien essentiel]**

Exemple :
> "Un cybercriminel utilise du phishing ciblé pour déployer un ransomware sur le système de production, exigeant une rançon pour déchiffrer les données."

---

### Étape 4 : Scénarios non-malveillants (1h)

**Objectif** : Identifier les risques sans intention malveillante

#### Types de scénarios non-malveillants

| Catégorie | Exemples | Source |
|-----------|----------|--------|
| **Pannes techniques** | Panne matérielle, bug logiciel | Infrastructure |
| **Erreurs humaines** | Mauvaise configuration, suppression | Exploitation, utilisateurs |
| **Catastrophes naturelles** | Incendie, inondation, tempête | Environnement |
| **Défaillances fournisseurs** | Indisponibilité service cloud | Tiers |
| **Surcharge** | Pic d'activité, saturation | Usage |

**Questions** :
- Quelles pannes avez-vous déjà eues ?
- Quels sont vos points de fragilité techniques ?
- Quels fournisseurs sont critiques ?
- Avez-vous un plan de continuité ?

---

### Étape 5 : Synthèse et validation (40 min)

**Activités** :
1. Revue de tous les scénarios identifiés
2. Élimination des doublons
3. Validation avec les participants
4. Préparation atelier 3 (évaluation de la gravité)

---

## 📝 Compte-rendu à produire

### Structure

```
1. ACTEURS DU RISQUE
   - Externes (cybercriminels, étatiques, hacktivistes...)
   - Internes (malveillants, négligents...)
   - Fiches détaillées par acteur

2. SCÉNARIOS DE CYBERATTAQUES
   - Par objectif d'attaque
   - Lien avec les biens essentiels

3. SCÉNARIOS NON-MALVEILLANTS
   - Pannes, erreurs, catastrophes
   - Défaillances fournisseurs

4. SYNTHÈSE
   - Matrice des sources de risque
   - Préparation atelier 3
```

---

## 💡 Astuces de facilitation

### Pour identifier les acteurs
- **Utiliser l'actualité** : "Vous avez vu l'attaque sur [secteur] ?"
- **Parler en termes de capacité** : pas de noms, mais de profils
- **Ne pas oublier l'interne** : souvent sous-estimé
- **Secteur critique** : si oui, ajouter les APT étatiques

### Pour les scénarios d'attaque
- **S'inspirer de MITRE ATT&CK** : tactiques réelles
- **Partir des biens essentiels** : "Comment voler [donnée critique] ?"
- **Varier les scénarios** : pas que du ransomware
- **Penser supply chain** : attaque via fournisseur

### Gérer les blocages
- Si "on n'est pas intéressant" : parler des ransomware opportunistes
- Si "tout est sécurisé" : rappeler l'erreur humaine
- Si silence : proposer des exemples du secteur

---

## ⚠️ Pièges classiques

| Piège | Solution |
|-------|----------|
| Trop focalisé sur ransomware | Forcer à penser autres attaques (espionnage, sabotage) |
| Oublier les menaces internes | Poser questions RH, accès privilégiés |
| Scénarios trop génériques | Demander : "Comment concrètement ?" |
| Paranoïa excessive | Rappeler : on cherche les risques réalistes |
| Manque de connaissance technique | Simplifier, utiliser des analogies |

---

## 🔗 Lien avec Atelier 3

Les scénarios identifiés serviront à construire les **risques cyber** :
> Source de risque + Objectif visé + Bien essentiel = Scénario de risque

---

*Guide pour Atelier 2 - Sources de Risque (EBIOS RM)*
