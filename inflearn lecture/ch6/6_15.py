def DFS(v):
    global cnt
    if v==n-1:
        cnt+=1

    else:
        for i in range(1,n):
            if ch[v][i]==1 and res[i]!=1:
                res[i]=1
                DFS(i)
                res[i]=0
        
if __name__=="__main__":
    n,m=map(int,input().split())
    ch=[[0]*n for i in range(n)]
    for i in range(m):
        a,b=map(int,input().split())
        ch[a-1][b-1]=1
    cnt=0
    res=[0]*n
    DFS(0)
    print(cnt)
    
#경로까지 출력 + 입력 받은 인덱스와 값 그대로 배열에 반영하는 코드 (똑같음 단지 시작지점이 다를 뿐)

def DFS(v):
    global cnt
    if v==n:
        cnt+=1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1,n+1): #i: 방문하려는 노드
            if g[v][i]==1 and ch[i]==0:
                ch[i]=1
                path.append(i)
                DFS(i)
                ch[i]=0
                path.pop()        
if __name__=="__main__":
    n,m=map(int,input().split())
    g=[[0]*(n+1) for _ in range(n+1)] #인접행렬
    ch=[0]*(n+1) #지나간 길 체크
    for i in range(m):
        a,b=map(int,input().split())
        g[a][b]=1
    cnt=0
    path=[]
    path.append(1)
    ch[1]=1
    DFS(1)
    print(cnt)
