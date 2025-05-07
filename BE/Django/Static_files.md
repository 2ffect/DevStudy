# Static files
## Static Files (정적파일)
- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일 (이미지, JS, CSS파일 등)

### 웹 서버와 정적 파일
- 웹 서버의 기본 동작은 특정 위치(URL)에 있는 자원(데이터)을 요청(HTTP request) 받아서 응답(HTTP response)을 처리하고 제공하는 것
- 이는 "자원에 접근 가능한 주소가 있다." 라는 의미
- 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공
- 서버에는 정작 파일을 제공하기 위한 경로(URL)가 있어야 함
![alt text](img/Static.png)

### Static files 제공하기
- Static files 경로
  1. 기본 경로 (약속 된 경로)
  2. 추가 경로 (추가 경로)

### Static files 기본 경로
- app폴더/static/
#### 기본 경로 Static file 제공하기
- articles/static/articles/ 경로에 이미지 파일 배치
- static files 경로는 DTL의 static tag를 사용해야 함
  - built-in tag가 아니기 때문에 load tag를 사용해 import 후 사용 가능

### STATIC_URL
- 기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL
  - 실제 파일이나 디렉토리 경로가 아니며, URL로만 존재

### CSS 적용 시
```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="{% static "articles/style.css" %}"> 
  <title>Document</title>
</head>
```
- static 태그 활용하여 css 파일의 위치를 지정

### Static files 추가 경로
- STATICFILES_DIRS 에 문자열 값으로 추가 경로 설정
- STATICFILES_DIRS
  - 정적 파일의 기본 경로 외 추가적 경로 목록을 정의하는 리스트

### 결론
- 정적 파일을 제공하려면 요청에 응답하기 위한 URL이 필요

## Media files
- 사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)

### 이미지 업로드
#### ImageField()
- 이미지 업로드에 사용되는 모델 필드
- 이미지 객체가 직접 DB에 저장되는 것이 아닌 '이미지 파일의 경로' 문자열이 저장 됨

### 미디어 파일 제공 전 준비사항
1. settings.yp에 MEDIA_ROOT, MEDIA_URL 설정
2. 작성한 MEDIA_ROOT 와 MEDIA_URL 에 대한 URL 지정

### MEDIA_ROOT
- 미디어 파일들이 위치하는 디렉토리의 절대 경로 (실제 저장될 경로로)

### MEDIA_URL
- MEDIA_ROOT 에서 제공되는 미디어 파일에 대한 주소를 생성 (STATIC_URL과 동일한 역할)

### MEDIA_ROOT 와 MEDIA_URL 에 대한 URL 지정
```py
# 프로젝트의 urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```
업로드 된 파일의 URL == settings.MEDIA_URL
MEDIA_URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_URL


### 이미지 업로드 
1. ImageField를 사용하려면 반드시 ! Pillow 라이브러리가 필요하기 때문에 설치 해야함.
2. blank = True 속성을 통해 빈 무자열이 저장될 수 있도록 제약 조건 설정
  - 게시글 작성 시 이미지 업로드 없이도 작성 할 수 있도록 하기 위함
```py
# app의 models.py
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
3. migration -> migrate 진행
4. form 요소의 enctype 속성 추가
```html
<!-- articles/create.html -->
<h1>CREATE</h1>
<form action="{% url "articles:create" %}" method="POST" enctype='multipart/form-data'>
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
```
- enctype : 데이터 전송방식을 결정하는 속성

5. ModelForm의 2번째 인자로 요청받은 파일 데이터 작성
```py
# app의 views.py
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
```

### 업로드 이미지 제공
- 'url' 속성을 통해 업로드 파일의 경로 값을 얻을 수 있음
- article.image.url
  - 업로드 파일의 경로
- article.image
  - 업로드 파일의 파일 이름
```html
<!-- article/detail.html -->
<img src="{{ article.image.url }}" alt="media_image">
```


### 업로드 이미지 수정
1. 수정 페이지 form 요소에 enctype 속성 추가
2. view 함수에서 업로드 파일에 대한 추가 코드 작성 (request.FILES)


### 미디어 파일 추가 경로
- ImageField() 의 upload_to 속성을 사용해 다양한 추가 경로 설정이 가능함.
```py
# 기본 경로 설정
iamge = models.ImageField(blanke=True, upload_to='images/')

# 업로드 날짜로 경로 설정
iamge = models.ImageField(blanke=True, upload_to='%Y/%m/%d/')

# 함수 형식으로 경로 설정
def articles_image_path(instance, filename):
    return f'images/{instance.user.username}/{filename}

iamge = models.ImageField(blanke=True, upload_to=articles_image_path)
```
- upload_to 는 MEDIA_ROO 이후 경로