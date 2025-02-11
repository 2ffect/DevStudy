import sys
sys.stdin = open("1989_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    str = input()
    N = len(str)
    result = 1

    for i in range(N):
        if str[i] != str[N-1-i]:
            result = 0

    print(f'#{tc} {result}')