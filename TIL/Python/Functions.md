# Functions (함수)
## 개요
### Functions (함수)
- 특정한 작업을 수행하기 위한 재사용 가능한 코드 묶음

### 함수를 사용하는 이유
- 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드 중복을 방지
- **재사용성**이 높아지고, 코드의 **가독성과 유지보수성**향상

```python
# 두 수의 합을 구하는 코드
num1 = 5
num2 = 3
sum_result = num1 + num2
print(sum_result) # 8

# 두 수의 합을 구하는 함수
def get_sum(num1, num2):
    return num1 + num2
```
<br>

### function call (함수 호출)
- 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것
- 형식 : function_name(arguments)
<br>

```python
# 함수를 호출하여 결과 출력
sum_result = get_sum(num1, num2)
print(sum_result) # 8
```

### 함수 구조
![alt text](/TIL/img/functions.png)

### 함수 정의와 호출
- 함수 정의(정의)
    - 함수 정의는 **def** 키워드로 시작
    - **def** 키워드 이후 함수 이름 작성
    - 괄호안에 **매개변수(parameter)**를 정의할 수 있음
    - **매개변수(parameter)**는 함수에 전달되는 값

- 함수 body
    - 콜론 (:) 다음 들여쓰기 된 코드 블록
    - 함수가 실행될 때 수행되는 코드를 정의
    ![alt text](/TIL/img/functions2.png)

- Docstring
    - 함수 body 앞에 선택적으로 작성 가능한 함수 설명서
    ![alt text](/TIL/img/functions3.png)

- 함수 반환 값
    - 함수는 필요한 경우 결과를 반환할 수 있음
    - return 키워드 이후에 반환할 값을 명시
    - return 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환
    - 함수 내에서 retunr문이 없다면 None이 반환됨
    ![alt text](/TIL/img/functions4.png)

- 함수 호출
    - 함수를 사용하기 위해서는 호출이 필요
    - 함수의 이름과 소괄호를 활용하여 호출
    - 필효한 경우 인자(argument)를 전달해야 함
    - 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 대입 됨
    ![alt text](/TIL/img/functions5.png)

```python
# 함수 정의
def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2

# 함수 호출
result = make_sum(100, 50)
print(result)
```

## 함수와 반환 값
### print() 함수는 반환 값이 없다.
- print() 함수는 화면에 값을 출력하기만 할 뿐 retunr 값이 없음
- 파이썬ㄴ에서 반환 값이 없는 함수는 기본적으로 None을 반환한다고 간주함
- 출력을 담당하는 함수는 결과를 return 하지 않으므로, 내부적으로 아무 값도 반환하지 않는 함수와 마찬가지로 None을 반환함

```python
return_value = print(1)
print(return_value) # None

def my_func():
    print('hello')

result = my_func()
print(result) # None
```

## 매개변수와 인자
### Parameter (매개변수)
- **함수를 정의할 때** , 함수가 받을 값을 나타내는 변수

### Argument (인자)
- **함수를 호출할 때** , 실제로 전달되는 값

#### 예시
```python
def add_number(x, y): # x와 y는 parameter (매개변수)
    result = x + y
    return result

a = 2
b = 3
sum_result = add_number(a, b) # a 와 b 는 argument (인자)
print(sum_result)
```

### 다양한 인자 종류
#### 1. Positional Arguments (위치인자)
- 함수 호출 시 인자의 위치에 따라 전달되는 인자
- 위치인자는 함수 호출 시 반드시 값을 전달해야 함
```python
# 1. Positional Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


greet('Alice', 25)  # 안녕하세요, Alice님! 25살이시군요.
greet(25, 'Alice')  # 안녕하세요, 25님! Alice살이시군요.
greet(
    'Alice'
)  # TypeError: greet() missing 1 required positional argument: 'age'

```

