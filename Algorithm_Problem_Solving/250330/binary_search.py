import sys
sys.stdin = open('5207_input.txt')

def binary_search(arr, target):
    global cnt
    start = 0
    end = N - 1
    # 양쪽을 번갈아 갔는지 확인하는 signal
    start_signal = end_signal = 0

    while start <= end:
        mid = (start + end) // 2

        # 타겟을 찾았을 때
        if arr[mid] == target:
            if (start_signal == end_signal) or abs(start_signal - end_signal) == 1:
                cnt += 1

        # 타겟값이 중앙값 보다 큰 경우
        # 스타트 지점을 옮긴다.
        if target > arr[mid] and start_signal == 0:
            start = mid + 1
            start_signal, end_signal = 1, 0
            continue

        elif target < arr[mid] and end_signal == 0:
            end = mid - 1
            start_signal, end_signal = 0, 1
            continue

        else:
            break


for tc in range(1, int(input()) + 1):

    # N = list A길이 , M = list B길이
    N, M = map(int, input().split())
    # 이진 탐색 대상 리스트, 솔트 필수
    A = sorted(list(map(int, input().split())))
    # 타겟 number_list
    B = list(map(int, input().split()))
    # 양쪽을 번갈아 탐색한 횟수
    cnt = 0

    for i in range(M):
        binary_search(A, B[i])

    print(f'#{tc} {cnt}')