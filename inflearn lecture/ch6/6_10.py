def DFS(v,s):
    global cnt

    if v==m:
        for i in range(m):
            print(arr[i],end=' ')
        print()
        cnt+=1

    else:
        for i in range(s,n+1):
            arr[v]=i
            DFS(v+1,i+1) 

if __name__=="__main__":
    n,m=map(int,input().split())
    arr=[0]*(n+1)
    cnt=0
    DFS(0,1)
    print(cnt)
