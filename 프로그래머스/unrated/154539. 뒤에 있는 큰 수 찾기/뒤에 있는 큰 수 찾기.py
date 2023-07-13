def solution(numbers):
    stack = [] #원소의 인덱스를 기록, stack에 있는 인덱스에 뒷 큰수를 기록할 수 있는지 없는지 확인하는 용도
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
            #아직 stack에 인덱스가 남아있다 = 해당 인덱스가 가리키는 값의 뒷 큰수를 못 찾음
            # = 아직 뒷 큰수를 발견하지 못한 값에 대해서도 while문 돌면서 뒷 큰수가 될 수 있는지 확인해주기
            while stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            stack.append(i)
    return answer