n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

cnt=0
while len(arr)>0:
    if len(arr)==1:
        cnt+=1
        break
    sum=arr[0]+arr[-1]
    if sum <= m :
        cnt+=1
        arr.pop()
        arr.pop(0)
    else : 
        arr.pop()
        cnt+=1

print(cnt)
