# Control Statement (제어문)
- 코드의 실행 흐름을 제어하는 데 사용되는 구문
- **조건**에 따라 코드 블록을 실행
- **반복**적으로 코드를 실행

## 제어문
- 조건문 
    - if , elif, else
- 반복문
    - for, while
- 반복문 제어
    - break, continue, pass

## 조건문
## 개요
- 주어진 조건식을 평가하여 해당 조건이 참(True) 인 경우에만 코드 블록을 실행하거나 건너 뜀
- 파이썬 조건문에 사용되는 키워드
    - if / elif / else

## 'if' statement (조건문)
### if 문 기본 구조
```python
if 표현식:
    코드 블록 # if 표현식이 true 라면 실행
elif 표현식:
    코드 블록 # if 표현식이 false 일 때 elif 표현식이 true 라면 실행
else:
    코드 블록 # if, elif 모두 false 라면 실행
```
<br>

### 예시

![alt text](/TIL/img/if1.png)
<br>

![alt text](/TIL/img/if2.png)
<br>

## 복수 조건문 
- 조건식을 동시에 검사하는 것이 아니라 "순차적"으로 비교함
```python
dust = 35

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

# 보통
```
## 중첩 조건문
```python
dust = 480

if dust > 150:
    print('매우 나쁨') # 먼저 출력 후
    if dust > 300: # 중첩 조건문
        print('위험해요!') # 이어서 출력
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

# 매우 나쁨
# 위험해요!
```

## 반복문
## 개요
- 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
- 파이썬 반복문에서 사용되는 키워드
    - for
        - 특정 작업을 반복적으로 수행
    - while
        - 주어진 조건이 참인 동안 반복해서 실행

## 'for' statement (for 반복문)
- for
    - 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복

### for 반복문 기본 구조
```python
for 변수 in 반복 가능한 객체:
    코드 블록
```

### 반복 가능한 객체 (iterable)
- 반복문에서 순회할 수 있는 객체 (시퀀스 객체 뿐 아니라 dict, set 등도 포함함)

### for 반복문 작동 원리
- 리스트 내 첫 항목이 변수에 할당되고 코드 블록이 실행
- 다음으로 변수에 2번째 항목이 할당되고 코드 블록이 실행
- ... 마지막으로 변수에 마지막 항목이 할당되고 코드 블록이 실행

```python
items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)

# apple
# banana
# coconut
```

### 딕셔너리 순회
- 딕셔너리의 경우 key : value 쌍으로 이루어져 있기 때문에 반복문 순회 시 key 값이 출력 됨. value 추가 출력을 해야 함
```python
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key) 
    print(my_dict[key])
# x
# 10
# y
# 20
# z
# 30
```

### 인덱스로 리스트 순회
- 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경
```python
numbers = [4, 6, 10, -8, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)  # [8, 12, 20, -16, 10]
```

### 2중 for문 (충첩된 반복문)
```python
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)
```
- 안쪽 반복문은 outers 리스트의 각 항목에 대해 한 번씩 실행된다.
- print가 호출되는 횟수 => len(outers) * len(inners)

### 중첩 리스트 순회
- 안쪽 리스트 요소에 접근하려면 바깥 리스트를 순회하면서 중첩 반복을 사용해 각 안쪽 반복을 순회
```python
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem)  # ['A', 'B'] ['c', 'd']

for elem in elements:
    for item in elem:
        print(item)  # A B c d
```

## 'while' statement (while 반복문)
- 주어진 조건식이 True 인 동안 코드를 반복해서 실행 -> 조건이 False 가 될 때 까지 반복함

### while 반복문 기본 구조
```python
while 조건식:
    코드블록
```

### 사용자 입력에 따른 반복
- while 문을 사용할 경우 특정 입력 값에 대한 종료 조건을 잘 활용 해야함, 종료 조건이 반드시 필요함.


## 적절한 반복문 활용하기
### for
- 반복 횟수가 명확하게 정해져 있는 경우에 유용
- 리스트, 튜플, 문자열 등 시퀀스 형식의 데이터를 처리할 때
### while
- 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
- 사용자의 입력을 받아 특정 조건이 충족 될 때 까지 반복하는 경우

## 반복 제어
- for문과 while은 매 반복마다 본문 내 모든 코드를 실행하지만 때때로 일부만 실행하는 것이 필요할 때가 있음

### 반복문 제어 키워드
- break
    - 반복을 즉시 중지
- continue
    - 다음 반복으로 건너 뜀
- pass
    - 아무런 동작 수행없이 넘어감

### 반복문 제어 예시
```python
# break
for i in range(10):
    if i == 5:
        break
    print(i) # 0 1 2 3 4 

# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i) # 1 3 5 7 9 

# pass
for i in range(10):
    pass # 아무 작업도 안함
```

### pass 예시
1. 코드 작성 중 미완성 부분
    - 구현해야 할 부분이 미완성일 경우
```python
def my_function():
    pass
```
2. 조건문에서 아무런 동작을 수행하지 않아야 할 때
```python
if condition:
    pass # 아무런 동작도 수행하지 않음
else:
    # 다른 동작 수행
```
3. 무한 루프에서 조건이 충족되지 않을 때 pass를 사용해 루프를 계속 진행
```python
while True:
    if condition:
        break:
    elif condition:
        pass # 루프 계속 진행
    else:
        print('..')
```

## List Comprehension
- 간결하고 효율적인 리스트 생성 방법

### List Comprehension 구조
```python
[expression for 변수 in iterable]

list(expression for 변수 in iterable)

[expression for 변수 in iterable if 조건식]

list(expression for 변수 in iterable if 조건식)
```

### List Comprehension 예시

```python
# 기존 방식
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)


# 리스트 컴프리헨션
squared_numbers2 = [num ** 2 for num in numbers]

print(squared_numbers2)
```
### List Comprehension with if

```py
# 기존 방식
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)

print(evens)  # [0, 2, 4, 6, 8]

# List Comprehension
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```