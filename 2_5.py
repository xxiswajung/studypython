n,m=map(int,input().split())
cnt=[0]*(n+m+3) #정n,m면체끼리 더했을때의 모든 결과를 담는 list
max=0

for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]=cnt[i+j]+1 #합의 결과가 나올때마다 가중치 +1

res = max(list)
for i in range(n+m+1):
    if cnt[i]==max: #가장 많이 나온 것들을 뽑아서
        print(i, end=' ') # !!!하나씩!!! 출력, 굳이 list로 축적하지 않아도 됨
