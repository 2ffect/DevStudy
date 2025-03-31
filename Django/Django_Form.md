# Django Form
## 개요
### HTML 'form'
- 지금까지 사용자로부터 데이터를 제출 받기위해 활용한 방법이지만 비정상적 혹은 악의적 요청을 필터링 할 수 없음
  - 유효한 데이터인지에 대한 확인이 필요함

### 유효성 검사
- 수집한 데이터가 정확하고 유효한지 확인하는 과정
- 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야함.
  - Django가 제공하는 Form을 활용하여 사용 가능

## Form Class
### Django 'form'
- 사용자 입력 데이터를 수집하고 처리 및 유효성 검사를 수행하기 위한 도구
  - 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공

### Form class 정의
```py
# articles/forms.py
from django import forms

class ArticleForm(forms.Form):
  title = forms.CharField(max_length = 10)
  content = forms.CharField()
```

## Widgets
- HTML 'input' element의 표현을 담당
- 단순히 input 요소의 속성 및 출력되는 부분을 변경하는 것


## Djnago ModelForm
Form - 사용자 입력 데이터를 DB에 저장하지 않을 때 (검색, 로그인 등)
Model Form - 사용자 입력 데이터를 DB에 저장해야 할 때 (게시글 작성, 회원가입 등)

### ModelForm
- Model과 연결된 Form을 자동으로 생성해주는 기능을 제공
  - Form + Model

## Meta Class
- ModelForm의 정보를 작성하는 곳

### Meta Class 주의사항
- Django에서 ModelForm에 대한 추가 속성 정보나 속성을 작성하는 클래스 일 뿐
- Python의 inner class와 같은 문법적 접근 X !!

### 'fields' 및 'exclude 속성
- exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음


### ModelForm 적용
- is_valid()
  - 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 반환

### 공백 데이터가 유효하지 않은 이유
- 별도로 명시하지는 않지만, 모델 필드에서 기본적으로 빈 값은 허용하지 않는 제약조건이 설정되어 있기 때문
  

## svae 메서드
- save()
  - 데이터베이스 객체를 만들고 저장하는 ModelForm의 인스턴스 메서드

### save() 메서드가 생성과 수정을 구분하는 법
- 키워드 인자 instance 여부를 통해 새로 생성할지, 기존 내용을 수정할지 결정함.
  

## Django Form 정리
- 사용자로부터 데이터를 수집하고 처리하기 위한 강력하고 유여한 도구
- HTML form 의 생성, 데이터 유효성 검사 및 처리를 쉽게할 수 있도록 도움

# HTTP 요청 다루기
## View 함수 구조 변화
### new & create view 함수간 공통점과 차이점
- 공통점 : 데이터 생성을 구현하기 위함
- 차이점 : new 는 GET method 요청만, create 는 POST method 요청만 처리

### new & create 함수 결합
- HTTP request method 차이점을 활용해 동일한 목적을 가지는 2개의 view 함수를 하나로 구조화
- articles/create/ 에서 GET을 받으면 게시글 생성페이지, POST를 받으면 게시글 생성

