n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
b=[[0]*(n+2) for _ in range(n+2)]

for i in range(n):
    for j in range(n):
        b[i+1][j+1]=a[i][j]

cnt=0

for i in range(1,n+1):
    for j in range(1,n+1):
        if b[i][j]>b[i][j-1] and b[i][j]>b[i][j+1] and b[i][j]>b[i-1][j] and b[i][j]>b[i+1][j]:
            cnt+=1

print(cnt)

#OR
n=int(input())
dx=[-1,0,1,0] #상하좌우 확인할 때 미리 선언하자
dy=[0,1,0,-1] #상하좌우 확인할 때 미리 선언하자
a=[list(map(int, input().split())) for _ in range(n)]
a.insert(0,[0]*n) # 위 : 리스트 두개 만들어서 하나씩 원소 합치기, 아래 : 기존 리스트에 insert, append 이용해서 원소 추가하기
a.append([0]*n)
for x in a:
    x.insert(0,0)
    x.append(0)

cnt=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1

print(cnt)

