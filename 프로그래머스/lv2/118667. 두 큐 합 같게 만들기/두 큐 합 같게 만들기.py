from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1=deque(queue1)
    queue2=deque(queue2)
    s = sum(queue1)+sum(queue2)
    if s%2!=0:
        return -1
    else:
        s = s//2
        t = sum(queue1)
        while True:
            if answer>2*(len(queue1)+len(queue2)):
                answer=-1
                break
            if t<s:
                t+=queue2[0]
                queue1.append(queue2.popleft())
                answer+=1
            elif t>s:
                t-=queue1[0]
                queue2.append(queue1.popleft())
                answer+=1
            else:
                break
    return answer