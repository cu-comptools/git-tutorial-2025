import numpy as np

def chebD(n):
    """
    Hint: https://people.maths.ox.ac.uk/trefethen/book.pdf, Chapter 6, pages
    51-55.
    """
    if n == 0:
        x = 1; D = 0; w = 0
    else:
        a = np.linspace(0.0, np.pi, n+1)
        x = np.cos(a)
        b = np.ones_like(x)
        b[0] = 2; b[-1] = 2
        d = np.ones_like(b)
        d[1::2] = -1
        c = b*d
        X = np.outer(x, np.ones(n+1))
        dX = X - X.T
        D = np.outer(c, 1/c) / (dX + np.identity(n+1))
        D = D - np.diag(D.sum(axis=1))
    return D, x
