# 재귀 호출 연습 2
def f(i, N, arr):        # i 배열 인덱스, N 배열 크기
    if i == N:
        return
    else:
        print(arr[i])
        f(i+1, N)

A = [1, 2, 3]
f(0, 3, A)

# 왜 안되징 ??
