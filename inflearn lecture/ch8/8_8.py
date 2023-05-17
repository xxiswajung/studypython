def TD(a,b):
    if dy[a][b]>0:
        return dy[a][b]
    if a==0:
        dy[a][b]=TD(a,b-1)+arr[a][b]
    elif b==0:
        dy[a][b]=TD(a-1,b)+arr[a][b]
    else:
        dy[a][b]=min(TD(a-1,b),TD(a,b-1))+arr[a][b]
    return dy[a][b]

if __name__=="__main__":
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    dy=[[0]*n for _ in range(n)]
    dy[0][0]=arr[0][0]
    print(TD(n-1,n-1))
