def DFS(v,P):
    global cnt
    if v==n:
        cnt+=1
        for j in range(P):
            print(chr(res[j]+64), end='')
        print()
    else:
        for i in range(1,27):
            if arr[v]==i:
                res[P]=i
                DFS(v+1,P+1)
            elif i>=10 and arr[v]==i//10 and arr[v+1]==i%10:
                res[P]=i
                DFS(v+2,P+1)



if __name__=="__main__":
    arr=list(map(int,input()))
    n=len(arr)
    arr.insert(n,-1) #25114인 경우, 마지막 숫자를 4n 으로 인식하게 되면 elif 에서 arr[v+1] index out of range 문제 발생함 -> 두자리수로 인식 못하게 -1 추가
    res=[0]*(n+3)
    cnt=0
    DFS(0,0)
    print(cnt)
