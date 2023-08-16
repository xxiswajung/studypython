def solution(rows, columns, queries):
    answer = []
    board = [[0]*columns for _ in range(rows)]
    k = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j]=k
            k+=1
    for x in queries:
        x1=x[0]-1
        y1=x[1]-1
        x2=x[2]-1
        y2=x[3]-1
        tmp=board[x1][y1]
        min_=tmp
        
        for i in range(x1,x2):
            board[i][y1]=board[i+1][y1]
            min_=min(min_,board[i][y1])
        for i in range(y1,y2):
            board[x2][i]=board[x2][i+1]
            min_=min(min_,board[x2][i])
        for i in range(x2,x1,-1):
            board[i][y2]=board[i-1][y2]
            min_=min(min_,board[i][y2])
        for i in range(y2,y1,-1):
            board[x1][i]=board[x1][i-1]
            min_=min(min_,board[x1][i])
        board[x1][y1+1]=tmp
        answer.append(min_)
        
    return answer