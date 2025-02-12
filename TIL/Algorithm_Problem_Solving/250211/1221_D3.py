import sys
sys.stdin = open("1221_input.txt", "r")
# GNS

T = int(input())

for tc in range(1, T+1):
    title = list(map(str, input().split()))
    arr = list(map(str, input().split()))
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    new_list = []

    for i in num:
        for j in arr:
            if j == i:
                new_list.append(j)

    result = ' '.join(new_list)

    print(f'{title[0]} \n{result}')