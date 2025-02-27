# 직사각형 네개의 합집합 면적 구하기

# 101*101 짜리 0으로 된 배열 만들기
# 좌표가 주어지면 해당 칸 만큼 전부 1 더하기
# 0이 아닌 좌표의 수 카운팅하기


arr = [[0] * 101 for _ in range(101)]

# 인풋 받고 받은 값으로 좌표를 계산하고 1씩 더해주기
for _ in range(4):
    # 인풋 받은 숫자를 각 변수 좌표에 담기 (x1, y1) = 좌측 상단 시작좌표 / (x2, y2) = 우측 하단 종료좌표
    x1, y1, x2, y2 = map(int, input().split())
    # 받은 좌표로 arr를 순회하며 arr[i][j]에 1을 더해줘야 한다.
    # i 의 range = x1 - x2
    N = x2 - x1
    # j 의 range = y2 - y1
    M = y2 - y1
    # arr[i][j]에 전부 1 더하기
    for i in range(N):
        for j in range(M):
            arr[x1 + i][y1 + j] += 1

# arr 에서 1이 아닌 숫자 찾기
cnt = 0
for k in range(101):
    for p in range(101):
        if arr[k][p] != 0:
            cnt += 1

print(cnt)