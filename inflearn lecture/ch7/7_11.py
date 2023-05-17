def DFS(x,y):
    global cnt
    if x==c and y==d:
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<n and arr[x][y]<arr[xx][yy]:
                ch[xx][yy]=1
                DFS(xx,yy)
                ch[xx][yy]=0

if __name__=="__main__":
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    ch=[[0]*n for _ in range(n)]
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    cnt=0
    p=min(map(min,arr))
    q=max(map(max,arr))
    for i in range(n):
        for k in range(n):
            if arr[i][k]==p:
                a=i
                b=k
            if arr[i][k]==q:
                c=i
                d=k
    ch[a][b]=1
    DFS(a,b)
    print(cnt)
