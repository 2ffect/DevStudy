# 중위순회
def in_order(v, N):
    global cnt
    # 노드가 N 이하일 때까
    if v <= N:
        # 왼쪽 자식 방문
        in_order(v * 2, N)
        cnt += 1
        tree[v] = cnt
        # 오른쪽 자식 방문
        in_order(v * 2 + 1, N)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # cnt 를 저장할 트리를 생성
    tree = [0] * (N + 1)
    cnt = 0
    # 중위순회를 1부터 N까지
    in_order(1, N)
    print(f'#{tc} {tree[1]} {tree[N//2]}')