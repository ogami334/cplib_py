#ソース　　　https://qiita.com/dn6049949/items/afa12d5d079f518de368#非再帰型segment-treeの実装
class SegmentTree:#再帰
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length() # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default]*(self.size*2-1) # 要素を単位元で初期化
        self.f = f

    def update(self, i, x):
        i += self.size-1
        self.dat[i] = x
        while i > 0:
            i = (i-1) >> 1
            self.dat[i] = self.f(self.dat[i*2+1], self.dat[i*2+2])

    def query(self, l, r, k=0, L=0, R=None):
        if R is None:
            R = self.size
        if R <= l or r <= L:
            return self.default
        if l <= L and R <= r:
            return self.dat[k]
        else:
            lres = self.query(l, r, k*2+1, L, (L+R) >> 1)
            rres = self.query(l, r, k*2+2, (L+R) >> 1, R)
            return self.f(lres, rres)



class SegmentTree:#非再帰(こちらの方が速い) #1-indexed
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        if size==1:
            self.size=2
        else:
            self.size = 2**(size-1).bit_length() # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default]*(self.size*2) # 要素を単位元で初期化
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])

    def query(self, l, r):
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres) # モノイドでは可換律は保証されていないので演算の方向に注意
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res
