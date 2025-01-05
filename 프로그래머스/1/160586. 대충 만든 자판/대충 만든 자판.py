def solution(keymap, targets):
    answer = []
    
    min_presses = {}
    
    # keymap에서 최소 누르기 횟수 계산
    for i, keys in enumerate(keymap):
        for idx, char in enumerate(keys):
            # 이미 저장된 값보다 더 적은 누르기 횟수라면 갱신
            if char in min_presses:
                min_presses[char] = min(min_presses[char], idx + 1)
            else:
                min_presses[char] = idx + 1
    
    answer = []
    
    for target in targets: 
        result = 0 
        for char in target:
            if char in min_presses:
                result += min_presses[char]
            else:
                result = -1
                break 
        answer.append(result)
    
    return answer 
            
            
    
    return answer