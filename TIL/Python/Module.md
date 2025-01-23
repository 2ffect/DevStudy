# Module (모듈)
## 개요
- 프로그램 전체를 모두 혼자 힘으로 작성하는 것은 드문 일, 다른 프로그래머가 이미 작성해 놓은 수천, 수백만 줄의 코드를 활용하는 것은 생산성에 있어 매우 중요한 일
## Module (모듈)
- 한 파일로 묶인 변수와 함수의 모음
- 특정한 기능을 하는 코드가 작성된 파이썬 파일 (.py)

### 모듈 예시
- math 내장 모듈
    - 파이썬이 미리 작성해 둔 수학 관련 변수와 함수가 작성 된 모듈
    ```python
    import math
    print(math.pi) # 3.141592653589793
    print(math.sqrt(2025)) # 45.0

    import random
    print(random.randint(1, 10)) # 1 ~ 10 사이 랜덤 int

    import datetime
    now = datetime.datetime.now()
    print(now) # 출력을 실행시킨 현재 시간
    ```

## 모듈 활용
### 모듈 가져져오기
- import 문 사용
```python
import math # 'math.py' 전체를 가져오겠다.
print(math.sqrt(2025))
```
- from 절 사용
```python
from math import sqrt # 'math.py'에서 'sqrt'를 가져오겠다. 
print(sqrt(2025))
```

### 모듈 사용하기
- ' . (dot) ' 연산자
    - "점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라" 의 의미
    ```python
    # 모듈명.변수명
    print(math.pi)
    
    # 모듈명.함수명
    print(math.sqrt(2025))
    ```
### 모듈 주의사항
- 서로 다른 모듈이 같은 이름의 함수를 제공 할 경우, 마지막에 import 된 이름으로 대체 됨
- 모듈 내 모든 요소를 한번에 import 하는 * 표기는 권장하지 않음

    ### 'as' 키워드
    - as 키워드를 사용해 별칭을 부여
        - 두 개 이상으 ㅣ모듈에서 동일한 이름의 변수, 함수 클래스 등을 가져올 때 발생하는 이름 충돌 해결 (아래 코드 정상 작동)
        ```python
        from math import sqrt
        from my_math import sqrt as my_sqrt

        sqrt(2025) # 45.0 
        my_sqrt(2025) # 45.0
        ```

## 파이썬 표준 라이브러리 (Python Standard Library)
- 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지 모음

## Package (패키지)
- 연관된 모듈들을 하나의 디렉토리에 모아놓은 것

### 패키지 사용하기
- 아래와 같은 디렉토리 구조로 작성
- 패키지 3개
- 모듈 2개
<br>
![alt text](/TIL/img/package.png)
<br>

```python
from my_package.math import my_math
from my_package.statistics import tools

print(my_math.add(1,2)) # 3
print(tools.mod(1,2)) # 1
```

### PSL 내부 패키지
- 설치 없이 바로 import 하여 사용
### 외부 패키지
- **pip**를 사용하여 설치 후 import 필요

## pip (파이썬 패키지 관리자)
- 외부 패키지들 설치를 도와주는 파이썬의 패키지 관리 시스템
- [PyPI](https://pypi.org/)(Python Package Index)에 저장된 외부 패키지 설치

### 패키지 설치
- 최신 / 특정 / 최소 버전을 명시하여 설치가능
```python
$ pip install SomePackage # 최신
$ pip install SomePackage==1.0.5# 특정
$ pip install SomePackage>=1.0.4 # 최소

# 삭제의 경우 install > uninstall 로 변경
```

### requests 외부 패키지 설치 및 사용 예시
```python
$ pip install requests # 외부 API 활용시 필수 패키지
```
<br>

![alt text](/TIL/img/pip.png)
<br>
- 성공적으로 설치 됨
- 설치 된 패키지를 확인하는 명령어 ( pip list )

### 사용 예시
```python
# HTTP 요청을 보낼 수 있도록 도와주는 requests 라이브러리 import
import requests

# 무작위 사용자 정보를 제공해주는 API의 URL
url = 'https://random-data-api.com/api/v2/users'

# requests.get(url)을 통해 API에 요청을 보냄
# 서버로부터 응답(Response)을 JSON 형태로 받아 Python 객체(딕셔너리/리스트 등)로 변환
response = requests.get(url).json()

# 받은 응답 데이터(딕셔너리 형태)를 출력
print(response)
```

### 패키지 사용 목적
- 모듈들을 효율적으로 관리하고 재사용 할 수 있도록 하고 모듈의 이름공간을 구분하여 충돌을 방지 할 수 있다.
