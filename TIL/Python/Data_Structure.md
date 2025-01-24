# Data Structure
## 개요
### Data Structure (데이터 구조)
- 여러 데이터를 효과적으로 사용, 관리하기 위한 구조 (str, list, dict 등등)
- 컴퓨터 공학에서는 '자료 구조' 라고 하고 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓는 것이다.
<br>

![alt text](/TIL/img/Structure.png)
<br>

### 데이터 구조 활용
- 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 메서드를 호출하여 다양한 기능을 활용

## 메서드 (method)
- 객체에 속한 함수 (객체의 상태를 조작하거나 동작을 수행)

### 메서드 특징
- 클래스(class) 내부에 정의되는 함수
- 클래스는 파이썬에서 '타입을 표현하는 방법'이며 이미 은연중에 사용해 왔다.

#### 메서드는 어딘가(클래스)에 속해 있는 함수이며, 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재한다.

### 메서드 호출 방법 / 예시
#### 데이터 타입 객체.메서드()
```py
print('hello'.capitalize()) # Hello

numbers = [1, 2, 3]
numbers.appedn(4)

print(numbers) # [1, 2, 3, 4]
```

# 시퀀스 데이터 구조
## 문자열
### 문자열 조회/탐색 및 검증 메서드
<br>

![alt text](/TIL/img/string.png)
<br>

- .find(x)
    - x의 첫 번째 위치를 반환, 없으면 -1 을 반환
```py
text = 'banana'
print(text.find('n')) # 2
print(text.find('z')) # -1
```
- .index(x)
    - x의 첫 번째 위치를 반환, 없으면 오류 발생
```py
# index
text = 'banana'
print(text.index('n')) # 2
print(text.index('z')) # ValueError: substring not found
```

- .isupper() / .islower()
    - is로 시작하면 반환값이 대부분 Boolean
    - 문자열이 모두 대/소문자로 이루어져 있는지 확인
    - 인자가 필요한 메서드 아님

```py
string1 = 'HELLO'
string2 = 'Hello'

# isupper
print(string1.isupper())  # True
print(string2.isupper())  # False

# islower
print(string1.islower())  # False
print(string2.islower())  # False
```

- .isalpha()
    - 문자열이 알파벳으로만 이루어져 있는지 확인
```py
# isalpha
string1 = 'Hello'
string2 = '123heis98576ssh'
print(string1.isalpha())  # True
print(string2.isalpha())  # False
```

### 문자열 조작 메서드 (새 문자열 반환)
- .replace(old, new[,count]) 
- [대괄호] 안의 인자는 선택적 인자
    - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
```py
# replace
text = 'Hello, world! world world'
new_text1 = text.replace('world', 'Python')
new_text2 = text.replace('world', 'Python', 2)
print(new_text1)  # Hello, Python! Python Python
print(new_text2)  # Hello, Python! Python world
print(text) # Hello, world! world world
```

- .strip([chars])
    - 문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거
```py
# strip
text = '  Hello, world!  '
new_text = text.strip()
print(text) #   Hello, world!
print(new_text) # Hello, world!
```

- .split(sep=None, maxsplit=-1)
    - sep를 구분자 문자열로 사용하여 무자열에 있는 단어들의 리스트를 반환
    - sep가 None 일 경우 공백을 구분자로 함
```py
# split
text = 'Hello, world!'
words1 = text.split(',')
words2 = text.split()
print(words1)  # ['Hello', ' world!']
print(words2)  # ['Hello,', 'world!']
```

- 'separator'.join(iterable)
    - iterable 의 문자열을 연결한 문자열을 반환
    - 'separator'을 구분자로 하여 리스트를 하나로 합침
```py
# join
words = ['Hello', 'world!', 'welcome', 'to', 'the', 'show']
new_text1 = ' '.join(words)
new_text2 = '+'.join(words)
print(new_text1)  # Hello world! welcome to the show
print(new_text2)  # Hello+world!+welcome+to+the+show
```

## 리스트
### 리스트 값 추가 및 삭제 메서드
<br>

![alt text](/TIL/img/list.png)
<br>

- .append(x)
    - 리스트 마지막에 항목 x를 추가
```py
# append
my_list = [1, 2, 3]

my_list.append(4)

print(my_list)  # [1, 2, 3, 4]
print(my_list.append(4))  # None
```

- .extend(iterable)
    - 리스트에 반복 가능한 객체의 모든 항목을 추가
```py
# extend
my_list = [1, 2, 3]
my_list.extend([4, 5 ,6])
print(my_list)  # [1, 2, 3, 4, 5, 6]

# .append() 와의 비교
my_list.append([4, 5, 6])
print(my_list) # [1, 2, 3, 4, 5, 6, [4, 5, 6]]

# 반복 가능한 객체가 아니면 추가 불가능
my_list.extend(5)
print(my_list) # TypeError: 'int' object is not iterable
```

