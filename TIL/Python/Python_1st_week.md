## Python을 배우는 이유
    1. 상대적으로 쉽고 간결한 문법
    2. 광범위한 응용 분야 (웹, 데이터분석, 인공지능, 자동화 스크립트 등 다양한 분야에서 사용)
    3. 세계적 규모의 풍부한 온라인 포럼 및 커뮤니티 생태계
    

## 알고리즘 구현에 유리한 Python
    1. 직관적인 문법
        - 복잡한 논리 구조의 알고리즘을 이해하고 구현하기에 쉬움
    2. 강력한 표준 라이브러리
        - 다양한 알고리즘 구현에 필요한 도구를 제공
    3. 빠른 프로토타이핑
        - 알고리즘을 빠르게 테스트하고 수정할 수 있음

## 파이썬이 프로그램이 실행되는 과정

- 인터프리터가 사용자의 명령어를 운영체제가 이해하는 언어로 바꿈 
    - 인터프리터로 운영체제간 이식도 가능 (확장성)
    ![alt text](/TIL/img/python.png)

<br>
- 인터프리터를 사용하는 2가지 방법
    1. shell 에서 한 번에 한 명령어씩 입력해서 실행
    2. 확장자가 **.py**인 파일에 작성된 파이썬 프로그램을 실행

## 표현식과 값
### 표현식
- 값으로 평가될 수 있는 코드조각

### 값
- 표현식이 평가된 결과
        
![alt text](/TIL/img/python2.png)
<br>
**표현식이 평가되어 값이 반환된다.**

### 평가
- 표현식을 실행하여 값을 얻는 과정
- 표현식을 순차적으로 평가하여 프로글매의 동작을 결정함함

## 문장
- 실행 가능한 동작을 기술하는 코드 (조건문, 반복문, 함수정의 등)
- 문장은 보통 여러 개의 표현식을 포함한다.
![alt text](/TIL/img/python3.png)
<br>
## 타입
- 변수나 값이 가질 수 있는 데이터의 종류
    - 어떤 종류의 데이터인지, 어떻게 해석되고 처리되어야 하는지를 정의함.
    ![alt text](/TIL/img/python4.png)
<br>
### 데이터 타입
1. Numeric Type
    - int(정수) , float(실수), complex(복소수)

2. Sequence Types
    - list, tuple, range

3. Text Sequence Type
    - str (문자열)

4. Non-sequence Types
    - set, dict

5. 기타
    - Boolean, None, Functions

### 타입의 중요성
- 데이터 타입에 맞는 연산을 수행할 수 있기 때문에 타입이 존재함

### 산술 연산자
![alt text](/TIL/img/python5.png)

### 연산자 우선순위
![alt text](/TIL/img/python6.png)
```python
print(-2 ** 4) # -16
print(-(2 ** 4)) # -16
print((-2) ** 4) # 16
```
첫 번째가 많이 헷갈리지만 우선순위에 따라 ** 진행 뒤 - 가 붙기 때문에 출력은 -16이 된다.


## 변수
- 값을 저장하기 위한 이름
### 변수 할당
- 표현식을 통해 변수에 값을 저장

```python 
degrees = 36.5

할당문 
"변수 degrees에 값 36.5를 할당했다."

#재할당
degrees = 'abc'
할당문
"변수 degrees에 값 'abc'를 재할당했다.
```

### 할당문 
```python
variable = expression
```
1. 할당 연산자(=) 오른쪽에 있는 표현식을 평가해서 값(메모리 주소)을 생성
2. 값의 메모리 주소를 '=' 왼쪽에 있는 변수에 저장
    - 존재하지 않는 변수 (할당당)
        - 새 변수를 생성
    - 존재했던 변수 (재할당)
        - 기존 변수를 재사용하여 변수에 들어있는 메모리 주소를 변경


## Date Types
- 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성 (연산자가 같더라도 데이터 타입 별로 동작의 결과가 달라진다.)
![alt text](/TIL/img/DateTypes.png)

