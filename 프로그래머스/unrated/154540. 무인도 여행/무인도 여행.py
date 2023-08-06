import sys

sys.setrecursionlimit(10000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(board,x,y,x_len,y_len):
    res=int(board[x][y])
    board[x][y]='X'
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<x_len and 0<=yy<y_len and board[xx][yy]!='X':
            res+=DFS(board,xx,yy,x_len,y_len)
    return res
                
def solution(maps):
    answer = []
    x_len = len(maps)
    y_len = len(maps[0])
    board=[]
    for x in maps:
        board+=[list(x)]
        
    for x in range(x_len):
        for y in range(y_len):
            if board[x][y]!='X':
                answer.append(DFS(board,x,y,x_len,y_len))
    if answer:
        return sorted(answer)
    else:
        return [-1]