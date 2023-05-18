import sys
sys.stdin=open("input.txt","r")

from collections import deque
n,m=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)] #인접행렬
degree=[0]*(n+1) #진입차수
dQ=deque()

for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1 #a에서 b로 일방향으로 갈 수 있다. 방향 그래프 
    degree[b]+=1
for i in range(1,n+1):
    if degree[i]==0:
        dQ.append(i)
while dQ:
    x=dQ.popleft()
    print(x, end=' ')
    for i in range(1,n+1):
        if graph[x][i]==1:
            degree[i]-=1
            if degree[i]==0:
                dQ.append(i)