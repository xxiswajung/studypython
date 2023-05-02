#compare BFS solving with DFS solving

#BFS
#: using queue
#: copy the input array 

from collections import deque

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
Q=deque()
dx=[-1,0,1,0]
dy=[0,1,0,-1]
maxnum=-21470000
maxv=max(map(max,arr))
tmp=[]
for k in range(1,maxv):
    cnt=0
    arr2=[item[:] for item in arr]
    for j in range(n):
        for t in range(n):
            if arr2[j][t]>k:
                Q.append((j,t))
                cnt+=1
                arr2[j][t]=k
                while Q:
                    res=Q.popleft()
                    for i in range(4):
                        x=res[0]+dx[i]
                        y=res[1]+dy[i]
                        if 0<=x<n and 0<=y<n and arr2[x][y]>k:
                            Q.append((x,y))
                            arr2[x][y]=k
    tmp.append(cnt)
print(max(tmp))


#DFS
#: Set recursion limit to prevent unlimited recursion
#: cnt=0 case means no more loop is needed therefore stop the loop

import sys
sys.setrecursionlimit(10**6)
def DFS(x,y,h):
    ch[x][y]=1
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and arr[xx][yy]>h:
            DFS(xx,yy,h)


if __name__=="__main__":
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    cnt=0
    res=0
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    for h in range(100):
        ch=[[0]*n for _ in range(n)]
        cnt=0
        for i in range(n):
            for j in range(n):
                if ch[i][j]==0 and arr[i][j]>h:
                    cnt+=1
                    DFS(i,j,h)
        res=max(res,cnt)
        if cnt==0:
            break
    print(res)
