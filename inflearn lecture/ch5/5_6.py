from collections import deque

n,m=map(int,input().split())
arr=[(pos,val) for pos, val in enumerate(list(map(int,input().split())))]
arr=deque(arr)
cnt=0

while True:
    cur=arr.popleft()
    if any(cur[1]<x[1] for x in arr):
        arr.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break
