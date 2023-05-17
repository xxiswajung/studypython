def DFS(v):
    global cnt

    if v==m:
        for k in range(m):
            print(res[k],end=' ')
        print()
        cnt+=1

    else:
        for i in range(1,n+1):
            if i not in res:
                res[v]=i
                DFS(v+1)
                res[v]=0
            
if __name__=="__main__":
    n,m=map(int,input().split())
    cnt=0
    res=[0]*m
    DFS(0)
    print(cnt)
