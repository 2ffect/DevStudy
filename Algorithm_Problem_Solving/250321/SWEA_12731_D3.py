# 두 전구
import sys
sys.stdin = open('12731_input.txt')

for tc in range(1, int(input()) + 1):
    a, b, c, d = map(int, input().split())

    X = [i for i in range(a, b)]
    Y = [j for j in range(c, d)]

    cnt = 0
    for x in X:
        if x in Y:
            cnt += 1

    print(f'#{tc} {cnt}')