# Executive Summary — Analyse EBIOS-RM IA

**Projet** : CareCoord AI / Santé Hospitalière | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL — ANSSI + HAS

---

## 🎯 Contexte & Enjeux en 3 Phrases

MedFlow Solutions (380 salariés, 145M€ CA) déploie CareCoord AI : prédiction admissions + optimisation plannings + **priorisation lits/bloc**. Classé "limited risk" (logistique) — **REJETÉ** : 🔴 **HIGH-RISK** (Annexe III point 5 — accès soins) / ⚠️ **MDR**. **Incident 1** : **discrimination âge** — priorisation lits réanimation **< 65 ans** = reports soins personnes âgées. **Incident 2** : **ransomware** — modèles chiffrés, **72h** retour manuel, retards prise en charge.

---

## 📊 Matrice Top 5 Risques

| Rang | Risque | Gravité | Vraisemblance | Niveau |
|:---:|:---|:---:|:---:|:---:|
| **1** | Discrimination âge/comorbidités | ⚫ 4/4 | 🔴 3/4 | **⚫ CATASTROPHIQUE** |
| **2** | Ransomware systémique | ⚫ 4/4 | 🔴 3/4 | **⚫ CATASTROPHIQUE** |
| **3** | Inégalités accès soins | ⚫ 4/4 | 🔴 3/4 | **⚫ CATASTROPHIQUE** |
| 4 | Perte subvention Horizon Europe | 🔴 3/4 | 🔴 3/4 | 🔴 CRITIQUE |
| 5 | Crise hospitalière régionale | ⚫ 4/4 | 🔴 3/4 | ⚫ CATASTROPHIQUE |

**Risque Global Brut** : ⚫ **CATASTROPHIQUE** (discrimination + cyber)

---

## ✅ Top 3 Actions Immédiates (P0 — 0-30 jours)

| Priorité | Action | Budget | Impact Risque |
|:---|:---|---:|:---|
| 🥇 | **Audit biais priorisation** | 400k€ | ↓ Discrimination |
| 🥈 | **Sécurisation API DPI** | 300k€ | ↓ Ransomware |
| 🥉 | **Plan reprise 4h** | 200k€ | ↓ Dépendance |

**Investissement immédiat** : **900k€**

---

## 💰 Arbitrage Fix / Pivot / Kill

| Option | Possible | Recommandation |
|:---|:---:|:---:|
| **FIX** | ✅ **OUI** | **CHOISIR** — Audit biais + cyber-résilience |
| PIVOT | ⚠️ Possible | Optimisation sans priorisation auto |
| KILL | ❌ NON | Trop préjudiciable (santé publique) |

---

## 📋 Décision Requise AUJOURD'HUI

- [ ] **AUDIT** biais priorisation (âge/comorbidités)
- [ ] **SÉCURISATION** API DPI (patch ANSSI)
- [ ] **PLAN** reprise 4h (DRP validé)

---

*Executive Summary — CareCoord AI | 1 page | HIGH-RISK/MDR — Équité + Cyber-résilience*
