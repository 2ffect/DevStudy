def bin_to_dec(arr):
    global ans
    result = 0
    pow = 0
    for number in reversed(arr):
        if number == 0:
            pow += 1
            continue
        else:
            result += 2 ** pow
            pow += 1

    ans.append(result)


for tc in range(1, int(input()) + 1):
    # 비트 문자열 입력 수
    N = int(input())
    # 비트 받기
    bit = ''
    # 한 문자열로 받기
    for _ in range(N):
        bit = bit + input().strip()
    # 7글자씩 끊어서 리스트화
    bin_to_decimal = []
    binary = []
    cnt = 0
    for i in bit:
        cnt += 1
        binary.append(int(i))
        if cnt == 7:
            bin_to_decimal.append(binary)
            cnt = 0
            binary = []
    ans = []
    for num in bin_to_decimal:
        bin_to_dec(num)

    print(f'#{tc}', *ans)
