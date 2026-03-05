# Documents à Demander au Client

## Liste exhaustive des documents utiles pour EBIOS RM

---

## 1. DOCUMENTS D'IDENTIFICATION

### 1.1 Organisation
| Document | Usage EBIOS | Priorité | Atelier |
|----------|-------------|----------|---------|
| Organigramme général | Identifier acteurs, responsabilités | Élevée | 1 |
| Organigramme sécurité | Identifier RSSI, équipe sécurité | Élevée | 1 |
| Liste des sites | Définir périmètre géographique | Élevée | 1 |
| Effectifs par site | Évaluer impact, ressources | Moyenne | 1 |

### 1.2 Gouvernance
| Document | Usage EBIOS | Priorité | Atelier |
|----------|-------------|----------|---------|
| Politique de sécurité | Socle de sécurité existant | Élevée | 1 |
| Charte informatique | Mesures existantes | Élevée | 1 |
| PSSI complète | Référentiel sécurité | Élevée | 1 |
| Registre des traitements RGPD | Données sensibles, flux | Élevée | 1, 3 |

---

## 2. DOCUMENTS TECHNIQUES

### 2.1 Architecture
| Document | Usage EBIOS | Priorité | Atelier |
|----------|-------------|----------|---------|
| Schéma réseau global | Cartographie technique | Élevée | 1, 2 |
| Schéma réseau détaillé | Identification vulnérabilités | Moyenne | 2 |
| Schéma architecture applicative | Systèmes, dépendances | Élevée | 1, 3 |
| Cartographie des flux | Flux de données, interconnexions | Élevée | 1, 2 |
| Inventaire des serveurs | Actifs techniques | Moyenne | 1 |
| Inventaire des postes de travail | Parc informatique | Faible | 1 |

### 2.2 Systèmes et applications
| Document | Usage EBIOS | Priorité | Atelier |
|----------|-------------|----------|---------|
| CMDB (Configuration Management DB) | Inventaire complet | Élevée | 1 |
| Liste des applications critiques | Biens essentiels | Élevée | 1 |
| Fiches applicatives (description, criticité) | Valeur métier | Élevée | 1 |
| Contrats de maintenance | Support, garanties | Moyenne | 1 |

---

## 3. DOCUMENTS OPÉRATIONNELS

### 3.1 Continuité et reprise
| Document | Usage EBIOS | Priorité | Atelier |
|----------|-------------|----------|---------|
| PCA (Plan de Continuité d'Activité) | Continuité, RTO/RPO | Élevée | 1, 3 |
| PRA (Plan de Reprise d'Activité) | Reprise, procédures | Élevée | 1, 3 |
| Analyse d'impact métier (BIA) | Valeur métier, criticité | Élevée | 1 |
| Procédures de sauvegarde | Mesures existantes | Moyenne | 1 |
| Tests PCA/PRA | Efficacité mesures | Moyenne | 1 |

### 3.2 Sécurité opérationnelle
| Document | Usage EBIOS | Priorité | Atelier |
|----------|-------------|----------|---------|
| Procédure gestion incidents | Réponse aux incidents | Élevée | 2, 3 |
| Registre des incidents | Historique, sources de risque | Élevée | 2 |
| Rapports d'audit sécurité | Écarts, axes d'amélioration | Élevée | 1, 4 |
| Plan de remédiation audit | Mesures en cours | Moyenne | 4 |
| Résultats tests intrusion | Vulnérabilités identifiées | Élevée | 2 |

---

## 4. DOCUMENTS MÉTIER

### 4.1 Processus et activités
| Document | Usage EBIOS | Priorité | Atelier |
|----------|-------------|----------|---------|
| Cartographie des processus métier | Compréhension activité | Élevée | 1 |
| Description des processus critiques | Biens essentiels | Élevée | 1 |
| Dépendances inter-processus | Impacts en cascade | Moyenne | 3 |
| Planning des activités saisonnières | Périodes sensibles | Faible | 2 |

### 4.2 Tiers et fournisseurs
| Document | Usage EBIOS | Priorité | Atelier |
|----------|-------------|----------|---------|
| Liste des fournisseurs critiques | Dépendances externes | Élevée | 2, 3 |
| Contrats avec clauses sécurité | Exigences contractuelles | Moyenne | 1 |
| Audits fournisseurs | Niveau de confiance | Moyenne | 2 |
| Plan de continuité fournisseurs | Risques supply chain | Moyenne | 3 |

---

## 5. DOCUMENTS RÉGLEMENTAIRES

### 5.1 Conformité
| Document | Usage EBIOS | Priorité | Atelier |
|----------|-------------|----------|---------|
| Référentiels réglementaires applicables | Exigences légales | Élevée | 1 |
| Certifications (ISO 27001, etc.) | Socle de sécurité | Élevée | 1 |
| Rapports de conformité | Écarts réglementaires | Moyenne | 1 |
| Échanges avec autorités de régulation | Contexte réglementaire | Faible | 1 |

---

## 6. MODÈLE DE DEMANDE AU CLIENT

```
Objet : Mission EBIOS RM - Documents nécessaires pour la préparation

Bonjour [Nom],

Dans le cadre de la mission d'analyse des risques EBIOS RM, nous aurions besoin des documents suivants pour préparer au mieux les ateliers :

DOCUMENTS PRIORITAIRES (pour l'atelier 1) :
□ Organigramme général et organigramme sécurité
□ Politique de sécurité / Charte informatique
□ Schémas d'architecture réseau et applicative
□ Liste des applications et systèmes critiques
□ Registre des traitements RGPD
□ PCA et PRA (si existants)
□ Rapports d'audit sécurité récents

DOCUMENTS COMPLÉMENTAIRES (pour approfondissement) :
□ Inventaire détaillé des systèmes (CMDB)
□ Cartographie des flux
□ Procédure de gestion des incidents
□ Registre des incidents des 12 derniers mois
□ Liste des fournisseurs critiques
□ Contrats avec clauses de sécurité

Délai souhaité : [X jours] avant le premier atelier
Format : Documents électroniques (PDF, visio, excel)

Merci de votre collaboration,
[Signature]
```

---

## 7. GESTION DES DOCUMENTS REÇUS

### 7.1 Classement
```
Documents_Client/
├── 01_Organisation/
├── 02_Technique/
├── 03_Operationnel/
├── 04_Metier/
├── 05_Reglementaire/
└── 99_Autres/
```

### 7.2 Traçabilité
| Document | Date réception | Version | Contact | Commentaire |
|----------|----------------|---------|---------|-------------|
| [Nom] | [Date] | [V] | [Nom] | [Commentaire] |

---

*Liste à adapter selon le contexte du client*
