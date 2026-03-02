# 🎓 Guide de Formation : EBIOS RM Spécial IA pour Auditeurs

> Former les auditeurs à appliquer la méthode EBIOS RM aux systèmes d'IA, en intégrant les exigences spécifiques de l'AI Act et de l'ISO 42001.

👥 **Public cible** : Auditeurs internes/externes, RSSI, consultants risque  
⏱️ **Durée** : 2 jours (14 heures) + exercices pratiques  
🎯 **Objectif pédagogique** : À l'issue de la formation, l'auditeur doit être capable de :
- Classifier un système IA selon l'Article 6 AI Act dans le cadre d'un audit EBIOS
- Identifier et évaluer les menaces cyber spécifiques à l'IA
- Produire un rapport d'audit combiné EBIOS + documentation AI Act

---

## 📚 Programme Détaillé

### Jour 1 : Fondamentaux Réglementaires & Méthodologie

#### 🕘 Module 1 : Contexte Réglementaire IA (2h)

**Objectifs**
- Comprendre l'articulation AI Act / ISO 42001 / EBIOS RM
- Identifier les exigences spécifiques aux systèmes IA

**Contenu**

**1.1 L'AI Act en 10 points clés**
- Champ d'application territorial et matériel
- Les 4 niveaux de risque + interdits (Art. 5)
- Classification Article 6 : arbre de décision pratique
- Exemptions Article 6(3) : les 4 conditions cumulatives
- Obligations par rôle (provider / deployer / distributor)

**1.2 ISO 42001 : Le management système de l'IA**
- Structure HLS : intégration avec ISO 27001/9001
- Clause 8 : opérationnalisation des contrôles IA
- Statement of Applicability : adapter la grille aux risques IA

**1.3 Articulation avec EBIOS RM**

| Atelier EBIOS | Enrichissement IA | Livrable combiné |
|:--------------|:------------------|:-----------------|
| Atelier 1 : Cadrage | Classification Article 6 + intended purpose | Fiche workflow + socle sécurité IA |
| Atelier 2 : Sources | Menaces IA (biais, drift, injection) | Cartographie risques enrichie |
| Atelier 3 : Scénarios | Templates SR-IA-XX + critères gravité IA | Scénarios risque IA validés |
| Atelier 4 : Traitement | Mesures AI Act (transparence, supervision) | Plan traitement réglementaire |
| Atelier 5 : Feuille route | Surveillance Art. 72 + monitoring IA | Feuille route conformité |

**Exercice pratique (30 min)**
> Classifiez 3 workflows fictifs avec la `checklist_art6_ebios.md` :
> 1. Chatbot FAQ interne → Risque limité (Art. 50)
> 2. Scoring de crédit clients → Haut risque (Annexe III)
> 3. Assistant rédaction juridique → Minimal (support)

---

#### 🕐 Module 2 : Menaces Cyber Spécifiques à l'IA (3h)

**Objectifs**
- Identifier les vecteurs d'attaque propres aux systèmes IA
- Évaluer leur impact sur les biens essentiels

**Contenu**

**2.1 Typologie des menaces IA**

```
Menaces IA
├── Intégrité du modèle
│   ├── Concept drift
│   ├── Données adversariales
│   └── Poisoning d'entraînement
├── Équité et non-discrimination
│   ├── Biais algorithmique
│   └── Discrimination indirecte
├── Robustesse et sécurité
│   ├── Prompt injection
│   ├── Jailbreak par roleplay
│   └── Extraction de prompts
├── Confidentialité
│   ├── Inférence données training
│   └── Fuite via sorties
└── Gouvernance
    ├── Opacité des décisions
    └── Impossibilité de recours
```

**2.2 Grille d'évaluation de gravité enrichie**

| Critère | Question clé | Impact |
|:--------|:-------------|:-------|
| **Droits fondamentaux** | Impact sur accès emploi/crédit/justice ? | 🔴 Critique si OUI |
| **Profilage** | Création de profil pour décision ? | Maintient haut risque |
| **Supervision humaine** | Revue effective ou formelle ? | Réduit gravité si veto |
| **Explicabilité** | Peut-on expliquer la décision ? | Augmente gravité si opaque |
| **Réversibilité** | Erreur corrigeable a posteriori ? | Réduit gravité si oui |

**2.3 Cas pratique : Prompt injection**

**Contexte** : LLM utilisé pour le tri de CV (IA-RH-001)

**Scénario SR-IA-04** :
1. Un candidat insère des instructions cachées dans son CV
2. Le LLM applique ces consignes
3. Score artificiellement gonflé

