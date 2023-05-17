dx=[-1,0]
dy=[0,-1]
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
dd=[[0]*n for _ in range(n)]
dd[0][0]=arr[0][0]

for i in range(n):
    for j in range(n):
        min=1240
        if i==0 and j==0:
            continue
        else:
            for k in range(2):
                x=i+dx[k]
                y=j+dy[k]
                if 0<=x<n and 0<=y<n and min>dd[x][y]:
                    min=dd[x][y]
            dd[i][j]=min+arr[i][j]
print(dd[n-1][n-1])

#####################################################
n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
dy=[[0]*n for _ in range(n)]
dy[0][0]=arr[0][0]
for i in range(1, n):
    dy[0][i]=dy[0][i-1]+arr[0][i]
    dy[i][0]=dy[i-1][0]+arr[i][0]
for i in range(1, n):
    for j in range(1, n):
        dy[i][j]=min(dy[i-1][j], dy[i][j-1])+arr[i][j]
print(dy[n-1][n-1])
