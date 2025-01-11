def solution(numbers):
    # 결과를 저장할 배열, 초기값은 모두 -1로 설정
    answer = [-1] * len(numbers)
    
    # 스택을 초기화 (스택에는 인덱스를 저장)
    stack = []

    # numbers 배열의 각 숫자와 인덱스를 순회
    for i in range(len(numbers)):
        # 현재 숫자를 가져옴
        current_number = numbers[i]
        
        # 스택이 비어 있지 않고, 현재 숫자가 스택 상단에 저장된 숫자보다 크다면
        while stack and numbers[stack[-1]] < current_number:
            # 스택에서 가장 위에 있는 인덱스를 꺼냄
            index = stack.pop()
            # 해당 인덱스의 "뒷 큰수"를 현재 숫자로 설정
            answer[index] = current_number
        
        # 현재 인덱스를 스택에 추가 (현재 숫자는 이후 비교를 위해 대기)
        stack.append(i)
    
    # 스택에 남아 있는 인덱스들은 뒷 큰수가 없으므로 기본값 -1 유지
    return answer
