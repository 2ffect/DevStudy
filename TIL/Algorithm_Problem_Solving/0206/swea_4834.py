T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    
    # 0~9 까지 세야함
    counts = [0] * 10 
    C = len(counts)
    for i in range(N):
        counts[arr[i]] += 1
    # print(list)

    # 가장 큰 값을 가진 인덱스 찾기 
    max_idx = 0
    max_num = 0

    for j in range(C):
        if counts[j] >= max_num: # 값이 같으면 큰 값 >=
            max_num = counts[j]
            max_idx = j
            

    print(f'#{tc} {max_idx} {max_num}')


