# 03.11

## Django Model

<br>

[TOC]

<br>

### 기본 세팅

1. `pjt05` 폴더 생성

2. `.gitignore.py` 파일 생성 : git에 push 할때 빼고 올릴 list 작성

3. 주어진 `requirements.txt`파일이 있다면 다음 명령어로 설치

   ```bash
   $ pip install -r requirements.txt
   ```

4. 가상환경 설치 후 실행

5. `vscode` 열기

6. 프로젝트, 어플리케이션 생성

7. `base.html` 만들고, 설정하기

8. 어플리케이션 `urls.py` 만들기 

   ```python
   # app_name/urls.py
   
   from django.urls import path
   from . import views
   
   app_name = 'movies'
   urlpatterns = [
       ...
   ]
   ```

9. `model`을 만들기 위해 `views.py`에 `import` 할 것

   ```python
   from django.shortcuts import render, redirect
   from .models import Movie
   ```


* `live-lecture`의 `django-model 참고하기`

<br>

### model 만들기

1. `models.py`에 새로운 클래스 생성하기

   ```python
   from django.db import models
   
   # Create your models here.
   class Movie(models.Model):
       title = models.CharField(max_length=20)
       audience = models.IntegerField()
       release_date = models.DateField()
       genre = models.CharField(max_length=30)
       score = models.FloatField()
       poster_url = models.TextField()
       description = models.TextField()
   
       def __str__(self):
         return self.title
   ```

   숫자, 문자, 날짜 등에 맞는 메서드를 사용해 필드를 생성해 준다. 그 후에 model에 생긴 변화를 반영하기 위해서 다음의 코드를 작성해주어야 한다.

   ```bash
   $ python manage.py makemigrations
   ```

   ```bash
   $ python manage.py migrate
   ```

<br>

### server 만들기

| 순서 |                  방법                  |
| :--: | :------------------------------------: |
|  1   |         `movies/urls.py` 작성          |
|  2   |         `movies/views.py` 작성         |
|  3   | `movies/templates/movies/__.html `작성 |
|  4   |         `runserver` 하여 확인          |

1. `urls.py` 작성하기

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'movies'
   urlpatterns = [
       path('', views.index, name='index'),
       path('new/', views.new, name='new'),
       path('create/', views.create, name='create'),
       path('<int:pk>/', views.detail, name='detail'),
       path('<int:pk>/edit/', views.edit, name='edit'),
       path('<int:pk>/update/', views.update, name='update'),
       path('<int:pk>/delete/', views.delete, name='delete'),
   ]
   ```

   `URL namespace`를 사용해서 여러개의 어플리케이션이 생성되었을 경우 혼동을 방지 할 수 있다. 어플리케이션 별로 `templates/{app_name}/`을 따로 만들어 주어야 한다. 

   `<int:px>`는 주소창을 통해 사용자가 원하는 값을 얻을 수 있도록 한다. 

2. `views.py` 작성하기

   ```python
   from django.shortcuts import render, redirect
   from .models import Movie
   
   # 1. index.html작성 전 함수 만들기
   def index(request):
       movies = Movie.objects.all()
       context = {
           'movies' : movies,
       }
       return render(request, 'movies/index.html', context)
   
   # 2. new.html작성 전 함수 만들기
   def new(request):
       return render(request, 'movies/new.html')
   
   # 3. create 함수는 return 값이 index.html이기 때문에 create.html을 작성해주지 않아도 된다.
   def create(request):
       title = request.POST.get('title')
       audience = request.POST.get('audience')
       release_date = request.POST.get('release_date')
       genre = request.POST.get('genre')
       score = request.POST.get('score')
   
       movie = Movie(title=title, audience=audience, release_date=release_date, genre=genre, score=score)
       movie.save()
   
       context = {
           'title':title, 
           'audience':audience, 
           'release_date':release_date, 
           'genre':genre, 
           'score':score,
       }
       return redirect('movies:detail', movie.pk)
   ```

   :red_circle: `redirect` 는 현재 변경사항도 포함하여 페이지를 열때 사용하는 함수라고 할 수 있다. 

3. `__.html` 작성하기

   ```html
   1. base.html 상속 받기
   2. block 만들기
   3. 부트 스트랩과 함수를 사용해 작성하기
   ```

   

   
