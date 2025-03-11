test = int(input())
for test in range(1, test+1):
    n = int(input())
    pascals = [[] for _ in range(n)]         #* *삼각형을 그릴 틀*
    pascals[0].append(1)
    print(pascals)#* *첫열은 그냥 삽입*
    for i in range(1, n):                    #* *2열부터 그릴 것임.*
        stack = pascals[i-1][:]              #* *1열(i-1열을 복사)*
        pascals[i].append(1)                 #* *첫인자 삽입*
        for j in range(1, i):                #* *다음인자부터는 i-1열의 인자를 하나하나 pop 해주며 다음에 나올 인자와의 합을 i열에 삽입해줌.*
            pascals[i].append(stack.pop()+stack[-1])
        pascals[i].append(1)             #* *마지막 인자 삽입.*
                                             #* *어차피 좌우대칭이므로 기존 파스칼 삼각형의 규칙인*                                    #* *i-1열의 0,1번째 인자의 합이 i열 1인자가 될 필요 없음
    print(f'#{test}')                        #* *stack 을 이용 i-1열의 i,i-1번째 인자가 i열의 1번 인자가 되는 방식.*
    for pas in pascals:
        print(*pas)


'''
논리와 증명 12.
n ** 2 이 3의 배수이면 n은 3의 배수임을 증명하라.

대우명제 : n이 3의 배수가 아니면, n ** 2은 3의 배수가 아니다.
대우명제가 참이면 본 명제도 참이 된다.

대우명제 증명
3의 배수가 아닌 조건
1. n = 3k + 1 -> n ** 2 == 9(k ** 2) + 6k + 1 == 3(3(k ** 2) + 2k) + 1
    -> 3의 배수는 (3(k**2) * 2k), 1이 더해지므로 n**2은 3의 배수가 아니다.
    
2. n = 3k + 2 -> n ** 2 == 9(k ** 2) + 12k + 4 == 3(3(k ** 2) + 4k + 1) + 1
    -> 3의 배수는 (3(k ** 2) + 4k + 1), 1이 더해지므로 n**2은 3의 배수가 아니다.

대우명제가 참이기 때문에 본 명제 n ** 2 이 3의 배수이면 n은 3의 배수는 참이다.


기초수식 4.
T(n) = T(n/2) + 1 = T(n/4) + 1 + 1 = T(n/8) + 1 + 1 + 1 = ...
T(n/2) = T(n/4) + 1 = T(n/8) + 1 + 1
T(n/4) = T(n/8) + 1
T(n) = T(n/(2^k)) + k
T(1) = 1
2^k = n 이면 k = log n
T(n) = T(1) + log n = 1 + log n
O(log n)
'''