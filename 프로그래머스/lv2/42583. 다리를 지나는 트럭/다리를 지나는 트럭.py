from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque(0 for _ in range(bridge_length))
    truck_weights=deque(t for t in truck_weights)
    bridge_weight=0
    
    while bridge: #다리 위에 트럭이 모두 없을 때 까지 반복
        answer+=1
        bridge_weight-=bridge.popleft()
        
        if truck_weights:
            if bridge_weight+truck_weights[0]<=weight:
                truck=truck_weights.popleft()
                bridge.append(truck)
                bridge_weight+=truck
            else:
                bridge.append(0) #무게가 넘으면 0을 추가해 다리 길이 유지
    return answer