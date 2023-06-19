def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-sum(number)+1):
        for j in range(len(want)):
            if discount[i:i+sum(number)].count(want[j])!=number[j]:
                break
        else:
            answer+=1
    return answer