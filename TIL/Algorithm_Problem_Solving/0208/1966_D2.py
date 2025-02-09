import sys
sys.stdin = open("1966.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    counts = [0] * (max(arr) + 1)
    temp = [0] * N

    for i in range(N):
        counts[arr[i]] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    for i in range(N-1, -1, -1):
        counts[arr[i]] -= 1
        temp[counts[arr[i]]] = arr[i]

    print(f'#{tc}', *temp)
