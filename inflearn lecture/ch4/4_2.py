def Count(len):
    cnt=0
    for x in arr:
        cnt+=(x//len)
    return cnt

k,n = map(int,input().split())
arr=[]
for i in range(k):
    arr.append(int(input()))
    
lt = 1
rt = max(arr)
res=0

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        lt=mid+1
        res=mid
    else:
        rt=mid-1
print(res)
