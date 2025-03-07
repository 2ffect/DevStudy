# 이진수 표현
# # 나
# T = int(input())
# for tc in range(1, T+1):
#     I, B = map(int, input().split())
#
#     cnt = 0
#     for idx in range(I):
#         # 맨 우측 비트부터 1인지 확인
#         if B & (1 << idx):
#             # 맞으면 횟수 추가
#             cnt += 1
#         # 1이 아니라면 브레이크
#         else:
#             break
#     # 1의 수가 I와 같다면 모두 켜져있으니까 ON
#     if cnt == I:
#         print(f'#{tc} ON')
#     else:
#         print(f'#{tc} OFF')

## 금기륜 강사님
def solution():
    target = M
    # N 번 확인한다
    for _ in range(N):
        # 맨 우측 비트가 1인지 체크
        # 0x1, 0b1, 1 모두 표현가능
        # - 0x1 : 비트 연산이라는 것을 명시하기 위해 사용
        if target & 0x1 == 0:
            # 0 이라면 더 볼 필요 없다.
            return False
        # 1 이라면 우측 비트를 삭제하고 다시 확인
        target = target >> 1
    return True

# # 조금 더 단순한 방법
# def solution():
#     # N개의 1을 구함
#     mask = (1 << N) - 1
#     result = (M & mask) == mask
#     return result

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = solution()
    if result:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')