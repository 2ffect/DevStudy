# 프로그래밍 패러다임
## 1. 절차 지향과 객체 지향
## 1-1. 절차 지향 프로그래밍
- 프로그램을 함수와 로직(절차) 중심으로 작성, 데이터를 함수에 전달하며 순차적으로 처리
<br>

```py
# 절차 지향 사고
# 예: 변수와 함수를 별개로 다룸
name = 'Alice'
age = 25


def introduce(name, age):
    print(f'안녕하세요, {name}입니다. 나이는 {age}살입니다.')


introduce(name, age)
```

### 절차 지향 프로그래밍 특징
- 입력을 받고, 처리하고, 결과를 내는 과정이 위에서 아래로 순차적으로 흐르는 형태
- 순차적인 명령어 실행
- 데이터와 함수의 분리
- 함수 호출의 흐름이 중요함
<br>

![alt text](/TIL/img/절차지향1.png)
<br>

### 절차 지향 프로그래밍 한계
1. 복잡성 증가
    - 프로그램 규모가 커질수록 데이터와 함수 관리가 어려움
    - 전역 변수의 증가로 인한 관리가 어려움

2. 유지보수 문제
    - 코드 수정 시 영향 범위 파악이 어려움
<br>

![alt text](/TIL/img/절차지향2.png)
<br>

## 1-2. 객체 지향 프로그래밍 (Object Oriented Programming)
- 데이터와 함수를 하나의 단위(객체)로 묶어서 관리, 객체들을 조합하고 재활용 하는 방식으로 프로그램 구성
<br>

```py
# 객체 지향 사고
# 예: 사람(객체) 안에 name, age와 이와 관련된 기능(메서드) 포함
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'안녕하세요, {self.name}입니다. 나이는 {self.age}살입니다.')


alice = Person('Alice', 25)
alice.introduce()  # 객체가 자신의 정보를 출력
```

### 객체 지향 프로그래밍 특징
- 프로그램을 데이터(변수)와 데이터를 처리하는 함수(메서드)를 하나의 단위(객체)로 묶어서 조직적으로 관리
- 데이터와 메서드의 결합

- 데이터와 해당 데이터를 처리하는 메서드가 하나의 객체로 통합되어 스스로 기능을 수행하는 능동적인 구조가 됨
    - 코드의 구조화와 재사용성을 높이는 동시에 실제 세계의 모델링 방식과 더욱 유사한 프로그램밍을 가능하게 함

**절차지향과 객체지향은 대조되는 개념이 아니다.**
- 객체지향은 기존 절차지향을 기반으로 객체라는 개념을 도입해 상속, 코드 재사용성, 유지보수성 등의 이점을 가지는 새로운 패러다임이다.
<br>


## 2. 객체 (Object)
- 실제 존재하는 사물을 추상화 한 것
- "속성(변수)"과 "동작(메서드)"을 가짐

### 객체 특징
- 속성(Attribute)
    - 객체의 상태/데이터
- 메서드(Method)
    - 객체의 행동/기능
- 고유성
    - 각 개체는 고유한 특성을 가짐



# 클래스 기초
## 1. 클래스 (Class)
- 데이터와 기능을 하나의 틀로 묶어 관리하는 방법, 사용자 정의 객체를 만드는 수단이자 속성과 메서드를 정리

### 클래스 정의
- class 키워드
- 클래스의 이름은 파스칼 케이스(Pascal Case) 방식으로 작성
```py
class MyClass:
    pass
```

### 클래스 예시
- **\_\_init__** 메서드는 "생성자 메서드"로 불리며, 새로운 객체를 만들 때 필요한 초기값을 설정

```py
class Person:
    def __init__(self, name, age): # __init__ : 초기화
        
        self.name = name  # 인스턴스 속성
        self.age = age  # 인스턴스 속성

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')
```

## 2. 인스턴스 (Instance)
- 클래스를 통해 생성된 객체

### 인스턴스 예시
- 클래스를 설계도라고 하면, 인스턴스는 그 설계도로 실제로 만들어진 '개별 물건'
- Person("Alice", 25)라면 Person이라는 설계도로 이름이 Alice이고 나이가 25인 '사람 객체'가 탄생 하는데 이 '사람 객체'가 **Person클래스로 나온 하나의 인스턴스**이다.

```py

```

## 3. 클래스와 인스턴스
![alt text](/TIL/img/class1.png)
<br>

- 변수 name의 타입은 str 클래스이다.
    - 변수 name은 str 클래스의 인스턴스이다.

```py
name = "Alice"

print(type(naem)) # <class 'str'>
```
- 문자열 타입의 변수는 str 클래스로 생성된 인스턴스다.
```py
print(help(str))

"""
class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
"""
```

**하나의 객체(object)는 특정 클래스의 인스턴스(instance)이다.**

## 4. 클래스 구성요소
- 생성자 메서드
    - 인스턴스 생성 시 자동 호출되는 특별한 메서드
    - \_\_init__이라는 이름의 메서드로 정의함
    - 인스턴스 변수의 초기화 담당
