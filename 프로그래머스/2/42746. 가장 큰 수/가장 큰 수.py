def solution(numbers):
    # 모든 숫자를 문자열로 바꿈
    numbers = list(map(str, numbers))
    
    # 핵심 정렬 로직: 두 문자열을 더한 것끼리 내림차순 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 정렬된 숫자를 이어 붙임
    answer = ''.join(numbers)
    
    # 예외 처리: '000' 같은 경우는 '0' 하나만 반환
    return '0' if answer[0] == '0' else answer
