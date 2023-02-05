n,k=map(int,input().split())
a=list(map(int,input().split()))

#pick 3 elements from list by combination -> use for loop and access by index
#No duplication result when 3 elements were added -> should use set(), not list[]

result = set()
for i in range(n):
    for j in range (i+1,n):
        for t in range (j+1,n):
            result.add((a[i]+a[j]+a[t]))
res=list(result)
res.sort(reverse=True)
print(res[k-1])

#What is set? 
#집합 : 1) 중복 허용 X 2) 순서 X
#set()에 값을 추가할 땐 'append(list에서 사용)'가 아니라, 'add'를 사용
