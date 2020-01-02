import pytest
from sigfigs import sigfigs

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

def test_sigfigs_add():
    sf = sigfigs.SigFigs()
    assert(sf.add("0.01","1") == '1')
