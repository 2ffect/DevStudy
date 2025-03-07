# Start 연습문제 3. 16진수 암호비트패턴 출력하기

def hex_to_binary(hex_string):
    hex_to_bin = {
        '0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011',
        '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111',
        '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011',
        'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111',
    }

    binary_string = ''.join(hex_to_bin[char] for char in hex_string.upper())
    return binary_string

def search_pass(binary_string):
    global result
    pass_string = {
        '001101' : '0', '010011' : '1', '111011' : '2',
        '110001' : '3', '100011' : '4', '110111' : '5',
        '001011' : '6', '111101' : '7', '011001' : '8',
        '101111' : '9',
    }

    for str in binary_string:
        if str in pass_string:
            result.append(pass_string.get(str))

T = int(input())
for tc in range(1, T+1):
    my_str = input().strip()
    N = len(my_str) * 4
    binary_str = hex_to_binary(my_str)

    binary_str = list(binary_str)

    # 맨 뒷 자리가 1이 될 때 까지 제거
    while binary_str[-1] != '1':
        binary_str.pop()

    # 뒤집어서 하나의 문자열로 정렬, 6자리씩 끊어서 저장 후 패턴찾기
    binary_str = ''.join(reversed(binary_str))

    check_list = []
    check_num = ''

    for i in binary_str:
        check_num += i
        if len(check_num) == 6:
            # 다시 뒤집어서 담아줘야 함
            a = ''.join(list(reversed(check_num)))
            check_list.append(a)
            check_num = ''

    result = []
    search_pass(check_list)
    result = list(reversed(result))

    print(f'#{tc}', *result)