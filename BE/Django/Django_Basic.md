# Web Application
## 클라이언트와 서버
### Client 클라이언트
- 서비스를 요청하는 주체 (사용자의 웹 브라우저, 모바일 앱)

### Server 서버
- 클라이언트의 요청에 응답하는 주체 (웹 서버, 데이터베이스 서버)

## Frontend & Backend
### 웹 개발에서의 Frontend 와 Backend
- Frontend (프론트엔드)
  - 사용자의 인터페이스(UI)를 구성하고, 사용자가 애플리케이션과 상호작용할 수 있도록 함
    - HTML, CSS, JavaScript, 프론트엔드 프레임워크 등

- Backend (백엔드)
  - 서버 측에서 동작하며, 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용 등을 담당
    - 서버 언어(Python, Java 등) 및 백엔드 프레임워크, 데이터베이스, API, 보안 등


## Framework
### Web Framework
- 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구
  - 개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공

## Django framework
- Python 기반의 대표적인 웹 프레임워크

### Django를 사용하는 이유
1. 다양성
   - Python 기반으로 웹, 모바일 앱 백엔드, API 서버 및 빅데이터 관리 등 광범위한 서비스 개발에 적합
2. 확장성
   - 대량의 데이터에 대해 빠르고 유연하게 확장할 수 있는 기능을 제공
3. 보안
   - 취약점으로부터 보호하는 보안 기능이 기본적으로 내장
4. 커뮤니티 지원
   - 개발자를 위한 지원, 문서 및 업데이트를 제공하는 활성화 된 커뮤니티


# 가상환경
## 개요
### 가상환경 (Virtual Environment)
- 하나의 컴퓨터 안에서 또 다른 '독립된' 파이썬 환경

### 가상 환경 생성 및 활성화
1. 가상환경 생성
  ```bash
  $ python -m venv venv(가상환경이름)
  ```
  - 현재 디릭토리에 venv 라는 폴더가 생성됨
  - venv 폴더 안에는 파이썬 실행파일, 라이브러리 등을 담을 공간이 마련됨
  - venv 라는 이름의 가상환경을 생선한 것이며 임의의 이름으로 생성 가능하나 관례적으로 venv 이름을 사용(그냥 venv 쓰기)
2. 가상환경 활성화
  ```bash
  $ source venv/Scripts/activate
  ```
  - 활성화 후, 프롬프트 앞에 (venv)와 같이 표시가 된다면 성공한 것
  - Mac/Linux 에서는 명령어가 다르니 주의
  >> source venv/bin/activate
3. 가상환경 종료
  ```bash
  deactivate
  ```
  - 활성화한 상태에서 입력하면 기본 Global파이썬 환경으로 돌아옴

## 의존성 패키지
### 의존성 (Dependencies)
- 하나의 소프트웨어가 동작하기 위해 필요로 하는 다른 소프트웨어나 라이브러리

### 의존성 패키지
- 프로젝트가 의존하는 "개별 라이브러리들"을 가리키는 말
  - "프로젝트가 실행되기 위해 꼭 필요한 패키지" 하나하나

1. 패키지 목록 확인
  ```bash
  pip list
  ```
  - 현재 가상 환경에서 설치된 라이브러리 목록을 확인
  - 갓 생성된 환경은 별도 패키지가 없기 때문에 pip, setuptools 정도만 표시된다.

2. 의존성 기록
  ```bash
  pip freeze > requirements.txt
  ```
  - pip freeze 명령어는 가상환경에 설치된 모든 패키지를 버전과 함께 출력
  - 이를 requirements.txt 파일에 저장하면 나중에 동일한 환경을 재현할 때 유요함
    - 다른 파일명으로도 가능하나 관례적으로 requirements를 사용
  - 협업 시 팀원에게 똑같은 버전의 라이브러리를 설치하도록 공유 가능

### 의존성 패키지 관리가 필요한 이유
1. 패키지마다 버전이 다르고, 버전이 다른 경우 함수명이나 동작이 달라질 수 있음
2. 프로젝트가 커질수록 사용하는 패키지의 개수도 늘어나므로, 어떤 버전을 쓰고 있는지 기록 및 공유가 필수적
3. 다른 PC나 팀원들이 같은 환경을 구성할 때 의존성 리스트가 반드시 필요

### 의존성 패키지 기반 설치
1. 가상환경 준비 (가상환경 생성 및 활성화)
2. requirements.txt로 부터 패키지 설치
  ```
  pip install -r requirements.txt
  ```

### 가상환경 주의사항
1. 가상 환경에 "들어가고 나오는" 것이 아니라, 사용할 Python 환경을 "On/Off" 로 전환하는 개념
   - 가상환경 활성화는 현재 터미널 환경에만 영향을 끼침
   - 새 터미널 창을 열면 다시 활성화해야 함
2. 프로젝트마다 별도의 가상환경을 사용
3. 일반적으로 가상환경 폴더 venv는 관련된 프로젝트와 동일한 경로에 위치시킴
4. 폴더 venv는 .gitignore 파일에 작성되어 원격 저장소에 공유되지 않음
   - 저장소 크기를 줄여 효율적인 협업과 배포를 가능하게 하기 위함(requirements.txt 를 공유)

### 가상환경이 필요한 이유
1. 프로젝트마다 다른 버전의 라이브러리 사용
2. 의존성 충돌 방지
3. 팀원 간 협업


