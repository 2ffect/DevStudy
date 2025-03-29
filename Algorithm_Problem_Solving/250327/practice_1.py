# 1,1,1 ~ 6,6,6  출력 코드
path = []
visited = [False for _ in range(3)]

def KFC(x):
    if x == 2:
        print(*path)
        return

    for i in range(3):
        if visited[i] == True:
            continue
        visited[i] = True
        path.append(i)
        KFC(x + 1)
        path.pop()
        visited[i] = False

KFC(0)