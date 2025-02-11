#N 개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이 출력

T = int(input())    # 테스트 케이스 수 입력받기
for tc in range(1, T+1): # 테스트 케이스 별 처리
    N = int(input()) # 케이스 별 입력 수
    arr = list(map(int, input().split())) # 케이스 별 arr 요소 입력받기

    max_v = arr[0]
    min_v = arr[0]

    for i in range(N):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]
    
    print(f"#{tc} {max_v - min_v}")