import random

M = int(input('M? '))
n1 = int(input('n1? '))
n2 = int(input('n2? '))
L1 = []
L2 = []
for i in range(n1):
    L1.append(random.randrange(M+1))
for i in range(n2):
    L2.append(random.randrange(M+1))
L1.sort()
L2.sort()
X = []
i1 = i2 = 0
while i1 < n1 and i2 < n2:
    if L1[i1] < L2[i2]:
        X.append(L1[i1])
        i1 += 1
    elif L1[i1] == L2[i2]:
        X.append(L1[i1])
        i1 += 1
        X.append(L2[i2])
        i2 += 1
    else:
        X.append(L2[i2])
        i2 += 1
if i1 == n1:
    X.extend(L2[i2:])
else:
    X.extend(L1[i1:])
print('L1 = ', L1)
print('L2 = ', L2)
print('X = ', X)
