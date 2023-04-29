from collections import deque

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
Q=deque()
cnt=0

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            Q.append((i,j))
            cnt+=1
            arr[i][j]=0
            while Q:
                res=Q.popleft()
                for k in range(8):
                    x=res[0]+dx[k]
                    y=res[1]+dy[k]
                    if 0<=x<n and 0<=y<n and arr[x][y]==1:
                        arr[x][y]=0
                        Q.append((x,y))
print(cnt)
