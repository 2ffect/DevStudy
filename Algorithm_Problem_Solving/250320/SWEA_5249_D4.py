# 최소 신장 트리

import sys
sys.stdin = open('5249_input.txt')

# 크루스칼 사용 (사이클이 없어야 할 조건)

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

    # 작은것을 대표자로
    if ref_x < ref_y:
        parents[ref_y] = ref_x

    else:
        parents[ref_x] = ref_y


for tc in range(1, int(input()) + 1):
    # 마지막 노드 번호, 간선의 수
    V, E = map(int, input().split())
    # 노드의 간선 정보를 저장
    v_info = []

    for _ in range(E):
        start, end, weight = map(int, input().split())

        # 저장
        v_info.append((start, end, weight))

    # 가중치를 기준으로 정렬
    v_info.sort(key=lambda x: x[2])
    # 대표자
    parents = [i for i in range(V + 1)]

    # 선택한 수
    cnt = 0
    # 최소신장트리
    result = 0

    for start, end, weight in v_info:
        # start와 end가 연결되지 않았다면 선택
        if find_set(start) != find_set(end):
            union(start, end)
            cnt += 1
            result += weight

            # 마지막 노드만큼 선택해왔으면 종료
            if cnt == V:
                break

    print(f'#{tc} {result}')