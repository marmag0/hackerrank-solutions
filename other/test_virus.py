import pytest

from virus import find_ifected_coverage


# testing using set of parameteres
# --------------------------------
@pytest.mark.parametrize("N, K, expected", [
    (7, [3], 3),
    (10, [2, 7], 2),
    (5, [0], 4),
    (5, [4], 4),
    (1, [0], 0),
    (10, [0, 9], 4),
    (3, [0, 1, 2], 0),
    (6, [2, 3], 2),
])

def test_find_infected_coverage_valid_cases(N, K, expected):
    """Tests standard, correct cases."""
    assert find_ifected_coverage(N, K) == expected


# testing using inline-defined arguments
# --------------------------------------
def test_find_infected_coverage_empty_k():
    """No one is infected - edge case."""
    assert find_ifected_coverage(10, []) is None

def test_find_infected_coverage_large_gap():
    """Tests significatn gap between infected."""
    assert find_ifected_coverage(100, [0, 99]) == 49


# testing errors
# --------------
def test_invalid_input_type():
    with pytest.raises(TypeError):
        find_ifected_coverage(7, "infected")


# fixtures
# --------
@pytest.fixture
def default_setup():
    """Prepare a dataset for testing"""
    data = {"N": 7, "K": [3]}
    return data

def test_with_fixture(default_setup):
    result = find_ifected_coverage(default_setup["N"], default_setup["K"])
    assert result == 3
