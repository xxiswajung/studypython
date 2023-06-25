def solution(n, k):
    answer = 0
    base = ''
    while n > 0:
        n, mod = divmod(n, k)
        base += str(mod)
    base=base[::-1].split('0')
    
    for x in base:
        chk=True
        if x=='' or int(x)<2:
            continue
        else:
            #모든 수의 약수는 대칭을 이루므로, 2~제곱근의 범위에서 소수가 없다면 이 수는 소수이다
            for i in range(2, int(int(x)**0.5) + 1):
                if int(x) % i == 0:
                    chk=False
                    break
            if chk==True:
                answer+=1
    return answer
            
