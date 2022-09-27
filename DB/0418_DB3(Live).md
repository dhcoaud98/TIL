# 04.18

## DB 03_Model Relationship2

[TOC]

<br>

### 1. Intro

#### 1. 병원 진료 기록 시스템 

> 병원 진료 기록 시스템을 통한 M:N 관계 학습
>
> * 환자와 의사가 사용하는 병원 진료 기록 시스템 구축

1. 1:N모델 관계 설정

   ```python
   # hospitals/models.py
   
   from django.db import models
   
   # Create your models here.
   class Doctor(models.Model):
       name = models.TextField()
   
       def __str__(self):
           return f'{self.pk}번 의사 {self.name}'
   
   
   class Patient(models.Model):
       doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
       name = models.TextField()
   
       def __str__(self):
           return f'{self.pk}번 환자 {self.name}'
   ```

   ```bash
   $ python manage.py makemingrations
   $ python manage.py migrate
   
   $ python manage.py shell_plus  # shell_plus 진행
   ```

   ```shell
   doctor1 = Doctor.objects.create(name='justin')  # 의사1
   doctor2 = Doctor.objects.create(name='eric')  # 의사1
   patient1 = Patient.objects.create(name='tony', doctor=doctor1)  # 환자1은 의사1에게 진료받음
   patient2 = Patient.objects.create(name='harry', doctor=doctor2)  # 환자2는 의사2에게 진료받음
   patient3 = Patient.objects.create(name='tony', doctor=doctor2)  # 환자3은 의사2에게 진료받음
   patient4 = Patient.objects.create(name='harry', doctor=doctor1, doctor2)  # 환자4는 의사2에게 진료받음
    # error 발생한다!!
    # 외래 키에 '1, 2'형식의 데이터를 사용할 수 없다. 
   ```

   :small_red_triangle: 오류를 해결하기 위해 `models`을 새로 작성!!

2. 중개 모델

   ```python
   # hospitals/models.py
   
   from django.db import models
   
   
   class Doctor(models.Model):
       name = models.TextField()
   
       def __str__(self):
           return f'{self.pk}번 의사 {self.name}'
   
   
   # 외래키 삭제
   class Patient(models.Model):
       name = models.TextField()
   
       def __str__(self):
           return f'{self.pk}번 환자 {self.name}'
   
   # 중개모델 작성
   class Reservation(models.Model):
       doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
       patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
   
       def __str__(self):
           return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
   ```

   ```shell
   # 데이터 베이스 초기화/ 마이그레이션 진행
   $ python manage.py makemingrations
   $ python manage.py migrate
   
   $ python manage.py shell_plus  # shell_plus 진행
   ```

   ```shell
   doctor1 = Doctor.objects.create(name='justin')
   patient1 = Patient.objects.create(name='tony')
   
   Reservation.objects.create(doctor=doctor1, patient=patient1)
   
   doctor1.reservation_set.all()
   patient1.reservation_set.all()
   
   patient2 = Patient.objects.create(name='harry')
   Reservation.objects.create(doctor=doctor1, patient=patient2)
   ```

   ![image-20220418103704031](0418_DB3(Live).assets/image-20220418103704031.png)

3. **ManytoManyField**

   * 다대다(M:N) 관계 설정 시 사용하는 모델 필드이다. 하나의 필수 위치 인자가 필요하다.

   ```python
   # hospitals/models.py
   
   from django.db import models
   
   # Create your models here.
   class Doctor(models.Model):
       name = models.TextField()
   
       def __str__(self):
           return f'{self.pk}번 의사 {self.name}'
   
   
   class Patient(models.Model):
       doctors = models.ManyToManyField(Doctor)
       name = models.TextField()
   
       def __str__(self):
           return f'{self.pk}번 환자 {self.name}'
   ```

   ```shell
   # 데이터 베이스 초기화/ 마이그레이션 진행
   $ python manage.py makemingrations
   $ python manage.py migrate
   
   $ python manage.py shell_plus  # shell_plus 진행
   ```

   ![image-20220418103933236](0418_DB3(Live).assets/image-20220418103933236.png)

   :small_red_triangle: `patient_doctors` 라는 테이블이 하나 생성된다.!!

   ```shell
   doctor1 = Doctor.objects.create(name='justin')
   patient1 = Patient.objects.create(name='tony')
   patient2 = Patient.objects.create(name='harry')
   
   patient1.doctors.add(doctor1)  # 환자1의 doctors 필드에 doctor1 넣음
   patient1.doctors.all()
   doctor1.patient_set.all()
   
   doctor1.patient_set.add(patient2)  # 의사2가 환자1을 예약 잡음(역참조)
   doctor1.patient_set.all()
   patient2.doctors.all()
   patient1.doctors.all()
   
   doctor1.patient_set.remove(patient1)
   doctor1.patient_set.all()
   patient1.doctors.all()
   
   patient2.doctors.remove(doctor1)
   patient2.doctors.all()
   doctor1.patient_set.all()
   ```

