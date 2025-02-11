import sys
sys.stdin = open("5356_input.txt", "r")

# 의석이 세로로 말해요

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(str, input())) for _ in range(5)]

    result = ''.join(new_list)

    print(f'#{tc} {result}')