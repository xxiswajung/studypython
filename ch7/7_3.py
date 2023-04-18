def DFS(v,L,M):
    global cnt
    if v==k:
        res=abs(L-M)
        ch[res]=1
    else:
        DFS(v+1,L+arr[v],M)
        DFS(v+1,L,M+arr[v])
        DFS(v+1,L,M)


if __name__=="__main__":
    k=int(input())
    arr=list(map(int,input().split()))
    S=sum(arr)
    ch=[0]*(S+1)
    cnt=0
    DFS(0,0,0)
    print(ch.count(0))
