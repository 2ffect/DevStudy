# 연습문제 1
# 5 X 5 배열에 25개 숫자 저장 후 
# 대각선 원소의 합을 구하시오.

s = 0
for i in range(5):
    s += A[i][i]
    s += A[i][4-i]
# 행과 열이 홀수 인 경우 가운데가 겹치기 때문에 
# 가운데 값을 한 번 빼줌
    s -= A[5//2][5//2]

# 연습문제 2
# 5 X 5 배열에 25개 숫자 저장 후 
# 이웃한 원소들과 차이의 절대값의 합

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    abs_sum = 0

    for i in range(N):
        for j in range(N):
            for di, dj in [[0,1], [1,0], [0, -1], [-1, 0]]:
                ni = i + dj
                nj = j + dj
                if 0 <= ni < N and 0 <= nj <N:
                    abs_sum += abs(arr[ni][nj] - arr[i][j])

    print(abs_sum)

    