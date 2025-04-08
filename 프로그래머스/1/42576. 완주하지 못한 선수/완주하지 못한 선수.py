from collections import Counter

def solution(participant, completion):
    # answer = Counter(participant) - Counter(completion)
    # return list(answer.keys())[0]
    participant.sort()
    completion.sort()
    
    # 일치하지 않는 이름을 찾기
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    # 끝까지 일치하면 마지막 참가자가 남은 사람
    return participant[-1]