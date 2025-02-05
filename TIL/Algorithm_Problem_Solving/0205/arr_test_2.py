# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

T = int(input()) 
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N = 배열 크기, M = 이웃한 수
    V = list(map(int, input().split()))

    max_v = 0
    min_v = 10000000


    # V[i]부터 V[M-1]까지 더해서 젤 작으면 min이고 젤 크면 max 인데? 

    for i in range(N-M+1):
        num = 0
        for j in range(i, i+M):
            num += V[j]

        if num > max_v:
            max_v = num
        if num < min_v:
            min_v = num
    

    # print(max_v, min_v)

    print(f"#{tc} {max_v - min_v}")

