n = int(input())
res = 0

for _ in range(n):
    money=0
    arr=list(map(int,input().split()))
    if arr[0]==arr[1]==arr[2]:
        money = 10000+arr[0]*1000
    elif arr[0]!=arr[1]!=arr[2]:
        money = max(arr)*100
    else:
        arr2=[0]*7
        ind = 0
        for x in arr :
            arr2[x] += 1
        max_num = arr2.index(max(arr2))
        money = 1000 + max_num*100
    if money > res :
        res=money
print(res)
