from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=int(input())
arr=[list(map(int,input())) for _ in range(n)]
Q=deque()
cnt=0
nmr=[]

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            arr[i][j]=0
            cnt=1
            Q.append((i,j))
            while Q:
                res=Q.popleft()
                for k in range(4):
                    x=res[0]+dx[k]
                    y=res[1]+dy[k]
                    if 0<=x<n and 0<=y<n and arr[x][y]==1:
                        arr[x][y]=0
                        cnt+=1
                        Q.append((x,y))
            nmr.append(cnt)
print(len(nmr))
nmr.sort()
for x in nmr:
    print(x)