#### 2. Default Argument Values (기본 인자 값)
- 함수 정의에서 매개변수에 기본 값을 할당하는 것
- 함수 호출 시 **인자를 전달하지 않으면** , 기본값이 매개변수에 할당됨
```python
# 2. Default Argument Values
def greet(name, age=20):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


greet('Bob')  # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40)  # 안녕하세요, Charlie님! 40살이시군요.
```

#### 3. Keyword Arguments (키워드 인자)
- 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
- 매개변수와 인자를 일치시키지 않아도 특정 매개변수에 값을 할당할 수 있음
- 인자의 순서는 중요하지 않으며 인자의 이름을 명시하여 전달.
- 단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함.
```python
# 3. Keyword Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
greet(age=35, name='Dave')  # 안녕하세요, Dave님! 35살이시군요.
greet('Dave', age=35) # 안녕하세요, Dave님! 35살이시군요.
greet(age=35, 'Dave')  # Positional argument cannot appear after keyword arguments
```

#### 4. Arbitrary Argument List (임의의 인자 목록)
- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 ( * )를 붙여 사용
- 여러개의 인자를 tuple로 처리
```python
# 4. Arbitrary Argument Lists
def calculate_sum(*args):
    print(args)  # (1, 100, 5000, 30)
    print(type(args))  # <class 'tuple'>


calculate_sum(1, 100, 5000, 30)

```
#### 5. Arbitrary Keyword Argument List (임의의 인자 목록)
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 ( ** )를 붙여 사용
- 여러 개의 인자를 dictionary로 묶어 처리
```python
# 5. Arbitrary Keyword Argument Lists
def print_info(**kwargs):
    print(kwargs)


print_info(name='Eve', age=30)  # {'name': 'Eve', 'age': 30
```

### 함수 인자 권장 작성순서
- 위치 -> 기본 -> 가변 -> 가변 키워드
- 호출 시 인자를 전달하는 과정에서 혼란을 줄일 수 있도록 함 
- 절대적 규칙이 아니므로 상황에 따라 유연하게 조정

## 재귀 함수
- 함수 내부에서 자기 자신을 호출하는 함수
- 대표적인 예시 - 팩토리얼
    - factorial 함수는 자기 자신을 재귀적으로 호출하여 입력된 숫자 n의 팩토리얼을 계산
    - 재귀 호출은 n이 0이 될 때 까지 반복되며, 종료 조건을 설정하여 재귀 호출이 멈추도록 함
    - 재귀 호출의 결과를 이용하여 문제를 작은 단위의 문제로 분할하고, 분할된 문제들의 결과를 조합하여 최종 결과를 도출
```python
def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    else:
        # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
        return n * factorial(n - 1)


# 팩토리얼 계산 예시
print(factorial(5))  # 120

```
### 재귀 함수 특징
- 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며 코드의 가독성이 높아짐
- 1개 이상의 basc case(종료되는 상황)가 존재하고, 수렴하도록 작성

### 재귀 함수를 사용하는 이유유
- 문제의 자연스러운 표현
    -복잡한 문제를 간결하고 직관적으로 표현 가능
- 코드 간결성
    - 상황에 따라 반복문 보다 알고리즘 코드가 더 간결하고 명확해질 수 있음
- 수학적 문제 해결
    - 수학적 정의가 재귀적으로 표현되는 경우, 직접적인 구현 가능

### 재귀 함수 활용 시 기억해야 할 것
1. 종료 조건을 명확히
2. 반복되는 호출이 종료 조건을 향하도록

## 내장 함수 (Built-in function)
- 파이썬이 기본적으로 제공하는 함수 (별도의 import 없이 바로 사용 가능)
- 자주 사용되는 내장 함수 예시
```python
numbers = [1, 2, 3, 4, 5]

print(numbers)  # [1, 2, 3, 4, 5]
print(len(numbers))  # 5
print(max(numbers))  # 5
print(min(numbers))  # 1
print(sum(numbers))  # 15
print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]
```
### 유용한 내장 함수 
#### 1. map(funcion, iterable)
- 순회 가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환
- 반복문 대신 대체로 사용할 수 있음음
```python
# map
numbers = [1, 2, 3]
result = map(str, numbers)
print(result)  # <map object at 0x00000239C915D760>
print(list(result))  # ['1', '2', '3']
```
- mpa() 활용
    - SWEA 문제의 input 처럼 문자열 '1 2 3' 이 입력되엇을 때 활용하는 예시시
