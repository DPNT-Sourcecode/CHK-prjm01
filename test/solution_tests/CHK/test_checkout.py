import pytest

from lib.solutions.CHK import checkout_solution

@pytest.mark.parametrize("skus, expected_total", [
    # Round 1 tests:
    ("", 0),
    ("A", 50),
    ("AA", 100),
    ("AAA", 130),
    ("AAAB", 160),
    ("B", 30),
    ("BB", 45),
    ("ABCD", 115),
    ("AAABB", 175),
    ("AAAAAABBBB", 340),
    ("XYZ", -1),
    ("AAA1",-1),
    # Round 2 tests:
    ("E", 40),
    ("EE", 80),
    ("EEB", 80),
    ("AAAAA", 200),
    ("AAAAAAA", 300),
    ("AAAAAAAA", 330),
    ("AAAAAAAAAA", 400),
    ("AAAAABBCDEE", 345) # 200 + 80 + 30 + 20 + 15
])
def test_checkout(skus, expected_total):
    assert checkout_solution.checkout(skus) == expected_total



