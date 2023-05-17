n=int(input())
arr=[]
for _ in range(n):
    arr.append(tuple(map(int,input().split())))
arr.sort(key=lambda x : (x[1],x[0]),reverse=True)

cnt=0
hg = 0

for x,y in arr:
    if hg < x:
        cnt+=1
        hg=x
print(cnt)
