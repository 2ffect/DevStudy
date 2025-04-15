# Many to Many relationshisps
## N:M or M:N
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
  - 양쪽 모두에 1:N 관계를 가짐

## 중개 모델
- Django 에서는 'ManyToManyField'로 중개 모델을 자동으로 생성

### ManyToManyField()
- M:N 관계 설정 모델 필드
- 어느 모델에 작성해도 상관 없으며 참조/역참조 관계만 잘 기억하면 됨
  - 필드를 작성한 모델이 참조 모델
  - 
```py
from django.db import models
class Doctor(models.Model):
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    # ManyToManyField 작성
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```


```shell
# 코드 예시
doctor1 = Doctor.objects.create(name='allie')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='duke')

patient1.doctors.add(doctor1)

In [8]: patient1.doctors.all()
Out[8]: <QuerySet [<Doctor: 1번 의사 allie>]>

In [9]: doctor1.patient_set.all()
Out[9]: <QuerySet [<Patient: 1번 환자 carol>]>

doctor1.patient_set.add(patient2)

In [11]: doctor1.patient_set.all()
Out[11]: <QuerySet [<Patient: 1번 환자 carol>, <Patient: 2번 환자 duke>]>


doctor1.patient_set.remove(patient1)
In [13]: doctor1.patient_set.all()
Out[13]: <QuerySet [<Patient: 2번 환자 duke>]>

In [14]: patient1.doctors.all()
Out[14]: <QuerySet []>
```

### 'through' argument
- 중개 테이블에 '추가 데이터'를 사용해 M:N 관계를 형성하려는 경우 사용

### M:N 주요사항
- M:N 관계로 맺어진 두 테이블에는 물리적인 변화가 없음
- ManyToManyField는 중개 테이블을 자동으로 생성
- ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
  - 참조/역참조의 방향 주의
- N:1 은 완전 종속 관계였지면 M:N은 종속 관계가 아님

### ManyToManyField 인자
1. related_name
  - 역참조시 사용하는 manger name 변경
```py
class Patient(models.Model):
    # ManyToManyField - related_name 작성
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()
# 변경 전
doctor.patient_set.all()

# 변경 후 (변경 후 이전 manager name은 사용 불가)
doctor.patients.all()
```
2. symmetrical
  - 관계 설정 시 대칭 유무를 설정함
  - ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용
  - 기본값 : True
    - True 인 경우
      - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함 (대칭)
      - 즉, 내가 당신의 친구라면 자동으로 당신도 내 친구가 됨
    - False 인 경우
      - True와 반대 (대칭되지 않음)

3. through
  - 사용하고자 하는 중개모델을 지정
  - 일반적으로 추가데이터를 M:N 관계와 연결하려는 경우에 활용함.

### M:N 대표 초작 methods
- add()
  - 관계 추가
  - 지정된 객체를 관련 객체 집합에 추가

- remove()
  - 관계 제거
  - 관련 객체 집합에서 지정된 모델 객체를 제거

### User -Article 간 사용 가능한 전체 related manager
- article.user
  - 게시글을 작성한 유저 - N:1
- user.article_set
  - 유저가 작성한 게시글 (역참조) - N:1
- article.like_user
  - 게시글을 좋아요 한 유저 - N:1
- user.like_articles
  - 유저가 좋아요 한 게시글(역참조) - N:1