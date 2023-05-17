n,m=map(int,input().split())
matrix=[[100]*n for _ in range(n)]

for _ in range(m):
    a,b,c=map(int,input().split())
    matrix[a-1][b-1]=c

for k in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])
for i in range(n):
    matrix[i][i]=0
for x in range(n):
    for y in range(n):
        if matrix[x][y]==100:
            matrix[x][y]='M'

for x in range(n):
    for y in range(n):
        print(matrix[x][y],end=' ')
    print()