```
numbers1 = input().split()
print(numbers1)  # ['1', '2', '3']

numbers2 = list(map(int, input().split()))
print(numbers2)  # [1, 2, 3]
```

#### 2. zip(*iterables)
- 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
- 두 iterables 의 요소 개수가 다를 경우 개수가 동일한 순서까지만 zip을 진행하고 리턴
```python
# zip
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)
print(pair)  # <zip object at 0x000001C76DE58700>
print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]

girls = ['jane', 'ashley']
boys = ['peter']
pair = zip(girls, boys)
print(pair)  # <zip object at 0x000001C76DE58700>
print(list(pair))  # [('jane', 'peter')]
```
## 함수와 Scope

### Python의 Scope(범위)
- 함수는 코드 내부에 **local scope**를 생성하며, 그 함수 외부부 공간은 **global scope**로 구분된다.

### 범위와 변수 관계
- scope
    - global scope : 코드 어디에서든 참조할 수 있는 공간
    - local scope : 함수가 만든 scope (함수 내부에서만 참조 가능)

- variable
    - global variable : global scope에 정의된 변수
    - local variable : local scope에 정의된 변수

- scope 예시
    - num은 local scope에 존재하기 때문에 global scope에서 사용할 수 없음 - 변수의 생명주기와 연관 있음
```python
# Scope 예시
def func():
    num = 20
    print('local', num)  # local 20

func()

print('global', num)  # NameError: name 'num' is not defined
```

### 변수 생명주기 (lifcycle)
- 변수의 수명주기는 변수가 선언되는 위치와 scope에 따라 결정된다.

1. built-in scope
    - 파이썬이 실행된 이후부터 영원히 유지
2. global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope
    - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

### 이름 검색 규칙 (Name Resolution)
- 파이썬에서 사용되는 이름(식별자)들은 특정한 공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아가며, LEGB Rule 이라고 한다.
    1. Local scope : 지역 범위 (현재 작업중인 범위)
    2. Enclosed scope : 지역 범위 한 단계 위 범위
    3. Global scope : 최상단에 위치한 범위
    4. Built-in scope :모든 것을 담고 있는 범위 (정의하지 않고 사용할 수 있는 모든 것)
    ![alt text](/TIL/img/namespace.png)
    * 함수 내에서는 바깥 space의 변수에 접근 가능하나 수정은 할 수 없음

## global 키워드
- 변수의 스코프를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우 사용함
```python
num = 0  # 전역 변수


def increment():
    global num  # num를 전역 변수로 선언
    num += 1


print(num)  # 0

increment()

print(num)  # 1
```

### global 키워드 주의사항
1. global 키워드 선언 전 참조 불가
```python
num = 0

def increment():
    # SyntaxError: name 'num' is used prior to global declaration
    print(num)
    global num
    num += 1
```
2. 매개변수에는 global 키워드 사용 불가
```python
num = 0

def increment(num):
    # "num" is assigned before global declaration
    global num
    num += 1
```

# 함수 스타일 가이드
## 함수이름 작성 규칙
### 기본 규칙
- 소문자와 언더스코어(_) 사용
- 동사로 시작하여 함수의 동작 설명
- 약어 사용 지양
```python
# Good
def calculate_total_price(price, tax):
    return price + (price * tax)

# Bad
def calc_price(p, t):
    return p + (p * t)
```
### 함수 이름 구성 요소
- 동사 + 명사
    - save_user()
- 동사 + 형용사 + 명사
    - calculate_total_price()
