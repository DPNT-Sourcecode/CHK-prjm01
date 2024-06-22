import pytest

from lib.solutions.CHK import checkout_solution

@pytest.mark.parametrize("skus, expected_total", [
    ("", 0),
    ("A", 50),
    ("AA", 100),
    ("AAA", 130),
    ("AAAB", 160),
    ("B", 30),
    ("BB", 45),
    ("ABCD", 115),
    ("AAABB", 175),
    ("AAAAAABBBB", 350),
    ("XYZ", -1),
    ("AAA1",-1)
])
def test_checkout(skus, expected_total):
    assert checkout_solution.checkout(skus) == expected_total