4. `related_name`

   * 현재는 `P->D`는 참조, `D->P`는 역참조이므로 역참조시 maneger의 이름을 설정한다. 

   ```python
   # hospitals/models.py
   
   from django.db import models
   
   # Create your models here.
   class Doctor(models.Model):
       name = models.TextField()
   
       def __str__(self):
           return f'{self.pk}번 의사 {self.name}'
   
   
   class Patient(models.Model):
       doctors = models.ManyToManyField(Doctor, related_name='patients')
       name = models.TextField()
   
       def __str__(self):
           return f'{self.pk}번 환자 {self.name}'
   ```

   ```shell
   # 마이그레이션 진행
   $ python manage.py makemingrations
   $ python manage.py migrate
   
   $ python manage.py shell_plus  # shell_plus 진행
   ```

   ```shell
   doctor1 = Doctor.objects.get(pk=1)
   
   doctor1.patients.all()  # 위에서 related_name으로 이름 변경했으므로 역참조 가능
   doctor1.patient_set.all()  # 더이상 조회 불가능
   ```

* 중개 테이블을 직접 작성하기 위해서 `through`옵션을 사용하여, 중개 테이블을 나타내는 Django모델을 지정할 수 있다. 가장 일반적인 용도는 중개 테이블에 추가 데이터를 사용해 다대다 관계로 연결하려는 경우에 사용한다. 
* 우선 ManyToManyField 는 존재하는 의사이름, 환자 이름만 사용할 수 있다. 따라서 아래에서 진행하는 방법을 통해 병명, 예약일 등의 추가 사항을 필드로 넣을 수 있다. 

<br>

### 2. ManyToManyField

> 다대다(M:N) 관계 설정 시 사용하는 모델 필드
>
> 하나의 필수 위치 인자(M:N 관계로 설정할 모델 클래스)가 필요하다.
>
> 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 만들 수 있다. 
>
> * add(), remove(), create(), clear() ...
>
> [참고] RelatedManager
>
> * 일대다 또는 다대다 관련 컨텍스트에서 사용되는 manager

1. ManyToManyField's **Arguments**
   1. **related_name**
      * target model이 source model을 참조할 때(역참조) 사용할 manager의 이름을 설정한다. ForeignKey의 related_name과 동일하다. 
   2. **through**
      * 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정할 수 있다. 
      * 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우 (extra data with a many-to-many relationship)에 주로 사용됨
   3. **symmetrical**
      * MTMF가 동일한 모델(on self)을 가리키는 정의에서만 사용한다. 
      * symmetrical=True(기본값)일 경우 Django는 person_set 매니저를 추가하지 않는다.
      * source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면, target 모델 인스턴스도 source 모델 인스턴스를 작동으로 참조하도록 한다. (즉, 내가 당신의 친구라면 당신도 내 친구가 되는 것이다.)
      * 대칭을 원하지 않는 경우 False로 설정 한다. 
      * Follow 기능 구현에서 다시 확인할 수있다. 

2. **Rlated Manager**

   * 1:N 또는 M:N 관련 컨텍스트에서 사용되는 매니저 이다.

   1. **add()**
      * 지정된 객체를 관련 객체 집합에 추가한다
      * 이미 존재하는 관계에서 사용하면 관계가 복제되지 않는다. 
      * 모델 인스턴스, 필드 값(PK)을 인자로 허용한다. 
   2. **remove()**
      * 관련 객체 집합에서 지정된 모델 객체를 제거한다.
      * 내부적으로 QuerySet.delete()를 사용하여 관계가 삭제된다.
      * 모델 인스턴스, 필드 값(PK)을 인자로 허용한다. 

