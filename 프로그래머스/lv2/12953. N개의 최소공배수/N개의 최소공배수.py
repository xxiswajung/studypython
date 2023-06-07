def solution(arr):
    a=max(arr)
    b=1
    for x in arr:
        b*=x
    for i in range(a,b+1):
        if all(i % num == 0 for num in arr) is True:
                return i
            
#####################
#Use Math Package and gcd

from math import gcd

def solution(arr):
    answer = 1
    for i in range(1, len(arr)):
        answer = (answer*arr[i]) // gcd(answer, arr[i]) 
        #최소공배수 = 두수의 곱 // 두수의 최대공약수
        #2개의 최소공배수를 먼저 구해 그 값과 arr의 다음값의 최소공배수를 구한다. 이를 반복!
    return answer
