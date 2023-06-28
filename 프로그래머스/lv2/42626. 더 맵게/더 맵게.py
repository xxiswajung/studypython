import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            return answer
        second = heapq.heappop(scoville)
        score = first + (second * 2)
        heapq.heappush(scoville, score)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1


#################################
#런타임 에러 고친 내 방식
#스코빌 철자 확인..

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if len(scoville)==1 and scoville[0]<K:
            return -1
        if scoville[0]>=K:
            return answer
        heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        answer+=1
      
