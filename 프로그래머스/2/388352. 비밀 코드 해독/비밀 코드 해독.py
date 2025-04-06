from itertools import combinations

def solution(n, q, ans):
    count = 0
    
    # n개의 수 중 5개를 고른 모든 조합을 확인
    for comb in combinations(range(1, n+1), 5):
        is_valid = True
        
        # 각 시도와 시스템 응답이 일치하는지 확인
        for i in range(len(q)):
            # 현재 조합과 시도한 수의 교집합의 개수를 센다
            match_count = len(set(comb) & set(q[i]))
            if match_count != ans[i]:
                is_valid = False
                break
        
        if is_valid:
            count += 1
    
    return count
