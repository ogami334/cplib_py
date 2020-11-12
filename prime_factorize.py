def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

####################################
#spfによる素因数分解

spf=[-1 for i in range(10**6+1)]
for i in range(2,10**6+1):
    for j in range(1,1+(10**6)//i):
        if spf[i*j]==-1:
            spf[i*j]=i
x=I()
lis=[]
while x>1:
    u=spf[x]
    lis.append(u)
    x//=u
print(lis)
