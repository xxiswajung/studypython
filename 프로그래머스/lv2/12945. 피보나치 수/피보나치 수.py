def solution(n):
    dy=[0,1]
    for i in range(n-1):
        dy.append((dy[i]+dy[i+1])%1234567)
    return dy[n]