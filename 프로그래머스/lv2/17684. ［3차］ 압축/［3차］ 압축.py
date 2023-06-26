def solution(msg):
    answer = []
    dict1={chr(i+64):i for i in range(1,27)}
    i=0
    while True:
        i+=1 
        str1 = ''.join(msg[:i])
        if str1 not in dict1:
            str2 = ''.join(msg[:i-1])
            answer.append(dict1[str2])
            dict1[str1] = len(dict1)+1
            msg=msg[i-1:]
            i=0
        if msg in dict1:
            answer.append(dict1[msg])
            break
    return answer