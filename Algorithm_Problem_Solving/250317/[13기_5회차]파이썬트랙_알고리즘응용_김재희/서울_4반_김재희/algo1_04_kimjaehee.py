# 싸피 이진수
'''
4
6 2
100101
7 3
1001011
7 5
1001011
7 2
0101101

#1 4
#2 6
#3 0
#4 3
'''


for tc in range(1, int(input()) + 1):
    # N : 이진수의 길이, K = 포함해야하는 1의 수
    N, K = map(int, input().split())
    binary = input().strip()

    check_bin = []
    short_bin = ''
    cnt = 0
    # 기준 바이너리 찾기
    for i in range(N):
        # 1의 수가 K개 라면
        if cnt == K:
            # 리스트에 추가하고 나머지 초기화
            check_bin.append(short_bin)
            cnt = 0
            short_bin = ''

        # 기준점이 1 일때
        if binary[i] == '1':
            # 짧은 이진수에 추가해주고 1의 수 추가
            short_bin += binary[i]
            cnt += 1
            for j in range(i+1, N):
                # 다음 숫자가 1이면 짧은 이진수에 추가하고 1의 수 차가
                if binary[j] == '1':
                    short_bin += binary[j]
                    cnt += 1
                    # 1이 K개면 종료
                    if cnt == K:
                        break
                # 다음 숫자가 0이면 짧은 이진수에 추가하고 다음 숫자 확인
                else:
                    short_bin += binary[j]

    # 조건이 충족되지 않으면
    if len(check_bin) == 0:
        # 해당 tc는 0을 출력
        print(f'#{tc} 0')
    else:
        # 최대 길이를 가지는 이진수를 찾아서 출력
        max_len = 0
        for check in check_bin:
            bin_len = len(check)
            max_len = max(max_len, bin_len)

        print(f'#{tc} {max_len}')
