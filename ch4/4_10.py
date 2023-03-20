n=int(input())
arr=list(map(int,input().split()))
arr2=[0]*n

for i in range(n):
    cnt=0
    for j in range(n):
        if cnt==arr[i] and arr2[j]==0:
            arr2[j]=i+1
            break
        if arr2[j] == 0:
            cnt+=1
    
for x in arr2:
    print(x,end=' ')
