from collections import deque
def solution(maps):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    n=len(maps)
    m=len(maps[0])
    answer=1
    Q=deque()
    Q.append((0,0,answer))
    
    while Q:
        x,y,answer=Q.popleft()
        maps[x][y]=0
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if xx==n-1 and yy==m-1:
                return answer+1
            elif 0<=xx<n and 0<=yy<m and maps[xx][yy]==1:
                Q.append((xx,yy,answer+1))
                maps[xx][yy]=0
    return -1