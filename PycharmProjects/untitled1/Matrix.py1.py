from random import *
class Matrix:
    def __init__(self,m=None,n=None):
        self.m=m
        self.n=n
        try:
            if (n>0)and(m>0):
                self.x=[]
                self.x=[[randint(1,5) for i in range(self.n)]for j in range(self.m)]
                print(self.x)
            else:
                raise Exception()
        except Exception as e:
            print('ValueError')
    def get_m(self):
        return self.m
    def get_n(self):
        return self.n
    def get_size(self):
        return (self.m,self.n)
    def get(self,i,j):
        Q=self.x[i]
        Q1=Q[j]
        return Q1
    def set(self,i,j,value):
        Q=self.x[i]
        Q[j]=value
        self.x[i:i]=[Q]
        self.x.pop(i+1)
        return (self.x)
    def __eq__(self,other):
        try:
            if (self.m==other.m)and(self.n==other.n):
                log=True
                Q1=[]
                Q2=[]
                for i in range(self.m):
                    Q1=self.x[i]
                    Q2=other.x[i]
                    for j in range(self.n):
                        if Q1[j]!=Q2[j]:
                            log=False
                            break
                    if log==False:
                        break
                print(log)
            else:
                raise RuntimeError()
        except RuntimeError as p:
            print('RuntimeError')
    def __add__(self, other):
        try:
            if (self.m==other.m)and(self.n==other.n):
                c=[]
                c=[[0 for i in range(self.n)]for j in range(self.m)]
                for i in range(self.m):
                    Q1=[]
                    Q2=[]
                    Q1=self.x[i]
                    Q2=other.x[i]
                    Q3=[]
                    for j in range(self.n):
                        sum=Q1[j]+Q2[j]
                        Q3=Q3+[sum]
                    c[i:i]=[Q3]
                    c.pop(i+1)
                print(c)
            else:
                raise RuntimeError()
        except RuntimeError as e:
            print('RuntimeError')
    def __sub__(self,other):
        try:
            if(self.m==other.m)and(self.n==other.n):
                c=[]
                c=[[0 for i in range(self.n)]for j in range (self.m)]
                for i in range(self.m):
                    Q1=[]
                    Q2=[]
                    Q1=self.x[i]
                    Q2=other.x[i]
                    Q3=[]
                    for j in range(self.n):
                        difference=Q1[j]-Q2[j]
                        Q3=Q3+[difference]
                    c[i:i]=[Q3]
                    c.pop(i+1)
                print(c)
            else:
                raise RuntimeError()
        except RuntimeError as e:
            print('RuntimeError')
    def __mul__(self,other):
        try:
            if(self.n==other.m):
                c=[]
                c=[[0 for i in range(self.n)]for j in range (self.m)]
                k=0
                for i in range(self.m):
                    Q1=[]
                    Q1=self.x[i]
                    Q3=[]
                    Q2=[]
                    for f in range (other.n):
                        sum=0
                        for j in range(other.m):
                            Q2=other.x[j]
                            mult=Q1[j]*Q2[k]
                            sum=sum+mult
                        if k<other.n:
                            k+=1
                        Q3=Q3+[sum]
                    c[i:i]=[Q3]
                    c.pop(i+1)
                    print('multiplication=',c)
            else:
                raise RuntimeError()
        except RuntimeError as error:
            print('RuntimeError')

a=Matrix(int(input()),int(input()))
b=Matrix(int(input()),int(input()))
a.__mul__(b)