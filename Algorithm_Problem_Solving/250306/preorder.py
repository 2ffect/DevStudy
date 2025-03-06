# 연습문제
# 트리의 총 수 V 와 V-1개의 간선이 주어진다.
# 간선은 항상 부모/자식 순서이다.
# 간선은 항상 부모 정점이 작은 것 부터 나열되고, 부모가 같다면 자식이 작은 것 부터 나열된다.

# 전위 순회하여 정점의 번호를 출력하라.

'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

# 전위순회 함수 - 방문한 정점(부모) 먼저 처리
def pre_order(T):
    # 존재하는 정점이라면,
    if T:
        print(T)    # 방문 정점에서 할 일 처리
        # 왼쪽 자식(서브트리) 로 이동
        pre_order(left[T])
        # 오른쪽 자식(서브트리) 로 이동
        pre_order(right[T])

# 중위순회 함수
def in_order(T):
    # 존재하는 정점이라면,
    if T:
        # 왼쪽 자식(서브트리) 로 이동
        in_order(left[T])
        # 방문 정점에서 할 일 처리
        print(T)
        # 오른쪽 자식(서브트리) 로 이동
        in_order(right[T])

# 후위순회 함수
def post_order(T):
    # 존재하는 정점이라면,
    if T:
        # 왼쪽 자식(서브트리) 로 이동
        post_order(left[T])
        # 오른쪽 자식(서브트리) 로 이동
        post_order(right[T])
        # 방문 정점에서 할 일 처리
        print(T)

N = int(input())
# 간선 수
E = N - 1
arr = list(map(int, input().split()))

# 부모를 인덱스로 자식 번호를 저장 하기
# 왼쪽
left = [0] * (N+1)
# 오른쪽
right = [0] * (N+1)

# 자식을 인덱스로 부모 번호를 저장하기
par = [0] * (N+1)

for i in range(E):
    f, t = arr[i*2], arr[i*2+1]
    # 자식을 인덱스로 부모를 저장
    par[t] = f
    # 왼쪽 자식이 아직 없다면
    if left[f] == 0:
        # 왼쪽 자식
        left[f] = t
    # 왼쪽 자식이 있는 경우
    else:
        # 오른쪽 자식
        right[f] = t

# 루트 찾기
root = 1
for i in range(1, N+1):
    # 부모 정점이 없으면 루트,
    if par[i] == 0:
        root = i
        break

pre_order(root)