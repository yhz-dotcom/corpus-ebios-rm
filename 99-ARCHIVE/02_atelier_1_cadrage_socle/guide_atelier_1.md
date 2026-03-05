# Guide Atelier 1 - Cadrage et Socle de Sécurité

## Objectif
Définir le périmètre de l'étude, identifier les biens essentiels et évaluer le socle de sécurité existant.

---

## 🎯 Livrables attendus

1. **Périmètre de l'étude** (contexte, cartographie)
2. **Biens essentiels identifiés** avec leur valeur métier (VM)
3. **Socle de sécurité** (mesures existantes évaluées)

---

## ⏱️ Durée et participants

- **Durée** : 4 à 6 heures
- **Participants** :
  - Sponsor (idéalement)
  - RSSI / Responsable sécurité
  - Responsable métier (MOA)
  - Responsable technique (RSI/DSI)
  - Référent RGPD (si possible)

---

## 📋 Déroulé de l'atelier

### Étape 1 : Introduction (30 min)

**Objectif** : Mettre à l'aise, rappeler le contexte

**Activités** :
- Tour de table (prénom, fonction, attentes)
- Rappel de la méthode EBIOS RM (5 ateliers)
- Présentation des règles de l'atelier :
  - Tout le monde peut parler
  - Pas de jugement sur les idées
  - Confidentialité des échanges
  - Téléphones en mode silencieux

**Votre rôle** : Animateur, créer un climat de confiance

---

### Étape 2 : Cadrage et périmètre (1h)

**Objectif** : Définir précisément ce qui est dans le périmètre

**Questions à poser** :
1. **Quelle entité ?** (si groupe : quelle filiale ?)
2. **Quels sites ?** (liste exhaustive)
3. **Quels périmètres applicatifs ?** (SI interne, clients, partenaires)
4. **Quelles exclusions ?** (et pourquoi ?)

**Pièges à éviter** :
- ❌ Périmètre trop large (impossible à analyser)
- ❌ Périmètre trop étroit (oublier des risques)
- ❌ Exclusions non justifiées

**Livrable** : Fiche de cadrage complétée

---

### Étape 3 : Identification des biens essentiels (2h)

**Objectif** : Identifier ce qui est critique pour l'organisation

**Méthode** :
1. **Brainstorming** (post-its) :
   - "Que doit absolument fonctionner pour que l'activité continue ?"
   - "Quelles informations sont les plus sensibles ?"
   - "Quels systèmes, si indisponibles, bloquent tout ?"

2. **Catégorisation** (regrouper les post-its) :
   - Processus métier
   - Applications / Systèmes
   - Données / Informations
   - Infrastructures
   - Personnel compétent

3. **Évaluation de la Valeur Métier (VM)**

| Niveau VM | Description | Critères |
|-----------|-------------|----------|
| **VM4 - Vital** | Arrêt d'activité immédiat | Impact vital, réglementaire, réputation majeure |
| **VM3 - Important** | Dégradation majeure | Impact financier important, clientèle |
| **VM2 - Utile** | Dégradation notable | Impact opérationnel, efficacité |
| **VM1 - Secondaire** | Impact limité | Confort, non critique |

**Questions pour évaluer la VM** :
- Si ce bien est indisponible pendant 24h, quelle conséquence ?
- Est-ce réglementairement protégé ?
- Quel impact financier ?
- Quel impact réputation ?

**Pièges à éviter** :
- ❌ Tout mettre en VM4 (pas de priorisation)
- ❌ Se baser uniquement sur l'avis technique
- ❌ Oublier les biens immatériels (savoir-faire, image)

---

### Étape 4 : Évaluation du socle de sécurité (1h30)

**Objectif** : Évaluer les mesures de sécurité existantes

**Méthode** : Évaluation par famille de mesures (ISO 27002)

| Famille | Exemples de mesures | Évaluation |
|---------|---------------------|------------|
| **5. Gouvernance** | Politique, rôles, responsabilités | 0-4 |
| **6. Ressources humaines** | Recrutement, formation, départ | 0-4 |
| **7. Gestion des actifs** | Inventaire, classification | 0-4 |
| **8. Contrôles d'accès** | IAM, privilèges, authentification | 0-4 |
| **10. Cryptographie** | Chiffrement, gestion clés | 0-4 |
| **A.5** | Sécurité physique | 0-4 |
| **A.8** | Sécurité technique | 0-4 |

**Échelle d'évaluation** :
- **0** : Non existant
- **1** : Ad hoc (informel, irrégulier)
- **2** : En développement (planifié, partiel)
- **3** : Déployé (documenté, appliqué)
- **4** : Maîtrisé (mesuré, amélioré)

**Votre rôle** : Faciliter, ne pas juger, encourager l'honnêteté

---

### Étape 5 : Synthèse et prochaines étapes (30 min)

**Objectif** : Valider les résultats et préparer l'atelier 2

**Activités** :
1. Récapitulatif des biens essentiels (VM3 et VM4)
2. Synthèse du socle de sécurité (forces/faiblesses)
3. Validation par les participants
4. Présentation de l'atelier 2 (sources de risque)
5. Planification date et participants atelier 2

---

## 📝 Compte-rendu à produire

### Structure du CR Atelier 1

```
1. INTRODUCTION
   - Date, lieu, participants
   - Contexte de la mission

2. CADRAGE
   - Périmètre défini
   - Exclusions justifiées

3. BIENS ESSENTIELS
   - Liste complète avec VM
   - Justification des VM4 et VM3

4. SOCLE DE SÉCURITÉ
   - Synthèse par famille
   - Forces identifiées
   - Axes d'amélioration

5. ANNEXES
   - Fiches de biens essentiels
   - Grille d'évaluation du socle
```

---

## 💡 Astuces de facilitation

### Pour identifier les biens essentiels
- **Commencer par le métier** (pas la technique)
- **Poser la question autrement** : "Qu'est-ce qui vous empêcherait de travailler demain ?"
- **Utiliser des exemples** : "Par exemple, pour une banque, le système de paiement est vital"
- **Ne pas censurer** : tout mettre sur post-its, trier après

### Pour évaluer le socle
- **Être factuel** : "Avez-vous une politique de sécurité écrite ?"
- **Demander des preuves** : "Pouvez-vous montrer le document ?"
- **Noter les écarts** : ce qui est prévu vs ce qui est fait
- **Rester bienveillant** : objectif = améliorer, pas juger

### Gérer les tensions
- Si désaccord sur VM : demander l'impact concret (€, clients, régulateur)
- Si défensif sur le socle : rappeler que c'est pour progresser
- Si silence : relancer avec des questions fermées

---

## ⚠️ Pièges classiques

| Piège | Solution |
|-------|----------|
| Trop de biens en VM4 | Forcer à choisir : "Top 3 des plus critiques ?" |
| Aucun document formel | Noter les pratiques informelles existantes |
| Sponsor absent | Prendre RDV séparé pour valider les résultats |
| Désaccord MOA/IT | Faire voter, ou noter les deux positions |
| Manque de temps | Prioriser : biens essentiels d'abord, socle peut attendre |

---

## ✅ Checklist de fin d'atelier

- [ ] Tous les biens essentiels identifiés et classés
- [ ] Valeur métier validée par le groupe
- [ ] Socle de sécurité évalué
- [ ] Prochain atelier planifié (date, participants)
- [ ] Photos des tableaux prises
- [ ] CR à envoyer sous 48h

---

*Guide pour Atelier 1 - Cadrage et Socle de Sécurité (EBIOS RM)*
