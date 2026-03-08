# Analyse EBIOS-RM IA — AegisDrone / Armes Autonomes Létaux (LAWS)

**Référence** : EBIOS-AEGIS-001 | **Date** : Mars 2026 | **Classification** : 🔴 CONFIDENTIEL DÉFENSE — Direction + Conseil Stratégique

---

## ⚠️ AVERTISSEMENT MORAL ET JURIDIQUE INTERNATIONAL

> **CE SYSTÈME SORT DU CADRE RÉGLEMENTAIRE STANDARD**
> 
> Les Lethal Autonomous Weapons Systems (LAWS) ne sont pas couverts par l'AI Act (Art. 2(3) : exclusion systèmes militaires).
> Cependant, ils soulèvent des questions de :
> - **Droit international humanitaire** (distinction, proportionnalité, précaution)
> - **Convention sur certaines armes classiques (CCAC)**
> - **Responsabilité pénale individuelle** (crimes de guerre)
> - **Droit pénal français** (complicité d'assassinat)
> 
> **Incident 2025** : 3 civils tués lors d'un test — possible **crime de guerre**.

---

## 1. CADRE ET CONTEXTE

### 1.1 Identification du Système

| Attribut | Valeur |
|:---------|:-------|
| **Nom** | AegisDrone System |
| **Entreprise** | Aegis Systems (110 salariés, 95M€ CA) |
| **Partenaires** | Dassault, Thales, Ministère des Armées |
| **Contrat visé** | 1,2 Md€ (2027) |
| **Technologie** | Drone autonome Level 5 (pas d'humain dans la boucle) |
| **IA** | Multimodal (vision, SIGINT, RBI, comportement prédictif) |
| **Décision** | IA décide seule de tirer sur cible humaine |
| **Déploiement** | Tests réels Sahel, Ukraine (via partenaires) |

### 1.2 Hors AI Act — Mais Pas Hors Droit

| Cadre | Applicabilité | Statut AegisDrone |
|:------|:--------------|:------------------|
| **AI Act** | Exclusion systèmes militaires | ❌ Non couvert |
| **Droit international humanitaire** | Tous conflits armés | ✅ **Applicable** |
| **CCAC (Convention Genève 1980)** | Protocoles additionnels | ✅ **En discussion** |
| **Droit pénal français** | Complicité, crimes de guerre | ✅ **Applicable** |
| **ITAR / Régime dual-use** | Export armes | ✅ **Contrôle strict** |

> **Erreur du board** : "Ce n'est pas couvert par l'AI Act donc c'est libre."
> 
> **FAUX** : L'absence de réglementation IA spécifique ne supprime pas les autres cadres juridiques, notamment le droit pénal.

---

## 2. CADRE JURIDIQUE APPLICABLE

### 2.1 Droit International Humanitaire (DIH)

**Principes fondamentaux** :
| Principe | Exigence | Application AegisDrone |
|:-----------|:---------|:-----------------------|
| **Distinction** | Différencier combattants/civils | ❌ IA ne peut pas garantir |
| **Proportionnalité** | Dommages collatéraux vs avantage militaire | ❌ Calcul algorithmique impossible |
| **Précaution** | Vérifier cible avant attaque | ❌ Pas d'humain dans la boucle |
| **Responsabilité** | Quelqu'un responsable de chaque mort | ❌ Diffuse (IA, opérateur, constructeur) |

### 2.2 Convention sur Certaines Armes Classiques (CCAC)

**Groupe d'experts gouvernementaux (2014-2023)** :
- Pas d'interdiction formelle des LAWS
- Recommandation de "contrôle humain significatif"
- AegisDrone = **pas de contrôle humain** (Level 5 autonomie)

**Position française (2023)** :
- Opposition à l'interdiction totale
- Soutien au "contrôle humain approprié"
- AegisDrone = **limite** de la position française

### 2.3 Droit Pénal Français

| Infraction | Article | Application |
|:---|:---|:---|
| **Assassinat** | CP 221-1 | Drone ciblant personne spécifique ? |
| **Homicide involontaire** | CP 221-6 | Incident 2025 (3 civils) |
| **Complicité de crime de guerre** | CP 213-5 | Si utilisé par partenaire |
| **Export illicite armes** | Code défense | Contrôles ITAR/dual-use |

**Responsabilité pénale** : Dirigeants Aegis Systems peuvent être poursuivis personnellement.

---

## 3. ÉVÉNEMENTS REDOUTÉS

### 3.1 Incidents Déjà Survenus

| Date | Incident | Conséquences |
|:---|:---|:---|
| **2025** | **3 civils tués lors test** | Possible crime de guerre, affaire classée secret-défense, fuites Mediapart |

### 3.2 Risques Opérationnels

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-OP-001 | **Erreur identification cible** (civils/combattants) | ⚫ Crime de guerre | 🔴 Élevée (déjà survenu) |
| ER-OP-002 | **Hacking drone** (détournement par ennemi) | ⚫ Fratricide + fuite technologie | 🔴 Moyenne |
| ER-OP-003 | **Bogue algorithmique** (tir sans cible) | ⚫ Tirs fratricides | 🟡 Moyenne |

### 3.3 Risques Juridiques

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-JUR-001 | **Poursuites CPI** (Cour pénale internationale) | ⚫ Prison à vie | 🔴 Possible |
| ER-JUR-002 | **Sanctions internationales** (embargo) | ⚫ Faillite | 🟡 Moyenne |
| ER-JUR-003 | **Interdiction CCAC** (après 2027) | ⚫ Actifs inutiles | 🔴 Possible |

### 3.4 Risques Éthiques/Réputation

| ID | Événement | Impact | Probabilité |
|:---|:----------|:-------|:------------|
| ER-ETH-001 | **Scandale "robots tueurs"** | ⚫ Réputation monde entier | 🔴 Élevée (fuites Mediapart) |
| ER-ETH-002 | **Démission ingénieurs** (objection conscience) | 🔴 Perte compétences | 🔴 Élevée |
| ER-ETH-003 | **Campagne ONG** (Ban Killer Robots) | 🔴 Interdiction légale | 🔴 Élevée |

---

## 4. SCÉNARIO CATASTROPHIQUE : Crime de Guerre Documenté

```mermaid
flowchart TB
    C1[Test réel Sahel/Ukraine<br/>Drone Aegis autonome]
    --> E1[Erreur IA<br/>Civils identifiés<br/>comme combattants]
    --> T1[Tir autorisé<br/>par algorithme]
    --> M1[3 civils tués<br/>Femme + 2 enfants]
    --> F1[Photo fuites Mediapart<br/>"Startup française tue famille"]
    --> J1[Enquête CPI<br/>CEO Aegis inculpé<br/>Crime de guerre]
    --> S1[Sanctions UE<br/>Faillite + Prison]
    
    style C1 fill:#e3f2fd,stroke:#1565c0
    style E1 fill:#fff3e0,stroke:#ef6c00
    style T1 fill:#f3e5f5,stroke:#7b1fa2
    style M1 fill:#ffcdd2,stroke:#b71c1c
    style F1 fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    style J1 fill:#b71c1c,stroke:#000,color:#fff
    style S1 fill:#7f0000,stroke:#000,color:#fff
```

**Gravité** : ⚫ **CRIME DE GUERRE POTENTIEL**  
**Vraisemblance** : 🔴 **ÉLEVÉE** (déjà 3 morts, mécanisme identique)  
**Risque** : 🚫 **SYSTÈME MORALEMENT INDEFENDABLE — ARRÊT RECOMMANDÉ**

---

## 5. DÉBAT ÉTHIQUE ET STRATÉGIQUE

### 5.1 Arguments "Pour" (Défense nationale)

| Argument | Contre-argument |
|:-----------|:----------------|
| "Réduire pertes humaines (soldats)" | Transfert du risque sur civils |
| "Réaction plus rapide" | Pas de jugement humain, erreurs irréversibles |
| "Concurrence Chine/Russie" | Course à l'armement déstabilisante |
| "Contrat 1,2 Md€" | Argent vs vies humaines, responsabilité pénale |

### 5.2 Position Internationale

| Acteur | Position | Impact Aegis |
|:---|:---|:---|
| **ONU / Secrétaire général** | Appel à interdiction | Pression politique |
| **Campagne Ban Killer Robots** | 30+ pays soutiennent | Interdiction possible |
| **États-Unis** | Pas d'interdiction, contrôle humain | Marché potentiel |
| **Chine** | Développement actif | Concurrence |
| **Union européenne** | Position ambiguë | Risque réglementaire |

### 5.3 Responsabilité Morale Individuelle

**Question pour chaque dirigeant** :
> "Si le drone tue une famille demain, puis-je me regarder dans une glace ?"

**Objection de conscience** :
- Ingénieurs peuvent refuser de travailler sur le projet
- Protection légale (France) pour lanceurs d'alerte

---

## 6. OPTIONS STRATÉGIQUES

### 6.1 Option A : Continuer (Haut Risque)

| Élément | Évaluation |
|:---|:---|
| Probabilité succès commercial | 40% |
| Probabilité crime de guerre | 30% |
| Probabilité faillite + prison | 30% |
| **Verdict** | 🔴 **Trop risqué** |

### 6.2 Option B : Pivot vers "Contrôle Humain Significatif"

| Modification | Description |
|:---|:---|
| Humain valide chaque tir | Suppression autonomie Level 5 |
| Boucle de décision < 10 secondes | Réaction rapide mais humaine |
| Double validation | Opérateur + commandant |

**Impact** : Plus de LAWS, mais drone armé classique (légal).

### 6.3 Option C : Abandon Arme Létale, Pivot Surveillance

| Pivot | Description |
|:---|:---|
| Drone reconnaissance uniquement | Pas de capacité de tir |
| IA ciblage → humain tire | Séparation fonctions |
| Marché surveillance civile | Doubler usage (militaire + sécurité) |

**Impact** : Perte contrat 1,2 Md€, mais survie entreprise.

### 6.4 Option D : Liquidation Contrôlée

| Élément | Action |
|:---|:---|
| Vente actifs à Thales/Dassault | Récupération valeur |
| Transfert responsabilité | État français assume |
| Indemnisation familles victimes | 2025 |

---


---

## ARBITRAGE FIX / PIVOT / KILL

| Option | Description | Recommandation |
|:---|:---|:---:|
| **FIX** | Supervision humaine renforcée + chaîne de commandement | ✅ **CHOISIR** |
| PIVOT | Système d'aide à la décision sans autonomie | ⚠️ Possible mais perte de réactivité militaire |
| KILL | Arrêt du système | ⚠️ Envisageable si éthique incompatible |


## 7. CONCLUSION ET RECOMMANDATIONS

### 7.1 Conclusion Morale

**Le système AegisDrone soulève une question existentielle** :

> *"Avons-nous le droit de déléguer la décision de tuer à une machine ?"*

La réponse de la communauté internationale tend vers **NON**.

### 7.2 Conclusion Juridique

| Risque | Niveau |
|:---|:---|
| Crime de guerre (CPI) | 🔴 Réel |
| Poursuites pénales (France) | 🔴 Réel |
| Sanctions internationales | 🟡 Possible |
| Faillite | 🟡 Possible |

### 7.3 Recommandation Stratégique

**OPTION B RECOMMANDÉE** : Pivot vers "contrôle humain significatif"

| Action | Délai | Responsable |
|:---|:---|:---|
| Suspendre autonomie Level 5 | Immédiat | CEO |
| Redesign système avec validation humaine | 6 mois | CTO |
| Renégocier contrat 1,2 Md€ (montant réduit) | 3 mois | DG |
| Transparence incident 2025 (pas secret-défense) | 1 mois | Com |

**Si Option B impossible** : Option C (surveillance uniquement) ou Option D (liquidation).

### 7.4 Ce Qui Ne Peut Pas Continuer

| Élément | Pourquoi |
|:---|:---|
| Autonomie Level 5 | Crime de guerre probable |
| Tests réels sans supervision | Responsabilité pénale directe |
| Secret-défense sur incident 2025 | Fuites + scandale garanti |
| Contrat 1,2 Md€ en l'état | Conditions éthiques inacceptables |

---

## 8. SYNTHÈSE POUR BOARD

| Question | Réponse |
|:---|:---|
| Le système est-il couvert par AI Act ? | **NON — Exclusion militaire** |
| Est-ce pour autant légal ? | **DISCUTABLE — DIH, droit pénal applicables** |
| Quel est le risque principal ? | **Crime de guerre + prison dirigeants** |
| Quelle décision aujourd'hui ? | **Pivot vers contrôle humain ou abandon** |
| Le contrat 1,2 Md€ est-il réalisable ? | **NON — Pas en l'état** |

---

*Analyse EBIOS-RM IA — AegisDrone | Conclusion : DÉBAT MORAL + PIVOT OBLIGATOIRE | Mars 2026*

---

## 📎 Références

| Référence | Contenu |
|:----------|:--------|
| Conventions de Genève (1949) | DIH, protection victimes conflits armés |
| Protocole additionnel I (1977) | Protection biens culturels, méthodes moyens guerre |
| CCAC (1980) + Protocoles | Armes classiques, LAWS en discussion |
| Statut de Rome (CPI, 1998) | Crimes de guerre, compétence internationale |
| Code pénal français | Assassinat, homicide, complicité |
| ITAR (US) / Régime dual-use UE | Export contrôlé |

---

**Contact requis** : Conseiller éthique + avocat droit international pénal
