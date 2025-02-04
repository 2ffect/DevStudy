# 에러와 예외
## 1. 디버깅
### 버그 (bug)
- 소프트웨어에서 발생하는 오류 또는 결함
- 프로그램의 예상된 동작과 실제 동작 사이의 불일치

### 디버깅 (Debugging)
- 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정
- 프로그램의 오작동 원인을 식별하여 수정하는 작업

### 디버깅 방법
1. print 함수 활용
    - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각

2. 개발 환경 (text editor, IDE) 등에서 제공하는 기능 활용
    - breakpoint, 변수 조회 등

3. Python tutor 활용 (단순 파이썬 코드의 경우)

4. 뇌 컴파일, 눈 디버깅 ( ;;;)

## 2. 에러
### 에러 (Error)
- 프로그램 실행 중 발생하는 예외 상황

1. 문법 에러 (Syntax Error)
    - 프로그램의 구문이 올바르지 않은 경우 발생 (프로그램 실행 X)
    - 오타, 괄호 및 콜론 누락 등 문법적 오류

2. 예외 (Exception)
    - 프로그램 실행 중 감지되는 에러 (프로그램 실행 O)

## 3. 예외
### 내장 예외 (Built-in Exceptions)
- 예외 상황을 나타내는 예외 클래스들
    - 파이썬에 이미 저장되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용 가능함
[내장 예외 종류](https://docs.python.org/ko/3/library/exceptions.html#)

# 예외처리 (Exception Handling)
- 예외가 발생했을 때 프로그램이 비정상적으로 종료되지 않고 적절하게 처리할 수 있도록 하는 방법

### 예외처리 사용 문구
1. try 
    - 예외가 발생할 수 있는 코드 작성
2. except
    - 예외가 발생했을 때 실행할 코드 작성
3. else
    - 예외가 발생하지 않았을 때 실행할 코드 작성
4. finally
    - 예외 발생 여부와 상관없이 항상 실행할 코드 작성 

## 1. try & except
### try - except 구조
- try 블록 안에 예외가 발생할 수 있는 코드 작성
- except 블록 안에 예외가 발생했을 때 처리할 코드 작성
- 예외가 발생하면 프로그램 흐름은 try 블록을 빠져나와 해당 예외에 대응하는 except 블록으로 이동

### 예외처리 예시
```py
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.') 

# 0으로 나눌 수 없습니다.

try:
    num = int(input('숫자입력 : '))
except ValueError:
    print('숫자가 아닙니다.')

# 숫자입력 : a
# 숫자가 아닙니다.
```

## 2. 복수 예외 처리
```py
try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
except(ValueError, ZeroDivisionError):
    print('에러가 발생했습니다.')

# 위 아래 두가지 방법으로 처리 가능

try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
except ValueError:
    print('숫자가 아닙니다.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생했습니다.')

```


## else & finally
- else 블록은 예외가 발생하지 않았을 때 추가 작업을 진행
- finally 블록은 예외 발생 여부와 관계없이 항상 실행할 코드를 작성

### 코드 예시
```py
try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
else:
    print(f'결과: {y}')
finally:
    print('프로그램이 종료되었습니다.')

``` 

## 참고 1. 예외 처리 주의 사항
- 내장 예외 클래스는 상속 계층구조를 가지기 때문에 except 절로 분기 시 반드시 하위 클래스를 먼저 확인 할 수 있도록 작성해야 함.

- [예외 계층 구조](https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy)

## 참고 2. 예외 객체 다루기
### as 키워드
- 예외 객체
    - 예외가 발생했을 때 예외에 대한 정보를 담고 있는 객체
- except 블록에서 예외 객체를 받아 상세한 예외 정보 활용 가능
```py
my_list = []

try:
    number = my_list[1]
except IndexError as error:
    print(f'{error}가 발생했습니다.')

# list index out of range가 발생했습니다.
```

### try-except 와 if-else
- try-except 와 if-else를 함께 사용할 수 있음
```py
try:
    x = int(input('숫자를 입력하세요 : '))
    if x < 0:
        print('음수는 허용되지 않습니다.')
    else:
        print('입력한 숫자 :', x)
except ValueError:
    print('오류발생생')
```

## 참고 3. EAFP & LBYL
### 예외 처리와 값 검사에 대한 2가지 접근 방식
1. EAFP "Easier to Ask for Forgiveness than Permission"
    - 예외처리를 중심으로 코드를 작성하는 접근 방식 (try - except)

2. LBYL "Look Before You Leap"
    - 값 검사를 중심으로 코드를 작성하는 접근 방식 (if - else)

### 접근방식 비교
```py
my_dict = {'key': 'value'}

# EAFP (Easier to Ask for Forgiveness than Permission, 허락보다 용서 구하기)
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')


# LBYL (Look Before You Leap, 돌다리도 두들겨보고 건너기)
if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('Key가 존재하지 않습니다.')
```
<br>

![alt text](/TIL/img/접근방식.png)
<br>
