def solution(files):
    answer = []
    for k in files:
        head, number, tail = '','',''
        chk=False
        
        for i in range(len(k)):
            if k[i].isdigit():
                head=k[:i]
                number=k[i:]
            
                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail=number[j:]
                        number=number[:j]
                        break
                break
        answer.append([head, number, tail])
                    
    answer.sort(key=lambda x:(x[0].upper(),int(x[1])))
    return [''.join(s) for s in answer]