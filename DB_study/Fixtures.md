# Fixtures
## 개요
### Fixtures
- Django 개발 시 데이터 베이스 초기화 및 공유를 위해 사용되는 파일 형식

### Fixtures 사용 목적
- 샘플, 초기 데이터 셋팅
- 협업 시 동일한 데이터 환경 맞추기

### 초기 데이터의 필요성
- 프로젝트의 앱을 처음 설정할 때 동일하게 준비 된 데이터로 데이터베이스를 미리 채우는 것이 필요한 순간이 있음
- Django에서는 Fixtures를 사용해 앱에 초기 데이터(initial data)를 제공

### fixtures 관련 명령어
- dumpdata : 생성 (데이터 추출)
- loaddata : 로드 (데잍너 입력)

## dumpadata
- 데이터베이스의 특정 모델 혹은 앱 전체 데이터를 추출

### dumpadata 기본 명령어
```bash
python manage.py dumpdata [앱이름.모델이름] [옵션] > 추출파일명.json
```
- 앱이름.모델이름 지정
  - 특정 모델의 데이터를 추출

- 앱이름만 지정
  - 해당 앱의 모든 모델에 대한 데이터를 추출

- 앱 혹은 모델명을 지정하지 않은 경우
  - 프로젝트 전체 모델에 대한 데이터를 추출
 
- --format 옵션을 통해 JSON,YAML 등의 형식 지정 가능 (default : JSON)

### dumpdata 명령어 예시
```bash
python manage.py dumpdata --indent 4 articles.article > articles.json
```
- articles 앱의 Article 모델 데이터를 추출
- 명령어 실행 후 프로젝트 폴더에 articles.json 파일이 생성됨
- articles.json 파일에는 Article 모델의 모든 데이터가 JSON 형식으로 작성되어 있음
- Fixtures 파일명은 자유롭게 작성 가능

### dumpdata 정리
- dumpdata 명령어를 사용하면 프로젝트 내 특정 앱 혹은 모델에 대한 데이터를 JSON 등 원하는 포맷으로 추출 가능
- 추후 다른 환경에서 loaddata로 불러와 동일한 데이터 상태 재현 가능
- 협업 및 배포에 큰 장점

## loaddata
- dumpdata를 통해 추출한 데이터 파일을 다시 데이터베이스에 반영

### loaddata 기본 명령어
```bash
python manage.py loaddata 파일경로
```
- Fixtures 파일의 기본 경로에 있는 파일을 DB에 반영
  - app_name/fixtures/
- Django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후의 경로로 fixtures 파일을 찾아 load 진행

### loaddata 주의사항
- loaddata를 실행하기 전 해당 모델에 대한 마이그레이션이 완료되어야 함
- 같은 PK를 가진 데이터가 이미 있는경우 중복 에러 발생할 수 있음
  - 기존 데이터를 지우거나 새로운 Fixture 파일을 사용해야 함
- 불러오는 순서 중요함

## Improve Query
- " query 개선하기 "
- 같은 결과를 얻기 위해 DB측에 보내는 query 개수를 점차 줄여 조회하기

### annotate
- SQL의 GROUP BY를 사용
- 쿼리셋의 각 개체에 계산된 필드를 추가
- 집계 함수 (Count, Sum 등)와 함께 사용됨

### select_related
- SQL의 INNER JOIN를 사용
- 1:1 또는 N:1 참조 관계에서 사용
  - ForeignKey 나 OneToOneField 관계에 대해 JOIN을 수행
- 단일 쿼리로 관련 객체를 함께 가져와 성능을 향상

### prefetch_related
- SQL이 아닌 Python을 사용한 JOIN을 진행
  - 관련 객체들을 미리 가져와 메모리에 저장하여 성능을 향상
- M:N 또는 N:1 역참조 관계에서 사용
  - ManyToManyField나 역참조 관계에 대해 별도의 쿼리를 실행

### select_related & prefetch_related
```py
def index_4(request):
    articles = Article.objects.prefetch_related(
        Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
    ).order_by('-pk')

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_4.html', context)
```