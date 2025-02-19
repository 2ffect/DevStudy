# 피자 굽기

# 화덕의 수만큼 피자를 순서대로 넣고
# 한바퀴 돌 때마다 피자의 치즈량이 반으로 줄어든다
# 치즈가 0이 되면 화덕에서 제거하고, 새로운 피자를 추가할 수 있다.
# 화덕에 가장 마지막까지 남아있는 피자의 번호는?

from collections import deque
import sys
sys.stdin = open("5099_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # N = 배열의 크기, M = 피자의 수
    N, M = map(int, input().split())
    # P = 피자 근데 이제 치즈를 곁들인
    P = deque(map(int, input().split()))

