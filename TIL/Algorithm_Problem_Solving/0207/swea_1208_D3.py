import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/JH/dump.txt", "r")

T = 10
for tc in range(1, T+1):
    dump_cnt = int(input())
    box_height = list(map(int, input().split()))

    for dump in range(dump_cnt):
        max_h = 0
        min_h = 0
        for i in range(100):
            if box_height[i] > box_height[max_h]:
                max_h = i

            if box_height[i] < box_height[min_h]:
                min_h = i

        box_height[max_h] -= 1
        box_height[min_h] += 1

    max_idx = 0
    min_idx = 0

    for i in range(100):
        if box_height[i] > box_height[max_idx]:
            max_idx = i
        if box_height[i] < box_height[min_idx]:
            min_idx = i

    result = box_height[max_idx] - box_height[min_idx]

    print(f'#{tc} {result}')