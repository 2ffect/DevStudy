def dec_to_bin(float_num):
    float_num = float_num
    binary = ''
    while float_num > 0:
        n = int(float_num * 2)
        binary += str(n)
        float_num = abs(int(float_num * 2) - float_num * 2)
    if len(binary) > 13:
        return 'overflow'
    else:
        return binary

for tc in range(1, int(input()) + 1):
    n = float(input())

    print(f'#{tc} {dec_to_bin(n)}')