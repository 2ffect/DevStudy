# Memoization
- 메모이제이션(memoization)은 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해 매번 다시 계산하지 않도록 하여
전체적인 실행속도를 빠르게 하는 기술, 동적 계획법의 핵심
 
## 메모이제이션 적용 알고리즘
```python
# memo를 위한 배열을 할당하고 모두 0으로 초기화 한다.
# memo[0]을 0으로 memo[1]을 1로 초기화한다.

def fibo1(n):
    global memo
    if n >= 2and memo[n] == 0:
        memo[n] = fibo1(n - 1) + fibo1(n - 2)
    return memo[n]

memo = [0] * (n + 1)
memo[0] = 0
memo[1] = 1
```