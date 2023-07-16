def solution(m, n, board):
    answer = 0
    # 1. 삭제할 블록을 중복없이 담을 집합 만들기
    rm=set()
    # 2. 문자열 board를 리스트 board로 바꿔 작업하기 쉽게 하기
    for i in range(m):
        board[i] = list(board[i])
    
    # 3. 종료시점 = 더 이상 위의 블록이 아래 블록을 채울 필요가 없을때 = 2X2 블록이 안 만들어질 때
    while True:
        # 4. 탐색범위 = 2X2 블록이 닿을 수 있는 범위 까지, 끝까지 갈 필요는 없음
        for i in range(m-1):
            for j in range(n-1):
                # 5. 빈칸인 경우, 2X2 블록 취급을 안 하므로 패스
                if board[i][j]==[]:
                    continue
                if board[i][j]==board[i][j+1]==board[i+1][j]==board[i+1][j+1]:
                    rm.add((i,j))
                    rm.add((i,j+1))
                    rm.add((i+1,j))
                    rm.add((i+1,j+1))
        # 6. board 다 탐색 후(끝난 것 아님), 제거해야할 블록이 있는 경우 : 블록 제거 후 개수 세기
        if rm:
            # 테스트 케이스의 블록의 크기가 4개인 경우, 6개인 경우로 나누면 커버할 수 없는 경우가 발생함 (ex. 블록의 크기가 7개). 따라서, 삭제할 블록의 좌표를 중복없이 기록하기 위해서 '집합'을 사용하여 좌표를 카운트한다. 
            answer+=len(rm)               
            for i, j in rm:
                board[i][j]=[]
            rm=set()
        # 7. 더 이상 제거할 블록이 없는 경우, 정답 리턴
        else:
            return answer
        
        # 8. 위의 블록을 아래로 내려 삭제된 블록 채우기
        while True:
            moved=0
            # 9. 위에서 아래로 내릴 때, 맨 아랫줄까지 건드릴 필요는 없으므로 m-1 까지
            for i in range(m-1):
                for j in range(n):
                    if board[i][j]!=[] and board[i+1][j]==[]:
                        board[i+1][j] = board[i][j]
                        board[i][j]=[]
                        moved=1
                    # 배열 슬라이스 덧셈으로 식을 바꾸면 경우의 수가 너무 많아지므로, board의 각 원소 마다 접근해서 변경해야함(일반화된 공식을 세울 수 있어야 함)
            if moved == 0:
                break
