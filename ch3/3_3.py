arr = list()
for i in range(1,21):
    arr.append(i)

for i in range(10):
    arr2 = list()
    n,m=map(int,input().split())
    arr2 = arr[n-1:m]
    arr2 = arr2[::-1] #arr.sort(reverse=True)는 내림차순으로 정렬하는것이므로, 결과는 무조건 20~1이 나오게 됨. 따라서, 순서만 반대로 뒤집어야 함
    arr[n-1:m] = arr2

for i in arr :
    print(i,end=' ')
