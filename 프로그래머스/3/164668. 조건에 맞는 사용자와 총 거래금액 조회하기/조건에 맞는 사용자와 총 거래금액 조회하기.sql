-- 코드를 입력하세요
SELECT 
    B.WRITER_ID AS USER_ID, 
    U.NICKNAME, 
    SUM(B.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS B
JOIN USED_GOODS_USER AS U ON B.WRITER_ID = U.USER_ID
WHERE B.STATUS = 'DONE'
GROUP BY B.WRITER_ID, U.NICKNAME
HAVING SUM(B.PRICE) >= 700000
ORDER BY TOTAL_SALES ASC;



# 완료된 중고거래의 총 금액이 70만원 이상 회원 
# 총거래금액 오름차순 
# 