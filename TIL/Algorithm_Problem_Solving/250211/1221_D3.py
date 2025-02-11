import sys
sys.stdin = open("1221_input.txt", "r")
# GNS

T = int(input())

for tc in range(1):
    title = list(map(str, input().split()))
    arr = list(map(str, input().split()))
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    counts = [0] * 10

    temp = [""]

    arr_len = int(title[1])
    print(arr_len)


    result = ' '.join(new_list)

    print(f'{title[0]} {result}')