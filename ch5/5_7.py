from collections import deque

ord=input()
n=int(input())

for i in range(n):
    res=input()
    ord=deque(ord)

    for x in res:
        if x in ord:
            if x!=ord.popleft(): #순서대로 잘 안되어 있음
                print("#%d NO" %(i+1))
                break
    
    if len(ord)==0: #순서대로 잘 되어 있고 + 필수가 다 들어 있음
        print("#%d YES" %(i+1))

    else: #필수가 다 안들어 있음
        print("#%d NO" %(i+1))
