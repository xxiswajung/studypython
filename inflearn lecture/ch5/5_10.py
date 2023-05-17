##heap 이용하기

import heapq as hq
a=[]
while True:
    n=int(input())
    if n==-1:
        break
    elif n==0:
        if len(a)==0:
            print(-1)
        else:
            print(hq.heappop(a)) #a 리스트에서 pop 해라 -> 최상의 부모노드(=최솟값)가 pop 된다
    else:
        hq.heappush(a,n) #a라는 리스트에 n 값을 push 해라

##그냥 풀기

arr=[]
while True:
    a=int(input())
    if a==-1:
        break
    elif a==0: 
        if len(arr)==0:
            print(-1)
        else:
            c=min(arr)
            b=arr.index(c)
            arr.pop(b)
            print(c)
    else:
        arr.append(a)
        
   
