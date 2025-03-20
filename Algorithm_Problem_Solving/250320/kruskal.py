import sys
sys.stdin = open('graph.txt')

# 크루스칼
# 모든 간선의 가중치를 보고
# 가중치가 작은 간선부터 고르자 (정렬)
# 이 때, 사이클이 발생하면 pass

def find_set(x): # 대표자 검색
    if x == parents[x]:
        return x

    # 경로 압축
    parents[x] = find_set(parents[x])
    return  parents[x]

def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    # 작은것을 대표자로.
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


V, E = map(int, input().split())
edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())

    # 간선에 대한 정보들을 저장
    edges.append((start, end, weight))

# 가중치를 기준으로 정렬
edges.sort(key=lambda x: x[2])
# 대표자 (정점을 기준으로)
parents = [i for i in range(V)]

# 작은 것 부터 고르며 진행
# N-1개를 선택할 때 까지

# 선택 수
cnt = 0
# MST 가중치의 합
result = 0

for start, end, weight in edges:
    # start와 end가 연결이 안 되어 있으면 선택
    if find_set(start) != find_set(end):
        union(start, end)
        cnt += 1
        result += weight

        if cnt == V-1:
            break

print(result)
