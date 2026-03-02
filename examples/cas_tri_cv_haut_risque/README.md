# Cas d'Usage : Tri Automatique de CV (Haut Risque)

**Référence**: examples/cas_tri_cv_haut_risque/  
**Classification**: 🔴 Haut Risque (Annexe III.3 - Emploi)  
**Date**: 2026-03-02

---

## 🎯 Contexte

**Entreprise**: HR Tech Solutions (PME, 50 employés)  
**Système**: RecrutIA Pro - Système de présélection automatique de CV  
**Cas d'usage**: Analyse automatique des CV pour présélectionner les candidats

---

## 📋 Étape 1 : Classification AI Act

### Résultat Checklist Article 6

| Étape | Question | Réponse |
|:------|:---------|:--------|
| 1 | Article 5 (interdit) | ❌ Non |
| 2 | Annexe I (sécurité) | ❌ Non |
| 3 | Annexe III.3 (emploi) | ✅ **Oui** |
| 4 | Exemption Art 6(3) | ❌ Non applicable (profilage) |
| 5 | Article 50 | ❌ Non |

### Classification Finale

```
🔴 HAUT RISQUE
├── Annexe III point 3(a) : Recrutement/sélection
├── Exemption Art 6(3) : Non (profilage détecté)
└── Obligations : Régime complet AI Act
```

---

## 🔍 Étape 2 : Audit Technique

### Commandes exécutées

```bash
# Classification
ai-act-audit classify \
  --name "RecrutIA Pro" \
  --description "Tri automatique de CV" \
  --domain "RH" \
  --employment-related \
  --uses-personal-data \
  --automated-decision-making

# Résultat: HIGH_RISK

# Tests robustesse
ai-act-audit jailbreak --target http://recruita-api.local

# Résultat: 2/8 vecteurs réussis (roleplay, encoding)
```

### Vulnérabilités identifiées

| Vecteur | Sévérité | Statut |
|:--------|:---------|:-------|
| DAN Roleplay | 🔴 Critique | ❌ Vulnérable |
| Base64 Encoding | 🟠 Haute | ❌ Vulnérable |
| Prompt Injection | 🟡 Moyenne | ✅ Résistant |

---

## 🛡️ Étape 3 : Analyse EBIOS RM Enrichie

### Atelier 1 - Cadrage

**Périmètre** : Système de scoring CV + API interne  
**Biens essentiels** : Base CV, Algorithme de matching, Interface RH  
**Classification AI Act** : 🔴 Haut risque (intégrée au rapport)

### Atelier 2 - Sources de Menace

Sources classiques + Sources IA :
- Biais dans données training (historique de recrutement)
- Attaquants exploitant les failles du LLM
- Dérive des compétences recherchées

### Atelier 3 - Scénarios de Risque

#### Scénarios EBIOS classiques
- SR-001 : Fuite de la base CV
- SR-002 : Indisponibilité du service

#### Scénarios IA spécifiques (ce module)

**SR-IA-03 : Biais discriminatoire**
- Source : Données historiques biaisées (80% candidats masculins retenus)
- Impact : Discrimination systémique
- Gravité : 🔴 Critique (droits fondamentaux)
- Mesure : Tests équité trimestriels + revue humaine

**SR-IA-04 : Prompt injection**
- Source : Vulnérabilités détectées aux tests
- Impact : Contournement des critères de sélection
- Gravité : 🟠 Élevé
- Mesure : Filtrage entrée/sortie + tests mensuels

### Atelier 4 - Plan de Traitement

| Risque | Mesure EBIOS | Mesure AI Act | Priorité |
|:-------|:-------------|:--------------|:---------|
| Biais | Tests pénétration | M-10-03 (tests équité) | P1 |
| Injection | Pare-feu applicatif | M-15-04 (tests jailbreak) | P1 |
| Fuite données | Chiffrement | M-10-05 (anonymisation) | P2 |

### Atelier 5 - Feuille de Route

**Fréquence** : Trimestrielle (haut risque)  
**Indicateurs** :
- Taux de drift des prédictions
- Écart de sélection genre/âge
- Résultats tests jailbreak

---

## 📄 Étape 4 : Documentation Technique (Annexe IV)

### Structure produite

```
documentation-technique/
├── 01-informations-generales.md
├── 02-description-systeme.md
├── 03-elements-conception.md
├── 04-donnees-training.md
├── 05-mesures-risques.md
├── 06-modification-systeme.md
├── 07-systeme-qualite.md
├── 08-surveillance-post-marche.md
├── 09-informations-deployeur.md
├── 10-previsibilite.md
├── 11-logique-systeme.md
└── 12-cybersecurite.md
```

### Extrait - Section Biais (point 4)

```markdown
## 4.4 Analyse des Biais

### Biais détectés
- **Genre** : Sous-représentation femmes (DI = 0.82)
- **Âge** : Favorisation 25-40 ans (DI = 0.75)

### Mesures de mitigation
- Rééchantillonnage dataset
- Seuil décision ajusté par groupe
- Revue humaine obligatoire

### Résiduel accepté
- Écart toléré : 5% max
- Justification : [documentée]
```

---

## ✅ Livrables Finaux

### Dossier EBIOS RM Complet
- [✅] Atelier 1 : Cadrage + Classification AI Act
- [✅] Atelier 2 : Sources menace (classiques + IA)
- [✅] Atelier 3 : Scénarios (EBIOS + IA spécifiques)
- [✅] Atelier 4 : Plan traitement (mesures EBIOS + AI Act)
- [✅] Atelier 5 : Feuille route trimestrielle

### Documentation AI Act
- [✅] Classification Article 6
- [✅] Documentation technique Annexe IV
- [✅] Déclaration UE conformité
- [✅] Registre UE système

### Rapport Audit
- [✅] Classification automatique
- [✅] Tests jailbreak
- [✅] Recommandations correctives

---

## 📊 Synthèse

| Aspect | Avant | Après |
|:-------|:------|:------|
| Conformité AI Act | ❌ Non évaluée | ✅ Haut risque documenté |
| Tests sécurité | ❌ Aucun | ✅ 8 vecteurs testés |
| Gestion biais | ❌ Informelle | ✅ Processus trimestriel |
| Documentation | ❌ Partielle | ✅ Annexe IV complète |

---

**Temps total mission** : 5 jours  
**Coût** : 15K€ (consultant + outils)  
**Prochaine revue** : T1 2026

---

*Exemple complet généré avec l'écosystème AI Governance*
