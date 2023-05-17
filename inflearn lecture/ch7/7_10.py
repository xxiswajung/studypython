def DFS(a,b):
    global cnt
    if a==6 and b==6:
        cnt+=1
    else:
        for i in range(4):
            x=a+dx[i]
            y=b+dy[i]
            if 0<=x<=6 and 0<=y<=6 and arr[x][y]==0:
                arr[x][y]=1
                DFS(x,y)
                arr[x][y]=0

if __name__=="__main__":
    arr=[list(map(int,input().split())) for _ in range(7)]
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    arr[0][0]=1
    cnt=0
    DFS(0,0)
    print(cnt)
