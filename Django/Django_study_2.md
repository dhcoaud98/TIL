# 03.09

## Django Model

<br>

[TOC]

<br>

### Model

"웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구이다."

1. models.py 

   클래스 함수를 작성할 수 있는 곳으로 이 곳에서 'title', 'content' 등의 행 제목을 가진 테이블을 생성시킬 수 있다.  테이블 생성 후 데이터는 `views.py`에서 작성할 수 있다. 

   ```python
   # articles/models.py
   
   class Article(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField() 
       created_at = models.DateTimeField(auto_now_add = True)
       updated_at = models.DateTimeField(auto_now = True)
   ```

2. 데이터베이스(DB) : 체계화된 데이터의 모임.

3. 퀴리(Query) : 데이터를 조회하기 위한 명령어. 조건에 맞는 데이터를 추출하거나 조작하는 명령어로 `Query를 날린다 == DB를 조작한다. `라는 의미이다. 

4. **Database의 기본구조**

   1) 스키마: structure, 데이터베이스에서 자료의구조, 표현방법, 관계 등을 정의한 구조

      :star: (jupyter Notebook에서 보여지는 흰색, 회색의 테이블이라고 생각하면 된다. 다음과 같은 구조로 이루어져 있다. 

      | column | datatype |
      | :----: | :------: |
      |   id   |   INT    |
      |  age   |   INT    |
      | phone  |   TEXT   |
      |  ...   |   ...    |

   2) 테이블: 열(필드field, 속성)과 행(레코드record, 튜플)로 이루어진다. SQL 데이터베이스에서는 테이블을 관계라고도 한다. 행의 갯수는 맨 위의 제목칸을 제외하고 나머지를 세어야 한다. 

   3) PK(기본키) : 행의 고유값으로 반드시 설정해야한다. id와 비슷하게 접근하면 된다.

<br>

### ORM

Object-Relational-Mapping

:small_red_triangle: **Django와 SQL** 간에 데이터를 변환하는 프로그래밍 기술이다. `Django`는 `python`을 `DB`는 `SQL`언어를 사용하기 때문에 언어가 호환되지 않는다. 이를 위해 내장 Django ORM을 사용한다. 

* 장점 : SQL언어를 알지 못해도 DB 조작이 가능하다. 절차적인 SQL을 객체 지향적인 python으로 생산성을 높인다.

* 단점 : ORM만을 사용해 완전하게 구현하기 어렵다.

  ```html
  "현대 웹 프레임 워크는 개발 속도를 높이는 것!!"
  
  DB를 객체로써 조작하기 위해 ORM을 이용하는 것이다. 
  ```

1. models.py 작성

   ```python
   # articles/models.py
   
   class Article(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField() 
       created_at = models.DateTimeField(auto_now_add = True)
       updated_at = models.DateTimeField(auto_now = True)
   ```

   * title과 content는 모델의 필드를나타낸다.  
   * 클래스를 하나의 모델로 생각하면 각각의 모델은 `django.models.Model` 클래스의 서브 클래스이다. `django.db.models` 모듈의 Modul 클래스를 상속 받는다.
   * `CharField(max_length=10)` 에서 `max_length`는 필수 인자이다. 테이터베이스 레벨과 Django의 유호성 검사(값을 검증하는 것)에서 활용
   * `TextField()` 글자수가 많을 때 사용한다. 
   * `auto_now_add` : 최초 생성일자
   * `auto_now` : 최종 수정일자

   :red_circle: 소문자, 대문자 구분 잘 하지 않으면 오류 날 수 있음!!

<br>

### Migrations

"Django가 model에 생긴 변화를 반영하는 방법"

다음과 같이 네가지 명령어를사용하면 된다. 

1. **makemigrations** : model에 변경사항이 생기면 항상 명령어를 입력해야한다. **설계도**를 만들때 사용한다.
2. **migrate** : 마이글이션(migration)을 DB에 반영하기 위해 사용한다. 설계도를 실제로 DB에 반영하는 과정이다. 
3. **sqlmigrate **:마이그레이션에 대한 SQL구문을 보기 위해 사용한다.
4. **showmigrations** : 마이그레이션 파일들이 migrate 됐는지 안됐는지 여부를 확인 할 수 있음

```bash
$ python manage.py makemigrations 
# 'migrations/0001_initial.py' 생성 확인

$ python manage.py migrate
# 0001_initial.py 설계도를 실제 DB에 반영

$ python manage.py sqlmigrate app_name 0001
# 해당 migrations 설계도가 SQL 문으로 어떻게 해석되어서 동작할지 미리 확인 할 수 있음

$ python manage.py showmigrations
# migrations 설계도들이 migrate 됐는지 안됐는지 여부를 확인 할 수 있음
```

