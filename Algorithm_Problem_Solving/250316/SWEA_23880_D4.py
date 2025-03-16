def in_order(v):
    global result

    if v:
        in_order(left[v])
        result.append(str(word[v]))
        in_order(right[v])


for tc in range(1, 11):
    # 정점의 수
    N = int(input())
    # 간선의 수
    E = N - 1

    # 부모 번호로 자식 번호
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    # 단어
    word = [0] * (N + 1)

    # 입력 받으면서 넣기
    for _ in range(N):
        in_put = input().split()
        L = len(in_put)

        if L > 3:
            n = int(in_put[0])
            word[n] = in_put[1]

            if left[n] == 0:
                left[n] = int(in_put[2])
                right[n] = int(in_put[3])

        elif len(in_put) > 2:
            n = int(in_put[0])
            word[n] = in_put[1]

            if left[n] == 0:
                left[n] = int(in_put[2])

        # 리프 노드
        else:
            n = int(in_put[0])
            word[n] = in_put[1]


    result = []
    in_order(1)
    ans = ''.join(result)
    print(f'#{tc} {ans}')
