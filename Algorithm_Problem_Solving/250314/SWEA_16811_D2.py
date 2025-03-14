# 당근 포장하기
import sys
sys.stdin = open('16811_input.txt')

# for tc in range(1, int(input()) + 1):
#     # 당근 수
#     n = int(input())
#     # 당근 리스트
#     c = list(map(int, input().split()))
#     c.sort()
#
#     min_diff = 9999999999
#     max_carrot = n//2
#
#     for i in range(n):
#         for j in range(n):
#             # 박스를 나눠서 담는 모든 경우의 수
#             s_box = c[:i]
#             m_box = c[i:j]
#             l_box = c[j:]
#
#             # 비어있는 상자가 있다면 건너뛰기
#             if (len(s_box) == 0) or (len(m_box) == 0) or (len(l_box) == 0):
#                 continue
#             # 같은 크기의 당근은 같은 박스에 있어야 함.
#             # s m 각 마지막 당근이 다음 박스에 들어있는지 확인
#             # 둘 중 하나라도 해당한다면 건너뛰기
#             if (s_box[-1] == m_box[0]) or (m_box[-1] == l_box[0]):
#                 continue
#             # 한 박스에는 max_carrot을 초과하여 담기면 건너뛰기
#             if (len(s_box) > max_carrot) or (len(m_box) > max_carrot) or (len(l_box) > max_carrot):
#                 continue
#
#             # 위 3개를 통과했다면, 가장 많이 들어간 박스와 가장 적게 들어간 박스를 찾고, 최소 차이를 갱신
#             max_box = max(len(s_box), len(m_box), len(l_box))
#             min_box = min(len(s_box), len(m_box), len(l_box))
#             min_diff = min(abs(max_box - min_box), min_diff)
#
#
#     if min_diff == 9999999999:
#         print(f'#{tc} -1')
#     else:
#         print(f'#{tc} {min_diff}')


# 승연
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     carrots = list(map(int, input().split()))
#     carrots.sort()
#     idx_lst = [i for i in range(N - 1)]
#
#     tmp_res = float('inf')
#     flag = -1
#
#     # for comb in combinations(idx_lst, 2):
#     #     box1 = carrots[:comb[0]+1]
#     #     box2 = carrots[comb[0]+1:comb[1]+1]
#     #     box3 = carrots[comb[1]+1:]
#     for a in range(N - 2):
#         for b in range(a + 1, N - 1):
#             box1 = carrots[:a + 1]
#             box2 = carrots[a + 1: b + 1]
#             box3 = carrots[b + 1:]
#             # for i in box1:
#             #     if i in box2 or i in box3:
#             #         break  # for i
#             #     for j in box2:
#             #         if j in box3:
#             #             break  # for j
#             # else:
#             if box1[-1] == box2[0] or box2[-1] == box3[0]:
#                 continue
#             if max(len(box1), len(box2), len(box3)) > N // 2:
#                 continue
#             else:
#                 flag = 0
#                 tmp_diff = max(len(box1), len(box2), len(box3)) - min(len(box1), len(box2), len(box3))
#                 tmp_res = min(tmp_res, tmp_diff)
#     if flag == 0:
#         res = tmp_res
#     else:
#         res = -1
#
#     print(f'#{tc} {res}')