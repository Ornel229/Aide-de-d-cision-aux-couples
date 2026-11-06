"""Moteur de scénarios pour la drépanocytose (hérédité autosomique récessive).

Allèles : A (normal), S (drépanocytaire), C (hémoglobine C), T (bêta-thalassémie).
Chaque parent transmet un de ses deux allèles avec une probabilité de 1/2.
Les probabilités sont calculées avec des fractions exactes (pas d'arrondi).

Ce module décrit des probabilités, pas des diagnostics.
"""
from fractions import Fraction

ORDER = "ASCT"
GENOTYPES = ["AA", "AS", "AC", "AT", "SS", "SC", "ST"]
CATEGORIES = ["non_porteur", "porteur", "drepano", "autre"]


def _norm(a, b):
    """Génotype normalisé (ex. 'SA' -> 'AS')."""
    return "".join(sorted((a, b), key=ORDER.index))


def category_of(genotype):
    """Catégorie d'un génotype : non_porteur, porteur, drepano ou autre."""
    if genotype == "AA":
        return "non_porteur"
    if genotype in ("AS", "AC", "AT"):
        return "porteur"
    if genotype in ("SS", "SC", "ST"):
        return "drepano"
    return "autre"  # CC, CT, TT : combinaisons à voir avec un spécialiste


def punnett_grid(g1, g2):
    """Grille 2x2 des génotypes possibles de l'enfant (une ligne par allèle du parent 1)."""
    return [[_norm(a, b) for b in g2] for a in g1]


def offspring_distribution(g1, g2):
    """Probabilité de chaque génotype de l'enfant, pour une grossesse."""
    dist = {}
    for row in punnett_grid(g1, g2):
        for genotype in row:
            dist[genotype] = dist.get(genotype, Fraction(0)) + Fraction(1, 4)
    return dist


def category_probabilities(g1, g2):
    """Probabilité par catégorie pour l'enfant, pour une grossesse."""
    out = {c: Fraction(0) for c in CATEGORIES}
    for genotype, p in offspring_distribution(g1, g2).items():
        out[category_of(genotype)] += p
    return out


def needs_counselling(g1, g2):
    """Vrai si un conseil génétique est recommandé pour ce couple."""
    probs = category_probabilities(g1, g2)
    if probs["drepano"] > 0 or probs["autre"] > 0:
        return True
    return any(category_of(g) in ("drepano", "autre") for g in (g1, g2))
