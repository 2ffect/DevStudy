# 이진 탐색
import sys
sys.stdin = open('5207_input.txt')

# arr = 검색할 리스트, b = 타겟값
def binary_search(arr, b):
    global cnt
    start = 0
    end = N-1
    # 왼쪽 / 오른쪽 이동가능성 확인
    # 0 = 이동 가능 / 1 = 이동 불가능
    start_signal = end_signal = 0

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == b:
            # 둘다 0/0 인 경우 바로 중심점을 찾은 경우 또는 같은 횟수를 움직인 경우
            # 둘의 차이 절대값이 1인 경우, 한 쪽만 이동시켜 찾은경우 또는 한쪽을 더 움직인 경우
            if start_signal == end_signal or abs(start_signal - end_signal) == 1:
                cnt += 1
                break

        # b가 중간값 보다 클 때, start 위치를 옮겨야 하는데 이때 스타트를 옮길 수 있다면
        if b > arr[mid] and start_signal == 0:
            start = mid + 1
            # start 를 옮겼기 때문에 start_signal = 1로 변경,
            # 기존 end_signal 이 1이었다면 이제 옮길 수 있기 때문에 0으로 변경
            start_signal, end_signal = 1, 0
            continue

        # b가 중간값 보다 작을때, end 위치를 옮겨야 하는데 이때 end를 옮길 수 있다면
        elif b < arr[mid] and end_signal == 0:
            end = mid - 1
            # end 를 옮겼기 때문에 end_signal = 1로 변경,
            # 기존 start_signal 이 1이었다면 이제 옮길 수 있기 때문에 0으로 변경
            start_signal, end_signal = 0, 1
            continue

        else:
            break

for tc in range(1, int(input()) + 1):
    # N = 이진탐색 할 리스트의 길이 / M = 이진 탐색 대상 숫자 리스트의 길이
    N, M = map(int, input().split())
    # 이진탐색 할 배열(sort 해)
    A = sorted(list(map(int, input().split())))
    # A 리스트에 속 해 있는지 확인할 리스트
    B = list(map(int, input().split()))
    # B의 요소가 A 에 속해있는 수
    cnt = 0
    # B 를 순회해서 가져와서 요소가 A에 속해있는지 이진탐색
    for i in range(M):
        binary_search(A, B[i])

    print(f'#{tc} {cnt}')
