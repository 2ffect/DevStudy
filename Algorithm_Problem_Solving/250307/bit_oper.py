
print(7 & 5)
print(7 | 5)

# 1. 이진수 변환
# 2. 각 자리를 AND, OR 연산

print(bin(0x4A3 | 25))

secret_code = 1004
print(7070 ^ secret_code)
print(6258 ^ secret_code)


# 비트연산 응용
arr = [1, 2, 3, 4]
print(f'부분 집합의 수 : {1 << len(arr)}')

for i in range(1 << len(arr)):      # 0 ~ 15
    for idx in range(len(arr)):
        # (1 << idx) : 0b1, 0b10, 0b100, 0b1000
        # i 의 idx번째 bit가 1인지 (부분집합에 포함되어 있는지 확인)
        if i & (1 << idx):
            print(arr[idx], end=" ")
    print()


# 응용. 부분집합의 합이 10인 부분집합과, 총 몇개인지 출력

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cnt = 0

for i in range(1 << len(arr)):
    subset = []
    total = 0
    for idx in range(len(arr)):
        if i & (1 << idx):
            subset.append(arr[idx])
            total += arr[idx]

    if total == 10:
        print(f'합이 10인 부분집합 : {subset}')
        cnt += 1

print(f'총 갯수 : {cnt}')

# ------------ 음수 표현
print(bin(5))
print(bin(5))

print(~4, bin(~4))