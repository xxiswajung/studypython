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
        
      