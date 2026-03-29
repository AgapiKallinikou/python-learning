# 2nd Method: Optimized algorithm O(p^2) operations
import math

p = int(input('max perimeter: '))
triplets = []
for a in range(1, (p+1)//2):
    b = a
    while True:
        csquared = a**2 + b**2
        c = int(math.sqrt(csquared))
        if a + b + c > p:
            break
        if c**2 == csquared:
            triplets.append((a, b, c))
        b += 1
print(triplets)
