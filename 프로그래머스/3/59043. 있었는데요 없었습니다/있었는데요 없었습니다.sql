-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A
JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.DATETIME < A.DATETIME
ORDER BY A.DATETIME;


# 입양일 잘못
# 보호 시작일보다 입양일이 먼저 
# 그것들 동물 아이디 이름 조회
# 보호 시작이 빠른순 