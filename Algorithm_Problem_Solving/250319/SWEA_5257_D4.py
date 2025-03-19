# 연산
from collections import deque
import sys
sys.stdin = open('5247_input.txt')

# N - 시작 숫자 / M - 목표숫자
def bfs(N, M):
    # 큐 생성
    my_queue = deque()
    # 각 oper 결과 값 별 연산 횟수를 저장할 리스트.
    chcek_oper = [-1] * 1000001
    # 초기값의 연산 횟수를 0으로 설정
    chcek_oper[N] = 0
    # 인큐
    my_queue.append(N)

    while my_queue:
        # 팝 해서 가져오기
        num = my_queue.popleft()
        # 팝 하여 가져온 num이 M 과 같으면, cnt를 리턴
        if num == M:
            return chcek_oper[num]

        # 4 가지 연산을 수행
        for oper in [num + 1, num - 1, num * 2, num - 10]:
            # 연산 결과가 1백만 이하고
            # check_oper[oper] 가 -1 일때만 <- 이거 안 해주면 중복된 계산 값이 나왔을 때 연산 횟수를 덮어쓰게 됨
            if oper <= 1000000 and chcek_oper[oper] == -1:
                # 결과 값을 큐에 담기
                my_queue.append(oper)
                # 연산 횟수 같이 담아주기
                chcek_oper[oper] = chcek_oper[num] + 1

for tc in range(1, int(input()) + 1):
    # N - 시작 숫자 / M - 목표숫자
    N, M = map(int, input().split())

    print(f'#{tc} {bfs(N, M)}')

# # 승연
# from collections import deque
#
# def calculate(num):
#     global M, visited
#
#     q = deque([num])
#     cnt_lst = [-1] * 1000000
#     cnt_lst[num] = 0
#     # print(q)
#
#     while q:
#         res = q.popleft()
#
#         if res == M:
#             return cnt_lst[res]
#         # if cnt_lst[res] == -1:
#         for n_res in [res + 1, res - 1, res * 2, res - 10]:
#             if n_res <= 1000000 and cnt_lst[n_res] == -1:
#                 q.append(n_res)
#                 cnt_lst[n_res] = cnt_lst[res] + 1
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     cnt = 0
#     visited = []
#     ans = calculate(N)
#     print(f'#{tc} {ans}')