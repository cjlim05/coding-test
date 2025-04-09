import math

def solution(progresses, speeds):
    answer = []
    
    # 각 작업이 완료되기까지 필요한 일수를 계산
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    # 배포 그룹 나누기
    current_day = days[0]
    count = 1

    for i in range(1, len(days)):
        if days[i] <= current_day:
            count += 1
        else:
            answer.append(count)
            current_day = days[i]
            count = 1

    answer.append(count)  # 마지막 그룹 추가

    return answer
