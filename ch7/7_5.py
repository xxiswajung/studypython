def DFS(v,A,B,C):
    global res
    if v==n:
        if A==B or B==C or A==C:
            return
        else:
            list=[A,B,C]
            ma=max(list)
            ni=min(list)
            if res>ma-ni:
                res=ma-ni
    else:
        DFS(v+1,A+arr[v],B,C)
        DFS(v+1,A,B+arr[v],C)
        DFS(v+1,A,B,C+arr[v])


if __name__=="__main__":
    n=int(input())
    arr=[]
    for _ in range(n):
        arr.append(int(input()))
    res=21470000
    DFS(0,0,0,0)
    print(res)
