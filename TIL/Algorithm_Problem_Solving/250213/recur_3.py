# 재귀 호출 연습 3
# 배열에 v 가 있으면 1, 없으면 0을 리턴
def serch_v(i, n, v):       # i 배열 인덱스, n 배열크기, v 찾는 값
    if i == n:              # 끝까지 가서 못 찾을 경우 0을 리턴
        return 0
    elif A[i] == v:       # 중간에 v 를 찾으면 1을 리턴 (끝까지 안 감)
        return 1
    else:                   # 1이 없으면, v 찾으로 진행
        return serch_v(i+1, n, v)

A = [1, 2, 3, 4, 5, 6, 7, 9]
n = len(A)
v = 8

ans = serch_v(0, n, v)
print(ans)
