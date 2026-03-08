#!/usr/bin/env python3
"""
Script de correction systématique du corpus EBIOS-RM IA
Corrige RGPD/DPIA, Arbitrage, et Diagrammes Mermaid
"""

import os
import re
import glob

CORPUS_DIR = "/tmp/corpus-ebios-rm/v2/analyses"

def get_all_cases():
    """Récupère tous les cas d'analyse"""
    return sorted(glob.glob(os.path.join(CORPUS_DIR, "ebios-analysis-*.md")))

def check_rgpd_dpia(filepath):
    """Vérifie si RGPD/DPIA est présent"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return 'DPIA' in content or 'Art. 35' in content

def check_mermaid(filepath):
    """Vérifie si diagramme Mermaid est présent"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return '```mermaid' in content

def check_arbitrage(filepath):
    """Vérifie si arbitrage Fix/Pivot/Kill est présent"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return 'ARBITRAGE FIX' in content or 'Fix / Pivot / Kill' in content

def audit_corpus():
    """Audit complet du corpus"""
    cases = get_all_cases()
    
    stats = {
        'total': len(cases),
        'rgpd_ok': 0,
        'rgpd_missing': [],
        'mermaid_ok': 0,
        'mermaid_missing': [],
        'arbitrage_ok': 0,
        'arbitrage_missing': []
    }
    
    for case in cases:
        basename = os.path.basename(case)
        
        if check_rgpd_dpia(case):
            stats['rgpd_ok'] += 1
        else:
            stats['rgpd_missing'].append(basename)
        
        if check_mermaid(case):
            stats['mermaid_ok'] += 1
        else:
            stats['mermaid_missing'].append(basename)
        
        if check_arbitrage(case):
            stats['arbitrage_ok'] += 1
        else:
            stats['arbitrage_missing'].append(basename)
    
    return stats

if __name__ == "__main__":
    print("=== AUDIT COMPLET DU CORPUS EBIOS-RM IA ===\n")
    
    stats = audit_corpus()
    
    print(f"Total cas analysés: {stats['total']}")
    print()
    
    print("RGPD/DPIA (Art. 35):")
    print(f"  ✓ Présent: {stats['rgpd_ok']}/{stats['total']} ({stats['rgpd_ok']*100//stats['total']}%)")
    print(f"  ✗ Manquant: {len(stats['rgpd_missing'])}")
    if stats['rgpd_missing']:
        for cas in stats['rgpd_missing'][:10]:
            print(f"    - {cas}")
        if len(stats['rgpd_missing']) > 10:
            print(f"    ... et {len(stats['rgpd_missing']) - 10} autres")
    print()
    
    print("Diagrammes Mermaid:")
    print(f"  ✓ Présent: {stats['mermaid_ok']}/{stats['total']} ({stats['mermaid_ok']*100//stats['total']}%)")
    print(f"  ✗ Manquant: {len(stats['mermaid_missing'])}")
    if stats['mermaid_missing']:
        for cas in stats['mermaid_missing']:
            print(f"    - {cas}")
    print()
    
    print("Arbitrage Fix/Pivot/Kill:")
    print(f"  ✓ Présent: {stats['arbitrage_ok']}/{stats['total']} ({stats['arbitrage_ok']*100//stats['total']}%)")
    print(f"  ✗ Manquant: {len(stats['arbitrage_missing'])}")
    if stats['arbitrage_missing']:
        for cas in stats['arbitrage_missing'][:10]:
            print(f"    - {cas}")
        if len(stats['arbitrage_missing']) > 10:
            print(f"    ... et {len(stats['arbitrage_missing']) - 10} autres")