**Évaluation EBIOS** :
- Source : Candidat malveillant
- Impact : Intégrité processus recrutement
- Gravité : 🟠 Élevée
- Vraisemblance : 🟡 Moyenne

**Mesures** :
- Technique : Filtrage regex + détection sémantique
- Organisationnel : Formation recruteurs
- Réglementaire : Documentation Annexe IV + tests Art. 15

**Exercice pratique (45 min)**
> Analysez le scénario SR-IA-03 (biais discriminatoire) pour un scoring de crédit.

---

#### 🕒 Module 3 : Atelier 1 & 3 EBIOS Appliqués à l'IA (3h)

**Objectifs**
- Appliquer concrètement les templates enrichis IA
- Valider la cohérence classification EBIOS ↔ AI Act

**Contenu**

**3.1 Atelier 1 : Cadrage avec classification AI Act**

**Checklist de validation croisée** :
```
1. L'intended purpose correspond-il à la finalité réelle ?
2. La classification Article 6 a-t-elle été faite avec la checklist complète ?
3. Si exemption Art. 6(3) : les 4 conditions sont-elles cumulatives ?
4. Le profilage a-t-il été correctement identifié ?
5. Les biens essentiels incluent-ils les droits fondamentaux ?
```

**3.2 Atelier 3 : Sélection et évaluation des scénarios IA**

**Méthode de priorisation** :
1. Lister tous les scénarios SR-IA-XX pertinents
2. Évaluer gravité avec la grille enrichie
3. Évaluer vraisemblance : expertise + exposition
4. Prioriser : 🔴 Critique + 🟠 Élevée vraisemblance
5. Documenter les scénarios écartés

**Piège à éviter** :
- ❌ Sous-estimer les scénarios "non techniques" (biais, opacité)
- ✅ Traiter équitablement risques cyber classiques ET risques IA

**3.3 Production du livrable combiné**

**Structure recommandée** :
```
Rapport d'Audit Combiné
├── 1. Synthèse exécutive
├── 2. Méthodologie
├── 3. Résultats détaillés
│   ├── 3.1 Classification et conformité
│   ├── 3.2 Analyse risques cyber EBIOS
│   └── 3.3 Mesures de traitement
├── 4. Conclusion et recommandations
└── Annexes
```

**Exercice pratique (60 min)**
> Produisez la section "Classification" et l'évaluation de 2 scénarios SR-IA.

---

### Jour 2 : Mise en Pratique & Validation

#### 🕘 Module 4 : Audit Technique avec l'AI Act Audit Tool (2h)

**Objectifs**
- Utiliser l'outil CLI pour valider la conformité technique
- Interpréter les résultats dans le cadre EBIOS

**Contenu**

**4.1 Prise en main de l'outil**

```bash
# Installation
pip install ai-act-audit

# Commandes essentielles
ai-act-audit classify --workflow IA-XXX
ai-act-audit logs --check-article-12
ai-act-audit jailbreak --vectors 3
ai-act-audit generate --artifact annex-iv
```

**4.2 Interprétation des résultats**

| Score | Interprétation | Action auditeur |
|:------|:---------------|:----------------|
| 90-100 | Conforme | Valider + documenter |
| 75-89 | Partiellement conforme | Écarts mineurs |
| 50-74 | Non conforme partiel | Action corrective prioritaire |
| < 50 | Non conforme critique | Suspension recommandée |

**4.3 Intégration dans le rapport EBIOS**

> "Les tests de robustesse ont révélé une vulnérabilité au vecteur 'roleplay_hypothetical' (score 88/100). Ce résultat alimente le scénario SR-IA-04 de l'Atelier 3 EBIOS, avec une vraisemblance réévaluée à 🟠 Élevée."

**Exercice pratique (45 min)**
> Exécutez l'audit tool sur un workflow de test et produisez un paragraphe de rapport.

---

#### 🕐 Module 5 : Production du Rapport Combiné (3h)

**Objectifs**
- Structurer un rapport d'audit professionnel
- Préparer la soutenance devant la direction / autorité de contrôle

**Contenu**

**5.1 Règles de rédaction pour auditeurs**

**Principes clés** :
- ✅ Fait vérifiable → Source documentée → Conclusion justifiée
- ✅ Distinguer constat de recommandation
- ✅ Hiérarchiser : critique / important / recommandé
- ✅ Anticiper les questions de l'autorité de contrôle

**Phrases types** :
```diff
- ❌ "Le système semble conforme"
+ ✅ "Sur la base des éléments examinés, le système satisfait aux exigences"

- ❌ "Il faudrait améliorer la documentation"
+ ✅ "La documentation ne contient pas l'architecture de mitigation des biais"
```

