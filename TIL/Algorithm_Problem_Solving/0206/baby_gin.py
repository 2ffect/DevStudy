# Baby-Gin Game
# 0 ~ 9 사이의 숫자카드 중 임으로 6장을 뽑아
# 3장의 카드가 연속적인 번호를 갖는경우는 run
# 3장의 카드가 동일한 번호를 갖는경우는 triple
# 6장의 카드가 run과 triple로만 구성 된 경우를 baby-gin
# 6자리 숫자를 입력 받아 baby-gin 여부를 판단

# 완전 검색 접근법
# 모든 경우의 수 생성
# 6개의 숫자로 만들 수 있는 모든 순열 생성(중복 포함)
# 앞 3자리와 뒤 3자리를 잘라, 각각 run, triple 여부 테스트
# 최종적으로 baby-gin 판단.

# 그리디 접근법
num = int(input())
c = [0] * 12            # [c10] , [c11] 은 항상 0으로 [c8], [c9]의 확인을 위해 여분을 추가

for i in range(6):
    c[num % 10] += 1    # 1의 자리를 알아내고 c[i]에 카운트 추가
    num //= 10          # 1의 자리를 제거

i = 0
tri = run = 0
while i < 10:           # 카드 번호가 9 까지니까 구간이 [0~9]
    if c[i] >= 3 :      # tri 조건 조사 후 맞으면 데이터 삭제
        c[i] -= 3       # 확인된 3을 빼주고
        tri += 1        # tri 1 올려줌
        continue
    
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # run 조건 조사 후 맞으면 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    
    i += 1 # i를 1개 올려준다

if tri + run == 2:
    print("Baby Gin")
else:
    print("Lose")