for tc in range(1, int(input()) + 1):
    # N 노드의 수, M 리프 노드 수, L 출력 노드번호
    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)
    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num
    # print(tree)

    for i in range(N, 0, -1):
        # print(i)
        if i <= N:
            # print(i)
            if tree[i] == 0:
                # print(i)
                if (i * 2 + 1) <= N:
                    tree[i] = tree[i * 2] + tree[i * 2 + 1]
                else:
                    tree[i] = tree[i] + tree[i * 2]

    print(f'#{tc} {tree[L]}')