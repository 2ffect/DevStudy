import sys
sys.stdin = open("1210_input.txt", "r")


T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(100)]

    print(arr)