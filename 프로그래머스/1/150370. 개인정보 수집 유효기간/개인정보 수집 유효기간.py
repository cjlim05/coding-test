from datetime import datetime

def solution(today, terms, privacies):
    # 오늘 날짜를 datetime 객체로 변환
    today = datetime.strptime(today, "%Y.%m.%d")
    
    # 약관 종류와 유효기간을 딕셔너리로 저장
    term_dict = {}
    for term in terms:
        type_, months = term.split()
        term_dict[type_] = int(months)
    
    # 결과 리스트
    expired = []
    
    # 개인정보 수집 일자와 약관 타입 처리
    for i, entry in enumerate(privacies):
        date, term_type = entry.split()
        start_date = datetime.strptime(date, "%Y.%m.%d")
        
        # 유효기간 계산
        months = term_dict[term_type]
        year = start_date.year
        month = start_date.month + months
        if month > 12:
            year += (month - 1) // 12
            month = (month - 1) % 12 + 1
        expire_date = datetime(year, month, start_date.day)
        
        # 오늘 날짜와 비교하여 만료 여부 확인
        if today >= expire_date:
            expired.append(i + 1)
    
    return expired
