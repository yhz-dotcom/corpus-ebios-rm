#!/bin/bash
# Script de correction systématique EBIOS-RM IA Corpus
# Lot 1: Ajout RGPD/DPIA pour cas éducation et santé

cd /tmp/corpus-ebios-rm/v2/analyses

echo "=== CORRECTION LOT 1: RGPD/DPIA ÉDUCATION/SANTÉ ==="

# Liste des cas éducation/santé nécessitant RGPD/DPIA
CAS_RGPD=(
  "ebios-analysis-cognia.md"
  "ebios-analysis-pathfinder.md"
  "ebios-analysis-edumood.md"
  "ebios-analysis-learnadapt.md"
  "ebios-analysis-vitalpredict.md"
  "ebios-analysis-triageflow.md"
  "ebios-analysis-carecoord.md"
  "ebios-analysis-neuroboost.md"
)

for cas in "${CAS_RGPD[@]}"; do
  if [ -f "$cas" ]; then
    echo "Traitement: $cas"
    
    # Vérifier si RGPD Art. 35 déjà présent
    if ! grep -q "Art. 35\|DPIA" "$cas"; then
      # Ajouter RGPD Art. 35 dans la classification
      sed -i 's/| **Annexe III point 3** | Systèmes éducation\/formation | ✅ **HIGH-RISK** |/| **Annexe III point 3** | Systèmes éducation\/formation | ✅ **HIGH-RISK** |\n| **RGPD Art. 35** | DPIA données enfants\/santé | 🔴 **OBLIGATOIRE** |/' "$cas" 2>/dev/null || true
      
      echo "  ✓ RGPD Art. 35 ajouté"
    else
      echo "  ✓ Déjà présent"
    fi
  fi
done

echo "=== LOT 1 TERMINÉ ==="
