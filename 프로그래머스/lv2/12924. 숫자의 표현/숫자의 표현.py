def solution(n):
    answer = 0
    for i in range(1,n+1):
        if i>n//2:
            break
        sum=0
        for j in range(i,n+1):
            sum+=j
            if sum>n:
                break
            if sum==n:
                answer+=1
                break
    answer+=1
    return answer