### 데이터 타입이 필요한 이유
- 값들을 구분하고 어떻게 다뤄야할지 알 수 있음
- 타입을 명시적으로 지정해야 코드를 읽는 사람이 변수의 의도를 더 쉽게 이해할 수 있고, 잘못된 데이터 타입으로 인한 오류를 미리 예방

### 1. Numeric Types
    1. int (정수 자료형)
        - 정수를 표현하는 자료형
        진수 표현
        - 2진수 (binary) : 0b
        - 8진수 (octal) : 0o
        - 16진수 (hexadecimal) : 0x

    2. float (실수 자료형)
        - 실수를 표현하는 자료형
        - 프로그래밍 언어에서 float는 실수에 대한 근삿값 (제한된 양의 메모리에서 저장할 수 있는 가장 가까운 값을 저장함함)
        - 실수 연산 시 주의사항
            - 부동소수점에러 발생 가능.
        - 해결책
            - decimal 모듈을 사용해 연산의 정확성을 보장

### 부동소수점 에러
```python
# 해결 전
a = 3.2 - 3.1
b = 1.2 - 1.1

print(a) # 0.100000000000009
print(b) # 0.999999999999987
print(a == b) # False 

# 해결 후
from decimal import Decimal
a = Decimal('3.2') - Decimal('3.1')
b = Decimal('1.2') - Decimal('1.1')

print(a) # 0.1
print(b) # 0.1
print(a == b) # True
```

### 2. Sequence Types
- 여러 개의 값들을 **순서대로 나열**하여 저장하는 자료형
    - (str, list, tuple, range)

### Sequnece Types 특징
    1. 순서 (Sequemce)
        - 값들이 순서대로 저장 (정렬 X)
    2. 인덱싱 (Indexing)
        - 각 값에 고유한 인덱스(번호)를 가지고 있으며, 인덱스를 사용해 특정 위치의 값을 선택하거나 수정할 수 있음
    3. 슬라이싱 (Slicing)
        - 인덱스 범위를 조절해 부분적인 값을 추출할 수 있음
    4. 길이 (Length)
        - len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음
    5. 반복 (Iteration)
        - 반복문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음

### Escape sequence
- 역슬래쉬 (backslash, \\) 뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합
- 파이썬의 일반적인 문법 규칙을 잠시 탈출한다는 의미 
![alt text](/TIL/img/Escapesequence.png)
<br>

```python
# Escape sequence
# 철수야 '안녕'
print('철수야 \'안녕\'')


print('이 다음은 엔터\n입니다.')
이건 어떻게 출력될 지 생각해보세용.
```

### f-string
- 문자열에 f 또는 F접두어를 붙이고 표현식을 {expression}로 작성하는 문법
- 문자열에 파이썬 표현식의 값을 삽입할 수 있음

```python
# String Interpolation "f-string"
bugs = 'roaches'
counts = 13
area = 'living room'

# roaches 13 living room
print(f'{bugs} {counts} {area}')
```

### 인덱스
- 시쿼스 내의 값들에 대한 고유한 번호로, 각 값의 위치를 식별하는 데 사용되는 숫자
- 문자열 hello의 인덱스
![alt text](/TIL/img/index.png)
<br>

### 슬라이싱
- 시퀀스의 일부분을 선택하여 추출하는 작업
    - 시작 인덱스와 끝 인덱스를 지정하여 해당 범위의 값을 포함하는 새로운 시퀀스를 생성성

### 슬라이싱 예시
![alt text](/TIL/img/slicing.png)
<br>
![alt text](/TIL/img/slicing2.png)
<br>
![alt text](/TIL/img/slicing3.png)
<br>

- 문자열은 변경이 불가능하다.
```python
my_str = 'hello'
# TypeError: 'str' object does not support item assignment
my_str[1] = 'z'
```

### List
- 여러 개의 값을 순서대로 저장하는 **변경 가능한** 시퀀스 자료형

- 리스트 표현
    - 0개 이상의 객체를 포함하며 데이터 목록을 저장
    - 대괄호 ([ ]) 로 표기
    - 데이터는 어떤 자료형도 저장할 수 있음
    ```python
    # 리스트 표현
    my_list_1 = []
    my_list_2 = [1, 'a', 3, 'b', 5]
    my_list_3 = [1, 2, 3, 'python', ['hello', 'world', '!!!']]
    my_list = [1, 'a', 3, 'b', 5]    
    ```
    <br>
