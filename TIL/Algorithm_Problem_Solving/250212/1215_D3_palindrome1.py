# 1차 시도
# 시작 시간 : 2/12 17:00
# 종료 시간 : 2/12 17:21 실패.

#2차 시도
# 시작 시간 :
# 종료 시간 :


import sys
sys.stdin = open("1215_input.txt", 'r')

for tc in range(1):
    n = int(input())
    arr = [list(input()) for _ in range(8)]

    # 찾아야 하는 회문의 길이 = n
    # 행, 열의 길이는 8로 고정
    # 행과 열을 모두 각 각 순회하며 회문을 찾은 뒤 cnt에 추가하기.
    # 각 각 행 열의 순회 조건은 8-n+1 까지
    # 회문의 조건에 맞는다면 cnt += 1

    cnt = 0
    # 행 순회 하며 회문 찾기
    for i in range(8-n+1):
        # 회문 범위를 가져와서, 회문이 맞는
        # cd 지 비교.
        for j in range(n):
            # 회문 조건에 안 맞으면 종료하고 i 구간 이동. break 사용.


        # 회문이면 cnt +1 하고 for i 순회
        else:
            cnt += 1


    print(cnt)
