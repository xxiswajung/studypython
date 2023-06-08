def solution(n):
    if n<3:
        return n
    dy=[0]*(n+1)
    dy[1]=1
    dy[2]=2
    for i in range(3,n+1):
        dy[i]=dy[i-2]+dy[i-1]
    return dy[n]%1234567