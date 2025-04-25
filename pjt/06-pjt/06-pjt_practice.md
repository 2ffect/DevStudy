# Q 객체
## Q 객체 생성
```py
from django.db.models import Q
Q(content__contains = 'dja') ## django, djapple 등
Q(title__startswith = 'he')
```

## Q 객체를 통한 ORM 조건 구성
- 비트 논리 연산자를 활용한 조건문 작성
  - AND = &
  - OR = |
  - NOT = ~

### AND 조건
- filter() 메서드 내 두 Q 객체를 & 로 연결
```py
def and_query(request):
  articles = Article.objects.filter(
    Q(content__contains = 'dja') & Q(title__startswith = 'he')
  )

  serializer = ArticleSerializer(article, many=True)
  return Response(Serializer.data)
```
### OR 조건
- filter() 메서드 내 두 Q 객체를 | 로 연결
```py
def and_query(request):
  articles = Article.objects.filter(
    Q(content__contains = 'dja') | Q(title__startswith = 'he')
  )
```

### NOT 조건
- filter() 메스드 내 Q 객체 앞에 ~
```py
def and_query(request):
  articles = Article.objects.filter(
    ~Q(title__startswith = 'he')
  )

```