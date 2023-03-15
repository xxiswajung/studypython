n=int(input())
arr=[]
for _ in range(n):
    arr.append(tuple(map(int,input().split())))
arr.sort(key=lambda x: (x[1],x[0])) #빨리 끝내고 더 많은 회의를 잡아야 하므로, 끝나는 시간으로 정렬해야 한다.

cnt=0
et=0 # 끝나는 시간의 변수

for x, y in arr:
    if x >= et: #빨리 끝나는 순서대로 정렬을 이미 했기 때문에, 첫번째 원소의 시작 시간은 고정
        cnt+=1
        et=y
print(cnt)
