# Cas Réel Anonymisé #2 — Scoring Crédit

**Secteur** : Banque / Finance | **Taille** : 2,000 employés | **Région** : Europe

---

## Contexte

### Client
- Banque régionale avec 200K clients
- Process crédit traditionnel : 5-7 jours, taux refus élevé
- Concurrence des néobanques (décision en 24h)

### Problématique
- Délai de décision trop long
- Biais inconscients des conseillers
- Non-conformité potentielle AI Act (Annexe III point 5)

### Solution IA Proposée
- Variante LoRA de Qwen3.5 pour scoring interne
- Analyse 150+ variables (revenus, historique, comportement)
- Décision automatique avec supervision sur alerte
- Temps cible : < 2 minutes

---

## Qualification EBIOS-RM

### Grille Express

| Q | Réponse | Justification |
|:-:|:--------|:--------------|
| 1 | Oui | Données financières métier |
| 2 | Oui | Décision crédit |
| 3 | Oui | Automatisé avec supervision alerte |
| 4 | Oui | Crédit = Annexe III point 5 |
| 5 | Oui | Données financières sensibles |

### Niveau Déterminé

**🔴 Level 3** — Décisionnel avec fine-tuning propriétaire

Justification :
- Annexe III applicable (accès services financiers essentiels)
- Fine-tuning substantiel (LoRA sur données internes)
- Rôle : Provider (for own use)
- Pas de marquage CE (usage strictement interne)

---

## Fiche EBIOS-RM Level 3 (Extraits)

### Cadrage Renforcé

**Points de Décision Délégués**
| Décision | IA ? | Supervision | Kill Switch |
|:---------|:-----|:------------|:------------|
| Scoring risque | ✅ Oui | Échantillonnage | ☐ |
| Décision approbation | ✅ Oui | Alertes seuil | ☑ Oui |
| Montant accordé | ✅ Oui | Plafond max | ☑ Oui |
| Taux d'intérêt | ✅ Oui | Fourchette | ☑ Oui |

**Biens Essentiels**
- BE-001 : Modèle scoring (IP critique)
- BE-002 : Données clients (RGPD + secret bancaire)
- BE-003 : Décisions automatisées (impact juridique)
- BE-004 : Réputation réglementaire (ACPR)
- BE-005 : Équité traitement (discrimination)

### Variante Technique (Module A)

```yaml
variante_technique:
  nom: "qwen3.5-lora-credit-v2.1"
  methode: "LoRA"
  
  parametres:
    rank: 32
    alpha: 64
    learning_rate: 0.00005
    
  donnees_entrainement:
    source: "Historique crédits 2019-2024"
    volume: 150000
    anonymisation: "K-anonymity k=5"
    
  evaluation:
    metriques:
      AUC-ROC: "0.87"
      Precision: "0.82"
      Recall: "0.79"
    tests_adversariaux: "15 attaques, 13 repoussées"
    
  reversibilite:
    possible: true
    procedure_rollback: "Activation modèle précédent"
    duree_max: "< 30 minutes"
```

### Sources Risque Étendues

| Risque | Probabilité | Impact | Mitigation |
|:-------|:------------|:-------|:-----------|
| Biais discriminant (genre, âge, zone) | Moyenne | Critique | Audit fairness trimestriel |
| Drift économique (crise, inflation) | Élevée | Élevé | Réentraînement semestriel |
| Extraction modèle (API) | Moyenne | Élevé | Rate limiting, watermarking |
| Fuite données training | Faible | Critique | Chiffrement, accès restreint |
| Contestation décision (non-explicable) | Élevée | Élevé | SHAP pour chaque décision |

### Scénario Critique : Drift Économique

```
Crise économique inattendue (ex: pandémie)
    │
    ▼
Modèle entraîné sur données "normales" obsolète
    │
    ▼
Taux d'approbation chute de 45% à 12%
    │
    ▼
Clients solvables refusés → Plaintes + Médias
    │
    ▼
Sanction ACPR + Perte réputation
```

**Mesures**
- Détection drift : comparaison mensuelle distributions
- Seuil alerte : variation > 15% taux approbation
- Procédure : réentraînement d'urgence + validation ACPR

### Conformité AI Act (Module B)

| Article | Exigence | Statut | Preuve |
|:--------|:---------|:-------|:-------|
| Art. 8 | Système qualité | ✅ | ISO 9001 étendu |
| Art. 9 | Documentation technique | ✅ | Dossier 150 pages |
| Art. 10 | Gestion risques | ✅ | EBIOS-RM complet |
| Art. 11 | Jeu de données | ✅ | Data sheet traçable |
| Art. 12 | Traçabilité | ✅ | Registre Article 60 |
| Art. 13 | Transparence | ✅ | Notice client |
| Art. 14 | Supervision humaine | ✅ | HITL sur alertes |
| Art. 15 | Exactitude, robustesse | ✅ | Tests adversariaux |

### Gouvernance Renforcée

```
                    ┌─────────────┐
                    │  Direction  │
                    │  Générale   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  Comité     │
                    │  Risques    │
                    │  (Mensuel)  │
                    └──────┬──────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   ┌────▼────┐      ┌─────▼─────┐     ┌─────▼─────┐
   │  AI     │      │   DPO     │     │  RSSI     │
   │ Officer │      │           │     │           │
   │(Métier) │      │(RGPD)     │     │(Securité) │
   └────┬────┘      └─────┬─────┘     └─────┬─────┘
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
                   ┌──────▼──────┐
                   │  Équipe ML  │
                   │  + Conformité│
                   └─────────────┘
```

---

## Résultats Après 12 Mois

| Métrique | Avant | Après | Évolution |
|:---------|:------|:------|:----------|
| Délai décision | 5-7 jours | 2 minutes | -99.9% |
| Taux approbation | 42% | 51% | +21% |
| Taux défaut | 3.2% | 2.8% | -12% |
| Satisfaction client | 6.8/10 | 8.5/10 | +25% |
| Coût traitement dossier | €45 | €8 | -82% |
| Audits fairness | — | 4/an | — |
| Incidents biais | — | 0 | — |

---

## Apprentissages Clés

### Ce qui a marché
- SHAP pour explicabilité (contestations -70%)
- Réentraînement semestriel (drift maîtrisé)
- Comité risques mensuel (gouvernance solide)
- Documentation ACPR proactive (pas de remarque)

### Ce qui a été difficile
- Premier dataset biaisé historique (corrigé par re-sampling)
- Acceptation conseillers (levée par démonstration gains)
- Définition "supervision appropriée" (négociation ACPR)

### Recommandations pour cas similaires
1. **Auditer le dataset avant** — biais historiques fréquents
2. **Impliquer régulateur tôt** — éviter surprises
3. **Métriques fairness en temps réel** — pas seulement audits
4. **Plan de rollback testé** — crise peut arriver
5. **Documentation traçable** — Article 60 AI Act

---

## Fichiers Associés

| Document | Lien |
|:---------|:-----|
| Fiche complète | `cases/case-2-finance-full.md` |
| Template utilisé | `../../templates/template-level-3.md` |
| Entrée registre | `../../registry/examples.yaml` (SIA-FIN-003) |
| Guide AI Act | `../../references/ai-act-deployer-provider.md` |

---

*Cas Réel #2 — Scoring Crédit | Anonymisé | Usage avec permission*
