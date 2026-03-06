# Guide d'Utilisation — Templates EBIOS-RM IA

**Objectif** : Ne plus jamais oublier la synthèse managériale

---

## 📦 Les 2 Templates

| Template | Usage | Audience | Format |
|:---|:---|:---|:---|
| `template-ebios-analysis-full.md` | Analyse complète | Équipe projet, auditeurs | 15-30 pages |
| `template-ebios-executive.md` | Synthèse décisionnelle | Direction, investisseurs | 1 page |

---

## 🔄 Workflow de Production

```mermaid
flowchart LR
    A[Collecte infos client] --> B[Remplir template-analyse-full]
    B --> C[Analyser risques]
    C --> D[Rédiger scénarios]
    D --> E[Plan traitement]
    E --> F[Générer executive-summary]
    F --> G[Livrer 2 fichiers]
    
    style A fill:#e3f2fd,stroke:#1565c0
    style B fill:#fff3e0,stroke:#ef6c00
    style C fill:#f3e5f5,stroke:#7b1fa2
    style D fill:#e8f5e9,stroke:#2e7d32
    style E fill:#fff9c4,stroke:#f57f17
    style F fill:#ffcdd2,stroke:#b71c1c
    style G fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px
```

---

## ✅ Checklist Livraison Analyse

### Fichier 1 : Analyse Complète

- [ ] `ebios-analysis-[client].md` créé
- [ ] Tous les champs [en gras] remplis
- [ ] 3+ scénarios de risque avec diagrammes Mermaid
- [ ] Budget chiffré (% CA réaliste)
- [ ] Gantt chart feuille de route
- [ ] Checklist pièges revue

### Fichier 2 : Executive Summary

- [ ] `ebios-[client]-executive.md` créé **(OBLIGATOIRE)**
- [ ] Contexte 3 phrases percutantes
- [ ] Top 5 risques = extraits de l'analyse
- [ ] Top 3 actions = mesures P0
- [ ] Trajectoire visuelle J+30 → M+6 → M+12
- [ ] Scénarios probabilisés (somme = 100%)
- [ ] Décisions actionnables pour aujourd'hui
- [ ] **1 page maximum**

---

## 🎯 Règle d'Or

> **Jamais d'analyse sans executive summary.**
> 
> Même si le client ne l'a pas explicitement demandé.
> Même si on est pressé.
> Même si "c'est pour usage interne".

---

## 📁 Structure Livrable Client

```
livrable-ebios-[client]-[date]/
├── 01-executive-summary.md          ← 🎯 Décideurs (1 page)
├── 02-analyse-complete.md           ← 📊 Équipe projet (15-30 pages)
├── 03-annexes/
│   ├── schema-technique.png
│   ├── extraits-normes.pdf
│   └── benchmarks-sectoriels.xlsx
└── README.md                        ← Guide de lecture
```

---

## 💡 Astuces de Productivité

### Pour l'Analyse Complète

1. **Commencer par la classification AI Act** — elle oriente tout
2. **Utiliser les cases du template** — elles sont là pour guider
3. **Ne pas effacer les sections vides** — les garder avec "[À compléter]"
4. **Valider les diagrammes Mermaid** — https://mermaid.live

### Pour l'Executive Summary

1. **Le faire DERNIER** — après l'analyse complète
2. **Copier-coller les chiffres** — pas de réinvention
3. **Tester sur décideur simulé** — "Mon DG comprend-il en 2 min ?"
4. **Imprimer en PDF** — vérifier la 1 page

---

## 🚨 Anti-Patterns

| Fait | Conséquence | Solution |
|:---|:---|:---|
| Analyse sans executive | Décideur noyé, pas de décision | **Toujours les 2 fichiers** |
| Executive trop technique | Décideur perdu, inaction | 3 phrases max pour contexte |
| Budgets non justifiés | Pas de budget débloqué | Benchmarks + marge 20% |
| Scénarios sans proba | Décideur ne sait pas prioriser | Toujours %, même approximatif |
| Trajectoire irréaliste | Désillusion, perte crédibilité | J+30 concret, M+6 ambitieux |

---

## 📚 Exemples de Référence

| Client | Analyse | Executive | Remarque |
|:---|:---|:---|:---|
| OptiRecrut | `ebios-analysis-optirecrut.md` | `ebios-optirecrut-executive.md` | Startup RH IA, classification erronée |
| [Prochain] | À créer | À créer | À toi de jouer |

---

## 🎓 Formation Rapide

### 5 min — Comprendre la différence

| | Analyse Complète | Executive Summary |
|:---|:---|:---|
| **Longueur** | 15-30 pages | 1 page |
| **Détail** | Tout | L'essentiel |
| **Audience** | Experts, auditeurs | Décideurs pressés |
| **Objectif** | Démontrer, prouver | Décider, agir |
| **Ton** | Technique, exhaustif | Stratégique, percutant |
| **Format** | Markdown, tableaux, Mermaid | Slide-like, visuel |

### 15 min — Premier exercice

1. Prendre un cas connu (OptiRecrut)
2. Lire l'analyse complète (10 min)
3. Lire l'executive summary (2 min)
4. Comparer : qu'est-ce qui est gardé ? jeté ? synthétisé ?

---

## 🔧 Personnalisation

### Adapter aux Secteurs

| Secteur | Ajuster dans analyse | Ajuster dans executive |
|:---|:---|:---|
| **Finance** | Accent conformité ACPR/EBA | Risque sanction réglementaire |
| **Santé** | Accent sécurité patient | Risque vie humaine |
| **Public** | Accent transparence algorithmique | Risque confiance citoyenne |
| **Retail** | Accent performance/conversion | Risque compétitivité |

### Adapter aux Tailles

| Taille | Analyse | Executive |
|:---|:---|:---|
| **Startup** | Léger, agile, budgets % CA | Focus survie/scale |
| **PME** | Complet mais pragmatique | Focus compétitivité |
| **Grand Groupe** | Exhaustif, multi-sites | Focus réputation/réglementaire |

---

## 📞 Support

En cas de doute sur l'utilisation :
1. Relire ce guide
2. Voir exemple OptiRecrut
3. Poser la question : "Mon DG comprendra-t-il en 2 min ?"

---

*Guide d'Utilisation Templates EBIOS-RM IA | Version 1.0 | Mars 2026*
