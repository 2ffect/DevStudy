'''
3
1 2 3
4 5 6
7 8 9 
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

# 0 으로 채워진 3*4 배열 만들기
arr2 = [[0] * 4 for _ in range(N)]
arr2[2][1] = 1
print(arr2)

### 행 우선 순회
for i in range(N):      # 행
    for j in range(N):  # 열
        print(arr[i][j]) # arr[행][열]


# N x M 배열의 크기와 저장 된 값이 주어질 때 모든 합 구하기
'''
3 4
1 7 2 8
6 2 9 8
5 7 4 2 
'''
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 행 우선 순회
sum = 0
for i in range(N):
    for j in range(M):
        sum += arr[i][j]

print(sum)

# 열 우선 순회
max_v = 0

for j in range(M):
    for i in range(N):
        sum 

# 지그재그 순회
if i % 2 == 0:
    for i in range(N):
        pass
else:
    for i in range(N-1, -1, -1):
        pass

# (arr[i][j + (m-1-2*j) * (i%2)])