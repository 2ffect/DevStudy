# 중복 순열과 순열 구하기

# N개의 주사위를 던져 나올 수 있는 모든 중복순열(1)과 순열(2)을 출력
# 주사위 숫자는 1~6, N개 결과 출력
# 중복 순열
def KKFFCC(x):
    # N + 1개가 되면 출력 후 리턴
    if x == N+1:
        print(*path)
        return
    # 중복이기 때문에 방문확인 X
    for i in range(1, 7):
        path.append(i)
        KKFFCC(x + 1)
        path.pop()
# 순열
def KFC(x):
    if x == N + 1:
        print(*path)
        return
    for i in range(1, 7):
        if visited[i] == True: continue
        visited[i] = True
        path.append(i)
        KFC(x + 1)
        path.pop()
        visited[i] = False

N, M = map(int, input().split())

path = []
visited = [False for _ in range(8)]

# M 이 1 1이면 중복순열을 출력
if M == 1:
    KKFFCC(1)
elif M == 2:
    KFC(1)
else:
    print('M 값이 틀렸습니다.')