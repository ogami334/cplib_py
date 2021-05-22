from math import gcd
class LDE:
    def __init__(self,a,b,c):
        self.a,self.b,self.c = a,b,c
        self.m,self.x,self.y = 0,[0],[0]
        self.check = True
        g = gcd(self.a, self.b)
        if c % g !=0:
            self.check = False
        else:
            self.extgcd(abs(self.a),abs(self.b),self.x,self.y)
            if a<0:self.x[0]=-self.x[0]
            if b<0:self.y[0]=-self.y[0]
            self.x = self.x[0]*c//g
            self.y = self.y[0]*c//g
            self.a //= g
            self.b //= g

    #拡張ユークリッドの互除法
    #返り値:aとbの最大公約数    
    def extgcd(self,a,b,x0,y0):
        if b==0:
            x0[0],y0[0] = 1,0
            return a
        d = self.extgcd(b,a%b,y0,x0)
        y0[0] -= (a//b)* x0[0]
        return d

    #パラメータmの更新(書き換え)
    def m_update(self,m):
        self.x +=(m-self.m)*self.b
        self.y -=(m-self.m)*self.a
        self.m = m
    def pos_update(self):# to return the minimum pair value
        self.m_update(self.m + min(self.x//(-self.b),(self.y//self.a)))
        #a>0,b<0の時にx>=0,y>=0となるような最小のx,yの組を返す関数
        #自作