answer = 0
count = 0
arr = ['A','E','I','O','U']
def DFS(string, word):
    global count, answer
    
    if string==word:
        answer = count
        return
    if len(string)>5:
        return
    count+=1
    
    for i in arr:
        DFS(string+i, word)

def solution(word):
    DFS('',word)
    return answer