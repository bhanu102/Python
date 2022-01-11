#to print greatest common divisor(GCD) or highest common factor(HCF)
def GCD(a, b):
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        if ((a % i == 0) and (b % i == 0)):
            gcd = i
    return gcd
print(GCD(48,60))