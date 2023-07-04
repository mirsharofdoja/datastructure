def gcd2(a,b):
    if b>a:
        a,b=b,a
    while a%b!=0:
        c=a%b
        a=b
        b=c
    return b
print(gcd2(64,72))