# import sys
# sys.stdin = open("1213_input.txt", "r")

for _ in range(1, 11):
    tc = int(input())
    p = input()
    t = input()

    count = t.count(p)

    print(f'#{tc} {count}')