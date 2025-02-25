# 최댓값

# 시작 시간 : 02/25 18:50
# 종료 시간 : 02/25 18:57 성공
# 9*9 배열이 주어질 때 최대값을 찾고 각 행과 열을 출력하라.

arr = [list(map(int, input().split())) for _ in range(9)]

# 최대값, 행, 열 찾기
max_num = 0
max_row = 0
max_col = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] >= max_num:
            max_num = arr[i][j]
            max_row = i+1
            max_col = j+1

print(max_num)
print(max_row, max_col)