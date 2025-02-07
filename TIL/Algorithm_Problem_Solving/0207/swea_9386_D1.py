import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/JH/input1.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = input()

    # 다음에 0이 나오면 최종 확정해야 하는 1의 최고 연속 수
    total_cnt = 0
    # 다음에 0이 나오면 초기화 해야 하는 cnt
    cnt = 0
    for i in arr:
        # print(i, tc, total_cnt, cnt)
        if i == '1':
            cnt += 1
        else:
            cnt = 0
        
        # cnt 랑 total_cnt 비교해서 큰 값을 total_cnt에 넣기기
        total_cnt = max(total_cnt, cnt)

    print(f'#{tc} {total_cnt}')