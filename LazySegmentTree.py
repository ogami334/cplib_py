import sys
def input(): return sys.stdin.readline().rstrip()

# LazySegmentTree
class LazySegmentTree:
  # f(X, X) -> X
  # g(X, M) -> X
  # h(M, M) -> M
  __slots__ = ["n", "seg", "x_unit", "m_unit", "f", "g", "h", "lazy"]

  def __init__(self, n, p, x_unit, m_unit, f, g, h):
    self.n = n
    self.seg = p*2
    self.x_unit = x_unit
    self.m_unit = m_unit
    self.f = f
    self.g = g
    self.h = h
    for i in range(self.n-1, 0, -1):
      self.seg[i] = self.f(self.seg[i<<1], self.seg[(i<<1)+1])
    self.lazy = [m_unit] * (self.n * 2)

  def update(self, l, r, x):
    l += self.n
    r += self.n
    ll = l // (l & -l)
    rr = r // (r & -r) - 1
    for shift in range(ll.bit_length()-1, 0, -1):
      i = ll >> shift
      self.lazy[i << 1] = self.h(self.lazy[i << 1], self.lazy[i])
      self.lazy[(i << 1)+1] = self.h(self.lazy[(i << 1)+1], self.lazy[i])
      self.seg[i] = self.g(self.seg[i], self.lazy[i])
      self.lazy[i] = self.m_unit
    for shift in range(rr.bit_length()-1, 0, -1):
      i = rr >> shift
      self.lazy[i << 1] = self.h(self.lazy[i << 1],   self.lazy[i])
      self.lazy[(i << 1)+1] = self.h(self.lazy[(i << 1)+1], self.lazy[i])
      self.seg[i] = self.g(self.seg[i], self.lazy[i])
      self.lazy[i] = self.m_unit
    while l < r:
      if l & 1:
        self.lazy[l] = self.h(self.lazy[l], x)
        l += 1
      if r & 1:
        r -= 1
        self.lazy[r] = self.h(self.lazy[r], x)
      l >>= 1
      r >>= 1
    while ll > 1:
      ll >>= 1
      self.seg[ll] = self.f(self.g(self.seg[ll << 1], self.lazy[ll << 1]), self.g(self.seg[(ll << 1)+1], self.lazy[(ll << 1)+1]))
      self.lazy[ll] = self.m_unit
    while rr > 1:
      rr >>= 1
      self.seg[rr] = self.f(self.g(self.seg[rr << 1], self.lazy[rr << 1]), self.g(self.seg[(rr << 1)+1], self.lazy[(rr << 1)+1]))
      self.lazy[rr] = self.m_unit

  def query(self, l, r):
    l += self.n
    r += self.n
    ll = l // (l & -l)
    rr = r // (r & -r) - 1
    for shift in range(ll.bit_length()-1, 0, -1):
      i = ll >> shift
      self.lazy[i << 1] = self.h(self.lazy[i << 1], self.lazy[i])
      self.lazy[(i << 1)+1] = self.h(self.lazy[(i << 1)+1], self.lazy[i])
      self.seg[i] = self.g(self.seg[i], self.lazy[i])
      self.lazy[i] = self.m_unit
    for shift in range(rr.bit_length()-1, 0, -1):
      i = rr >> shift
      self.lazy[i << 1] = self.h(self.lazy[i << 1],   self.lazy[i])
      self.lazy[(i << 1)+1] = self.h(self.lazy[(i << 1)+1], self.lazy[i])
      self.seg[i] = self.g(self.seg[i], self.lazy[i])
      self.lazy[i] = self.m_unit
    ans_l = ans_r = self.x_unit
    while l < r:
      if l & 1:
        ans_l = self.f(ans_l, self.g(self.seg[l], self.lazy[l]))
        l += 1
      if r & 1:
        r -= 1
        ans_r = self.f(self.g(self.seg[r], self.lazy[r]), ans_r)
      l >>= 1
      r >>= 1
    return self.f(ans_l, ans_r)

# X(要素) -> (文字列の長さ, sum)
# M(作用) -> 置き換える数字

mod=998244353
n,q=map(int,input().split())
num=2**((n-1).bit_length())
p=[]
for i in range(num):
  if i<n:
    p.append(200002)
  else:
    p.append(0)
digit=[1]
for _ in range(num):
  digit.append(digit[-1]*10%mod)
inv9=pow(9,mod-2,mod)
def f(a,b):
  asum,alen=divmod(a,200001)
  bsum,blen=divmod(b,200001)
  return ((digit[blen]*asum+bsum)%mod)*200001+alen+blen
def g(x,y):
  if y is None:
    return x
  _,xlen=divmod(x,200001)
  return ((digit[xlen]-1)*inv9*y%mod)*200001+xlen
def h(x,y):
  if y is None:
    return x
  return y
seg=LazySegmentTree(num,p,0,None,f,g,h)
for _ in range(q):
  l,r,d=map(int,input().split())
  seg.update(l-1,r,d)
  ans,_=divmod(seg.query(0,n),200001)
  print(ans)
