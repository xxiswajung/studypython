def DFS(v,s,sum):
    global cnt
    if v==k: #종착지점에 조건문을 2개 이상 걸면, 하나라도 해당이 안되는 것들은 무한반복(=종료 못함)
        if sum%m==0: #따라서 종료조건은 분리해서 이중조건으로 작성
            cnt+=1
    
    else:
        for i in range(s,n):
            DFS(v+1,i+1,sum+arr[i]) #뽑은 배열을 굳이 만들지 말고 계속 누적

if __name__=="__main__":
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    m=int(input())
    cnt=0
    DFS(0,0,0)
    print(cnt) 
