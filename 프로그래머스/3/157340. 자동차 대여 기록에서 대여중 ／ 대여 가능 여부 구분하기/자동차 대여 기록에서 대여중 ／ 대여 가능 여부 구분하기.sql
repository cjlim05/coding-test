-- 코드를 입력하세요
SELECT 
    CAR_ID, 
    CASE 
    WHEN MAX(CASE WHEN START_DATE <= DATE '2022-10-16' AND END_DATE >= DATE '2022-10-16' THEN 1 ELSE 0 END) = 1
      THEN '대여중'
    ELSE '대여 가능'
  END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC 


# 2022년 10월 16일에 대여 중인 자동차인 경우 '대여중' 나머지는 '대여가능' -> AVAILABILITY 칼럼명 
# 반납 날짜가 2022년 10월 16일인 경우에도 '대여중'
# 자동차 ID를 기준으로 내림차순 정렬해주세요.

