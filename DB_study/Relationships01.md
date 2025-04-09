# Many to on relationships
## 모델 관계
### Many to on relationships (N:1 or 1:N)
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계
- 0개 이상(N)과 1개(1)
### Comment(N) - Article(1)
- 0개 이상의 댓글은 1개의 게시글에 작성될 수 있다.

### ForeignKey()
- 한 모델이 다른 모델을 참조하는 관계를 설정하는 필드
  - N:1 관계 표현
  - 데이터베이스에서 외래키로 구현
- ForeignKey 클래스의 인스턴스 이름은 참조하는 모델 클래스 일므의 단수형으로 작성하는 것을 권장
- 외래키는 ForeignKey 클래스를 작성하는 위치와 관계없이 테이블의 마지막 필드로 생성 됨

### ForeignKey(to, on_delete)
- to
  - 참조하는 모델 class 이름
- on_delete
  - 외래키가 참조하는 객체(1)가 사라졌을 때, 외래키를 가진 객체(N)를 어떻게 처리할지 정의하는 설정(데이터 무결성)
### on_delete의 'CASCADE'
- 참조 된 객체(부모 객체)가 삭제될 때 이를 참조하는 모든 객체도 삭제되도록 지정

### 생성 된 외래키 필드
- 필드 이름 = '참조 대상 클래스 이름' + '_' + '클래스 이름'
  - article + _ + id

## 관계 모델 참조
### 역참조
- N:1 관계에서 1에에서 N을 참조하거나 조회하는 것 (1 -> N)
- 모델 간 관계에서 관계를 정의한 모델이 아닌 관계의 대상이 되는 모델에서 연결 된 객체들에 접근하는 방식
  - N은 외래키를 가지고 있어 물리적으로 참조가 가능하지만, 1은 N에 대한 참조 방법이 존재하지 않아 별도 역참조 키워드 필요

### 역참조 사용 예시
```shell
article.comment_set.all()
```
- article : 모델 인스턴스
- comment_set : 역참조 이름
- all() : QuerySet API
- 특정 게시글에 작성된 댓글 전체를 조회하는 요청

### related manager
- N:1 혹은 M:N 관계에서 역참조 시 사용하는 매니저

### related manager 규칙
- N:1 관계에서 생성되는 related manager 이름은 "모델명_set" 형태로 자동 생성됨
- 특정 게시글의 댓글 목록 참조 (Article -> Comment)
  - article.comment_set.all()