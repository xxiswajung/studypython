n=int(input())
arr=[]
max =0

for i in range(n):
    arr.append(list(map(int,input().split())))


for j in range(n):
    if max < sum(arr[j]):
        max=sum(arr[j])


for i in range(n):
    res = 0
    for j in range(n):
        res += arr[j][i]
    if res > max:
        max = res

res = 0
res2 = 0
for i in range(n):
    res += arr[i][i]
    res2 += arr[n-1-i][i]

if res2 > res : 
    res=res2
if res > max:
    max = res
print(max)
