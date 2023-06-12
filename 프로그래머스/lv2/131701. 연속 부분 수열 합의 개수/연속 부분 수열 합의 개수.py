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

###########################
#another solving 

def solution(elements):
    answer = set()
    ll = len(elements)
    elements = elements * 2
    
    for i in range(ll) : 
        for j in range(ll) : 
            answer.add(sum(elements[j:j+i+1]))
    return len(answer)
