from collections import deque
def solution(order):
    answer = []
    order = deque(order) #트럭에 실어야 하는 순서
    a = deque(sorted(order)) #기존 컨테이너
    b = [] #보조 컨테이너 
    while len(order)!=0:
        item = order.popleft()
        if b and item == b[-1]:
            answer.append(b.pop())
        elif item in a:
            idx=a.index(item)
            for i in range(idx):
                b.append(a.popleft())
            # while a.index(item)!=0:
            #     b.append(a.popleft())
            answer.append(a.popleft())
        else:
            break     
    return len(answer)