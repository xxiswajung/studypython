import math

def solution(n, k):
    k-=1 #k가 1을 기준으로 시작하기 때문에 1을 줄여준 상태에서 시작
    answer = []
    array = [i for i in range(1,n+1)]
    
    for i in range(n,0,-1):
        div, k = divmod(k,math.factorial(i-1))
        answer.append(array.pop(div))
    return answer
