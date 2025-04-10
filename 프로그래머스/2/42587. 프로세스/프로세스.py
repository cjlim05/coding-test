from collections import deque

def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    count = 0

    while queue:
        cur = queue.popleft()
        
        # 현재 프로세스보다 높은 우선순위가 뒤에 있으면 다시 넣기
        if any(cur[0] < item[0] for item in queue):
            queue.append(cur)
        else:
            count += 1
            if cur[1] == location:
                return count
