def divide(p):
    num1=0
    num2=0
    
    for i in range(len(p)):
        if p[i]=='(':
            num1+=1
        else:
            num2+=1
        if num1==num2:
            return p[:i+1],p[i+1:]

def check(u):
    stack=[]
    for p in u:
        if p=='(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    if not p:
        return ""
    u,v=divide(p)
    if check(u):
        return u+solution(v)
    else:
        answer='('
        answer+=solution(v)
        answer+=')'
        
        for p in u[1:len(u)-1]:
            if p =='(':
                answer+=')'
            else:
                answer+='('
        return answer
    