### 요약
1. 가상환경 만들기                (python -m venv venv)
2. 가상환경 활성화                (source venv/Scripts/activate)
3. 필요 의존성 패키지 설치          (pip install)
4. 의존성 관리                    (pip freeze > requirements.txt)
5. 동일 환경 구성                 (pip install -r requirements.txt)
6. 작업이 끝나면 가상환경 비활성화 (deactivate)


# Django 프로젝트
## 프로젝트 생성 및 서버 실행
1. 장고 설치 (pip install django)
  - pip list로 잘 설치 되었는지 확인 후 의존성 패키지 관리
2. 프로젝트 생성
  ```
  django-admin startproject firstpjt(프로젝트 이름) .(현재 디렉토리)
  ```
  - firstpjt 라는 이름의 dajngo 프로젝트를 생성
  - . 현재 디렉토리에 생성 하겠다. 라는 뜻

3. 서버 실행
  ```
  python manage.py runresrver
  ```
  - manage.py 와 동일한 위치에서 명령어 진행

## Django Design Pattern
### 디자인 패턴
- 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책
  - 공통적인 문제를 해결하는 데 쓰이는 형식화 된 관행
  - "애플리케이션 구조는 이렇게 구성하자" 라는 관행

### MVC 디자인 패턴
- Model, View, Controller
- 애플리케이션을 구조화하는 대표적인 패턴 
  - (데이터 & 사용자 인터페이스 & 비즈니스 로직)
  - 시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이 독립적이고 쉽게 유지 보수 할 수 있는 애플리케이션을 만들기 위해 위 3가지로 분리함

### MTV 디자인 패턴
- Model, Template, View
- Django 에서 애플리케이션을 구조화하는 패턴
  (기존 MVC 패턴과 동일하나 단순히 명칭을 다르게 정의한 것)

### 프로젝트와 앱
### Django project
- 애플리케이션의 집합 (DB설정, URL연결, 전체 앱 설정 등을 처리)
  
### Django application
- 독립적으로 작동하는 기능 단위 모듈
  (각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성)

### 앱을 사용하기 위한 순서 (약속/규칙)
1. 앱 생성
  ```
  python manage.py startapp articles
  ```
  - 앱의 이름은 '복수형'으로 지정하는 것을 권장
2. 앱 등록
  ```
  프로젝트 디렉토리의 settings.py 에서 
  아래 영역에 추가
  INSTALLED_APPS = [
    여기 추가,
  ]
  ```
  - 반드시 앱을 생성(1) 한 후에 등록(2) 해야 함
  - 등록 후 생성은 불가.
  
### 프로젝트 구조
- settings.py
  - 프로젝트의 모든 설정을 관리
- urls.py
  - 요청 들어오는 URL에 따라 이에 해당하는 적절한 views를 연결
- \__init__.py
  - 해당 폴더를 패키지로 인식하도록 설정
- asgi.py
  - 비동기식 웹 서버와 연결 관련 설정
- wsgi.py
  - 웹 서버와 연결 관련 설정
- manage.py
  - Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

### 앱 구조
- admin.py
  - 관리자용 페이지 설정
- models.py
  - DB와 관련된 Model을 정의
  - MTV 패턴의 M
- views.py
  - HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환 (url, model, template과 연계)
  - MTV 패턴의 V
- apps.py
  - 앱의 정보가 작성된 곳
- tests.py
  - 프로젝트 테스트 코드를 작성하는 곳

## 요청과 응답
요청발생 > urls.py > views.py -> models.py or templates -> views.py -> 응답

1. URLs
  ```py
  # atriclse 라는 앱의 views에서 가져올거다
  from articles import views

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', views.index),
  ]
  ```
  - http://127.0.0.1:8000/articles/ 로 요청이 왔을때, request 객체를 views 모듈의 index view 함수에게 전달하며 호출

2. View
  - view 함수가 저장되는 곳
  - 특정 경로에 있는 template과 request 객체를 결합해 응답 객체를 반환
  ```py
  from django.shortcuts import render

  # Create your views here.
  def index(request):
      # (메인 페이지가 담겨있는) 응답 객체를 반환
      return render(request, 'articles/index.html')
  ```

3. Template
   1. 앱 폴더 안에 templates 폴더 생성 **폴더명은 반드시 templates 여야 하며 개발자가 직접 생성해야 함**
   2. templates 폴더 안에 atricles 폴더 생성
   3. atricles 폴더 안에 template 파일 생성


### 데이터에 흐름에 따른 코드 작성하기
URLs -> View -> Template


### Django 프로젝트 생성 루틴 정리 + git
1. 가상환경 생성
2. 가상환경 활성화
3. Django 설치
4. 패키지 목록 파일 생성(패키시 설치시 마다 진행)
5. .gitinnore 파일 생성 (첫 add 전)
6. git 저장소 생성 (git init)
7. Django 프로젝트 생성


## Django 관련
### LTS (Long-Term Support)
- 프레임워크나 라이브러리 등의 소프트웨어에서 장기간 지원되는 안정적인 버전을 의미
- 기업이나 대규모 프로젝트에서는 소프트웨어 업그레이드에 많은 비용과 시간이 필요하기 때문에 안정적이고 장기간 지원되는 버전이 필요
