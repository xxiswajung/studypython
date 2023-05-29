def solution(brown, yellow):
    tot = brown+yellow
    for b in range(1,tot+1): #b는 세로
        if tot%b==0: 
            a=tot/b #a는 세로
            if a>=b: #문제조건 : 가로가 세로보다 길거나 같다.
                if 2*a+2*b==brown+4:
                    return [a,b]