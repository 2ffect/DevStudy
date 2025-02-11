import sys
sys.stdin = open("4831_input.txt", "r")

# 전기버스
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    # 충전 횟수
    cnt = 0
    for i in range(N+1):


    print(cnt)