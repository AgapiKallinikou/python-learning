# 1st Method: Exhaustive algorithm O(p^3) operations

p = int(input('max perimeter: '))
triplets = []
for a in range(1, p+1):
    for b in range(1, p+1):
        for c in range(1, p+1):
            if a**2 + b**2 == c**2 and a + b + c <= p:
                triplets.append((a, b, c))
print(triplets)
