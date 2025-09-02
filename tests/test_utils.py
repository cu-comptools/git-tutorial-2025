import numpy as np
from utils import quadroots as qr
from utils import chebutils as ch

def test_quadroots_1():
    a = 2.0
    b = -5.0
    c = 2.0
    roots = qr.quadroots(a, b, c)
    x1_exact = 8.0
    x2_exact = 2.0
    assert (np.abs(roots[0] - x1_exact) < 1e-14) and (np.abs(roots[1] - x2_exact)) < 1e-14 

def test_chebD_1():
    n = 1
    D, _ = ch.chebD(n)
    assert (D == np.array([[0.5, -0.5], [0.5, -0.5]])).all()

