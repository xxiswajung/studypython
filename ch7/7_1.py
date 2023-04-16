def DFS(v,C,L):
    global res
    if L>m: #if v==n if res>=C 는 따로 명령어를 적지 않았으므로 자동으로 return(종료)
        return
    if v==n: #모든 문제의 풀이여부를 다 확인하고 난 뒤 최종 점수 확인
        if res<C:
            res=C
    else:
        DFS(v+1,C+S[v],L+T[v])
        DFS(v+1,C,L)

if __name__=='__main__':
    n,m=map(int,input().split())
    S=[]
    T=[]
    for _ in range(n):
        s,t=map(int,input().split())
        S.append(s)
        T.append(t)
    res=0
    DFS(0,0,0)
    print(res)
