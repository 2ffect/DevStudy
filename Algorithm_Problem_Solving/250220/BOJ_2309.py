# 일곱 난쟁이
# 제한 시간 2시간

# 시작 시간 : 02/20 18:40
# 종료 시간 : 02/20 20:22 성공

# 9명의 난쟁이의 키를 입력받아 7명의 합으로 100이 되는 경우
# 해당 난쟁이의 키를 오름차순으로 출력하라.
# 난쟁이 9명의 키를 합 한 뒤 랜덤으로 2명씩 뽑아 제외한 값이 100이 되면 진짜 난쟁이들만 남는다.

# 삭제할 난쟁이의 키를 담을 변수
a = b = 0

# 리스트로 받아오기
shorts = []
for _ in range(9):
    shorts.append(int(input()))

# 모든 난쟁이 키의 합
total = sum(shorts)

for i in range(9):
    # i와 겹치지 않아야 하기 때문에 i+1 부터 시작
    for j in range(i+1, 9):
        # 총 합에서 두 난쟁이의 키를 뺀 값이 100이 될 경우
        if total - shorts[i] - shorts[j] == 100:
            # 각 변수에 난쟁이 키를 저장.
            a = shorts[i]
            b = shorts[j]
# 가짜 난쟁이 제거 후 정렬
shorts.remove(a)
shorts.remove(b)
shorts.sort()

# 출력
for short in shorts:
    print(short)