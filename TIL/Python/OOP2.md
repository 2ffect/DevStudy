# 상속
## 1. 개요
### 상속 (Inheritance)
- 한 클래스(부모)의 속성과 메서드를 다른 클래스(자식)가 물려 받는 것

### 상속이 필요한 이유
1. 코드 재사용
    - 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음
    - 기존 클래스를 수정하지 않고 기능을 확장 가능

2. 계층 구조
    - 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
    - 부모 클래스와 자식 클래스 간의 관계를 표현하고 더 구체적인 클래스를 만들 수 있음

3. 유지 보수의 용이성
    - 상속을 통해 기존 클래스의 수정일 필요한 경우 해당 클래스만 수정하면 되므로 유지 보수가 용이해짐
    - 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화 할 수 있음

### 상속 예시
```py
class Animal:
    def eat(self):
        print('먹는 중')


class Dog(Animal):
    def bark(self):
        print('멍멍')


my_dog = Dog()

my_dog.bark()  # 멍멍

# 부모 클래스(Animal) 메서드 사용 가능

my_dog.eat() # 먹는 중
```

## 2. 클래스 상속
### 상속 없이 구현 하는 경우
- 하나의 클래스로 생성 할 경우 학생/교수 정보를 별도 표기하기 어렵다.
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')


s1 = Person('김학생', 23)
s1.talk()  # 반갑습니다. 김학생입니다.

p1 = Person('박교수', 59)
p1.talk()  # 반갑습니다. 박교수입니다.

```
- 교수/학생 클래스로 분리 하더라도 메서드가 중복으로 정의 될 수 있다.
```py
class Professor:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def talk(self):  # 중복
        print(f'반갑습니다. {self.name}입니다.')


class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def talk(self):  # 중복
        print(f'반갑습니다. {self.name}입니다.')

```

### 상속을 사용한 계층구조 변경
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):  # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')


class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department


class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa


# 인스턴스 생성
p1 = Professor('김교수', 50, '경제학과')
s1 = Student('김싸피', 20, 3.5)
# 부모 Person 클래스의 talk 메서드를 활용

p1.talk() # 반갑습니다. 김교수입니다.
s1.talk() # 반갑습니다. 김싸피입니다.
```


## 3. 메서드 오버라이딩 (Method Overriding)
- 부모 클래스의 메서드를 같은 이름, 같은 파라미터 구조로 재정의 하는 것
- 자식 클래스가 부모 클래스의 메서드를 덮어써 새로운 동작을 구현할 수 있음

### 메서드 오버라이딩 예시
```py
class Animal:
    def eat(self):
        print('Animal이 먹는 중')


class Dog(Animal):
    # 오버라이딩 (부모 클래스 Animal의 eat 메서드를 재정의)
    def eat(self):
        print('Dog가 먹는 중')


my_dog = Dog()

my_dog.eat()  # Dog가 먹는 중
```

### [참고] 메서드 오버로딩
- 같은 이름의 메서드이지만 파라미터의 수로 메서드를 다르게 설정하는 것
- 파이썬에서는 지원하지 않음. 가장 마지막에 선언한 메서드만 호출가능.

## 4. 다중 상속
- 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

### 다중 상속 예시
```py
# 다중 상속 예시
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'

class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'

class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'


baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # FirstChild 의 상속 순서가 Dad, Mom 이기 때문에 XY
```

## [참고] 다이아몬드 문제 (The diamond Problem)
- 두 클래스 B와 C가 A에 상속되고 클래스 D가 B와 C 모두에서 상속될 때 B와 C가 재정의한 메서드가 A에 있고 D가 이를 재정의 하지 않은 경우라면
D는 B의 메서드 중 어떤 버전을 상속하는가 ? 아니면 C의 메서드 버전을 상속하는가 ?
<br>

![alt text](/TIL/img/diamond.png)
<br>

## 해결책
- MRO(Method Resolution Order) 알고리즘을 사용하여 클래스 목록을 생성
- 부모 클래스로부터 상속된 속성들의 검색을 깊이 우선으로, 왼쪽에서 오른쪽으로, 계층 구조에서 겹치는 같은 클래스를 두 번 검색하지 않음.
- D 에서 없으면 B 에서 없으면 C 순서로 탐색함

### MRO (Method Resolution Order)
- 파이썬이 메서드를 찾는 순서에 대한 규칙 / 메서드 결정 순서

