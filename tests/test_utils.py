import numpy as np
from utils import quadroots as qr
from utils import chebutils as ch

def test_quadroots_1():
    a = 2.0
    b = -5.0
    c = 2.0
    roots = qr.quadroots(a, b, c)
    x1_exact = 2.0
    x2_exact = 0.5
    assert (np.abs(roots[0] - x1_exact) < 1e-14) and (np.abs(roots[1] - x2_exact)) < 1e-14 

def test_chebD_1():
    n = 1
    D,x = ch.chebD(n)
    D_i1 = 0.5
    D_i2 = -0.5
    assert (np.abs(D[0,0] - D_i1) < 1e-14) and (np.abs(D[1,0] - D_i1) < 1e-14) and (np.abs(D[0,1] - D_i2) < 1e-14) and (np.abs(D[1,1] - D_i2) < 1e-14)
    pass
