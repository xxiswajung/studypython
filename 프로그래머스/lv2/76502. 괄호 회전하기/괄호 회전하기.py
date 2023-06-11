def solution(s):
    answer = 0
    s=list(s)
    for i in range(len(s)):
        s=s[1:]+s[:1]
        stack=[]
        for j in range(len(s)):
            x=s[j]
            if stack:
                if stack[-1]+x=='[]' or stack[-1]+x=='()' or stack[-1]+x=='{}':
                    stack.pop()
                else:
                    stack.append(x)
            else:
                stack.append(x)
        if len(stack)==0:
            answer+=1
    return answer