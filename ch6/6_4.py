import sys

def DFS(v):
    res=0
    if v==n:
        for i in range(n):
            if ch[i]==1:
                res+=arr[i]
        if res==(total-res): #res==total//2 가 안되는 이유 : total이 홀수인 경우는 무조건 NO인데, 이런경우 YES가 나올 수 있기 때문
            print("YES")
            sys.exit(0) #프로그램을 아예 종료
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    total=sum(arr)
    ch=[0]*n
    DFS(0)
    print("NO")
    
#############################
import sys

def DFS(v,res):
    if res>total//2: #시간복잡도를 줄이기 위해
        return #부분집합의 합이 전체집합의 합의 반보다 큰 경우 더이상 볼 필요가 없음
    if v==n:
        if res==(total-res):  #res==total//2 가 안되는 이유 : total이 홀수인 경우는 무조건 NO인데, 이런경우 YES가 나올 수 있기 때문
            print("YES")
            sys.exit(0) #프로그램을 아예 종료
    
    else:
        DFS(v+1,res+arr[v])
        DFS(v+1,res)


if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    total=sum(arr)
    DFS(0,0)
    print("NO")
