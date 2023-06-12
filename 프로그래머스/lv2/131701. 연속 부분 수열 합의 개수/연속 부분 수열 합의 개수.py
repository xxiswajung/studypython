def solution(elements):
    answer = set()
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            if j+i>=len(elements):
                res=sum(elements[j:len(elements)])+sum(elements[:(j+i)%len(elements)])
            else:
                res=sum(elements[j:j+i])
            answer.add(res)
    return len(answer)