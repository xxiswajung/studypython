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
