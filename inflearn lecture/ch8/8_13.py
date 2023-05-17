n=int(input())
matrix=[[100]*(n+1) for _ in range(n+1)]
while True:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    matrix[a][b]=1
    matrix[b][a]=1

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if matrix[i][j]>matrix[i][k]+matrix[k][j]:
                matrix[i][j]=matrix[i][k]+matrix[k][j]
#########################################################
#sol.1

min=1247000
arr=[]
res=0
for i in range(n+1):
    if min>sum(matrix[i]):
        min=sum(matrix[i])
        res=max(matrix[i][1:n+1])    
for i in range(n+1):
    if min==sum(matrix[i]):
        arr.append(i) 
print(res, len(arr))
for x in arr:
    print(x,end=' ')
    
#########################################################
#sol.2

score=100
arr=[]
res=[0]*(n+1)
for i in range(1,n+1):
    for j in range(1,n+1):
        res[i]=max(res[i],matrix[i][j]) #각 사람별 배열(res)에 최대 점수 뽑기
    score=min(score,res[i]) #그 사람들 중 가장 점수가 작은 사람 뽑기
print(res)
for i in range(1,n+1):
    if res[i]==score:
        arr.append(i) 
print(score, len(arr))
for x in arr:
    print(x,end=' ')
