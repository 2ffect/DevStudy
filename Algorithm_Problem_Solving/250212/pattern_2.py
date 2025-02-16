t = 'TTTTTATTAATA'
p = 'TTA'

N = len(t)
M = len(p)

def p_search(p, t):
    for i in range(N-M+1):      # t에서 패턴 비교를 시작할 인덱스 위치
        for j in range(M) :     # p에서 비교할 위치 인덱스
            if t[i+j] != p[j]:
                break

        else:                   # break에 걸리지 않고 for가 성공적으로 끝난경우 실행
            return i            # 패턴이 처음 나타난 인덱스 리턴

    return -1                   # t 에 p 패턴이 없는 경우

print(p_search(p, t))

