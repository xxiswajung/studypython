from itertools import permutations
def solution(numbers):
    answer = 0
    numbers=list(numbers)
    n = set()
    for k in range(1,len(numbers)+1):
        for i in permutations(numbers,k):
            n.add(int(''.join(i)))
    for x in n:
        if x == 0 or x == 1 :
            continue
        else:
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    break
            else:
                answer+=1
    return answer