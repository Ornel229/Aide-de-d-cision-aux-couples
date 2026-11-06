from fractions import Fraction as F

from genetique import (GENOTYPES, category_probabilities, needs_counselling,
                       offspring_distribution)


def test_as_x_as():
    d = offspring_distribution("AS", "AS")
    assert d == {"AA": F(1, 4), "AS": F(1, 2), "SS": F(1, 4)}
    assert needs_counselling("AS", "AS")


def test_aa_x_as_no_disease():
    p = category_probabilities("AA", "AS")
    assert p["drepano"] == 0 and p["porteur"] == F(1, 2) and p["non_porteur"] == F(1, 2)
    assert not needs_counselling("AA", "AS")


def test_as_x_ss():
    p = category_probabilities("AS", "SS")
    assert p["drepano"] == F(1, 2) and p["porteur"] == F(1, 2)


def test_ss_x_ss():
    assert category_probabilities("SS", "SS")["drepano"] == 1


def test_as_x_ac_gives_sc():
    assert offspring_distribution("AS", "AC")["SC"] == F(1, 4)
    assert needs_counselling("AS", "AC")


def test_at_x_at_other_combination():
    assert category_probabilities("AT", "AT")["autre"] == F(1, 4)
    assert needs_counselling("AT", "AT")


def test_probabilities_sum_to_one():
    for a in GENOTYPES:
        for b in GENOTYPES:
            assert sum(category_probabilities(a, b).values()) == 1


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
    print("Tous les tests passent.")
