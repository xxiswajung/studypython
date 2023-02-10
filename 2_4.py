#temporary add code

n = int(input())
arr = list(map(int,input().split()))

avg = round(sum(arr) / n)

min = 2147000000

for idx, x in enumerate(arr): #enumerate() 까먹지 말기
    tmp=abs(x-avg) # t < min 이 아님 + 전에 임시변수에 avg와의 차이를 미리 계산해 해당 수가 평균값과 얼마나 멀어졌는지 확인할 필요 있음
    if tmp<min:
        min=tmp
        score=x #평균과 가까운 점수 기록
        res=idx+1 #평균과 가까운 점수의 index 기록(+1 주의)
    elif tmp==min: #평균과 가까운 점수가 또 존재
        if x>score: #근데 이 점수가 기존의 점수 보다 높음
            score=x #점수 갱신
            res=idx+1 # 위치 갱신
        #평균과 가까운 점수가 또 존재해다 기존의 점수보다 높지 않다=기존의 점수와 같다=학생번호가 더 빠른, index가 더빠른 애를 답으로 하므로 기록할 필요X
print(avg, res)
