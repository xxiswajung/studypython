from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_weight = 0 #시간 줄이기 위한 변수, sum은 오래 걸림 : 현재 다리 위의 무게
    bridge = deque(0 for _ in range(bridge_length)) #다리
    truck_weights = deque(t for t in truck_weights)
    
    while bridge : 
        answer+=1
        bridge_weight-=bridge.popleft()
        
        if truck_weights:
            if bridge_weight+truck_weights[0]<=weight:
                truck=truck_weights.popleft()
                bridge.append(truck)
                bridge_weight+=truck
            else:
                bridge.append(0)
    return answer