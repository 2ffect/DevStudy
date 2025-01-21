# Deepcopy
- 기존의 리스트를 보존하기 위해 새로이 복사를 하는 경우가 있다.
- 이럴 때 잘못 복사를 해온다면 메모리 주소가 같아지기 때문에 기존의 대이터에 손상을 주는 경우가 발생하게 된다.
- 따라서 깊은복사가 필요하다.


### deepcopy 이용
- Deepcopy를 이용할 경우 복사 대상 리스트의 내부 객체들 까지 모두 copy 된다.
```python
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
a[0][1] = 3
print(a) # [[1,3], [3,4]]
print(b) # [[1,2], [3,4]]

위와 같이 a 를 수정해도 b가 변하지 않는다.
```
### slicing 이용
```python
a = [[1, 2], [3, 4]]
b = [arr[:] for arr in a]
a[0][1] = 3
print(a) # [[1,3], [3,4]]
print(b) # [[1,2], [3,4]]
```
- slicing을 이용 할 경우 import가 필요없다.
- 따라서 모듈을 사용하는 deepcopy보다 간결하다.