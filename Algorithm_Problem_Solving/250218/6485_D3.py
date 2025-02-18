# 삼성시의 버스노선
# 제한시간 1시간

# 시작 시간 : 02/18 16:40
# 종료 시간 : 02/18 17:39


# 테스트 케이스 마다 노선이 주어진다 ?
# 노선은 [1, 3] 이면 1, 2, 3번 버스 정류장을 가는 버스, [2, 5] 이면 2, 3, 4, 5에 가는 버스다.
# 버스 정류장이 1 ~ 5000번까지 있을 때 주어진 노선에 의 버스 정류장에 +1을 하면 된다.
# 주어진 노선 별 방문 정류장을 모두 더하고,
# 주어지는 수 만큼 버스 정류장을 일렬로 출력한다.?

import sys
sys.stdin = open("6485_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    # 주어지는 버스 정류장 노선의 수
    N = int(input())
    # 2차원 배열로 노선을 받아온다.
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 출력해야 할 노선의 수
    P = int(input())
    # 출력해야 할 정류장의 번호? 엔터로 들어오는걸 하나의 리스트로 만들어 두면 나중에 쓰기 좋을듯 ?
    # 엔터로 하나하나 들어오는걸 어떻게 리스트로 받지 ?
    num_list = []
    for _ in range(P):
        num_list.append(int(input()))
    # 이게 맞다고 ,, ?

    # 버스 정류장 생성 (1 ~ 5000)
    bus_stop = [0] * 5000

    # 2차원 배열에서 노선 하나를 가져와서, [1, 3] 이면, 생성한 버스정류장의 1부터 3번까지 +1 을 해줘야 하는데.
    # 노선 하나를 가져와서 그걸 다시 어떻게 쓸래 ?
    # 그 안에 있는 인덱스를 활용해서 bus_stop 에 더해줘야지.
    # 근데 무조건 2개의 정수로 주어지니까 가져온 노선의 인덱스는 0, 1
    # 가져온 인덱스 범위를 인덱스로 가지는 bus_stop에 +1을 해준다.
    for i in range(N):
        bus = arr[i]
        # print(bus)

        for j in range(1):
            for k in range(bus[j]-1, bus[j+1]):
                bus_stop[k] += 1

                # print(bus_stop[k])
    # print(bus_stop[:P])

    # print(f'#{tc}', *bus_stop[:P])
    # 이게 아니라고?????????
    # num_list 에 저장 된 값을 인덱스로 활용해서 출력해라 ?

    # # #{tc} 랑 어떻게 구분을 짓지?
    # print(f"#{tc}", end=' ')
    # for p in num_list:
    #     print(bus_stop[p-1], end=' ')

    # 이거라고 ?;;;
    # 아닌데 ?
    # 새 리스트에 추가해봐
    result = []
    for p in num_list:
        result.append(bus_stop[p-1])

    print(f'#{tc}', *result)