<br>

![alt text](/TIL/img/init.png)
<br>

- 인스턴스 변수(속성)
    - 각 인스턴스 별 고유한 속성
    - self.변수명 형태로 정의
    - 인스턴스마다 독립적인 값 유지지
<br>

![alt text](/TIL/img/instance.png)
<br>

- 클래스 변수 (속성)
    - 모든 인스턴스가 공유하는 속성
    - 클래스 내부에서 직접 정의
<br>

![alt text](/TIL/img/class2.png)
<br>

```py
class Circle:
    # 클래스 변수(속성)
    pi = 3.14

    # 생성자 메서드
    def __init__(self, radius):
        self.radius = radius

# 인스턴스 생성
# c1 = Circle() # TypeError: __init__() missing 1 required positional argument: 'radius'
c1 = Circle(1)
c2 = Circle(5)

# 인스턴스 변수(속성)
print(c1.radius) # 1
print(c2.radius) # 5

# 클래스 변수(속성)
print(c1.pi) # 3.14
print(c1.pi) # 3.14
```

## 클래스 변수와 인스턴스 변수
- 클래스 변수와 동일한 이름을 인스턴스 변수 생성 시 클래스 변수가 아닌 인스턴스 변수에 먼저 참조하게 됨.
- class.class_variable로 클래스 변수 참조 가능

```py
# c1의 인스턴스 변수 pi를 생성
c1.pi = 100

print(c1.pi)  # 100
print(Circle.pi)  # 3.14

# c2는 인스턴스 변수 pi가 없으므로 클래스 변수 pi를 참조
print(c2.pi)  #
```

# 메서드
## 1. 메서드란
### 메서드 (Method)
- 클래스 내부에 정의된 함수로 해당 객체가 어떻게 동작할지를 정의함

### 메서드 종류
1. 인스턴스 메서드
2. 클래스 메서드
3. 스태틱 메서드
<br>

![alt text](/TIL/img/method1.png)
<br>

## 2. 인스턴스 메서드
### 인스턴스 메서드 (Instance method)
- 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드
    - 인스턴스의 상태를 조작하거나 동작을 수행함

### 인스턴스 메서드 구조
- 클래스 내부에 정의되는 메서드의 기본
- 반드시 첫 번째 인자로 **인스턴스 자신(self)** 을 받음
- 인스턴스의 속성에 접근하거나 변경 가능

```py
class MyClass:
    def instance_method(self, arg1, ...):
        pass
# self는 매개변수 이름이라 다른 이름 설정이 가능하지만 사용하지 않을 것을 강력히 권장함.
```

### self 동작 원리
<br>

![alt text](/TIL/img/self.png)
<br>

- str 클래스가 upper 메서드를 호출했고, 그 첫번째 인자로 문자열 인스턴스가 들어간 것.
    - 인스턴스 메서드의 첫번째 인자가 반드시 인스턴스 자기 자신인 이유.

<br>

![alt text](/TIL/img/self2.png)
<br>

- 'hello'라는 문자열 객체가 단순히 어딘가의 함수로 들어가는 인자로 활용되는 것이 아닌 객체 스스로 메서드를 호출하여 코드를 동작하는 객체 지향적인 표현인 것

### 인스턴스 메서드 활용
```py
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

c = Counter()
print(c.count) # 0
c.increment()
print(c.count) # 1

c2 = Counter()
c.increment() 
print(c2.count) # 0 
print(c.count) # 2
```

### 생성자 메서드 (constructor method)
- 인스턴스 객체가 생성될 때 자동으로 호출 되는 메서드
    - 인스턴스 변수들의 초기값을 설정

### 생성자 메서드 활용
```py
class Person:
    def __init__(self, name):
        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 생성자 메서드의 매개변수 이름
        self.name = name
        print('인스턴스가 생성되었습니다.')

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')


person1 = Person('지민')  # 인스턴스가 생성되었습니다.
person1.greeting()  # 안녕하세요. 지민입니다.

# 실제동작방식은 아래와 같음음
Person.greeting(person1) # 안녕하세요. 지민입니다.
```

## 3. 클래스 메서드
### 클래스 메서드 (class method)
- 클래스가 호출하는 메서드
    - 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

### 클래스 메서드 구조
- @classmethod 데코레이터를 사용하여 정의함
- 호출 시 첫번째 인자로 해당 메서드를 호출하는 클래스(cls)가 전달됨
- 클래스를 인자로 받아 클래스 속성을 변경하거나 읽는데 사용
```py
class Myclass:

    @classmethod
    def class_method(cls, arg1, ...):
        pass

# cls는 매개변수 이름이라 다른 이름 설정이 가능하지만 사용하지 않을 것을 강력히 권장함.
```

### 클래스 메서드 활용
```py
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increase_population() # 클래스 메서드 호출이기 때문에 클래스가 호출

    @classmethod
    def increase_population(cls):
        cls.population += 1 

person1 = Person('Alice')
person2 = Person('Bob')
print(Person.population)  #2

```

