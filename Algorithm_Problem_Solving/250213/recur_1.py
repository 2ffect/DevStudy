# 재귀호출 연습 1
def f(i, N):
    if i == N:     # 중단 조건
        return
    else:          # 재귀 호출
        f(i+1, N)

# f(0, 3)
# f(0, 1000)