# Guide de Formation : EBIOS RM "Spécial IA"

**Référence**: docs/GUIDE_FORMATION_EBIOS_IA.md  
**Version**: 1.0  
**Date**: 2026-03-02  
**Durée**: 2 jours

---

## 🎯 Objectifs de la Formation

À l'issue de cette formation, les auditeurs seront capables de :
1. Classifier un système IA selon l'AI Act dans le cadre EBIOS
2. Identifier les scénarios de risque spécifiques à l'IA
3. Intégrer les mesures AI Act dans le plan de traitement EBIOS
4. Produire un dossier de conformité combiné

---

## 📚 Programme

### Jour 1 : Fondamentaux

#### Matin (4h) : Contexte Réglementaire

**Module 1 : L'AI Act Décrypté (1h30)**
- Article 5 : Pratiques interdites
- Article 6 : Classification des risques
- Annexes I, III : Secteurs concernés
- Article 6(3) : Exemptions et pièges
- Article 50 : Obligations de transparence

**Module 2 : Intégration EBIOS ↔ AI Act (1h30)**
- Pourquoi enrichir EBIOS ?
- Mapping des 5 ateliers
- Nouveau dossier `09_integration_ai_act_iso42001/`
- Processus en 3 étapes

**Atelier Pratique (1h)**
- Classification de 3 systèmes :
  - Chatbot support client
  - Système de scoring crédit
  - Correcteur orthographique

#### Après-midi (4h) : Scénarios de Risque IA

**Module 3 : Menaces Spécifiques IA (2h)**

| Catégorie | Menace | Exemple |
|:----------|:-------|:--------|
| Intégrité | Concept drift | Modèle obsolète |
| Équité | Biais discriminatoire | Recrutement sexiste |
| Sécurité | Prompt injection | Jailbreak LLM |
| Confidentialité | Extraction données | Fuite training data |
| Gouvernance | Opacité | Boîte noire inexplicable |

**Module 4 : Les 8 Scénarios SR-IA (1h30)**
- SR-IA-01 : Dérive des performances
- SR-IA-02 : Données adversariales
- SR-IA-03 : Biais discriminatoire ⭐
- SR-IA-04 : Prompt injection ⭐
- SR-IA-05 : Extraction données
- SR-IA-06 : Manipulation scénarios
- SR-IA-07 : Opacité
- SR-IA-08 : Dépendance GPAI

⭐ Scénarios prioritaires pour haut risque

**Atelier Pratique (30min)**
- Sélection des scénarios pertinents pour un cas réel

---

### Jour 2 : Opérationnel

#### Matin (4h) : Mesures et Livrables

**Module 5 : Mesures de Traitement (2h)**

| Article AI Act | Mesure | Intégration EBIOS |
|:---------------|:-------|:------------------|
| Art. 10 | Gouvernance données | Atelier 4 |
| Art. 12 | Logs traçabilité | Atelier 4 |
| Art. 13 | Transparence | Atelier 4 |
| Art. 14 | Supervision humaine | Atelier 4 |
| Art. 15 | Robustesse | Atelier 4 |

**Module 6 : Documentation Annexe IV (1h30)**
- Structure des 12 points
- Articulation avec EBIOS
- Exemple : Point 4 (données) + Point 5 (risques)

**Atelier Pratique (30min)**
- Rédaction d'une section Annexe IV

#### Après-midi (4h) : Cas Pratique Complet

**Mission Simulation : Tri de CV (4h)**

| Phase | Durée | Activité |
|:------|:------|:---------|
| 1 | 30min | Classification AI Act |
| 2 | 45min | Atelier 1 EBIOS enrichi |
| 3 | 45min | Ateliers 2-3 (scénarios IA) |
| 4 | 45min | Atelier 4 (mesures) |
| 5 | 30min | Atelier 5 (feuille route) |
| 6 | 45min | Documentation Annexe IV |

**Restitution et Q/R (30min)**

---

## 📖 Ressources Pédagogiques

### Documents fournis
- [✅] `mapping_ebios_aiact.md` - Correspondance méthodologique
- [✅] `checklist_art6_ebios.md` - Checklist classification
- [✅] `template_scenario_ia.md` - 8 scénarios de référence
- [✅] `mesures_traitement_aiact.md` - Mesures par article
- [✅] `grille_evaluation_gravite_ia.md` - Évaluation impact
- [✅] `livrables_combines.md` - Structure dossier final

### Outils pratiques
- ai-act-audit-tool (classification + tests)
- Template EBIOS RM standard
- Exemple cas tri CV

---

## ✅ Évaluation des Acquis

### QCM (20 questions)

**Exemples** :
1. Un système de scoring crédit est-il concerné par l'Annexe III ?
2. Quelles sont les 4 conditions cumulatives de l'Article 6(3) ?
3. Quel scénario IA pour un biais de genre en recrutement ?
4. Quelle fréquence de ré-évaluation pour un haut risque ?

### Cas Pratique (2h)

Classifier et analyser un système IA fourni par le formateur.

### Seuil de réussite
- QCM : 14/20 minimum
- Cas pratique : Classification correcte + 3 scénarios pertinents

---

## 🎓 Certification

**Attestation de formation** délivrée par [Organisme]  
**Validité** : 2 ans  
**Renouvellement** : Module actualisation réglementaire (4h)

---

## 📞 Contact Formation

Pour organiser une session :  
📧 formation@ai-governance-ecosystem.ai

---

**Version**: 1.0  
**Dernière mise à jour**: 2026-03-02
