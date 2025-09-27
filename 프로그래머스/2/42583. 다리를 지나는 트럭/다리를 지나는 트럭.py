from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0                         # 경과 시간
    bridge = deque()                  # 다리 위 트럭: (트럭 무게, 진입 시점)
    bridge_weight = 0                 # 다리 위 트럭 총 무게
    waiting_trucks = deque(truck_weights)  # 대기 트럭

    while waiting_trucks or bridge:   # 대기 트럭 또는 다리 위 트럭이 있으면 계속
        time += 1                     # 1초 경과

        # 1️⃣ 다리 맨 앞 트럭이 다 지나갔는지 확인
        if bridge:
            truck_weight, enter_time = bridge[0]  # 맨 앞 트럭 정보 bridge = [(7, 10), (4, 15), (9, 22)]
            if time - enter_time >= bridge_length:
                bridge.popleft()                 # 다 건너면 제거
                bridge_weight -= truck_weight    # 다리 무게 감소

        # 2️⃣ 다음 트럭 올릴 수 있는지 확인
        if waiting_trucks:
            next_truck = waiting_trucks[0]  # 다음 트럭 무게
            if bridge_weight + next_truck <= weight and len(bridge) < bridge_length:
                waiting_trucks.popleft()       # 대기 트럭에서 제거
                bridge.append((next_truck, time))  # 다리에 올림
                bridge_weight += next_truck

    return time
