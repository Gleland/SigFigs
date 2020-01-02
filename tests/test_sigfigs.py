import pytest
from sigfigs import sigfigs

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

def test_sigfigs_add():
    sf = sigfigs.SigFigs()
    assert(sf.add("0.01","1") == '1')


def test_sigfigs_count():
    sf = sigfigs.SigFigs()
    test_cases = {
            "100.0": 4,
            "0.00203": 3,
            "-100.0": 4,
            "1203450": 6,
            "1000": 1,
            "5420": 3,
            "01000.": 4,
            "-0.006700": 4,
            "01000.0": 5,
            "0.06540": 4,
            "0.002": 1,
            "009009.": 4,
            "0.0020": 2,
            "90090.": 5
    }
    for case, count in test_cases.items():
        assert(sf.count(case) == count)
