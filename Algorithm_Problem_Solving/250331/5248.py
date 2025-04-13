'''
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
'''

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[] for _ in range(1, N + 1)]
    print(adj)
    for i in range(M):
        f, t = arr[i * 2], arr[i * 2 + 1]
        adj[f].append(t)
        adj[t].append(f)

    print(adj)