- .insert(i, x)
    - 리스트의 지정 인덱스 i 위치에 항목 x 를 삽입
```py
# insert
my_list = [1, 2, 3]
my_list.insert(2, 5)
print(my_list)  # [1, 2, 5, 3]
```

- .remove(x)
    - 리스트에서 첫 번째로 x와 일치하는 항목을 하나만 삭제
```py
# remove
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2, 2, 2]
```

- .pop(i)
    - 리스트에서 지정한 인덱스 i 의 항목을 제거하고 **반환** 해준다. i를 지정하지 않을 경우 마지막 항목을 제거 한다.

```py
# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(1)

print(item1)  # 5
print(item2)  # 2
print(my_list)  # [1, 3, 4]
```

- .clear()
    - 리스트의 모든 항목을 삭제 (빈 리스트로 만든다.) 리스트 초기화 할 때 활용용
```py
# clear
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []
```

### 리스트 탐색 및 정렬 메서드
<br>

![alt text](/TIL/img/list2.png)
<br>

- .index(x)
    - 리스트에서 첫 번째로 일치하는 항목 x의 인덱스를 반환
```py
# index
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)  # 1
```

- .count(x)
    - 리스트에서 항목 x와 일치하는 개수를 반환
```py
# count
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print(counting_number)  # 3
```

- .reverse()
    - 리스트의 순서를 역순으로 변경 (정렬 X)
```py
# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
# print(my_list.reverse())  # None
print(my_list)  # [9, 1, 8, 2, 3, 1]
```
- .sort()
    - 원본 리스트를 오름차순으로 정렬
    - 내림차순의 경우 (reverse=Treu) 작성
```py
# sort
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list)  # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list)  # [100, 3, 2, 1]
```

## 복사
## 객체와 참조
### 가변/불변 객체 개념
1. Mutable 객체 : 생성 후 내용을 변경할 수 있는 객체
    - list, dict, set ..
2. Immutable 객체 : 생성 후 내용을 변경할 수 없는 객체
    - int, float, str, tuple

### 변수 할당의 의미
- 파이썬에서 변수 할당은 객체에 대한 참조를 생성하는 과정
    - 변수는 객체의 메모리 주소를 가리키는 Label 역할
    - ' = ' 연산자를 사용해 변수에 값을 할당
    - 할당 시 새로운 객체가 생성되거나 기존 객체에 대한 참조가 생성 됨

### 메모리 참조 방식
- 변수는 객체의 '메모리 주소'를 저장
- 여러 변수가 동일한 객체를 참조할 수 있음
    - 가변 객체 예시
```py
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(a)  # [100, 2, 3, 4]
print(b)  # [100, 2, 3, 4]
print(a is b)  # True
```
    - 불변 객체 예시
```py
a = 20
b = a
b = 10

print(a)  # 20
print(b)  # 10
print(a is b)  # False
```

### 가변/불변 메모리 관리 방식과 이유
- 가변
    - 생성 후 수정할 수 있음
    - 변경 되더라도 같은 메모리 주소 유지
- 불변
    - 생성 후 수정할 수 없음
    - 새로운 값을 할당하면 새로운 객체가 생성되고 변수는 새 객체를 참조함

### 이유
1. 성능 최적화
    - 불변 객체는 변경이 불가하므로 여러 변수가 같은 객체를 안전하게 공유할 수 있음
    - 가변 객체는 내용 수정이 빈번한 경우 새 객체를 생성하지 않고 직접 수정하여 성능을 향상시킴
2. 메모리 효율성
    - 불변 객체는 동일한 값을 가진 여러 객체가 메모리르 공유하기 때문에 효율적
    - 가변 객체는 크기가 큰 데이터를 효율적으로 수정 가능함

## 얕은 복사
- 객체의 최상위 요소만 새로운 메모리에 복사
- 내부에 중첩 된 객체가 있다면 그 객체의 참조만 복사된다는 한계가 있음.
    - a , b 의 주소는 다르지만 내부 객체의 주소는 같기 때문에 함께 변경됨.
```py
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [999, 2, [3, 4, 5]]

b[2][1] = 100
print(a)  # [1, 2, [3, 100, 5]]
print(b)  # [999, 2, [3, 100, 5]]
print(a[2] is b[2])  # True
```

### 1차원 리스트와 다차원 리스트에서 차이점
1. 1차원 리스트
    - 얕은 복사로 충분히 독립적인 복사본을 만들 수 있음
2. 다차원 리스트
    - 최상위 리스트만 복사되고 내부 리스트는 여전히 원본과 같은 객체를 참조


## 깊은 복사 [Deepcopy](/TIL/Python/Deepcopy.md)
