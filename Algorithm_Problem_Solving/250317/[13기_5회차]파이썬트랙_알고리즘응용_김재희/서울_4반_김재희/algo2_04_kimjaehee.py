# 이진 > 십진
def bin_to_de(arr):
    global bin_to_de_result
    result = 0
    pow = 0

    for num in reversed(arr):
        if num == '1':
            result += 2 ** pow
            pow += 1
            continue
        else:
            pow += 1
            continue

    bin_to_de_result.append(result)


# 전위
def pre_order(v, N):
    global pre_binary0
    # 노드 번호가 유효할때
    if v <= N:
        pre_binary.append(tree[v])
        # 왼쪽 노드 확인
        pre_order(2 * v, N)
        # 오른쪽 노드 확인
        pre_order(2 * v + 1, N)


# 중위
def in_order(v, N):
    global in_binary
    if v <= N:
        in_order(2 * v, N)
        in_binary.append(tree[v])
        in_order(2 * v + 1, N)


# 후위
def post_order(v, N):
    global post_binary
    if v <= N:
        post_order(2 * v, N)
        post_order(2 * v + 1, N)git
        post_binary.append(tree[v])

'''
4
4
0 0 1 1
4
0 1 1 0
5
0 1 0 1 0
4
1 1 0 0

#1 10
#2 6
#3 24 
#4 12
'''

for tc in range(1, int(input()) + 1):
    # N 노드의 수
    N = int(input())
    arr = input().split()
    # 트리 만들기
    tree = [0] * (N+1)
    # 트리에 arr값을 저장
    for i in range(N):
        # 트리 1번 인덱스 부터 값 저장
        tree[1 + i] = arr[i]

    # 각 순회법 별로 값을 저장할 리스트.
    pre_binary = []
    in_binary = []
    post_binary = []
    # 각 순회법으로 순회
    pre_order(1, N)
    in_order(1, N)
    post_order(1, N)

    # 각 순회를 결과값 이진을 십진 변환 값으로 변환 저장할 리스트
    bin_to_de_result = []
    # 이진 -> 십진 변환
    bin_to_de(pre_binary)
    bin_to_de(in_binary)
    bin_to_de(post_binary)

    # 최대값을 찾아 결과 출력
    print(f'#{tc} {max(bin_to_de_result)}')