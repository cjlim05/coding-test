from heapq import heappush, heappop

def solution(arguments):
    max_heap = []
    min_heap = []
    
    for arg in arguments:
        if arg == "D 1":  # 최대값 삭제
            if max_heap:
                # 최대값 찾아서 삭제
                val = max(max_heap)
                max_heap.remove(val)
                
                # 동기화: 최소 힙에도 삭제된 값 반영
                if min_heap and val in min_heap:
                    min_heap.remove(val)

        elif arg == "D -1":  # 최소값 삭제
            if min_heap:
                val = heappop(min_heap)  # 최소값은 그대로 heappop
                # 동기화: 최대 힙에서도 삭제
                if val in max_heap:
                    max_heap.remove(val)

        else:  # 삽입
            num = int(arg[2:])
            heappush(min_heap, num)
            max_heap.append(num)  # 최대 힙에서는 그냥 리스트 사용

    if not min_heap:
        return [0, 0]
    
    # 최종 결과
    return [max(max_heap), min_heap[0]]
