def solution(n):
    a=format(n,'b')
    a=a.count('1')
    num=n
    while True:
        num+=1
        if a==format(num,'b').count('1'):
            answer=num
            break
    return answer