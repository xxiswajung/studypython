def solution(sequence, k):
    answer = []
    n = len(sequence)
    j = 0
    s = 0
    for i in range(n):
        while s < k and j < n:
            s+=sequence[j]
            j+=1
        if s == k :
            answer.append([i,j-1])
        s-=sequence[i]
        #j가 다시 시작점부터 시작할 필요 없음 : 시작점의 값(=sequence[i])만큼 빼줘도 k가 안 되기 때문에 처음부터 다시 시작할 필요가 없기 때문이다
        #위의 주석이 이해가 안되면 https://url.kr/bh8d4u 참고
    return sorted(answer,key=lambda x:x[1]-x[0])[0]
    # 부분 합이 k와 같은 인덱스들을 다 저장한 뒤, 인덱스 차이가 적은 순대로 정렬한 뒤 가장 첫번째의 값만 출력한다