**5.2 Checklist de validation finale**

- [ ] Classification AI Act justifiée par l'arbre de décision
- [ ] Exemptions Article 6(3) avec 4 conditions cumulatives
- [ ] Scénarios IA couvrant les menaces spécifiques
- [ ] Gravité avec grille enrichie (droits fondamentaux prioritaires)
- [ ] Chaque mesure référence l'exigence AI Act
- [ ] Écarts hiérarchisés avec plan d'action daté
- [ ] Preuves techniques annexées et traçables
- [ ] Rapport compréhensible par un non-expert

**5.3 Préparation à la soutenance**

**Questions fréquentes** :

| Question | Réponse attendue |
|:---------|:-----------------|
| "Pourquoi pas haut risque ?" | Arbre de décision + exemption + absence profilage |
| "Comment garantir l'absence de discrimination ?" | Métriques + fréquence tests + mitigation + supervision |
| "Que se passe-t-il si dérive ?" | Monitoring + alerte + escalade + rollback |

**Exercice final (90 min)**
> Simulation d'audit complet : "Analyse de sentiment des feedbacks employés"
> Livrables : Classification + 2 scénarios + Synthèse + 3 réponses aux questions

---

#### 🕒 Module 6 : Clôture & Ressources (1h)

**Synthèse des bonnes pratiques**

```
Pré-audit → Classification AI Act → Sélection scénarios IA
    → Audit technique tool → Rapport combiné
    → Validation croisée → Recommandations actionnables
```

**Ressources post-formation**

- 📁 `checklist_art6_ebios.md`
- 📁 `template_scenario_ia.md`
- 📁 `grille_evaluation_gravite_ia.md`

**Veille réglementaire**

- 📬 Commission Européenne : AI Act updates
- 🔔 ANSSI EBIOS : RSS Feed
- 📚 ISO 42001 : ISO Store

**Certification**

✅ **Attestation** délivrée après validation de l'exercice final  
🔄 **Mise à jour annuelle** recommandée  
🎓 **Parcours avancé** : "Auditeur Lead IA" (3 jours supplémentaires)

---

## 📎 Annexes

### Annexe A : Glossaire

| Terme | Définition |
|:------|:-----------|
| **Intended purpose** | Finalité documentée du système, base classification Article 6 |
| **Profilage** | Traitement automatisé pour évaluer aspects personnels |
| **Supervision humaine** | Intervention effective avec pouvoir de veto |
| **Concept drift** | Dégradation performances due à évolution données |
| **Prompt injection** | Technique pour contourner consignes système |
| **Métrique d'équité** | Mesure quantitative absence biais (DIR, Equal Opportunity) |

### Annexe B : Template fiche d'entretien pré-audit

```
Fiche d'entretien - Système IA [ID]

Participants
- Responsable métier : ______
- Responsable technique : ______
- DPO / RSSI : ______
- Auditeur : ______

Questions clés
1. Quelle est la finalité exacte ? (intended purpose)
2. Décisions automatisées ? Niveau d'autonomie ?
3. Données personnelles traitées ? Lesquelles ?
4. Quel modèle ? (foundation / fine-tuned / from scratch)
5. Données d'entraînement : sélection et validation ?
6. Mécanismes de monitoring de performance / dérive ?
7. Qui est responsable en cas d'erreur ?
8. Comment contester une suggestion du système ?
9. Procédure de mise à jour du modèle ?

Documents à collecter
- [ ] Fiche workflow ISO 42001
- [ ] Documentation technique
- [ ] DPIA RGPD
- [ ] Logs d'exploitation
- [ ] Procédures supervision humaine
```

### Annexe C : Grille de maturité conformité IA

| Niveau | Description |
|:-------|:------------|
| **1 : Ad-hoc** | Classification non documentée, pas de monitoring, réaction aux incidents |
| **2 : Défini** | Classification justifiée, scénarios IA identifiés, supervision formalisée |
| **3 : Géré** | Documentation Annexe IV complète, monitoring continu, tests périodiques |
| **4 : Optimisé** | SMSI unifié, automatisation CI/CD, veille proactive, adaptation continue |

---

> 💡 **Conseil pédagogique** : Alternez théorie (30%) et pratique (70%). Les auditeurs retiennent mieux en faisant qu'en écoutant.

🔗 **Ressources complémentaires** :
- [`examples/cas_tri_cv_haut_risque/`](../examples/cas_tri_cv_haut_risque/)
- [`scripts/validation/`](../scripts/validation/)
- [`docs/RETEx-conformite-IA.md`](../docs/RETEx-conformite-IA.md)
