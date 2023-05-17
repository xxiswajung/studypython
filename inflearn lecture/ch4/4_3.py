def Count(len):
    cnt = 1
    a = 0
    for x in arr:
        if a+x > len:
            a = x
            cnt+=1
        else: 
            a += x
    return cnt

n,m=map(int,input().split())
arr=list(map(int,input().split()))

lt=1
rt=sum(arr)
res=0

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)<=m:
        rt=mid-1
        res=mid
    else:
        lt=mid+1
print(res)
