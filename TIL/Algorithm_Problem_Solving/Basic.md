# Algorithm Problem Solving
## APS 기본 학습 목표
- 입출력을 제외한 내장함수 사용하지 않기
- 기본적인 내장함수의 동작원리 이해 하기
- 좋은 알고리즘 이해하고 활용하기

## 알고리즘
- 문제를 해결하기 위한 절차나 방법.

- 의사코드와 순서도 크게 두 가지로 알고리즘을 표현
<br>

![alt text](/TIL/Algorithm_Problem_Solving/img/pseudocode.png)
<br>

### 무엇이 좋은 알고리즘 인가?
1. 정확성 : 얼마나 정확하게 동작하는가
2. 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가
3. 메모리 사용량 : 얼마나 적은 메모리를 사용하는가
4. 단순성 : 얼마나 단순한가
5. 최적성 : 더 이상 개선할 여지없이 최적화되었는가

### 알고리즘 성능 분석 필요
- 많은 문제에서 성능 분석의 기준으로 알고리즘의 작업량을 비교한다.
- 알고리즘의 작업량을 표현할 때 **시간복잡도**로 표현한다.
<br>

![alt text](/TIL/Algorithm_Problem_Solving/img/1_to_100_1.png)
<br>

## 시간 복잡도 (Time Complexity)
- 실제 걸리는 시간을 측정
- 실행되는 명령문의 개수를 계산
<br>

![alt text](/TIL/Algorithm_Problem_Solving/img/1_to_100_2.png)
<br>

### 시간복잡도 빅-오(O) 표기법
- 빅-오 표기법 (Big-O Notation)
- 시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항만 표시
- 계수(Confficient) 는 생략하여 표시
<br>

![alt text](/TIL/Algorithm_Problem_Solving/img/Big_O.png)
<br>

### 시간 복잡도별 실제 실행 시간 비교
<br>

![alt text](/TIL/Algorithm_Problem_Solving/img/Time_Complexity.png)
<br>

## 배열 (Array)
- 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조
  
### 배열의 필요성
- 배열을 사용하면 하나의 선언을 통해 둘 이상의 변수를 선언할 수 있어 다수의 변수로 하기 힘든 작업을 배열을 활용해 쉽게 할 수 있다.

### 1차원 배열의 선언
```py
# 1차원 배열 선언의 예
arr = list()
arr = []
arr = [0] * 10 # 10칸짜리 일차원 배열

arr = [1, 2, 3]
```

### 1차원 배열의 접근
```py
arr[0] = 10 # 배열 arr의 0번 원소에 10을 저장
arr[idx] = 20 # 배열 arr의 idx번 원소에 20을 저장
```

