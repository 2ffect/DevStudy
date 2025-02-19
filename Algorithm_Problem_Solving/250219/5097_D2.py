# 회전

# 시작 시간 : 02/19 14:30
# 종료 시간 : 02/19 14:49 성공

from collections import deque
import sys
sys.stdin = open("5097_input.txt", "r")

# N개의 숫자로 이루어진 수열을 받아
# 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때
# 가장 앞에 있는 숫자를 출력

T = int(input())
for tc in range(1, T+1):
    # N 배열의 크기, M 반복 횟수
    N, M = map(int, input().split())
    # arr 를 deque로 생성
    arr = deque(map(int, input().split()))

    for j in range(M):
        a = arr.popleft()
        arr.append(a)

    print(f'#{tc} {arr[0]}')
