# Cas Réel Anonymisé #1 — Recrutement Tech

**Secteur** : Technology / Software | **Taille** : 500 employés | **Région** : Europe

---

## Contexte

### Client
- Scale-up tech en forte croissance
- 50+ recrutements/an sur profils tech
- Process manuel : tri de 200+ CV/semaine par 2 recruteurs

### Problématique
- Temps de tri excessif (20h/semaine)
- Biais inconscients dans la présélection
- Manque de traçabilité des décisions

### Solution IA Proposée
- Qwen3.5 analyse les CV et propose liste courte
- Justifications structurées pour chaque recommandation
- Validation humaine systématique avant contact candidat

---

## Qualification EBIOS-RM

### Grille Express

| Q | Réponse | Justification |
|:-:|:--------|:--------------|
| 1 | Oui | Analyse CV (données métier RH) |
| 2 | Oui | Influence présélection |
| 3 | Non | Validation humaine systématique |
| 4 | Oui | Recrutement = Annexe III point 4(a) |
| 5 | Oui | Données personnelles (CV) |

### Niveau Déterminé

**🟡 Level 2** — Workflow avec exception Art. 6(3)

Justification :
- Annexe III applicable (recrutement)
- Mais validation humaine systématique et documentée
- Exception Art. 6(3) AI Act invoquée

---

## Fiche EBIOS-RM Level 2 (Extraits)

### Cadrage

**Points de Décision Délégués**
| Décision | IA ? | Supervision |
|:---------|:-----|:------------|
| Analyse CV | ✅ Oui | Échantillonnage qualité |
| Présélection | ✅ Oui | Validation systématique |
| Contact candidat | ❌ Non | Recruteur décide |
| Entretien | ❌ Non | Jamais délégué |

**Biens Essentiels**
- BE-001 : Qualité présélection (équité, pertinence)
- BE-002 : Données candidats (confidentialité)
- BE-003 : Réputation employeur (expérience candidat)

### Sources Risque

| Risque | Probabilité | Impact | Mitigation |
|:-------|:------------|:-------|:-----------|
| Biais genre/âge dans scoring | Moyenne | Élevé | Audit fairness trimestriel |
| Hallucination compétences | Moyenne | Moyen | Vérification croisée recruteur |
| Fuite données candidats | Faible | Critique | Chiffrement, accès restreint |

### Scénario Critique

```
Algorithme reproduit biais historiques (équipe tech masculine)
    │
    ▼
Sous-représentation femmes dans présélection
    │
    ▼
Discrimination systémique + sanction réglementaire
```

**Mesures**
- Dataset d'entraînement audité (répartition genre/âge)
- Métrique fairness : taux sélection femmes = taux candidatures
- Alertes si écart > 10%

### Conformité

**AI Act**
- Annexe III point 4(a) : Recrutement ✅
- Exception Art. 6(3) : Validation humaine systématique ✅
- Rôle : Deployer

**RGPD**
- AIPD réalisée (référence : AIPD-RH-2024-003)
- DPO consulté et validé ✅

---

## Résultats Après 6 Mois

| Métrique | Avant | Après | Évolution |
|:---------|:------|:------|:----------|
| Temps tri CV | 20h/semaine | 5h/semaine | -75% |
| Temps qualif candidat | 2 semaines | 3 jours | -85% |
| Satisfaction candidats | 6.5/10 | 8.2/10 | +26% |
| Diversité équipe tech | 12% femmes | 28% femmes | +133% |
| Incidents biais détectés | — | 2 (corrigés) | — |

---

## Apprentissages Clés

### Ce qui a marché
- Validation humaine systématique bien acceptée
- Métriques fairness visibles par l'équipe
- Audit régulier par Data Scientist externe

### Ce qui a été difficile
- Premier dataset biaisé (corrigé par rééquilibrage)
- Résistance initiale des recruteurs (levée par démonstration)
- Définition "systématique" de la validation (clarifiée)

### Recommandations pour cas similaires
1. Auditer le dataset AVANT le fine-tuning
2. Impliquer les recruteurs dès la conception
3. Métriques fairness en temps réel
4. Plan de rollback si biais persistant

---

## Fichiers Associés

| Document | Lien |
|:---------|:-----|
| Fiche complète | `cases/case-1-rh-full.md` |
| Template utilisé | `../../templates/template-level-2.md` |
| Entrée registre | `../../registry/examples/example-1-rh.yaml` |

---

*Cas Réel #1 — Recrutement Tech | Anonymisé | Usage avec permission*
