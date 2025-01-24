# Deepcopy
- 객체의 모든 수준의 요소를 새로운 메모리에 복사 (중첩된 객체까지 모두 새로운 객체로 생성됨)

- 기존의 리스트를 보존하기 위해 새로이 복사를 하는 경우가 있다.
- 이럴 때 잘못 복사를 해온다면 메모리 주소가 같아지기 때문에 기존의 대이터에 손상을 주는 경우가 발생하게 된다.
- 따라서 깊은복사가 필요하다.

### deepcopy 이용
- Deepcopy를 이용할 경우 복사 대상 리스트의 내부 객체들 까지 모두 copy 된다.
```python
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0][1] = 3
print(a) # [[1, 2], [3, 4]
print(b) # [[1, 3], [3, 4]]
print(a is b) # False

위와 같이 a 를 수정해도 b가 변하지 않는다.
```
### 복잡한 deepcopy
```py
original = {
    'a': [1, 2, 3],
    'b': {
        'c': 4,
        'd': [5, 6],
    },
}
copied = copy.deepcopy(original)

copied['a'][1] = 100
copied['b']['d'][0] = 500

print(f'원본: {original}')  # {'a': [1, 2, 3], 'b': {'c': 4, 'd': [5, 6]}}
print(f'복사본: {copied}')  # {'a': [1, 100, 3], 'b': {'c': 4, 'd': [500, 6]}}
print(
    f'original["b"]와 copied["b"]가 같은 객체인가? {original["b"] is copied["b"]}'
)  # False

```

### slicing 이용
```python
a = [[1, 2], [3, 4]]
b = [arr[:] for arr in a]
b[0][1] = 3
print(a) # [[1, 2], [3, 4]
print(b) # [[1, 3], [3, 4]]
print(a is b) # False

```
- slicing을 이용 할 경우 import가 필요없다.
- 복잡해지는 경우 slicing 보다 improt 가 빠르겠다.

