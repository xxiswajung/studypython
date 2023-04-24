from collections import deque

arr=[list(map(int,input().split())) for _ in range(7)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
ch=[[0]*7 for _ in range(7)]
Q=deque()
Q.append((0,0))
arr[0][0]=1
while Q:
    res=Q.popleft()
    for i in range(4):
        x=res[0]+dx[i]
        y=res[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and arr[x][y]==0:
            arr[x][y]=1 #지나온길 다시 못 가게 
            ch[x][y]=ch[res[0]][res[1]]+1
            Q.append((x,y))
if ch[6][6]==0:
    print(-1)
else:
    print(ch[6][6])
