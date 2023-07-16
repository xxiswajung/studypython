def solution(m, n, board):
    answer = 0
    rm=set()
    for i in range(m):
        board[i] = list(board[i])
    
    while True:
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]==[]:
                    continue
                if board[i][j]==board[i][j+1]==board[i+1][j]==board[i+1][j+1]:
                    rm.add((i,j))
                    rm.add((i,j+1))
                    rm.add((i+1,j))
                    rm.add((i+1,j+1))
        if rm:
            answer+=len(rm)               
            for i, j in rm:
                board[i][j]=[]
            rm=set()
        else:
            return answer
                           
        while True:
            moved=0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j]!=[] and board[i+1][j]==[]:
                        board[i+1][j] = board[i][j]
                        board[i][j]=[]
                        moved=1
            if moved == 0:
                break