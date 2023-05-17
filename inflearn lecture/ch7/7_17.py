def DFS(L,s): #combination 조합 방법과 비슷하게 풀이
    global res

    if L==m:
        sum=0
        for j in range(len(hs)):
            x1=hs[j][0]
            y1=hs[j][1]
            dis=21470000

            for x in cb:
                x2=pz[x][0]
                y2=pz[x][1]
                dis=min(dis,abs(x1-x2)+abs(y1-y2))
            sum+=dis
        if sum<res:
            res=sum
    else:
        for i in range(s,len(pz)):
            cb[L]=i
            DFS(L+1,i+1)


if __name__=="__main__":
    n,m=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]
    hs=[] #집 좌표
    pz=[] #피자가게 좌표
    cb=[0]*m #combination, 살아남는 피자가게의 경우의수
    res=21470000

    for i in range(n):
        for j in range(n):
            if arr[i][j]==1:
                hs.append((i,j))
            elif arr[i][j]==2:
                pz.append((i,j))
    DFS(0,0) 
    print(res)
