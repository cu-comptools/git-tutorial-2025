import numpy as np

def chebD(n):
    """
    Computes a spectral differentiation matrix and Chebysev grid
    
    Parameters
    ----------
    n: <int>
        An integer defining the number of grid points (n+1)
    
    Returns
    -------
    D: (n+1)x(n+1) matrix
        differentiation matrix
    x: (n+1)-d array
        Chebysev grid
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
