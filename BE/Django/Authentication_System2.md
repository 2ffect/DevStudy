# 인증 시스템
## 회원가입
- User 객체를 Create하는 과정

### UserCreationForm()
- 회원 가입 시 사용자 입력 데이터를 받는 built-in ModelForm

### get_user_model()
- 현재 프로젝트에서 활성화 된 사용자 모델(active user model)을 반환하는 함수

### User 모델을 직접 참조하지 않는 이유
- get_user_model()을 사용해 User모델을 참조하면 커스텀 User 모델을 자동으로 반환해주기 때문
- Django는 필수적으로 User 클래스를 직접 참조하는 대신 get_user_molde()을 사용해 참조해야 한다고 강조하고 있음

## 회원 탈퇴
- User 객체를 Delete 하는 과정

## 회원정보 수정
- User 객체를 Update 하는 과정

## 비밀번호 변경
- 인증된 사용자의 Session 데이터를 Update 하는 과정

### PasswordChangeForm()
- 비밀번호 변경 시 사용자 입력 데이틀 받는 built-in Form

### 암호 변경 시 세션 무효화
- 비밀번호가 변경되면 기존 세션과 회원 정보가 일치하지 않게 되기 때문에 로그아웃 처리 됨

### update_session_auth_hash(request, user)
- 암호 변경 시 세션 무효화를 막아주는 함수
- 암호가 변경되면 새로운 password의 Session Data로 기존 session을 자동으로 갱신

## 인증된 사용자에 대한 접근 제한
### 로그인 사용자에 대한 접근을 제한하는 2가지 방법
1. is_authenticated 속성
2. login_required 데코레이터

### is_authenticated
- 사용자가 인증 되었는지 여부를 알 수 있는 User model 속성
- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
- 비인증 사용자에 대해서는 항상 False
- User Class로 만들어졌으면 True, 아니면 False

### login_required 데코레이터
- 인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터
  - 비인증 사용자의 경우, accounts/login/주소로 redirect 시킴