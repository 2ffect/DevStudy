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

## 1. Numeric Types
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

## 2. Sequence Types
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

### List (리스트)
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

### tuple (튜플)
- 여러 개의 값을 순서대로 저장하는 **변경 불가능한** 시퀀스 자료형

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
<br>

## 3. Non-Sequence Types
### dict (딕셔너리)
- key - value 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형

- 딕셔너리 표현
    - key는 변경 불가능한 자료형만 사용 가능 (str, int, float, tuple, range ...)
    - value는 모든 자료형 사용 가능
    - 중괄호 ({ })로 표기

- 딕셔너리 사용
    - key를 통한 value에 접근
    ```python
    my_dict = {'apple': 12, 'list': [1, 2, 3]}
    print(my_dict['apple']) # 12
    print(my_dict['list'][1]) # 2
    ```

    - 값 추가 & 변경
    ```python    
    # 추가
    my_dict['banana'] = 50
    print(my_dict)  # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}

    # 변경
    my_dict['apple'] = 100
    print(my_dict)  # {'apple': 100, 'list': [1, 2, 3], 'banana': 50}
    ```

### set (세트 (집합 자료형))
- 순서와 **중복이 없는** **변경 가능한** 자료형

- 세트 표현
    - 수학에서의 집합과 동일한 연산 처리 가능
    - 중괄호 ({ })
    - 빈 세트를 생성 시 소괄호 (( )) 사용
    ```python
    my_set = set()
    ```
- 세트의 집합 표현
```python
# 세트의 집합 연산
my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

# 합집합
print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}
# 차집합
print(my_set_1 - my_set_2)  # {1, 2}
# 교집합
print(my_set_1 & my_set_2)  # {3}
```
- **세트는 순서가 없기 때문에 인덱스로 접근이 불가**

## 4. Other Types
### None
- 파이썬에서 **'값이 없음'**을 표현하는 자료형
- None 표현
```python
variable = None
print(variable) # None
```

### Boolean (불리언)
- 참(True)과 거짓(False)을 표현하는 자료형
- 불리언 표현
    - 비교 / 논리 연산의 평과 결과로 사용됨
    - 주로 조건 / 반복문과 함께 사용
    ```python
    bool_1 = True
    bool_2 = False

    print(bool_1) # True
    print(bool_2) # False
    print(3 > 1) # True
    print('3' != 3) # True
    ```

### Collection
- 여러 개의 항목 또는 요소를 담는 자료구조
    - str, list, tuple, set, dict
- 컬렉션 정리
    ![alt text](/TIL/img/Collection.png)
    - 시퀀스인 경우 순서 O
    - 논시퀀스인 경우 순서 X
    <br>

<br>

## 형변환 (Type Conversion)
- 한 데이터 타입을 다른 데이터 타입으로 변환하는 과정
    - 암시적 형변환 / 명시적 형변환

### 암시적 형변환
- 파이썬이 자동으로 수행하는 형변환
- 암시적 형변환 예시
    - 정수와 실수의 연산에서 정수가 실수로 변환됨
    - Boolean 과 Numeric Type에서만 가능
    ```python
    print(3 + 5.0) # 8.0
    print(True + 3) # 4
    print(True + False) # 1

    True는 1 False는 0으로 취급하기 때문
    ```

### 명시적 형변환
- 프로그래머가 직접 지정하는 형변환
- 암시적 형변환이 아닌 경우를 모두 포함
- 명시적 형변환 예시
    - str -> int : 형식에 맞는 숫자만 가능
    ```python
    print(int('1')) # 1
    
    # ValueError: invalid literal for int() with base 10: '3.5'
    print(int('3.5'))
    print(int(3.5)) # 3
    print(float('3.5')) # 3.5
    ```
    <br>

    - int -> str : 모두 가능
    ```python
    print(str(1) + '등') # 1등
    ```

- 컬렉션 간 형변환 정리
![alt text](/TIL/img/TypeConversion.png)

## 연산자
### 산술 연산자
![alt text](/TIL/img/operator1.png)

### 복합 연산자
- 연산과 할당이 함께 이루어짐
![alt text](/TIL/img/operator2.png)
- 왼쪽 의미에 쓰여진 것으로 먼저 연습 후 예시로 사용

    - 복합 연산자 예시
    ```python
    # 복합 연산자
    y = 10
    y -= 4
    # y = y - 4
    print(y)  # 6

    z = 7
    z *= 2
    print(z)  # 14

    w = 15
    w /= 4
    print(w)  # 3.75

    q = 20
    q //= 3
    print(q)  # 6
    ```

### 비교 연산자
![alt text](/TIL/img/operator3.png)

- **== 비교 연산자**
    - 값(데이터)가 같은지를 비교
    - 동등성(equality)
    - 예를들어, 1 == True의 경우 파이썬 내부적으로 True를 1로 간주할 수 있으므로 True 결과가 나옴.
    - 예시
    ```python
    print(2.0 == 2)  # True
    print(2 != 2)  # False
    print('HI' == 'hi')  # False
    print(1 == True) # True
    ```

- **is 비교 연산자**
    - 객체 자체가 같은지를 비교
    - 식별성(identity)
    - 두 변수가 동일한 메모리 주소(레퍼런스)를 가리키고 있을 때만 True
    - 예시
    ```python
    # SyntaxWarning: "is" with a literal. Did you mean "=="?
    print(1 is True)  # False
    print(2 is 2.0)  # False
    ```

### 왜 is 대신 ==를 사용해야 하나?
- 숫자나 문자열 같은 값 자체를 비교하는 상황이 더 많은데 is를 사용시 의도치 않은 결과 (False)가 나오거나 내부 구현 차이로 기대하는 결과가 달라질 수 있기 때문에 == 를 사용하는 것을 권장.

### is 연산자는 언제 사용하는가? 
1. #### None을 비교 할 때
- 같은 주소에 있는가? 라는 질문에 답을 해야 할 때
- 파이썬 공식 스타일 가이드에서 None을 비교할 때 == 대신 is를 사용하라고 권장

2. #### 싱글턴 객체를 비교할 때
- 프로그램 전체에서 오직 1개만 존재하도록 만들어진 특별한 객체
- None, True, False 는 파이썬에서 딱 1개만 사용되며 미리 정해진 하나의 객체가 재사용되기 때문에 여러 곳에서 쓰더라도 같은 메모리 주소를 가리킨다.

### == 와 is 정리
- 값 비교에는 ==을 사용하고, 객체(레퍼런스) 비교에는 is를 사용하는 것이 원칙
- is는 주로 None비교나, 싱글턴 객체에 대한 정체성 체크에 사용

### 논리 연산자
![alt text](/TIL/img/operator4.png)
 - 비교 연산자와 함께 사용 가능


### 단축평가
- 논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작
- 코드 실행을 최적화하고 불필요한 연산을 피할 수 있도록 단축평가를 함
- 단축평가 동작
    - and
    - or

### 멤버십 연산자
- 특정 값이 시퀀스나 다른 컬렉션에 속하는지 여부를 확인
![alt text](/TIL/img/membership.png)

### 시퀀스형 연산자
- \+ 와 * 는 시퀀스 간 연산에서 산술 연산자일때와 다른 역할을 가짐
![alt text](/TIL/img/sequence.png)

### 연산자 우선순위 정리
![alt text](/TIL/img/operator5.png)
