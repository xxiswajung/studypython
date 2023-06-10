def solution(citations):
    for h in range(max(citations),min(citations)-1,-1):
        answer = 0
        for x in citations:
            if x>=h:
                answer+=1
        if answer>=h:
            return h
    else:
        return answer