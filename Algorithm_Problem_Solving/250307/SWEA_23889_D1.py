#  Start 연습문제 2. 16진수를 10진수로 변환하기

def hex_to_binary(hex_string):
    # 16진수를 2진수로 변환하기 위한 매핑 테이블
    hex_to_bin_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    # 각 16진수 문자를 대응하는 2진수로 변환하여 연결
    binary_string = ''.join(hex_to_bin_map[char] for char in hex_string.upper())
    return binary_string

def binary_to_demical(n):
    demical_number = 0
    pow = 0

    for num in reversed(n):
        if num == '1':
            demical_number += 2 ** pow
            pow += 1
        else:
            pow += 1

    return demical_number

T = int(input())

for tc in range(1, T+1):
    my_str = input()
    bin_list = []
    binary = hex_to_binary(my_str)

    # print(binary)
    # 7자리 씩 묶기
    my_bin = ''
    for i in binary:
        my_bin += i
        if len(my_bin) == 7:
            bin_list.append(my_bin)
            my_bin = ''

    else:
        bin_list.append(my_bin)

    # print(bin_list)
    # 10진 숫자로 출력
    result = []
    for number in bin_list:
        result.append(binary_to_demical(number))

    print(f'#{tc}', *result)


