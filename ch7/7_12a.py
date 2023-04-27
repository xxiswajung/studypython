def DFS(x,y):
  global cnt
  cnt+=1
  arr[x][y]=0
  for i in range(4):
    xx=x+dx[i]
    yy=y+dy[i]
    if 0<=xx<n and 0<=yy<n and arr[xx][yy]==1:
      DFS(xx,yy)

if __name__=="__main__":
  n=int(input())
  arr=[list(map(int,input())) for _ in range(n)]
  res=[]
  dx=[-1,0,1,0]
  dy=[0,1,0,-1]
  for i in range(n):
    for j in range(n):
      if arr[i][j]==1:
        cnt=0
        DFS(i,j)
        res.append(cnt)
  print(len(res))
  res.sort()
  for x in res:
    print(x)
