L=int(input())
arr=list(map(int,input().split()))
m=int(input())

for i in range(m):
    arr.sort(reverse=True)
    arr[0]-=1
    arr[L-1]+=1
print(max(arr)-min(arr))
