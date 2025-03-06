# 중위 순회

def in_order(v):
    global result
    if v:
        in_order(left[v])
        result.append(str(word[v]))
        in_order(right[v])

import sys
sys.stdin = open("1231_input.txt")

for tc in range(1, 11):
    # 정점의 수
    N = int(input())
    # 간선의 수
    E = N - 1

    left = [0] * (N+1)
    right = [0] * (N+1)
    par = [0] * (N+1)
    word = [0] * (N+1)

    # 인풋 받으면서 바로 트리 만들기.
    # E 번 받는다.
    for _ in range(N):
        # 인풋의 길이가 다르므로 길이 기준으로 분류,
        in_put = input().split()
        L = len(in_put)

        # 길이가 2 이상이면 자식노드가 존재함
        if L > 3:
            # 기준 정점
            n = int(in_put[0])
            word[n] = in_put[1]

            # 자식노드의 자리가 비었는지 확인 후 넣기
            if left[n] == 0:
                left[n] = int(in_put[2])
                right[n] = int(in_put[3])

        elif L > 2:
            # 기준 정점
            n = int(in_put[0])
            word[n] = in_put[1]

            # 자식노드의 자리가 비었는지 확인 후 넣기
            if left[n] == 0:
                left[n] = int(in_put[2])

        # 2 이하 이면 리프노드
        else:
            # 기준 정점
            n = int(in_put[0])
            word[n] = in_put[1]

    # 루트 찾기
    root = 1
    for i in range(1, N+1):
        if par[i] == 0:
            root = i
            break

    result = []
    in_order(root)
    ans = ''.join(result)
    print(f'#{tc} {ans}')