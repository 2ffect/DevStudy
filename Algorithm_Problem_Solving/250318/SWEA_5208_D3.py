# 전기버스 2
import sys
sys.stdin = open('5208_input.txt')

def sub_set(cnt, total, subset):
    global charge_set
    # total이 station의 수와 같아지면 cnt를 리턴
    if total == station:
        charge_set.append(subset)
        return

    # 백트레킹
    if total > station:
        return

    if cnt == station-1:
        return

    sub_set(cnt + 1, total + battery[cnt], subset + [battery[cnt]])
    sub_set(cnt + 1, total, subset)

for tc in range(1, int(input()) + 1):
    # battery[0] = 정류장 수 / battery[1:] = 정류장 별 배터리 용량
    battery = list(map(int, input().split()))
    station = battery[0]
    start_point = battery[1]
