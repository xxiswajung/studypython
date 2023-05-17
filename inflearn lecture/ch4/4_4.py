def Count(len):
    cnt=1 # 말 1마리 배치
    ep=arr[0] # 말 배치 end point, 말 1마리를 end point에 배치한다
    for i in range(1,n):
        if arr[i]-ep>=len: #배치할 말의 위치와 이미 배치한 말 간의 거리가 주어진 거리보다 멀거나 같은지
            cnt+=1
            ep=arr[i]
    return cnt

n,c=map(int,input().split())
arr=[]
arr2=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort()

lt=1
rt=arr[n-1]

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)