3. :red_circle: **through** 사용하기!!

   * 모델 관계 설정하기

   ```python
   from django.db import models
   
   
   class Doctor(models.Model):
       name = models.TextField()
   
       def __str__(self):
           return f'{self.pk}번 의사 {self.name}'
   
   
   class Patient(models.Model):
       doctors = models.ManyToManyField(Doctor, through='Reservation')
       name = models.TextField()
   
       def __str__(self):
           return f'{self.pk}번 환자 {self.name}'
   
   
   class Reservation(models.Model):
       doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
       patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
       symptom = models.TextField()
       reserved_at = models.DateTimeField(auto_now_add=True)
   
       def __str__(self):
           return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
   ```

   ```shell
   # 데이터 베이스 초기화/ 마이그레이션 진행
   $ python manage.py makemingrations
   $ python manage.py migrate
   
   $ python manage.py shell_plus  # shell_plus 진행
   ```

   ![image-20220418111448157](0418_DB3(Live).assets/image-20220418111448157.png)

   ```shell
   doctor1 = Doctor.objects.create(name='justin')
   patient1 = Patient.objects.create(name='tony')
   patient2 = Patient.objects.create(name='harry')
   ```

   ```shell
   # 예약 생성 - 1 (의사가 예약하는 경우)
   reservation1 = Reservation(doctor=doctor1, patient=atient1, symptom='headache')
   reservation1.save()
   
   doctor1.patient_set.all()
   <QuerySet [<Patient:1번 환자 tony>]>
   
   patient1.doctors.all()
   <QuerySet [<Doctor:1번 의자 justin>]>
   ```

   ![image-20220418111932798](0418_DB3(Live).assets/image-20220418111932798.png)

   ```shell
   # 예약 생성 - 2 (환자가 예약하는 경우)
   patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})
   doctor1.patient_set.all()
   
   patient2.doctors.all()
   
   # 예약 삭제 
   doctor1.patient_set.remove(patient1)
   patient2.doctors.remove(doctor1)
   ```

   ![image-20220418112116088](0418_DB3(Live).assets/image-20220418112116088.png)

> [데이터베이스에서의 표현]
>
> Django는 다대다 관계를 나타내는 중개 테이블을 만듦
>
> 테이블 이름은 다대다 이름의 이름과 이를 포함하는 모델의 테이블 이름을 조합하여 생성된다. 
>
> <br>
>
> [중개 테이블의 필드 생성 규칙]
>
> 1. source model 및 target model 모델이 다른 경우
>    * id
>    * <containing_model>_id
>    * <other_model>_id
> 2. ManyToManyField가 동일한 모델을 가리키는 경우 
>    * id
>    * from _ <model> _ id
>    * to _ <model> _ id

<br>

#### 1. 좋아요 기능 (Like)

1. **Like 구현**

   ```python
   # articles/models.py
   
   class Article(models.Model):
       user = models.ForiegnKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
       like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
       ...
   ```

   ```bash
   $ python manage.py makemigrations
   ```

   :small_red_triangle: 에러가 발생하는데 like_users 필드 생성시 자동으로 역참조는 .article_set 매니저를 생성한다. 그러나 이전 1:N(User:Article)관계에서 이미 해당 매니저 이름을 사용 중이기 때문이다. 이를 위해 related_name이 필요하다. 

   ```python
   # articles/models.py
   
   class Article(models.Model):
       user = models.ForiegnKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
       like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
       ...
   ```

   ```bash
   $ python manage.py makemigrations
   $ python manage.py migrate
   ```

   ![image-20220418112840530](0418_DB3(Live).assets/image-20220418112840530.png)

   :star: 현재 User - Article 간 사용 가능한 DB API

   > 1. article.user (참조 : article 모델 안에 user가 있으므로)
   >    * 게시글을 작성한 유저 - 1: N
   >
   > 2. article.like_user (참조 : artucke 모델 안에 like_user가 있으므로)
   >    * 게시글을 좋아요한 유저 - M:N
   > 3. user.article_set (역참조)
   >    * 유저가 작성한 게시글(역참조) - 1:N
   > 4. userk.like_articles (역참조)
   >    * 유저가 좋아요한 게시글(역참조) - M:N

   ```python
   # articles/urls.py
   
   urlpattenrs = [
       ...
       path('<int:article_pk>/likes/', views.likes, name='likes'),
   ]
   ```

   ```python
   # articles/views.py
   
   @require_POST
   def likes(request, article_pk):
       if request.user.is_authenticated:  # 로그인 된 사용자라면?
           article = get_object_or_404(Article, pk=article_pk)
           
           # 좋아요 취소(좋아요 목록에 있는데, 좋아요를 한번 더 눌렀다면 좋아요 취소)
           if article.like_users.filter(pk=request.user.pk).exists():
               article.like_users.remove(request.user)
           # 좋아요 
           else:
               article.like_users.add(request.user)
           return redirect('articles:index')
       return redirect('accounts:login')
   ```

   * `exists()`

     QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환한다. 

     특히 규모가 큰 QuerySet의 컨텍스트에서 특정 개체 존재 여부와 관련된 검색에 유용하다.

     고유한 필드(예:PK)가 있는 모델이 QuerySet의 구성원인지 여부를 찾는 가장 효율적인 방법이다.

   ```django
   <!-- articles/index.html -->
   
   
   ...
   <div>
     <form action='{% url 'articles:likes' article.pk %}' method="POST">
       {% csrf_token %}
       {% if user in article.like_users.all %} 
         <input type='submit' value="좋아요 취소">
       {% else %}
         <input type='submit' value="좋아요">
       {% endif %} 
     </form>      
   </div>
   ```

   ![image-20220418142205906](0418_DB3(Live).assets/image-20220418142205906.png)

   :small_red_triangle: 좋아요 버튼 클릭 후 테이블을 확인한다.  

