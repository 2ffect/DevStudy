# 수열

N, K = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = -9999

for i in range(N - K + 1):
    point = arr[i]
    for j in range(1, K):
        point += arr[i+j]
    if max_sum <= point:
        max_sum = point

print(max_sum)
