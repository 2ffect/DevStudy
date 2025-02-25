# 자리배정

# 시작 시간 : 02/25 18:58
# 종료 시간 : 02/25 19:58 성공

C, R = map(int, input().split())
K = int(input())

# R행 C열을 가지는 달팽이 그리기
# 달팽이를 전부 그려놓고, 순회하면서 K를 찾고, i, j값을 반대로 출력하면 돼
# 그럼 달팽이를 뒤집어 그리지 않아도 된다.

# 0으로 가득찬 R * C 배열 그리기
arr = [[0] * R for _ in range(C)]

# 델타 지정
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# i,j 초기
i = 0
j = 0
d = 0
# cnt 초기화
cnt = 1

# cnt가 C*R과 같아지면 종료 == 배열이 가득 참
while cnt < C*R+1:
    arr[i][j] = cnt
    cnt += 1

    ni = i + di[d]
    nj = j + dj[d]

    if (0 <= ni < C) and (0 <= nj <R) and arr[ni][nj] == 0:
        i = ni
        j = nj

    else:
        d = (d+1) % 4
        ki = i + di[d]
        kj = j + dj[d]
        if (0 <= ki < C) and (0 <= kj < R) and arr[ki][kj] == 0:
            i = ki
            j = kj

# 달팽이를 그렸다면 K값을 찾고 인덱스 저
row = 0
col = 0

for k in range(C):
    for p in range(R):
        if arr[k][p] == K:
            row = k
            col = p

# K 가 맞다면 각각 +1 하여 출력
if arr[row][col] == K:
    print(row+1, col+1)
# 아니면 0 출력
else:
    print(0)