-- 코드를 입력하세요
SELECT MCDP_CD as '진료과 코드', count(*) as '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD >= '2022-05-01' and APNT_YMD <= '2022-06-01'
GROUP BY MCDP_CD
ORDER BY `5월예약건수`, `진료과 코드`;



# 2022년 5월에 예약한  환자수 -> 진료코드 별로 조회
# 컬럼명은 '진료과 코드', '5월예약건수'로 지정
# 진료과별 예약한 환자 수를 기준으로 오름차순 정렬
# 예약한 환자 수가 같다면 진료과 코드를 기준으로 오름차순