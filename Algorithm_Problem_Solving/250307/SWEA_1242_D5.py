# 암호코드 스캔

import sys
sys.stdin = open('1242_input.txt')

def hex_to_binary(hex_string):
    hex_binary_mapping = {
        '0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011',
        '4' : '0100', '5' : '0101', '6' : '0110', '7' : '0111',
        '8' : '1000', '9' : '1001', 'A' : '1010', 'B' : '1011',
        'C' : '1100', 'D' : '1101', 'E' : '1110', 'F' : '1111',
    }

    binary_string = ''.join(hex_binary_mapping[char] for char in hex_string.upper())
    return binary_string

T = int(input())

for tc in range(1):
    # 배열의 크기
    N, M = map(int, input().split())
    # 배열 받기
    arr = [list((input().strip())) for _ in range(N)]

    # M 이 26 이하면 암호 가로길이 56
    # 27~50 이면 가로길이 56 ~ 112 (56배수)
    # 51 ~ 126 이면 가로길이 56 ~ 280 (56배수)
    # 127 부터 56배수면 된다.
    # 16진수니까 0부터 시작할 수 있음, 일단 1~F로 시작한다고 찾고,
    # 암호 길이가 모자르면 앞에 0000추가 - > 확인
    # 뒤에 0000추가 -> 확인

    # 배열 순회하며 암호가 포함되었다면 i 부터 0 만날 때 까지 담기. password 의 길이는 정해져 있다.
    if M <= 26:
        for i in ra
    # elif 26 < M <= 50:
    #
    # elif 50 < M <= 126:
    #
    # elif 126 < M:

