n=int(input())
arr=list(map(int,input().split()))

pk=0
cnt=0
arr2=[]
while True:
    if pk>arr[0] and pk<arr[-1]:
        cnt+=1
        pk=arr.pop()
        arr2.append("R")
    elif pk<arr[0] and pk>arr[-1]:
        cnt+=1
        pk=arr.pop(0)
        arr2.append("L")
    elif pk<arr[0] and pk<arr[-1]:
        if arr[0]<arr[-1]:
            cnt+=1
            pk=arr.pop(0)
            arr2.append("L")
        else:
            cnt+=1
            pk=arr.pop()
            arr2.append("R")
    else:
        break
print(cnt)
for x in arr2:
    print(x,end='')
