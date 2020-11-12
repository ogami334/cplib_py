def cmod(n, r, p):
    x,y  = 1, 1
    for i in range(r):
        x = x * (n - i) % p
        y = y * (r - i) % p
    return (x * pow(y, p - 2, p)) % p
#フェルマーの小定理
#なるべく数を小さくする
#powの第3引数pのおかげで計算が速くなる

from operator import mul
from functools import reduce
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under
a = cmb(n, r)
#一番早そう

from math import factorial
def comb1(n,r):
    a = factorial(n)//factorial(r)//factorial(n - r)
    return a

from scipy.special import comb
def comb2(n,r):
    a=comb(n,r,exact=True)
    return a
print(comb2(10000,2000))
#pypyでは使えない

MOD = 998244353
fact = [0] * 220000
invfact = [0] * 220000
fact[0] = 1
for i in range(1, 220000):
    fact[i] = fact[i-1] * i % MOD
invfact[220000 - 1] = pow(fact[220000 - 1], MOD-2, MOD)
for i in range(220000 - 2, -1, -1):
    invfact[i] = invfact[i+1] * (i+1) % MOD
def nCk(n, k):
    if k < 0 or n < k:return 0
    return fact[n] * invfact[k] * invfact[n-k] % MOD
#このようにすると、コンビネーションの逆元を複数回求めないといけない場合に便利
