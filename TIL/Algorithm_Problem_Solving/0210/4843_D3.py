import sys
sys.stdin = open("4843_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 총 10개 인덱스 홀/짝 구분 후 짝수는 max, 홀수는 min 으로 찾기
    for i in range(10):
        if i % 2 == 0:
            # i 가 짝수 일 때
            for j in range(N-1):
                # 최대 값 초기화 및 최대값 순서로 솔트
                max_idx = i
                for k in range(i+j, N):
                    if arr[max_idx] < arr[k]:
                        max_idx = k
                arr[max_idx], arr[i] = arr[i], arr[max_idx]
    # print(arr)
        else:
            # i 가 홀수 일 때
            for p in range(N-1):
                # 최소 값 초기화 및 최소값 순서대로 솔트
                min_idx = i
                for q in range(i+p, N):
                    if arr[min_idx] > arr[q]:
                        min_idx = q
                arr[min_idx], arr[i] = arr[i], arr[min_idx]


    result = ' '.join(map(str, arr[:10]))

    print(f'#{tc} {result}')

