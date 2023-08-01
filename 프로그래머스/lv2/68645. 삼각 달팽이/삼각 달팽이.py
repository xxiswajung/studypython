def solution(n):
    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0 # for문 실행시 x값을 처음에 0으로 세팅해주기 위해 초기값은 -1로 세팅
    num = 1
    
    for i in range(n): # 조건문 3개인 이유 : 방향을 트는 경우가 3가지(아래, 오른쪽, 위) 이기 때문
        for j in range(i, n): 
            if i % 3 == 0:      # 아래
                x += 1          
            elif i % 3 == 1:    # 오른쪽
                y += 1            
            elif i % 3 == 2:    # 위
                x -= 1
                y -= 1      
            res[x][y] = num
            num += 1
            
    for i in res:
        for j in i:
            if j:
                answer.append(j)
    return answer