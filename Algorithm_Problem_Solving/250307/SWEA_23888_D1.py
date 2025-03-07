#  Start 연습문제 1. 2진수를 10진수로 출력하기

def bin_to_dec(n):
    decimal_number = 0
    pow = 0

    for num in reversed(n):
        if num == '1':
            decimal_number += 2 ** pow
            pow += 1
        else:
            pow += 1

    return decimal_number

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 한 번에 다 받기
    numbers = ''
    for _ in range(N):
        numbers += input().strip()
    # 7자 씩 끊기
    bin_num = []
    bin = ''
    for i in numbers:
        bin += i
        if len(bin) == 7:
            bin_num.append(bin)
            bin = ''
            continue

    result = []
    for num in bin_num:
        result.append(bin_to_dec(num))

    print(f'#{tc}', *result)