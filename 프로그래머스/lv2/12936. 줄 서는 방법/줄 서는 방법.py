import math

def solution(n, k):
    k-=1
    answer = []
    array = [i for i in range(1,n+1)]
    
    for i in range(n,0,-1):
        div, k = divmod(k,math.factorial(i-1))
        answer.append(array.pop(div))
    return answer