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
    ("XYz", -1),
    ("AAA1",-1),
    # Round 2 tests:
    ("E", 40),
    ("EE", 80),
    ("EEB", 80),
    ("AAAAA", 200),
    ("AAAAAAA", 300),
    ("AAAAAAAA", 330),
    ("AAAAAAAAAA", 400),
    ("AAAAABBCDEE", 345),
    # Round 3 tests:
    ("F", 10),
    ("FF", 20),
    ("FFF", 20),
    ("FFFF", 30),
    ("FFFFF", 40),
    ("FFFFFF", 40),
    # Round 4 tests:
    ("HHHHHHHHHH", 80),
    ("HHHHH", 45),
    ("HHHHHHHHHHHHHHH", 125),
    ("HHHHHHHHHHH", 90),
    ("KK", 120),
    ("K", 70),
    ("NNNM", 120),
    ("NNN", 120),
    ("NNNMM", 135),
    ("PPPPP", 200),
    ("PPPPPP", 250),
    ("QQQ", 80),
    ("QQ", 60),
    ("RRRQ", 150),
    ("RQ", 80),
    ("UUUU", 120),
    ("UUUUUU", 200),
    ("UUUUUUUU", 240),
    ("UUUUUUUUU",280),
    ("VVV", 130),
    ("VV", 90),
    ("V", 50),
    ("VVVVV", 220),
    ("VVVVVV", 260),
    # Round 5 tests:
    ("STX", 45),
    ("SSSS", 65),
    ("STXYZ", 86),
    ("ZYXTS", 86),
    ("SSSZTTTZXXXZYYYZZZZZSSSAAAWO", 517),
    ("SSSZ", 65),
    ("ZZZS", 65),
    ("STXS", 62)
])
def test_checkout(skus, expected_total):
    assert checkout_solution.checkout(skus) == expected_total
