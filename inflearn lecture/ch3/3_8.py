n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
m = int(input())

for i in range(m):
    a,b,c=map(int,input().split())
    
#모범 답안
#     if b == 0 : #왼쪽으로 이동
#         for j in range(c):
#             arr[a-1].append(arr[a-1].pop(0))
#     else:
#         for j in range(c): #오른쪽으로 이동
#             arr[a-1].insert(0,arr[a-1].pop())

#내 풀이

    arr1=list()
    arr2=list()
    arr3=list()
    arr4=list()
    arr1=arr[a-1]
    if c >= n :
        c = c % n
    if b == 0: #왼쪽으로
        arr2=arr1[:c]
        arr3=arr1[c:]
    else:
        arr2=arr1[:n-c]
        arr3=arr1[n-c:]
    arr4=arr3+arr2
    arr[a-1]=arr4
for x in arr:
    print(x,end='\n')
s=0
e=n-1
res=0
for i in range(n):
    if s<e:
        res+=sum(arr[i][s:e+1])
    else:
        res+=sum(arr[i][e:s+1])
    s+=1
    e-=1
print(res)