- 리스트 시퀀스 특징
    - 인덱싱 가능
    - 슬라이싱 가능
    - 길이측정 가능

    ```python
    # 중첩된 리스트 접근
    my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
    print(len(my_list))  # 5
    print(my_list[-1][-1])  # !!!
    print(my_list[-1][-2][0])  # w

    # 리스트는 가변
    my_list = [1, 2, 3]
    my_list[0] = 100

    print(my_list) # 100, 2, 3

    # ★★★
    my_list_test = [1, 'world', 3]
    my_list_test[1] = 100
    print(my_list_test) # 1, 100, 3

    # ★★★ 위 경우는 문자열을 바꾼것이 아닌, 리스트의 요소를 변경한 것 즉,리스트의 요소가 바라보는 주소가 변경되는 것. 
    ```

### tuple
- 여러 개의 값을 순서대로 저장하는 **변경 불가능한** 시퀀스 자료형형

- 튜플 표현
    - 0개 이상의 객체를 포함하여 데이터 목록을 저장
    - 소괄호 (( ))표기
    - 데이터는 어떤 자료형도 저장할 수 있음
    ```python
    # 튜플 표현
    my_tuple_1 = ()
    my_tuple_2 = (1,)
    # 단일 요소 튜플을 만들 때는 반드시 Trailing comma (후행 쉼표)를 사용해야 함 
    # (1) 의 경우 int 1로 해석 됨

    my_tuple_3 = (1, 'a', 3, 'b', 5)
    ```

- 튜플은 어디에 쓰일까?
    - 튜플의 불변 특성을 사용해 **내부 동작**과 안전한 데이터 전달에 사용된다.
    - ex) 다중 할당, 값 교환, 그룹화, 함수 다중 반환값 등
    ![alt text](/TIL/img/tuple.png)

### range
- **연속된 정수 시퀀스를 생성**하는 **변경 불가능한** 자료형 

- range 기본 구문
    - 모든 매개변수는 **정수**만 사용 가능
    ```python
    range(시작 값, 끝 값, 증가 값)
    ```

- range 매개변수 별 특징
    - range(n)
        - 0부터 n-1 까지 1씩 증가
    - range(n, m)
        - n부터 m-1 까지 1씩 증가
    - range(n, m, step)
        - n부터 m-1 까지 step씩 증가

```python
# range
my_range_1 = range(5)
my_range_2 = range(1, 10)
my_range_3 = range(5, 0, -1)

print(my_range_1)  # range(0, 5)
print(my_range_2)  # range(1, 10)
print(my_range_3)  # range(5, 0, -1)

# 리스트로 형 변환 시 데이터 확인 가능
print(list(my_range_1))  # [0, 1, 2, 3, 4]
print(list(my_range_2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(my_range_3))  # [5, 4, 3, 2, 1]
```

- 증가 값 규칙
    - 기본 증가 값은 1
    - 음수 증가 값
        - 감소하는 수열 생성
    - 양수 증가 값
        - 증가하는 수열 생성
    - 증가 값이 0이면 error

    - 음수 증가 시
        - 시작 값이 끝 값보다 커야 함
    ```python
    # 시작 값이 끝 값보다 큰 경우 (정상)
    print(list(range(5, 1, -1)))  # [5, 4, 3, 2]
    # 시작 값이 끝 값보다 작은 경우
    print(list(range(1, 5, -1)))  # []
    ```
    
    - 양수 증가 시
        - 시작 값이 끝 값보다 작아야 함
    ```python
    # 시작 값이 끝 값보다 작은 경우 (정상)
    print(list(range(1, 5)))  # [1, 2, 3, 4]
    # 시작 값이 끝 값보다 큰 경우
    print(list(range(5, 1)))  # []
    ```

- range는 주로 반복문과 함께 활용 됨
```python
for i in range(1, 10):
    print(i)  # 1 2 3 4 5 6 7 8 9

for i in range(1, 10, 2):
    print(i)  # 1 3 5 7 9
```