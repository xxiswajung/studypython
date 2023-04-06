import sys
input=sys.stdin.readline #대량으로 입력 받을때 빨리 받을 수 있음

def DFS(L):
    global cnt
    if L==m:
        for k in range(m):
            print(res[k], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            res[L]=i
            DFS(L+1)

if __name__=="__main__":
    n,m=map(int,input().split())
    res=[0]*m
    cnt=0
    DFS(0)
    print(cnt)