## 4. 스태틱 메서드
### 스태틱 메서드 (static method)
- 클래스, 인스턴스 상관없이 독립적으로 동작하는 메서드

### 스태틱 메서드 구조
- @staticmethod 데코레이터를 사용하여 정의
- 호출 시 자동으로 전달받는 인자가 없음(self, cls 등 받지 않음)
- 인스턴스나 클래스 속성에 직접 접근하지 않는 '도우미 함수' 비슷한 역할을 함

```py
class MyClass:

    @staticmethod
    def static_method(arg1, ...):
        pass
```

### 스태틱 메서드 예시
```py
class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b


print(MathUtils.add(4,5))  # 9
```

## 5. 메서드 활용
### 입출금 가능한 은행 계좌 클래스 만들기
```py
# 입출금이 가능한 은행 계좌 클래스 만들기
# 은행 계좌를 모델링하는 클래스를 만들고, 입출금 기능(메서드)를 구현


class BankAccount:
    interest_rate = 0.02  # 이자율

    def __init__(self, owner, balance=0):
        self.owner = owner  # 계좌 소유자
        self.balance = balance  # 초기 잔액

    # 입금
    def deposit(self, amount):
        self.balance += amount

    # 출금
    def withdraw(self, amount):
        if self.balance >= amount:
           self.balance -= amount
        else:
            print("잔액 부족 !")

    # 이자율 설정
    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    # 금액이 양수인지 검증
    @staticmethod
    def is_positive(amount):
        return amount > 0


# 계좌 개설 (인스턴스 생성)
alice_acc = BankAccount('Alice', 1000)
print(alice_acc.owner) # Alice
print(alice_acc.balance) # 1000

# 입금 및 출금 (인스턴스 메서드 호출)
alice_acc.deposit(500) 
print(alice_acc.balance) # 1500
alice_acc.withdraw(1000)
print(alice_acc.balance) # 500
alice_acc.withdraw(1000) # 잔액부족

# 잔액 확인 (인스턴스 변수 참조)
print(alice_acc.balance) # 500

# 이자율 변경 (클래스 메서드 호출)
BankAccount.set_interest_rate(0.03)
print(BankAccount.interest_rate)  # 0.03

# 잔액이 양수인지 확인 (정적 메서드 호출)
print(BankAccount.is_positive(alice_acc.balance))  # True
```
## 6. 메서드 정리
### 메서드 정리
- 인스턴스 메서드
    - 인스턴스의 상태를 변경하거나 해당 인스턴스의 특정 동작을 수행

- 클래스 메서드
    - 인스턴스의 상태에 의존하지 않는 기능을 정의
    - 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

- 스태틱 메서드
    - 클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행

### 누가 어떤 메서드를 사용해야 하는가?
- 클래스가 사용해야 할 것
    - 클래스 메서드
    - 스태틱 메서드

- 인스턴스가 사용해야 할 것 
    - 인스턴스 메서드

#### 할 수 있다 != 써도 된다.
- 인스턴스가 모든 메서드를 호출할 수 있다. Python에서 기능적으로 막아두진 않았지만 각 각의 메서드는 OOP 패러다임에 따라 명확한 목적을 갖고 설계되었기 때문에 용도에 맞는 메서드만 사용할 것

```py
class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'


instance = MyClass()

# 클래스가 할 수 있는 것
print(MyClass.instance_method(instance)) # ('instance method', <__main__.MyClass object at 0x00000160FFFEEF10>)
print(MyClass.class_method()) # ('class method', <class '__main__.MyClass'>)
print(MyClass.static_method()) # static method

# 인스턴스가 할 수 있는 것
print(instance.instance_method()) # ('instance method', <__main__.MyClass object at 0x00000160FFFEEF10>)
print(instance.class_method()) # ('class method', <class '__main__.MyClass'>)
print(instance.static_method()) # static method
```

## 참고 1. 클래스와 인스턴스 간 이름 공간
- 클래스를 정의하면 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면 인스턴스 객체가 생성되고 또 다른 독립적인 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면 인스턴스 > 클래스 순서로 탐색하게 되고 인스턴스에 존재하지 않으나 클래스에 존재하는 속성이라면 해당하는 클래스 속성을 가져옴

## 참고 1-1. 독립적인 이름 공간이 가지는 이점
- 객체 지향 프로그래밍의 중요한 특성 중 하나로 클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장하여 코드의 가독성, 유지보수성, 재사용성을 높이는데 도움을 줌.

## 참고 2. 매직 메서드 (magic method)
- Double underscore('__') 가 있는 메서드로 특수한 동작을 위해 만들어진 인스턴스 메서드
- 특정 상황에 자동으로 호출
<br>

![alt text](/TIL/img/magic_method.png)
<br>

## 참고 3. 데코레이터 (Decorator)
- 다른 함수의 코드를 유지한 채 수정하거나 확장히기 위해 사용되는 함수
- 함수를 인자로 받아와 기능을 수정, 확장함
<br>

![alt text](/TIL/img/Decorator.png)