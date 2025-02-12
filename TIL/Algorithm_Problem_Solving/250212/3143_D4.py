import sys
sys.stdin = open("3143_input.txt", "r")


# 가장 빠른 문자열 타이핑
# A 안에 B 가 있으면 그 단어는 횟수 1로 인정
# 나머지 글자 수만큼 +1

T = int(input())

for tc in range(1, T+1):
    t, p = map(str, input().split())

    # 타이핑 횟수
    cnt = 0
    # t에 포함된 p 갯수 더하기
    cnt += t.count(p)
    # t에서 p 제거한 길이(나머지 문자의 수) 더하기
    cnt += len(t.replace(p , ''))


    print(f'#{tc} {cnt}')