# 정점의 수
v = int(input())
tree = list(map(int, input().split()))
# 간선의 수
n = v - 1

# 부모 번호로 부터 자식 번호를 저장
left = [0] * (v + 1)
right = [0] * (v + 1)
# 자식 번호로 부터 부모 번호를 저장
par = [0] * (v + 1)

for i in range(n):
    # p = 부모, c = 자식, 단방향
    p, c = tree[i * 2], tree[i * 2 + 1]
    # 부모 노드 기록
    par[c] = p
    # 왼쪽 노드부터 삽입
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

# 루트 찾기
root = 1
for i in range(1, n+1):
    if par[i] == 0:
        root = i
        break
result = []

def pre_order(v):
    # v가 유효하다면
    if v:
        result.append(v)
        pre_order(left[v])
        pre_order(right[v])

pre_order(root)

print(*result)
