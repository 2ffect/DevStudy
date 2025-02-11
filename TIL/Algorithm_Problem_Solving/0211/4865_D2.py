import sys
sys.stdin = open("4865_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    max_cnt = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt =cnt

    print(f'#{tc} {max_cnt}')