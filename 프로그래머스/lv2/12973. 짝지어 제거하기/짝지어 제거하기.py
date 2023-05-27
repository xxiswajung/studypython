def solution(s):
    stack=[]
    for i in s:
        if not stack: #stack이 비어있으면
            stack.append(i) #문자열의 원소 추가
        else: #stack에 뭔가 있는 경우
            if i==stack[-1]: #문자열의 원소와 가장 최근에 넣은 stack의 원소가 같으면
                stack.pop() #stack 꺼내기
            else:
                stack.append(i)
    if stack: #stack에 원소가 있다 == 짝원소 못찾음
        return 0
    else:
        return 1