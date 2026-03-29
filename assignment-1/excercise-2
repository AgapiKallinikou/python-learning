prec = float(input('Enter the desired precision: '))
e = 0                 # The approximation of e (initially 0)
err = 3               # The maximum error (initially 3/1! = 3)
n = 0                 # The number of iterations
nfact = 1             # The value of n! (initially 0! = 1)
while err > prec:     # while the error is greater than the desired precision
    e += 1 / nfact    # increase e by 1/n!
    nfact *= (n+1)    # nfact is now (n+1)!
    err = 3 / nfact   # recalculation of the error
    n += 1            # since n is increased by 1, nfact is now n!
print(e)
