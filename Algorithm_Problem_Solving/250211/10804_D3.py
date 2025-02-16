import sys
sys.stdin = open("10804_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    input_str = list(input())
    N = len(input_str)

    # 문자열 뒤집기
    for i in range(N//2):
        input_str[i], input_str[N-1-i] = input_str[N-1-i], input_str[i]

    # 거울 문자열에 맞게 넣기
    mirror = []
    for i in input_str:
        if i == 'q':
            mirror.append('p')
        if i == 'p':
            mirror.append('q')
        if i == 'b':
            mirror.append('d')
        if i == 'd':
            mirror.append('b')

    print(f"#{tc} {''.join(mirror)}")