<br>

### Database API

"django에서 DB를 조작하기 위한 도구이다."

```python
Article.objects.all()
<Queryset[]>

# 전체 데이터를 조회(DB에 인스턴스 객체를 얻기 위한 쿼리문 날리기)
```

* Article : 클래스 네임 (보통 앱 네임을 단수로 쓴다.)
* objects : manager
* all() : QuerySet API (Query는 DB로부터 전달받은 객체 목록이다.)

1. **Django shell** (실제 프로젝트 진행에서는 보통 사용하지 않고, 확인용으로 사용한다.)

   일반 python shell을 통해서는 장고 프로젝트 환경에 접근할 수 없기 때문에 Python shell을 활용해 DB API 구문 테스트를 진행한다.

   ```bash
   $ pip install ipython
   $ pip install django-extensions
   ```

   설치 후 라이브러리 등록 및 실행

   ```python
   # settings.py
   
   INSTALLED_APPS = [
       ...,
       'django_extentions',
       ...,
   ]
   ```

   ```bash
   $ python manage.py shell_plus
   ```

<br>

### CRUD

#### Create(생성)

데이터를 생성하는 방법에는 3가지가 있다. 

1. ```python
   article = Article()
   # Arricle이라는 클래스로부터 article이라는 인스턴스 생성
   
   article.title = 'first'
   article.content = 'django!'
   article.save()
   ```

2. ```python
   article = Article(title='second', content='django!!')
   article.save()
   ```

3. ```python
   Article.objects.create(title='third', content='django!!!')
   ```

   다음과 같은 테이블이 만들어진다. 주로 2번을 사용할 것을 권장한다. 1과 2는 단순히 인스턴스 생성을 하는 것이고, 이는 DB에 영향을 미치지 않기 때문에 반드시 save()해주어야 한다. 

   |  #   |  id  | title  |  content  | created_at | updated_at |
   | :--: | :--: | :----: | :-------: | :--------: | :--------: |
   |  1   |  1   | first  |  django!  |    ...     |    ...     |
   |  2   |  2   | second | django!!  |    ...     |    ...     |
   |  3   |  3   | third  | django!!! |    ...     |    ...     |

<br>

#### Read(읽기)

1. all() : 현재 QuerySet의 복사본을 반환

   ```python
   Arricle.objects.all()
   ```

2. get()

   ```python
   article = Article.objects.get(pk=100)
   # pk=100인 행의 데이터를 가져옴
   # 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생 시킴
   # pk와 같이 고유성을 보장하는 조회에서만 사용해야 함
   ```

3. filter()

   ```python
   Article.objects.filter(content='django!')
   <QuerySet [<Article: first>]>
   
   Article.objects.filter(title='second')
   <QuerySet [<Article: second>]>
   ```

:small_red_triangle_down: **Field lookup** :small_red_triangle_down:

​	위의 메서드에 대한 키워드 인수로서 `__`를 이용한다. 

```python
Article.objects.filter(pk__gt=2)
```

<br>

#### Update(갱신)

업데이트를 위해서는 `1. 조회 / 2. 변경 / 3. 저장` 단계를 지켜야 한다.

```python
1. 조회
article = Article.objects.get(pk=1)
article.title

2. 변경
article.title = 'byebye'

3. 저장
article.save()
```

<br>

#### Delete(삭제)

QuerySet의 모든 행에 대해 SQL 삭체 쿼리를 수행하고 반환

```python
article.delete()
```



---

위의 모든 과정은 `models.py`에서 테이블을 생성하고, `articles/views.py`에 함수로써 작성할 수 있다. 

1. ```python
   # articles/models.py
   
   class Article(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField() 
       created_at = models.DateTimeField(auto_now_add = True)
       updated_at = models.DateTimeField(auto_now = True)
   ```

2. ```python
   # articles/views.py
   
   from .models import Article
   
   def index(request):
       article = Article.objects.all()
       context = {
           'articles': articles,
       }
       return render(request, 'articles/index.html', context)
   ```

3. 어플리케이션 마다 `urls.py`를 생성하여 사용하기 위해서 해야하는 일!

   :red_circle: project의 `urls.py`에 다음과 같이 작성한다.

   ```python
   from django.urls import path, include
   
   urlpattern = [
       ...,
       path('articles/', include('articles.urls')),
   ]
