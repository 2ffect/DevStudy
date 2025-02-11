# 배수 스위치

# N 개의 전구 1 ~ N
# N 개의 스위치 1 ~ N
# i 번 스위치는 i 배수 번호를 가지는 전구의 상태를 모두 반전.
# 모든 전구를 끄기 위해 눌러야 하는 스위치 횟수
# Y = 켜짐
# N = 꺼짐

arr = list(input())
N = len(arr)

# 스위치 작동 횟수
cnt = 0
# 전구 순회
for i in range(1, N+1):
    # 전구가 켜져있으면 끄고
    if arr[i-1] == 'Y':
        # 스위치 작동
        cnt += 1
        arr[i-1] = 'N'
        # 스위치를 끌 때 i의 배수에 위치한 스위치가 같이 동작함.
        # 0은 1번 스위치임.
        for j in range(i+1, N+1):
            if j % i == 0:
                if arr[j-1] == 'Y':
                    arr[j-1] = 'N'
                else:
                    arr[j-1] = 'Y'


if 'Y' not in arr:
    print(cnt)
else:
    print(-1)
