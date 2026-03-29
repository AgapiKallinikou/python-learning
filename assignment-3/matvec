def matvec(A, x):
    m = len(A)
    n = len(x)
    for row in A:
        if len(row) != n:
            return []
    y = [0.0]*m
    for i in range(m):
        for j in range(n):
            y[i] += A[i][j]*x[j]
    return y
