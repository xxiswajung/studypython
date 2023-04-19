def DFS(v,sum):
    global cnt
    if sum>T:
        return
    if v==k:
        if sum==T:
            cnt+=1
    else:
        for j in range(n[v]+1):
            DFS(v+1,sum+(p[v]*j))


if __name__=="__main__":
    T=int(input())
    k=int(input())
    p=[]
    n=[]
    total=0
    for _ in range(k):
        a,b=map(int,input().split())
        p.append(a)
        n.append(b)
    cnt=0
    DFS(0,0)
    print(cnt)
