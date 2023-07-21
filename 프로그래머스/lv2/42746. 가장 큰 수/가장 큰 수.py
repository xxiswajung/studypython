def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x:x*3, reverse=True)
    # 1. 실제로 원소에 3번 곱하는 것이 아닌, 비교 당시에만 3번 곱하기
    # 2. 3번 곱하는 이유 : numbers의 원소는 1000이하라고 명시했으므로, 최소 3자리를 비교하여 어떤 원소가 ASCII 순으로 가장 큰지 비교하기 위해
    # 3. 문자열의 비교는 첫번째 원소부터 들여다보며 ASCII 상으로 큰 순대로 정렬함. 첫번째 원소의 ASCII 값이 같으면 두번째원소로 비교.
    # 4. 이렇게 numbers의 원소를 ASCII 값으로 내림차순 정렬을 하면 가장 큰 수를 만들 수 있음 
    answer = answer.join(numbers)
    return str(int(answer))
