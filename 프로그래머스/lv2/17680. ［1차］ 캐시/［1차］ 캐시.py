def solution(cacheSize, cities):
    answer = 0
    stack = []
    
    if cacheSize == 0 :
        answer = 5*len(cities)
    else:
        for x in cities:
            xx=x.lower()
            if xx in stack :
                idx=stack.index(xx)
                stack.pop(idx)
                stack.append(xx)
                answer += 1
            else:
                if len(stack)==cacheSize:
                    stack.pop(0)
                stack.append(xx)
                answer += 5
    return answer