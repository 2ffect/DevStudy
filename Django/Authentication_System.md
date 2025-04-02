# 인증 시스템
## HTTP
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 규약
- 웹 (WWW) 에서 이루어지는 모든 데이터 교환의 기초

### HTTP 특징
1. 비 연결 지향(connectionless)
  - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음

2. 무상태 (stateless)
  - 연결을 끊는 순간 클라이언트와 서버 간 통신이 끝나며 상태 정보(로그인 등)가 유지되지 않음
  - 상태가 없다는 것
    - 장바구니에 담음 상품을 유지할 수 없음
    - 로그인 상태를 유지할 수 없음

## Cookie(쿠키)
- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
  - 서버가 제공하여 클라이언트 측에 저장되는 작은 데이터 파일
  - 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식

### 쿠키 동작 예시
1. 브라우저가 웹 서버에 웹 페이지를 요청
2. 웹 서버는 요청된 페이지와 함께 쿠키를 포함한 응답을 브라우저에 전송
3. 브라우저는 받은 쿠키를 저장소에 저장, 쿠키의 속성(만료 시간, 도메인, 주소, 로그인 정보 등)도 함께 저장됨
4. 이후, 브라우저가 같은 웹 서버에 웹 페이지를 요청할 때, 저장된 쿠키 중 해당 요청에 적용 가능한 쿠키를 포함하여 함께 전송
5. 웹 서버는 쿠키를 통해 정보 확인, 사용자 식별, 세션 관리 등 수행
6. 웹 서버가 요청에 대한 응답을 보내며 필요 시 새로운 쿠키를 설정하거나 기존 쿠키를 수정 할 수 있음

### 쿠키 작동 원리와 활용
1. 쿠키 저장 방식
  - 브라우저(클라이언트)는 쿠키를 Key-Value 데이터 형식으로 저장
  - 쿠키에는 이름, 값 외에도 만료시간, 도메인, 경로 등 추가 속성 포함

2. 쿠키 전송 과정
  - 서버는 HTTP 응답 헤더의 Set-Cookie 필드를 통해 클라이언트에게 쿠키를 전송
  - 브라우저는 받은 쿠키를 저장, 동일한 서버에 재 요청 시 HTTP 요청 헤더의 Cookie 필드에 저장된 쿠키를 함께 전송

3. 쿠키의 주요 용도
  - 두 요청이 동일한 브라우저에서 들어왔는지 아닌지 판단 할 때 주로 사용
  - 이를 통해 사용자의 로그인 상태를 유지할 수 있음
  - 상태가 없는 (stateless) HTTP 프로토콜에서 상태 정보를 기억시켜 주는 역할
  -> 서버에게 인증정보가 담긴 쿠키를 매 요청마다 계속 보내는 것 (로그인 유지 가능)

### 쿠키 사용 목적
1. 세션 관리 (Session management)
  - 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리

2. 개인화 (Personalization)
  - 사용자 선호 설정(언어 설정, 테마 등) 저장

3. 트래킹 (Tracking)
  - 사용자 행동을 기록 & 분석

## 세션 (Session)
- 서버 측에서 생성되는 클라이언트와 서버 간 상태를 유지
- 상태 정보를 저장하는 데이터 저장 방식
  - 쿠키에 세션 데이터를 저장하여 매 요청시마다 세션 데이터를 함께 보냄

### 세션 작동 원리
1. 클라이언트가 로그인 요청 후 인증에 성공하면 서버가 session 데이터를 생성 후 저장
2. 생성된 session 데이터에 인증할 수 있는 session id를 발급
3. 발급한 session id를 클라이언트에게 응답 (데이터는 서버에 저장되며, 클라이언트에 key만 주는 것)
4. 클라이언트는 응답 받은 session id를 쿠키에 저장
5. 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 session id가 저장된 쿠키를 서버에 전달
6. 쿠키는 요청 할 때 마다 전송되므로 쿠키에 포함된 session id를 확인해 로그인 되어있다는 것을 확인시킴

