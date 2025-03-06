# Tree 연습문제 1. 전위 순회

import sys
sys.stdin = open("23879_input.txt")

# 전위 순회
def pre_order(T):
    global pre_list
    # 유효한 노드라면
    if T:
        # 리스트에 추가
        pre_list.append(T)
        # 왼쪽 노드로 이동
        pre_order(left[T])
        # 오른쪽 노드로 이동
        pre_order(right[T])

    return pre_list
# N = 정점 수 / E = 간선 수 / arr = 입력 받은 쌍
N = int(input())
E = N - 1
arr = list(map(int, input().split()))

# 부모 번호로 부터 자식 번호를 저장
left = [0] * (N+1)
right = [0] * (N+1)
# 자식 번호로 부터 부모 번호 저장
par = [0] * (N+1)

for i in range(E):
    # from = f / to = t
    f, t = arr[i * 2], arr[i * 2 + 1]
    # 자식 번호에 부모 번호저장
    par[t] = f
    # 왼쪽 노드가 비었다면 왼쪽에 넣기
    if left[f] == 0:
        left[f] = t
    # 왼쪽 노드가 차있다면 오른쪽에 넣기
    else:
        right[f] = t

# 루트 찾기
root = 1 # 임의 값
# 노드번호인 1번부터 마지막 노드번호까지 순회
for j in range(1, N+1):
    # par[j]가 0이라면 부모가 없는 것, 즉 루트 노드가 된다.
    if par[j] == 0:
        root = j
        break

pre_list = []
print(*pre_order(root))
