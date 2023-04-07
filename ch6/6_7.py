def DFS(v,S):
    global min
    if S>m or v>=min :
        return
    if S==m:
        if min>v:
            min=v
    else:
        for i in range(n):
            DFS(v+1,S+arr[i])


if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    m=int(input())
    min=21480000
    arr.sort(reverse=True)
    DFS(0,0)
    print(min)
