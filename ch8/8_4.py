n=int(input())
arr=list(map(int,input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1]=1
res=0

for i in range(2,n+1):
    max=0
    for j in range(i-1,0,-1):
        if arr[j]<arr[i] and dy[j]>max:
            # 1) 이전 숫자보다 크고(증가수열) 2) 그중 가장 길게 만들수 있는 숫자 찾기
            max=dy[j]
    dy[i]=max+1 # 앞의 숫자들 중 가장 긴 값에서 +1 (=자기자신)
    if dy[i]>res:
        res=dy[i] # 최댓값 구하기
print(res)
