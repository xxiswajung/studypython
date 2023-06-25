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
            # 3부터 root(k)까지 2씩 증가하며 확인(3, 5, 7...),
            # 이는 작은 값들의 배수일 때 발생하는 중복을 제거하며 확인(소수 찾기 최적화)
            for i in range(2, int(int(x)**0.5) + 1):
                if int(x) % i == 0:
                    chk=False
                    break
            if chk==True:
                answer+=1
    return answer
            