### 요약
- 서버 측에서는 세션 데이터를 생성 후 저장하고 이 데이터에 접근할 수 있는 세션 ID를 생성
- 이 ID를 클라이언트로 전달하고, 클라이언트는 쿠키에 이 ID를 저장
- 이후 같은 서버로 요청 시 해당 쿠키도 요청과 함께 전송함

### 쿠키와 세션의 목적
- 클라이언트와 서버 간 상태 정보를 유지하고 사용자를 식별하기 위해 사용


## Django Authentication System
- 사용자 인증과 관련된 기능을 모아 놓은 시스템

### Authentication (인증)
- 사용자가 자신이 누구인지 확인하는 것 (신원 확인)

### 사전 준비
- accounts 앱 생성 및 등록
  - auth와 관련한 경로나 키워드들을 django 내부적으로 accounts 라는 이름을 사용하고 있기 때문에 되도록 'accounts'로 지정하는 것을 권장

## Custom User Model
### User model 대체하기

### 기본 User Model의 한계
- Django의 기본 User 모델은 username, password 등 제공되는 필드가 매우 제한적임
- 추가적 사용자 정보(ex. 생년월일, 주소, 나이 등) 가 필요하다면 이를 위해 기본 User Model을 사용하기 어려움. (별도의 설정없이 사용 가능해 간편하지만, 개발자가 직접 수정하기 어려움)

### User model 대체의 필요성
- 프로젝트의 특정 요구사항에 맞춰 사용자 모델을 확장할 수 있음
- 이메일을 username으로 사용하거나, 다른 추가 필드를 포함시킬 수 있음

### Custom User Model로 대체하기
1. 커스텀 User 클래스 작성
```py
# accounts/models.py
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass
```
2. AUTH_USER_MODEL 값을 위에서 작성한 User 모델로 변경 
```py
# settings.py 맨 아래 새로 작성
AUTH_USER_MODEL = 'accounts.User'
```
3. admin site 에 대체한 User 모델 등록
  - 기본 User모델이 아니기 때문에 등록하지 않으면 admin 페이지에 출력되지 않음
```py
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)
```

#### AUTH_USER_MODEL
- Django 프로젝트의 User를 나타내는 데 사용하는 모델을 지정하는 속성
- 프로젝트 진행 중에는 변경할 수 없음 (데이터베이스 초기화 후 진행해야 함)

### 프로젝트 시작 시
- 프로젝트 시작 전 반드시 User 모델을 대체해야 함 
- Django는 기본 User 모델이 충분 하더라도 커스텀 User 모델을 설정하는 것을 강력히 권장 !
  - 동일하게 작동하지만, 커스텀 모델의 경우 필요에 따라 맞춤 설정이 가능하기 때문
  -  첫 migrate를 실행 전 이 작업을 마쳐야 함

## Login
- 로그인은 Session을 Create하는 과정

### AuthenticationForm()
- 로그인 인증에 사용할 데이터를 입력 받는 built-in form

### login(request, user)
- AuthenticationForm을 통해 인증된 사용자를 로그인 하는 함수

### get_user()
- AuthenticationForm의 인스턴스 메서드
  - 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

```py
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def login(requset):
    if requset.method == 'POST':
        form = AuthenticationForm(requset, requset.POST)
        if form.is_valid():
            # 로그인 인증을 위한 함수
            auth_login(requset, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context ={
        'form' : form
    }
    return render(requset, 'accounts/login.html', context)
```

## Logout
- 로그아웃은 Session을 Delete 하는 과정

### Logout(request)
- DB에서 현재 요청에 대한 Session Data를 삭제
- 클라이언트의 쿠키에서도 Session Id를 삭제
```py
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

## Templat with Authentication data
### 템플릿과 인증 데이터
- Templat with Authentication data
  - 템플릿에서 인증 관련 데이터를 출력하는 방법

### context processors
- 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
- 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함된다.
  - django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드 해 둔 것