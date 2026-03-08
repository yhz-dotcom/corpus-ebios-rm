#!/usr/bin/env python3
"""
Correction Lot 5: RGPD/DPIA massif - tous cas sensibles
"""

import os
import re

CORPUS_DIR = "/tmp/corpus-ebios-rm/v2/analyses"

# Tous les cas nécessitant RGPD/DPIA avec justification
TOUS_CAS_RGPD = {
    # Santé (données médicales sensibles - Art. 9)
    "ebios-analysis-aegiscounter.md": "RGPD Art. 9/35 : Logs réseau + SIEM = données personnelles sensibles",
    "ebios-analysis-agriopti.md": "RGPD Art. 35 : Données parcellaires + GPS = données localisation précise",
    "ebios-analysis-agrosentinel.md": "RGPD Art. 35 : Données agricoles détaillées = données professionnelles sensibles",
    "ebios-analysis-gridoptim.md": "RGPD Art. 35 : Données consommation énergie = données comportementales",
    "ebios-analysis-gridpredict.md": "RGPD Art. 35 : Données smart grid = données personnelles détaillées",
    "ebios-analysis-gridsmart.md": "RGPD Art. 35 : Données IoT énergie = données comportementales",
    "ebios-analysis-helios.md": "RGPD Art. 35 : Données production solaire = données professionnelles",
    "ebios-analysis-hybridrecruit.md": "RGPD Art. 9 : Données militaires + biométrie = catégorie spéciale",
    "ebios-analysis-lifeguard.md": "RGPD Art. 9/35 : Données santé comportementale = DPIA obligatoire",
    "ebios-analysis-mediagen.md": "RGPD Art. 35 : Génération contenu média = données sources sensibles",
    "ebios-analysis-milselect.md": "RGPD Art. 9 : Données militaires sensibles = catégorie spéciale",
    "ebios-analysis-narrativeflow.md": "RGPD Art. 9/35 : Profilage psychographique + opinions = DPIA requise",
    "ebios-analysis-optirecrut.md": "RGPD Art. 35 : Données RH détaillées + scoring = DPIA obligatoire",
    "ebios-analysis-pensiondao.md": "RGPD Art. 35 : Données financières blockchain = traçabilité complexe",
    "ebios-analysis-scorelife.md": "RGPD Art. 9/35 : Scoring social santé = données sensibles interdites",
    "ebios-analysis-sentinelai.md": "RGPD Art. 9/35 : Logs SIEM + flux réseau = DPIA obligatoire",
    "ebios-analysis-surveileye.md": "RGPD Art. 9 : Biométrie faciale = catégorie spéciale interdite",
    "ebios-analysis-terravox.md": "RGPD Art. 35 : Données vocales + localisation = DPIA requise",
    "ebios-analysis-workvibe.md": "RGPD Art. 35 : Surveillance émotionnelle employés = DPIA obligatoire",
    
    # Éducation (données enfants - Art. 8)
    "ebios-analysis-audiencedna.md": "RGPD Art. 8/35 : Données enfants publicitaires = protection renforcée",
    "ebios-analysis-echomorph.md": "RGPD Art. 8/35 : Manipulation enfants = données vulnérables",
    "ebios-analysis-mediagen.md": "RGPD Art. 8/35 : Contenu enfants généré = consentement parental",
    "ebios-analysis-psycholoot.md": "RGPD Art. 8/35 : Prédation enfants gaming = protection renforcée",
    
    # Finance (données sensibles)
    "ebios-analysis-adpulse.md": "RGPD Art. 9/35 : Profilage émotionnel + données santé mentale",
    "ebios-analysis-agriscore.md": "RGPD Art. 35 : Scoring agricole détaillé = données professionnelles",
    "ebios-analysis-ecocredit.md": "RGPD Art. 9/35 : Score carbone + revenu = discrimination interdite",
    "ebios-analysis-ecocredit-sus.md": "RGPD Art. 35 : Données ESG entreprises = données commerciales sensibles",
    "ebios-analysis-forceselect.md": "RGPD Art. 9 : Données militaires = catégorie spéciale",
    "ebios-analysis-gridoptim.md": "RGPD Art. 35 : Données infrastructure critique = sécurité renforcée",
    "ebios-analysis-gridsmart.md": "RGPD Art. 35 : Smart grid données = criticité élevée",
    "ebios-analysis-lifeguard.md": "RGPD Art. 9 : Données santé inférées = interdiction stricte",
    "ebios-analysis-pensiondao.md": "RGPD Art. 35 : Crypto + retraite = données financières sensibles",
    "ebios-analysis-scorelife.md": "RGPD Art. 9 : Scoring social = interdiction catégorie spéciale",
}

def add_rgpd(filepath, justification):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'DPIA' in content or 'Art. 35' in content or 'Art. 9' in content or 'Art. 8' in content:
        return False, "Déjà présent"
    
    # Chercher tableau classification
    pattern = r"(\| \*\*Annexe III point \d+\*\* \| .+? \| .+? \|)"
    match = re.search(pattern, content)
    
    if match:
        insertion_point = match.end()
        new_line = f"\n| **RGPD** | {justification.split(' : ')[1]} | 🔴 **OBLIGATOIRE** |"
        content = content[:insertion_point] + new_line + content[insertion_point:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Ajouté"
    
    # Alternative: chercher "Piège" ou conclusion section 1
    match = re.search(r"\*\*Piège.*\*\*", content)
    if match:
        insertion_point = match.start()
        new_line = f"| **RGPD** | {justification.split(' : ')[1]} | 🔴 **OBLIGATOIRE** |\n| "
        content = content[:insertion_point] + new_line + content[insertion_point:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Ajouté (alt)"
    
    return False, "Pattern non trouvé"

if __name__ == "__main__":
    print("=== CORRECTION LOT 5: RGPD/DPIA MASSIF ===\n")
    
    ajoutes = 0
    deja_present = 0
    non_trouve = 0
    
    for cas, justification in TOUS_CAS_RGPD.items():
        filepath = os.path.join(CORPUS_DIR, cas)
        if os.path.exists(filepath):
            success, msg = add_rgpd(filepath, justification)
            if success:
                ajoutes += 1
                print(f"✓ {cas}")
            elif "Déjà" in msg:
                deja_present += 1
            else:
                non_trouve += 1
                print(f"○ {cas}: {msg}")
        else:
            print(f"✗ {cas}: Fichier non trouvé")
    
    print(f"\n=== LOT 5 TERMINÉ ===")
    print(f"Ajoutés: {ajoutes}, Déjà présents: {deja_present}, Non trouvés: {non_trouve}")
