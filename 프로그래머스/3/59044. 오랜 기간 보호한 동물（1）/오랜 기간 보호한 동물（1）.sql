-- 코드를 입력하세요
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS AS A
WHERE A.ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_OUTS)
ORDER BY DATETIME
LIMIT 3;



# 입양 못간 동물 중
# 가장 오래 보소에 있는 동물 3마리의
# 이름 보호시작일 
# 보호 시작일 순 