def DFS(t,p):
    global res
    if t==n+1: #종료지점
        if p>res:
            res=p
    else:
        if t+T[t]<=n+1:
            DFS(t+T[t],p+P[t])
        DFS(t+1,p) #오늘은 상담 안하고 내일로 넘김

if __name__=="__main__":
    n=int(input())
    T=[]
    P=[]
    for _ in range(n):
        a,b=map(int,input().split())
        T.append(a) #index를 날짜로 사용하기 위해
        P.append(b)
    T.insert(0,0)
    P.insert(0,0)
    res=0
    DFS(1,0)
    print(res)