## 5. super() 메서드
- 부모 클래스 (또는 상위 클래스)의 메서드를 호출하기 위해 사용하는 내장 함수

### super()기능
- 다중 상속 상황에서 특히 유용하며, MRO를 따르기 때문에 여러 부모 클래스를 가진 자식 클래스에서 당므에 호출 할 부모 메서드를 순서대로 호출 할 수 있게 함

### 사용 사례
1. 단일 상속 구조
    - 명시적으로 이름을 지정하지 않고 부모 클래스를 참조할 수 있으므로 코드를 더 유지관리 하기 쉽게 만들 수 있음
    - 클래스 이름이 변경 되거나 부모 클래스가 교체 되어도 super()를 사용하면 코드 수정이 더 적게 필요함

2. 다중 상속 구조
    - MRO를 따른 메서드 호출
    - 복잡한 다중 상속 구조에서 발생할 수 있는 문제를 방지

## 다중 상속 super() 예시
```py 
# 다중 상속
class ParentA:
    def __init__(self):
        super().__init__()
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()  # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child'

    def show_value(self):
        super().show_value()  # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')


child = Child()
child.show_value()
"""
Value from ParentA: ParentA
Value from Child: Child
"""

print(child.value_c)  # Child
print(child.value_a)  # ParentA
print(child.value_b)  # ParentB
```
<Child 클래스의 MRO>
Child -> ParentA -> ParentB

super()는 단순히 “직계 부모 클래스를 가리킨다”가 아니라, 
MRO 순서를 기반으로 “현재 클래스의 다음 순서” 클래스(또는 메서드)를 가리킴

따라서 ParentA에서 super()를 부르면 MRO상 다음 클래스인 ParentB.__init__()가 호출됨

- 1.1 Child 클래스의 인스턴스를 생성할 때 일어나는 일
    1.	child = Child() 호출 시, Child.__init__()가 실행
    2.	Child.__init__() 내부에서 super().__init__()를 호출
        - 여기서 Child의 super()는 MRO에 의해 ParentA의 __init__()를 가리킴
    3.	ParentA.__init__()로 진입

- 1.2. ParentA.__init__() 내부
	1.	ParentA.__init__()에는 다시 super().__init__()가 있음
	2.	ParentA를 기준으로 MRO에서 “다음 클래스”는 ParentB, 따라서 ParentA의 super().__init__()는 ParentB.__init__() 호출
    3.	ParentB.__init__()가 실행되면서 self.value_b = 'ParentB'가 설정됨
	4.	ParentB.__init__()가 종료된 후, 다시 ParentA.__init__()로 돌아와 self.value_a = 'ParentA'가 설정됨
	5.	ParentA.__init__() 종료 후, 다시 Child.__init__()로 돌아감
	6.	마지막으로 Child.__init__() 내에서 self.value_c = 'Child'가 설정되고 종료

- 1.3 결과적으로 child 인스턴스는 value_a, value_b, value_c 세 속성을 모두 갖게 됨
	- child.value_a → 'ParentA'
	- child.value_b → 'ParentB' 
	- child.value_c → 'Child'

### super()의 이점
- 다중 상속 상황에서 super()는 다음에 호출해야 할 부모 메서드를 MRO 순서에 따라 결정하기 때문에, 명시적으로 특정 부모 클래스를 가리키지 않고도 올바른 순서로 부모 초기화나 메서드 호출이 가능하게 함. 이를 통해 복잡한 상속 구조에서도 코드를 유연하고 깔끔하게 유지할 수 있음

### super() 정리
- super() 를 사용할 때 MRO를 잘 이해하고 있어야 함
- ClassName.mro()를 통해 MRo 순서 파악이 가능함.

## MRO가 필요한 이유
1. 부모 클래스들이 여러 번 액세스 되지 않도록 각 클래스에서 지정된 왼쪽에서 오른쪽으로 가는 순서를 보존하고 각 부모를 오직 한 번만 호출하고 부모들의 우선 순위에 영향을 주지 않으면서 서브 클래스를 만드는 단조적인 구조 형성이 가능함
2. 프로그래밍 언어의 신뢰성 있고 확장성 있는 클래스를 설계할 수 있도록 도움을 줌
3.  클래스 간 메서드 호출 순서가 예측 가능하게 유지되며, 코드의 재사용성과 유지보수성이 향상됨.