- get/set 접두사
    - get_username(), set_username()


## 단일 책임 원칙
- 모든 객체는 하나의 명확한 목적과 책임만을 가짐
- 하나의 함수는 하나의 기능만 하도록 설계해야 함

## 함수 설계 원칙
1. 명확한 목적
    - 함수는 한 가지 작업만 수행
    - 함수 이름으로 목적을 명확히 표현

2. 책임 분리
    - 데이터 검증, 처리, 저장 등을 별도 함수로 분리
    - 각 함수는 독립적으로 동작하도록 설계

3. 유지보수성
    - 작은 단위의 함수로 나누어 관리
    - 코드 수정 시 영향 범위를 최소화

# Packing & Unpacking
## Packing
- 여러 개의 값을 하나의 변수에 묶어서 담는 것

### 패킹 예시
- 한 변수에 콤마(,)로 구분된 값을 넣으면 자동으로 튜플로 처리
```python
packed_values = 1, 2, 3, 4, 5
print(packed_values)  # (1, 2, 3, 4, 5)
```
- ' * '을 활용한 패킹 (변수 할당 시)
    -   '* 변수명'을 사용하면 "나머지 모든 값"을 리스트로 묶어서 받을 수 있음
```python
numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5
```
- ' * '을 활용한 패킹 (함수 매개변수 작성 시)
    -   '* 변수명'을 사용하면 호출 시 여러 개의 인자를 한 변수에 묶어서 받을 수 있음
    - 이때 함수 내부에서 해당 매개 변수는 튜플 형태로 취급
```python
def my_func(*args):
    print(args)  # (1, 2, 3, 4, 5)
    print(type(args))  # <class 'tuple'>


my_func(1, 2, 3, 4, 5)
```

## Unpacking
- 패킹된 변수를 풀어서 개별 변수나 함수 인자로 전달

### 언패킹 예시
- 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
```python 
packed_values = 1, 2, 3, 4, 5
a, b, c, d, e = packed_values
print(a, b, c, d, e)  # 1 2 3 4 5
```
- ' * '을 활용한 언패킹 (함수 인자 전달)
    - 시퀀스(리스트, 튜플 등)를 함숭 전달할 때,
    각 요소를 "풀어서" 개별 인자로 넘겨줄 수 있음

```python
def my_function(x, y, z):
    print(x, y, z)

names = ['alice', 'jane', 'peter']
my_function(*names)  # alice jane peter
```
- ' ** '을 활용한 언패킹 (딕셔너리 -> 함수 키워드 인자)
    - 딕셔너리의 키 - 값 쌍을 분리해 함수의 키워드 인자로 전달할 때 사용
```python
def my_function(x, y, z):
    print(x, y, z)


my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)  # 1 2 3
```

# Lambda expressions (람다 표현식)
- 한 줄로 간단한 함수를 정의

## 람다 표현식 구조
```python
lambda 매개변수 : 표현식
```
- lambda 키워드
    - 람다 함수를 선언하기 위해 사용되는 키워드
- 매개변수
    - 함수에 전달되는 매개변수들
    - 여러 개의 매개변수가 있을 경우 쉼표로 구분
- 표현식
    - 함수의 실행되는 코드 블록으로, 결과값을 반환하는 표현식으로 작성


## 람다 표현식 예시
- 간단한 연산이나 함수를 한 줄로 표현할 때 사용
- 함수를 매개변수로 전달하는 경우에도 유용하게 활용
1. ![alt text](/TIL/img/lambda.png)
<br>

2. ![alt text](/TIL/img/lambda2.png)

## 람다 표현식 활용 (with map 함수)
```python
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x**2

# lambda 미사용
squared1 = list(map(square, numbers))
print(squared1)  # [1, 4, 9, 16, 25]

# lambda 사용
squared2 = list(map(lambda x: x**2, numbers))
print(squared2)  # [1, 4, 9, 16, 25]
```























