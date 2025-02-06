T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    
    # 0~9 까지 세야함
    counts = [0] * 10 
    C = len(counts)
    for i in range(N):
        counts[arr[i]] += 1
    
    # 각 최대 값 정의
    max_num = 0
    max_idx = 0
