def gcd(a,b):
    while a!=b:
        c=abs(a-b)
        a=b
        b=c
    return a