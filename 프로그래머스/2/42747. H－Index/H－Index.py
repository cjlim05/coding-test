def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    
    for i in range(n + 1):  # h는 0부터 n까지 가능
        count = sum(1 for x in citations if x >= i)
        if count >= i:
            answer = i  # 조건 만족하는 i 중 최대값 저장

    return answer