#### 2. Profile Page

> 자연스러운 follow 흐름을 위한 회원 프로필 페이지 작성하기

```python
# accounts/urls.py

urlpattenrs = [
    ...
    path('<username>/', views.profile, name='profile'),
    ...
]
```

```python
# accounts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from dhabgi,dibtrub.auth import get_user_model

def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

```django
<!-- accounts/profile.html -->

{% extends 'base.html' %}

{% block content %}
<h1>{{ person.username }}님의 프로필</h1>

<hr>

<h2>{{ persen.username }}'s 게시글</h2>
{% for comment in person.comment_set.all %}
  <div>{{ comment.title }}</div>
{% endfor %}

<hr>

<h2>{{per.username }}'s 댓글</h2>
{% for comment in person.comment_set.all %}
  <div>{{ comment.content }}</div>
{% endfor %}

<hr>

<h2>{{per.username }}'s 좋아요한 게시글</h2>
{% for article in person.like_articles.all %}
  <div>{{ article.title }}</div>
{% endfor %}

<hr>

<a href='{% url 'articles:index' %}'>back</a>
{% endblock %}
```

```django
<!-- base.html -->

<body>
  <div class='container'>
    {% if request.user.is_authenticated %}
      <h3>Hello, {{ user }}</h3>
      <a href="{% url 'accounts:profile' user.username %}">내 프로필</a>
      ...
  </div>
  ...
</body>
```

```django
<!-- articles/index.html -->

<p>
  <b>작성자 : <a href='{% url 'accounts:profile' article.user.username %}'>{{ article.user }}</a></b>
</p>
```

#### 3. 팔로우 기능(Follow)

* ManyToManyField 작성 후 마이그레이션

```python
# accounts/models.py

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')  # symmetrical=False로 둔 이유는 팔로우하면 자동으로 맞팔로우를 만들지 않기 위해
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

![image-20220418151020796](0418_DB3(Live).assets/image-20220418151020796.png)

```python
# accounts/urls.py

urlpattenrs = [
    ...,
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```

```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
    if request.user.is_auenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        if person != request.user:  # 내가 아닌 다른 사람의 일때만
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                persom.followers.add(request.user)
        return redirect('accounts:profile', person.username)  # 나라면?
    return redirect('accounts:login')
```

```django
<!-- accounts/profile.html -->
<!-- profile 페이지에 팔로우와 언팔로우 버튼 작성
1. 팔로잉 수/팔로워 수 출력
2. 자기 자신을 팔로우 할 수 없음 -->

{% extends 'base.html' %}

{% block content %}
<h1>{{ person.username }}님의 프로필</h1>

<div>
  <div>
    팔로잉 : {{ person.followerings.all|length }} / 팔로워 : {{ person.followers.all|length }}    
  </div>
  {% if user != person %}
    <div>
      <form action='{% url 'accounts:follow' person.pk %}' method='POST'>
        {% csrf_token %}
        {% if user in person.followers.all %}
          <input type='submit' value='Unfollow'>
        {% else %}
          <input type='submit' value='Follow'>
        {% endif %}
      </form>
    </div>
  {% endif %}
</div>
<hr>
<!-- with 사용 할 수도 있음. --> 

<h2>{{ persen.username }}'s 게시글</h2>
{% for comment in person.comment_ser.all %}
  <div>{{ comment.title }}</div>
{% endfor %}

<hr>

<h2>{{per.username }}'s 댓글</h2>
{% for comment in person.comment_ser.all %}
  <div>{{ comment.content }}</div>
{% endfor %}

<hr>

<h2>{{per.username }}'s 좋아요한 게시글</h2>
{% for article in person.like_articles.all %}
  <div>{{ article.title }}</div>
{% endfor %}

<hr>

<a href='{% url 'articles:index' %}'>back</a>
{% endblock %}
```

![image-20220418151957951](0418_DB3(Live).assets/image-20220418151957951.png)



<br>

