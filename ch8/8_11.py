n,m=map(int,input().split())
dy=[0]*(m+1)

for i in range(n):
    s,t=map(int,input().split())
    # for j in range(t,m+1):
    #     dy[j]=max(dy[j],dy[j-t]+s) #문제에선 문제를 중복해서 풀지 않는다고 했음 -> 기존방식대로 풀면 안됨!
    for j in range(m,t-1,-1):
        dy[j]=max(dy[j],dy[j-t]+s) #거꾸로 점수를 더해야 중복되지 않음
print(dy[m])
