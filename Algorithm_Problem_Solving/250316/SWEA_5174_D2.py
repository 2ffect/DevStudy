def sub_tree(v):
    global cnt

    if v:
        cnt += 1
        sub_tree(left[v])
        sub_tree(right[v])


T = int(input())

for tc in range(1, T+1):
    # E = 간선의 개수,  R = 기준노드
    E, R = map(int, input().split())
    # 부모/자식 쌍
    arr = list(map(int, input().split()))

    # 부모 노드를 기준으로 자식 노드를 기록
    left = [0] * (E + 2)
    right = [0] * (E + 2)
    # 자식 노드를 기준으로 부모 노드를 기록
    par = [0] * (E + 2)

    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        par[c] = p
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    # print(left)
    # print(right)
    # print(par)

    cnt = 0
    sub_tree(R)

    print(f'#{tc} {cnt}')