# 단순 2진 암호코드
import sys
sys.stdin = open("1240_input.txt")

info = {
    0: '0001101', 1: '0011001', 2: '0010011', 3: '0111101',
    4: '0100011', 5: '0110001', 6: '0101111', 7: '0111011',
    8: '0110111', 9: '0001011'
}

T = int(input())
for tc in range(1, T+1):
    # 배열의 크기
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]
    # 암호 모든 코드 1로 끝남, 거꾸로 한 줄씩 조회하면서 1이 등장하면 거기서부터 56자리 가져오기 == 그게 검증해야할코드
    # 리스트에 다 추가하고 뒤집기
    pass_num = []
    # 한 줄씩 가져오기
    for ar in arr:
        re_ar = list(reversed(ar))
        # print(re_ar)
        # 뒤로 순회하며 1을 찾기
        for i in range(M):
            if re_ar[i] == '1':
                # ar[i]가 1이면 거기부터 56개 담기 7*8
                pass_num.append(re_ar[i:i+56])
                break
        if len(pass_num) > 0:
            break

    pass_num = ''.join(reversed(pass_num[0]))

    # 7자씩 끊어서 암호코드에 맞춰서 정리
    trans_num = []
    num = ''
    for i in pass_num:
        num += i
        if len(num) == 7:
            trans_num.append(num)
            num = ''
    dem_num = []
    for trans in trans_num:
        for key, value in info.items():
            if value == trans:
                dem_num.append(key)

    # 자리수 계산
    single = [dem_num[0], dem_num[2], dem_num[4], dem_num[6]]
    double = [dem_num[1], dem_num[3], dem_num[5], dem_num[7]]

    if ((sum(single) * 3) + sum(double)) % 10 == 0:
        print(f'#{tc} {sum(dem_num)}')
    else:
        print(f'#{tc} 0')