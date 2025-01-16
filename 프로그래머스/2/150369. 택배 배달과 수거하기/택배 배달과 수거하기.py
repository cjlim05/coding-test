def solution(cap, n, deliveries, pickups):
    # 총 이동 거리
    total_distance = 0

    # 배달과 수거할 택배의 잔여 개수를 관리할 인덱스
    delivery_index = n - 1
    pickup_index = n - 1

    while delivery_index >= 0 or pickup_index >= 0:
        # 현재 배달과 수거가 필요한 가장 먼 집을 찾음
        while delivery_index >= 0 and deliveries[delivery_index] == 0:
            delivery_index -= 1
        while pickup_index >= 0 and pickups[pickup_index] == 0:
            pickup_index -= 1

        # 배달과 수거가 필요한 가장 먼 집의 거리
        max_distance = max(delivery_index, pickup_index) + 1

        # 한 번의 이동으로 처리할 수 있는 배달 및 수거를 계산
        delivery_load = 0
        pickup_load = 0

        # 배달 처리
        for i in range(delivery_index, -1, -1):
            if delivery_load + deliveries[i] > cap:
                deliveries[i] -= (cap - delivery_load)
                delivery_load = cap
                break
            delivery_load += deliveries[i]
            deliveries[i] = 0

        # 수거 처리
        for i in range(pickup_index, -1, -1):
            if pickup_load + pickups[i] > cap:
                pickups[i] -= (cap - pickup_load)
                pickup_load = cap
                break
            pickup_load += pickups[i]
            pickups[i] = 0

        # 왕복 거리 추가
        total_distance += max_distance * 2

    return total_distance