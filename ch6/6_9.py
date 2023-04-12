def DFS(v):
    global res

    if v==n:
        s=[]
        for j in range(n):
            s.append(res[j])
        while len(s)!=1:
            for i in range(len(s)-1):
                s.append(s[0]+s[1])
                s.pop(0)
            s.pop(0)
        if s[0]==f:
            for k in range(n):
                print(res[k],end=' ')
            sys.exit(0)
    
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res.append(i)
                DFS(v+1)
                res.pop()
                ch[i]=0

if __name__=="__main__":
    n,f=map(int,input().split())
    ch=[0]*(n+1) #중복 방지 배열
    res=[]
    DFS(0)
    
#######################################

#빨리 계산하기 위해 이항계수를 사용한 방법

def DFS(v,sum):
    
    if v==n and sum==f:
        for x in p:
            print(x,end=' ')
        sys.exit(0)
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                p[v]=i
                DFS(v+1,sum+(p[v]*b[v])) 
                ch[i]=0


if __name__=="__main__":
    n,f=map(int,input().split())
    p=[0]*n #배열
    b=[1]*n #이항계수
    ch=[0]*(n+1) #중복 방지 배열
    
    for i in range(1,n):
        b[i]=b[i-1]*(n-i)//i #combination 공식

    DFS(0,0)

#######################################

# 이항계수(원래 이렇게 풀어야 함)+라이브러리 사용
# same as 6_12.py

import itertools as it

n,f=map(int,input().split())
b=[1]*n
for i in range(1,n):
    b[i]=b[i-1]*(n-i)//i
a=list(range(1,n+1))

for tmp in it.permutations(a):
    sum=0
    for L,x in enumerate(tmp):
        sum+=(b[L]*x)
    if sum==f:
        for x in tmp:
            print(x, end=' ')
        break
