def solution(numbers):
    answer = []
    for i in numbers:
        if i%2==0:
            answer.append(i+1)
        else:
            odd='0'+bin(i)[2:]
            idx=odd.rindex('0')
            odd=list(odd)
            odd[idx]='1'
            odd[idx+1]='0'
            answer.append(int(''.join(odd),2))
    return answer