import math

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

if a != 0:
    # Quadratic case
    D = b**2 - 4*a*c
    if D == 0:
        x = -b/(2*a)
        print(f'Double root: x = {x:.3f}')
    elif D > 0:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        print(f'Two roots: x1 = {x1:.3f}, x2 = {x2:.3f}')
    else:
        print('No real roots.')
else:
    # Linear case
    if b != 0:
        x = -c/b
        print(f'x = {x:.3f}')
    else:
        print('No function of x provided.')
