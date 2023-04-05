def DFS(v,s,ts): #ts: 지금까지 부분집합으로 고려된 원소들의 합
    global max #전역변수로 사용
    if s+(arrs-ts)<max: #시간단축, time error 피하기 위해 작성
        return #현재 부분집합의 합+(남은 원소들의 총 합)이 최댓값보다 작으면 더이상 볼 필요 없음
    if s>c:
        return
    else:
        if v==n:
            if max<s:
                max=s
        else:
            DFS(v+1,s+arr[v],ts+arr[v])
            DFS(v+1,s,ts+arr[v])


if __name__=="__main__":
    c,n=map(int,input().split())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    arrs=sum(arr)
    max=0
    DFS(0,0,0)
    print(max)
