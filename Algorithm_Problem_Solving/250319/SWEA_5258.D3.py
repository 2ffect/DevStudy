# 그룹 나누기
import sys
sys.stdin = open('5258_input.txt')

def make_set(x):
    # 1 ~ n 까지의 원소가 잇다면, 총 n 개의 집합을 생성
    # 각 원소의 부모(!= 대표자) 를 자신으로 초기화
    parents = [i for i in range(N + 1)]

    return parents

def find_set(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x

def union(x, y):
    # x와 y의 대표자를 검색
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 이미 같은 집합이라면? 병합 X
    if ref_x == ref_y:
        return
    # 다른 집합이라면, 합친다.
    # 문제에 따라 우선되는 집합으로 합치면 된다.
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


for tc in range(1, int(input()) + 1):
    # N = 총 인원 수 / M = 신청서 수
    N, M = map(int, input().split())
    parents = make_set(N + 1)
    union_list = list(map(int, input().split()))

    for i in range(M):
        f, t = union_list[i * 2], union_list[i * 2 + 1]
        union(f, t)

    result = []
    for j in range(1, N+1):
        result.append(find_set(j))

    ans = len(set(result))

    print(f'#{tc} {ans}')
