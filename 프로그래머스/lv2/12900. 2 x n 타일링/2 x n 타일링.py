def solution(n):
    dy=[0]*(n+1)
    dy[1]=1
    dy[2]=2
    
    for i in range(3,n+1):
        dy[i]=(dy[i-1]+dy[i-2])%1000000007
        
    return dy[n]