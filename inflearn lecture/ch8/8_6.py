n=int(input())
bricks=[]
for _ in range(n):
    a,b,c=map(int,input().split())
    bricks.append((a,b,c))
bricks.sort(reverse=True)
dy=[0]*n
dy[0]=bricks[0][1]
res=bricks[0][1]

for i in range(1,n):
    max_h=0
    for j in range(i-1,-1,-1):
        if bricks[i][2]<bricks[j][2] and max_h<dy[j]:
            max_h=dy[j]
    dy[i]=max_h+bricks[i][1]

    res=max(res,dy[i])
print(res)