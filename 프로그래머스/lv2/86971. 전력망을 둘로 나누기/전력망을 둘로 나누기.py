from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start]=True #시작 송전탑 방문 함
    cnt=0
    
    while queue:
        v=queue.popleft() #시작:start 송전탑
        cnt+=1
        for i in graph[v]: #start 송전탑에 연결된 다른 송전탑에 대해
            if not visited[i]:
                queue.append(i)
                visited[i]=True
    return cnt

def solution(n, wires):
    answer = n-2 #최대:n-1, 최소:1개 => 최대 차이는 n-2 개
    for i in range(len(wires)):
        tmp = wires.copy()
        graph = [[] for i in range(n+1)]
        visited = [False]*(n+1)
        tmp.pop(i) # 전선 제거
        
        for wire in tmp:
            x,y=wire
            graph[x].append(y)
            graph[y].append(x)
        for idx, g in enumerate(graph):
            if g!=[]: #다른 것과 연결된 것을 시작점으로 지정
                start=idx
                break
        cntt=bfs(graph, start, visited)
        cntt1=n-cntt
        answer=min(answer,abs(cntt-cntt1))
    return answer