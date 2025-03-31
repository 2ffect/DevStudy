# 최소신장 트리
import sys
sys.stdin = open('MST_input.txt')

def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        start, end, weight = map(int, input().split())
        edges.append((start, end, weight))

    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(V + 1)]
    # 간선 선택 수
    cnt = 0
    # MST
    mst = 0

    for start, end, weight in edges:
        # start와 end가 연결이 안 되어 있으면 선택
        if find_set(start) != find_set(end):
            union(start, end)
            cnt += 1
            mst += weight

            if cnt == V:
                print(f'#{tc} {mst}')
                break

