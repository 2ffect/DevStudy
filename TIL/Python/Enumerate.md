## enumerate(iterable, start=0)
- iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장 함수
- 인덱스의 시작 번호호 설정 가능

## enumerate 예시
```py
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

"""
0 apple
1 banana
2 cherry
"""

for index, fruit in enumerate(fruits, 3):
    print(index, fruit)

"""
3 apple
4 banana
5 cherry
"""
```