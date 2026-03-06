# Executive Summary — Analyse EBIOS-RM IA

**Projet** : VitalPredict Triage Hospitalier | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — Board + Conseil Médical

---

## 🎯 Contexte & Enjeux en 3 Phrases

VitalPredict (120 salariés, 18M€ CA) déploie un système IA de triage aux urgences traitant **1,200 patients/jour**. L'équipe classe le système "limited risk" — **erreur critique** : santé publique = AI Act **Haut Risque** + possible **interdiction Article 5**. Un faux négatif mortel a déjà eu lieu (nov. 2025), le dataset est biaisé (sous-représentation +80 ans/ruraux), et la dépendance API Mistral a causé une panne de 2h en janvier 2026.

**Enjeu** : Sans action immédiate, retrait marché HAS, décès en série, faillite.

---

## 📊 Matrice Top 5 Risques

| Rang | Risque | Gravité | Vraisemblance | Niveau |
|:---:|:---|:---:|:---:|:---:|
| **1** | Faux négatif mortel en série (biais dataset) | ⚫ 4/4 | 🔴 3/4 | **⚫ CATASTROPHIQUE** |
| **2** | Retrait marché HAS/ANSM (classification erronée) | ⚫ 4/4 | 🔴 3/4 | **⚫ CATASTROPHIQUE** |
| **3** | Fuite 450k dossiers médicaux | ⚫ 4/4 | 🟡 2/4 | **🔴 CRITIQUE** |
| 4 | Panne système aux urgences (>30 min) | 🔴 3/4 | 🔴 3/4 | 🔴 CRITIQUE |
| 5 | Discrimination systémique (ruraux, +80 ans) | ⚫ 4/4 | 🔴 3/4 | ⚫ CATASTROPHIQUE |

**Risque Global Brut** : ⚫ **CATASTROPHIQUE** (sans mesures = faillite assurée)

---

## ✅ Top 3 Actions IMMÉDIATES (0-7 jours)

| Priorité | Action | Budget | Impact Risque |
|:---|:---|---:|:---|
| ⚫🥇 | **SUSPENDRE déploiement** nouveaux hôpitaux | 0€ | ↓ Morts évitables |
| ⚫🥈 | **AUDIT EXTERNE URGENT** incident nov. 2025 | 50k€ | ↓ Risque répétition |
| ⚫🥉 | **CORRIGER DATASET** biais âge/géographie | 30k€ | ↓ Discrimination |

**Investissement immédiat** : **80k€** + report Série C

---

## 📈 Trajectoire Risque Résiduel

```
Risque Global
    │
    ▼
⚫ CATASTROPHIQUE (aujourd'hui)
    │
    ├──► 🔴 CRITIQUE (après mesures P0 — 7j)
    │      • Suspension déploiement ✓
    │      • Audit externe lancé ✓
    │      • Dataset correction démarrée ✓
    │
    └──► 🟡 MAJEUR (après 3 mois)
           • MDR certification ✓
           • Re-architecture on-premise ✓
           • DPO temps plein ✓
              │
              └──► 🟢 ACCEPTABLE (après 12 mois)
                     • ISO 42001/27001/HDS ✓
                     • Dataset équilibré national ✓
                     • Validation clinique prospective ✓
```

| Horizon | Risque | Condition |
|:---|:---|:---|
| **J+7** | 🔴 **Critique** | Suspension effective + audit lancé |
| **M+3** | 🟡 **Majeur** | Budget 800k€ débloqué, MDR engagée |
| **M+12** | 🟢 **Acceptable** | 2,95M€ investis, certifications obtenues |

---

## 💰 Investissement Recommandé

| Période | Budget | % CA | Livrable Clé |
|:---|---:|---:|:---|
| Immédiat (7j) | 150k€ | 0,8% | Suspension, audit, corrections |
| Court terme (3m) | 800k€ | 4,4% | MDR, re-architecture, DPO temps plein |
| Moyen terme (12m) | 2M€ | 11% | ISO 42001/27001/HDS, dataset national |
| **Total 12 mois** | **2,95M€** | **16,4%** | Risque acceptable, Série C possible |

**Impact Série C** : Report juin 2026 → décembre 2026 (ou valuation -30%)

**Alternative** : 0€ → Retrait marché d'ici 6 mois, faillite

---

## 🎲 Scénarios Futurs

| Scénario | Probabilité | Issue | Déclencheur |
|:---|:---:|:---|:---|
| **🟢 Succès** | 60% | Leader IA santé EU, Série C 50M€+ | Exécution rigoureuse, transparence |
| **🟡 Survie** | 25% | Niche régionale, rachat Big Pharma | Retards partiels, concurrents rapides |
| **🔴 Faillite** | 15% | Liquidation judiciaire, poursuites | Inaction, nouveau décès, scandale |

---

## 📋 Décision Requise AUJOURD'HUI

**Avant 18h** :
- [ ] **SUSPENDRE** tout déploiement nouvel hôpital
- [ ] Accepter **report Série C** (déc 2026)
- [ ] Débloquer **budget 2,95M€** sur 12 mois
- [ ] Nommer **DPO temps plein** (recrutement immédiat)

**Cette semaine** :
- [ ] Lancer **audit HAS externe** incident nov. 2025
- [ ] Commencer **correction dataset** biais
- [ ] Engager **certification MDR** dispositif médical

---

## ⚠️ Si Aucune Décision Aujourd'hui

| Délai | Conséquence |
|:---|:---|
| J+7 | Nouvel incident probable, alerte HAS |
| M+1 | Médias "IA dangereuse", perte 1er client CHU |
| M+3 | Retrait marché ANSM, impossibilité Série C |
| M+6 | Faillite, poursuites pénales dirigeants |

---

## 📞 Contact

**Analyste** : [Nom consultant EBIOS-RM IA Santé]  
**Rapport complet** : `ebios-analysis-vitalpredict.md` (400+ lignes, 12,456 bytes)  
**Urgence** : 🔴 **CRITIQUE — Réponse requise sous 24h**

---

*Executive Summary — VitalPredict | Pour Board et Investisseurs Série B | 1 page | URGENT*
