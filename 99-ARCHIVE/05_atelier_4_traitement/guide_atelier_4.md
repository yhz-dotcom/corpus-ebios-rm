# Guide Atelier 4 - Traitement du Risque

## Objectif
Définir les mesures de sécurité pour traiter les risques et évaluer le risque résiduel.

---

## 🎯 Livrables attendus

1. **Mesures de sécurité** identifiées pour chaque risque prioritaire
2. **Plan de traitement** des risques (feuille de route initiale)
3. **Risque résiduel** évalué après application des mesures

---

## ⏱️ Durée et participants

- **Durée** : 4 à 6 heures
- **Participants** :
  - RSSI / Responsable sécurité
  - Responsable technique (faisabilité technique)
  - Responsable financier (budget)
  - MOA (priorisation métier)
  - RH (si mesures organisationnelles)

---

## 📋 Déroulé de l'atelier

### Étape 1 : Rappel et priorisation (30 min)

**Rappel Atelier 3** :
- Liste des risques évalués
- Focus sur risques critiques (12-16) et élevés (8-9)

**Priorisation** : Sélectionner les risques à traiter (top 10-15)

---

### Étape 2 : Options de traitement (30 min)

**4 options pour traiter un risque** :

| Option | Description | Quand l'utiliser |
|--------|-------------|------------------|
| **Réduire** | Mettre en œuvre des mesures de sécurité | Cas général |
| **Éviter** | Ne pas réaliser l'activité à risque | Risque inacceptable |
| **Partager** | Transférer le risque (assurance, sous-traitance) | Coût réduction trop élevé |
| **Accepter** | Retenir le risque (avec justification) | Risque faible ou coût disproportionné |

---

### Étape 3 : Identification des mesures (2h30)

**Objectif** : Trouver les mesures adaptées pour réduire les risques

#### Sources de mesures

| Source | Description |
|--------|-------------|
| **ISO 27002:2022** | 93 mesures de sécurité organisées en 4 thèmes |
| **ANSSI** | Guides sectoriels, recommandations |
| **Socle de sécurité existant** | Renforcer les mesures déjà en place |
| **Bonnes pratiques** | Retour d'expérience, cas similaires |

#### Format d'une mesure

| Champ | Description |
|-------|-------------|
| Nom | [Intitulé clair] |
| Description | [Ce qu'il faut faire] |
| Objectif | [Quel risque traite-t-elle ?] |
| Mise en œuvre | [Comment la déployer ?] |
| Responsable | [Qui pilote ?] |
| Échéance | [Quand ?] |
| Budget | [Combien ?] |

#### Exemples de mesures par type de risque

**Risque : Ransomware**
- Sauvegardes régulières et testées
- Segmentation réseau
- EDR (Endpoint Detection and Response)
- Sensibilisation au phishing

**Risque : Fuite de données**
- DLP (Data Loss Prevention)
- Chiffrement des données
- Contrôles d'accès renforcés
- Audit logs

**Risque : Indisponibilité**
- Redondance infrastructure
- PCA/PRA
- Maintenance préventive
- Surveillance 24/7

---

### Étape 4 : Évaluation du risque résiduel (1h)

**Objectif** : Évaluer le risque après application des mesures

**Méthode** : Réévaluer la vraisemblance (l'impact reste identique)

| Mesures implémentées | Nouvelle vraisemblance | Explication |
|---------------------|------------------------|-------------|
| Aucune | V inchangée | - |
| Partielles | V - 1 | Réduction modérée |
| Complètes | V - 2 | Réduction significative |

**Exemple** :
- Risque initial : I3 × V3 = 9 (Élevé)
- Mesures : EDR + Sauvegardes + Sensibilisation
- Vraisemblance résiduelle : V1 (Peu probable)
- Risque résiduel : I3 × V1 = 3 (Faible) ✅

---

### Étape 5 : Plan de traitement (1h)

**Objectif** : Construire le plan d'action

#### Priorisation des mesures

| Critère | Pondération | Évaluation |
|---------|-------------|------------|
| Efficacité | 40% | Réduction de risque |
| Coût | 30% | Budget nécessaire |
| Facilité | 20% | Complexité de mise en œuvre |
| Délai | 10% | Temps de déploiement |

#### Classification des mesures

| Type | Description | Exemples |
|------|-------------|----------|
| **Quick win** | Rapide, peu coûteux, efficace | MFA, patchs, procédures |
| **Stratégique** | Important, investissement | SIEM, SOC, outils EDR |
| **Structurel** | Long terme, transformation | Formation, culture sécurité |
| **Différé** | Moins urgent, planifié | Remplacement matériel |

#### Feuille de route initiale

| Priorité | Mesure | Échéance | Budget | Responsable |
|----------|--------|----------|--------|-------------|
| P1 | [Mesure] | [Date] | [Montant] | [Nom] |
| P2 | [Mesure] | [Date] | [Montant] | [Nom] |

---

### Étape 6 : Synthèse (30 min)

**Activités** :
1. Revue des mesures identifiées
2. Validation du plan de traitement
3. Préparation atelier 5 (feuille de route détaillée)

---

## 📝 Compte-rendu à produire

### Structure

```
1. OPTIONS DE TRAITEMENT
   - Réduire, éviter, partager, accepter
   - Justification des choix

2. MESURES DE SÉCURITÉ
   - Liste des mesures par risque
   - Référence ISO 27002 ou autre
   - Description détaillée

3. RISQUE RÉSIDUEL
   - Évaluation avant/après
   - Risques acceptés (justification)

4. PLAN DE TRAITEMENT INITIAL
   - Mesures prioritaires
   - Échéances, budgets, responsables
```

---

## 💡 Astuces de facilitation

### Pour identifier les mesures
- **Commencer par les quick wins** : victoires rapides, crédibilité
- **S'inspirer du secteur** : "Les banques font ça..."
- **Benchmark** : "Vos concurrents ont déployé..."
- **Ne pas réinventer** : ISO 27002 a déjà listé les bonnes pratiques

### Pour évaluer le risque résiduel
- **Être honnête** : pas de "V1 partout" artificiel
- **Distinguer théorie/pratique** : mesure déployée ≠ mesure efficace
- **Considérer la maturité** : débutant vs expert

### Pour le plan de traitement
- **Budget réaliste** : demander une fourchette au CFO
- **Échéances réalisables** : tenir compte des ressources
- **Responsables nommés** : pas de "à définir"

---

## ⚠️ Pièges classiques

| Piège | Solution |
|-------|----------|
| Trop de mesures | Prioriser : Top 10 maximum par an |
| Mesures trop coûteuses | Proposer alternatives (organisational vs technique) |
| Oublier le facteur humain | Inclure formation, sensibilisation |
| Risque résiduel trop élevé | Ajouter mesures complémentaires |
| Plan irréaliste | Valider faisabilité avec RSSI/RSI |

---

## 🔗 Lien avec Atelier 5

Le plan de traitement sera détaillé et intégré dans la **feuille de route stratégique**.

---

*Guide pour Atelier 4 - Traitement du Risque (EBIOS RM)*
