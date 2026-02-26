# Guide Atelier 3 - Scénarios de Risque

## Objectif
Construire les scénarios de risque complets et évaluer leur gravité (impact × vraisemblance).

---

## 🎯 Livrables attendus

1. **Scénarios de risque** complets (source + objectif + bien essentiel)
2. **Évaluation de la gravité** pour chaque scénario
3. **Cartographie des risques** (risques majeurs identifiés)

---

## ⏱️ Durée et participants

- **Durée** : 6 à 8 heures (atelier le plus long)
- **Participants** :
  - RSSI / Responsable sécurité
  - Responsable métier (pour évaluer l'impact)
  - Responsable technique (pour évaluer la vraisemblance)
  - Sponsor (validation des risques critiques)

---

## 📋 Déroulé de l'atelier

### Étape 1 : Rappel et construction des scénarios (1h30)

**Rappel** : Atelier 1 (biens) + Atelier 2 (sources) = Atelier 3 (risques)

**Construction d'un scénario de risque** :

```
[Source de risque] cherche à [objectif] sur [bien essentiel]
```

**Exemple** :
> "Un cybercriminel (source) cherche à chiffrer les données (objectif) sur le système de production (bien) pour exiger une rançon."

**Méthode** :
1. Prendre un bien essentiel (VM3 ou VM4)
2. Identifier les sources de risque qui pourraient le viser
3. Définir l'objectif d'attaque
4. Construire le scénario complet

---

### Étape 2 : Évaluation de l'impact (2h)

**Objectif** : Évaluer l'impact potentiel du scénario sur l'organisation

#### Échelle d'impact (1 à 4)

| Niveau | Description | Critères |
|--------|-------------|----------|
| **I4 - Catastrophique** | Arrêt d'activité, menace survie | > 10M€, régulateur saisi, média national |
| **I3 - Majeur** | Dégradation grave, impact durable | 1-10M€, clients impactés, sanction |
| **I2 - Significatif** | Dégradation notable, gérable | 100K-1M€, opérations perturbées |
| **I1 - Mineur** | Impact limité, rapidement géré | < 100K€, impact local |

#### Dimensions d'impact à évaluer

| Dimension | Questions |
|-----------|-----------|
| **Financier** | Coût direct (perte, rançon, amende) + indirect (opportunité, image) |
| **Opérationnel** | Arrêt de production ? Dégradation de service ? |
| **Réputation** | Impact image de marque ? Perte de confiance clients ? |
| **Réglementaire** | Sanctions ? Obligations de notification ? |
| **Humain** | Blessures ? Stress ? Départ de collaborateurs ? |
| **Environnemental** | Impact environnement ? (si applicable) |

**Règle** : L'impact retenu est le **maximum** des dimensions évaluées.

---

### Étape 3 : Évaluation de la vraisemblance (2h)

**Objectif** : Évaluer la probabilité que le scénario se réalise

#### Échelle de vraisemblance (1 à 4)

| Niveau | Description | Fréquence indicative |
|--------|-------------|---------------------|
| **V4 - Quasi-certain** | Survenue attendue | > 1 fois / an |
| **V3 - Probable** | Forte chance | 1 fois / 1-3 ans |
| **V2 - Possible** | Peut survenir | 1 fois / 3-10 ans |
| **V1 - Peu probable** | Survenue rare | < 1 fois / 10 ans |

#### Facteurs de vraisemblance

| Facteur | Éléments à considérer |
|---------|----------------------|
| **Menace** | Capacité de l'attaquant, motivation, ressources |
| **Vulnérabilité** | Failles connues, manque de patching, config faible |
| **Opportunité** | Accès possible, fenêtres d'attaque, exposition |
| **Cibles** | Valeur pour l'attaquant, facilité d'accès |

**Questions pour évaluer la vraisemblance** :
- Cette attaque arrive-t-elle dans notre secteur ?
- Avons-nous des vulnérabilités connues ?
- L'attaquant a-t-il les capacités nécessaires ?
- Existe-t-il des mesures qui réduisent déjà ce risque ?

---

### Étape 4 : Calcul de la gravité et matrice (1h30)

**Gravité = Impact × Vraisemblance**

#### Matrice de gravité

| Vraisemblance \ Impact | I1 Mineur | I2 Significatif | I3 Majeur | I4 Catastrophique |
|------------------------|-----------|-----------------|-----------|-------------------|
| **V4 Quasi-certain** | 4 | 8 | 12 | 16 |
| **V3 Probable** | 3 | 6 | 9 | 12 |
| **V2 Possible** | 2 | 4 | 6 | 8 |
| **V1 Peu probable** | 1 | 2 | 3 | 4 |

#### Niveaux de risque

| Score | Niveau | Couleur | Action |
|-------|--------|---------|--------|
| 12-16 | **Critique** | Rouge | Traitement prioritaire immédiat |
| 8-9 | **Élevé** | Orange | Traitement prioritaire |
| 4-6 | **Moyen** | Jaune | Traitement planifié |
| 1-3 | **Faible** | Vert | Surveillance, acceptation possible |

---

### Étape 5 : Validation et synthèse (1h)

**Activités** :
1. Revue des scénarios les plus critiques (rouge/orange)
2. Validation avec le sponsor
3. Identification des risques à traiter en priorité
4. Préparation atelier 4 (mesures de sécurité)

---

## 📝 Compte-rendu à produire

### Structure

```
1. SCÉNARIOS DE RISQUE
   - Liste complète des scénarios
   - Pour chaque : description, impact, vraisemblance, gravité

2. CARTOGRAPHIE DES RISQUES
   - Risques critiques (12-16)
   - Risques élevés (8-9)
   - Risques moyens (4-6)
   - Risques faibles (1-3)

3. SYNTHÈSE EXÉCUTIVE
   - Top 5 des risques les plus graves
   - Recommandations immédiates

4. ANNEXES
   - Fiches détaillées des scénarios
   - Justifications des évaluations
```

---

## 💡 Astuces de facilitation

### Pour évaluer l'impact
- **Quantifier quand possible** : "Combien ça coûte une heure d'arrêt ?"
- **Pire cas réaliste** : pas le scénario catastrophe impossible
- **Différencier les biens** : un VM4 aura forcément I3 ou I4
- **Valider avec le métier** : ils connaissent l'impact opérationnel

### Pour évaluer la vraisemblance
- **S'appuyer sur les stats** : "Dans votre secteur, X% ont subi ransomware"
- **Écarter le "jamais arrivé"** : absence de preuve ≠ preuve d'absence
- **Considérer le socle** : si mesures faibles, V augmente
- **Expertise technique** : le RSSI/RSI évalue les vulnérabilités

### Gérer les désaccords
- Si désaccord I vs V : séparer les évaluations (groupe métier vs technique)
- Si écart important : prendre le plus élevé (principe de précaution)
- Si blocage : argumenter avec des cas réels du secteur

---

## ⚠️ Pièges classiques

| Piège | Solution |
|-------|----------|
| Tous les risques en rouge | Forcer à prioriser : "Top 3 seulement" |
| Tous les risques en vert | Rappeler les attaques du secteur |
| Impact surestimé | Demander preuve chiffrée |
| Vraisemblance sous-estimée | "Ça arrive aux autres, pourquoi pas nous ?" |
| Désaccord persistant | Noter les deux évaluations, arbitrage sponsor |

---

## 🔗 Lien avec Atelier 4

Les risques **critiques (12-16)** et **élevés (8-9)** seront prioritaires pour le plan de traitement.

---

*Guide pour Atelier 3 - Scénarios de Risque (EBIOS RM)*
