def solution(s):
    s=list(s)
    res=[]
    for i in range(len(s)):
        if s[i]=="(":
            res.append('(')
        else:
            if len(res)==0:
                return False
            else:
                res.pop()
    if len(res)==0:
        return True
    else:
        return False