di = [0, 1, 0, -1] # 오른쪽 부터 시계 방향으로로
dj = [1, 0, -1, 0]

i = 2
j = 3
# 기준 위치에서 시계 방향으로 위치 값 출력력
for dir in range(4):
    ni = i + di[dir]
    nj = j + dj[dir]
    # print(ni, nj)

N = 2
M = 3

for i in range(N):
    for j in range(M):
        for dir in range(4):
            
            ni = i + di[dir]
            nj = j + dj[dir] 

            # 인덱스가 유효할 경우만
            if 0 <= ni < N and 0 <= nj < M:
                print(ni, nj)
                
print()

for i in range(N):
    for j in range(M):
        for di, dj in [[0,1], [1,0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                print(ni, nj)