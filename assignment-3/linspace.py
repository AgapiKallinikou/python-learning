def linspace(a, b, n=100):
    X = []
    for v in range(n):
        X.append(a + v*(b-a)/(n-1))
    return X
