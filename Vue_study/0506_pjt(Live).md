# 05.06

## pjt

[TOC]

> [준비사항]
>
> 1. migrate 진행
>
> 2. fixtures 진행
>
>    * 모델 별로 dumpdata 실행
>
>      ```bash
>      $ python manage.py dumpdata --indent 4 articles.articles > articles.json
>      $ python manage.py dumpdata --indent 4 articles.comments > comments.json
>      $ python manage.py dumpdata --indent 4 articles.users > users.json
>      ```
>
>    * 클론 받은 B가 해야하는 일 load
>
>      ```bash
>      $ python manage.py migrate
>      # fixture 폴더 안에 appname과 동일한 폴더를 만들고 안에 .json 넘길 때 
>      $ python manage.py loaddata articles/articles.json comments/comments.json users/users.json
>      ```
>
> 3. ERD 공부하기

<br>

### 1. 프로젝트 소개

* 알고리즘을 적용한 서버 구성

### 2. Social Login 

> 1. django allauth
>
> 2. google login

1. allauth 설치

   ```bash
   $ pip install django-allauth
   ```

   ```python
   # settings.py
   
   INSTALLED_APPS = [
       ...,
       'django.contrib.sites',
       ...,
       'allauth',
       'allauthaccount',
       'allauth.socialaccount',
       ...,
       'allauth.socialaccount.providers.google',
   ]
   
   AUTHENTICATION_BACKENDS = [
       ...,
   ]
   
   # djcnao.contrib.sites 사용시 반드시 SITE_ID 설정 필요
   SITE_ID = 1
   
   # social login 바로 넘어가기
   SOCIALACCOUNT_LOGIN_FORMS = TRUE
   ```

   ```python
   # urls.py
   
   ...
   path('accounts/', include('allauth.url')),
   ...
   ```

   ```django
   <!-- login.html -->
   
   {% load socialaccount %}
   
   <div>
     <a href="{% provider_login_url 'google'next=/community/ %}">구글 로그인하러가기</a>
   </div>
   ```

   ```bash
   $ python manage.py migrate
   ```

   * oauth2 검색 

### 3. Paginator

> * bootstrap paginator

```python
from .models import Movie
from django.core.paginator import Paginator

def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context ={
        'movies':page_obj,
    }
    return renders(request, 'movies/index.html', context)
```

```django
<!-- index.html -->

<h1>Movie</h1>

<div>
    {% for movie in movies %}
    <div>
        <h2>{{movie.title}}</h2>
        <p>{{movie.overview}}</p>
        <a href='{% url 'movies:detail' movie.pk %}'>[detail]</a>
    </div>
    {% endfor %}
</div>
<div class="pagination">
    <span class="step-links">
        {% if movies.has_previous %}
            <a href="?page=1">&laquo; first</a>
            <a href="?page={{ movies.previous_page_number }}">previous</a>
        {% endif %}

        <span class="current">
            Page {{ movies.number }} of {{ movies.paginator.num_pages }}.
        </span>

        {% if movies.has_next %}
            <a href="?page={{ movies.next_page_number }}">next</a>
            <a href="?page={{ movies.paginator.num_pages }}">last &raquo;</a>
        {% endif %}
    </span>

</div>
```

* bootstrap pagination 사용[추천]

  ```bash
  $ pip install django-bootstrap-v5
  ```

  ```python
  # settgings.py
  
  INSTALLED_ = [
      ...,
      'bootstrap5',
      ...,
  ]
  
  ```

  ```django
  <!-- index.html -->
  {% extents 'base.html' %}
  
  {% block content %}
  {% load bootstrap5 %}
  <h1>Movie</h1>
  
  <div>
      {% for movie in movies %}
      <div>
          <h2>{{movie.title}}</h2>
          <p>{{movie.overview}}</p>
          <a href='{% url 'movies:detail' movie.pk %}'>[detail]</a>
      </div>
      {% endfor %}
  </div>
  
  <div class='d-flex justify-content-center'>
      {% bootstrap_pageination_movies %}
  </div>
  
  {% endblock %}
  ```

### 4. Installed scroll

```django
{% extents 'base.html' %}
{% block content %}
{% load bootstrap5 %}
<h1>Movie</h1>

<div>
    {% for movie in movies %}
    <div>
        <h2>{{movie.title}}</h2>
        <p>{{movie.overview}}</p>
        <a href='{% url 'movies:detail' movie.pk %}'>[detail]</a>
    </div>
    {% endfor %}
</div>
{% comment %}
1. 스크롤이 바닥에 도달 했을 때, : document / event
2. 추가 데이터 10개를 불러옴(AJAX) : axios
3. 응답 json 데이터 10개를 화면에 붙임 : DRF
{% endcomment %}
</div>
{% endblock %}
```

```bash
$ pip install djangorestframework
```

```python
# settings.py

'rest_framework',
```

```django
<!-- base.html -->

<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

```

```django
{% extents 'base.html' %}
{% block content %}
{% load bootstrap5 %}
<h1>Movie</h1>

<div id='movieList'>
    {% for movie in movies %}
    <div class='movie'>
        <h2>{{movie.title}}</h2>
        <p>{{movie.overview}}</p>
        <a href='{% url 'movies:detail' movie.pk %}'>[detail]</a>
    </div>
    {% endfor %}
    
    <!-- 여기에 JSON 내용을 담은 Element append -->
    
</div>
{% endblock %}

{% comment %}
1. 스크롤이 바닥에 도달 했을 때, : document / event
2. 추가 데이터 10개를 불러옴(AJAX) : axios
3. 응답 json 데이터 10개를 화면에 붙임 : DRF
{% endcomment %}
{% block script %}
<script>
    let page = 2
    const movieList = document.querySelector('#movieList')
	dovument.addEventListener('scroll', function(event){
    const {scrollTop, clientHeight, scrollHeight} = document.documentElement
    // 완전 바닥에 도달하는 코드
    if (element.scrollHeight - element.scrollTop === element.clientHeight){
        console.log('바닥이야!')
    }
    if (scrollHeight + clientHeight >= scrollHeight - 5){
        console.log('바닥이야!')
        axios({
            mothod : 'get',
            url:'movies/ajax/?page=${page}'
        })
        	.then(res => {
            	// console.log(res.data)
            	const movies = res.data
                movies.forEach(movie => {
                    // movie.title, movie.overview
                    const div = document.createElement('div')
                    const h2 = document.createElement('h2')
                    h2.innerText = movie.title
                    const p = document.createElement('p')
                    p.innerText = movie.overview
                    const a = document.createElement('a')
                    a.innerText = '[DETAIL]'
                    a.href = '/movies/${movie.id}'
                    const hr = document.createElement('hr')
                    
                    div.append(h2, p, a, hr)
                    movieList.appendChild(div)
                })
            	page ++
        })
        	.catch(err => console.log(error(err)))
    }
    
    
})
</script>



{% endblock script %}
```

* movies에 serializers.py 만들기

  ```python
  from rest_framework import serializers
  from .models import Movie
  
  class MovieSerializer():
  
  	class Meta:
          model = Movie
          fields = '__all__'
  ```

  ```python
  # urls.py
      
  path('ajax/', view.ajax, name='ajax'),
  ```

  ```python
  from .models import Movie
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  
  def index(request):  # 엔터치고 들어온다면? HTML
      movies = Movie.objects.all()
      paginator = Paginator(movies, 10)
      
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
      
      context ={
          'movies':page_obj,
      }
      return renders(request, 'movies/index.html', context)
  
  @api_view(['GET'])
  def ajax_index(request):  # json파일
      movies = Movie.objects.all()
      paginator = Paginator(movies, 10)
      
      page_number = request.GET.get('page')
      # querySet
      page_obj = paginator.get_page(page_number)
      
      serialixer = MovieSerializer(page_obj, many=True)
      return Response(serializer.data)
      
  ```

  ```django
  {% extents 'base.html' %}
  {% block content %}
  {% load bootstrap5 %}
  <h1>Movie</h1>
  
  <div id='movieList'>
      {% for movie in movies %}
      <div class='movie'>
          <h2>{{movie.title}}</h2>
          <p>{{movie.overview}}</p>
          <a href='{% url 'movies:detail' movie.pk %}'>[detail]</a>
      </div>
      {% endfor %}
      
      <!-- 여기에 JSON 내용을 담은 Element append -->
      
  </div>
  {% endblock %}
  
  {% comment %}
  1. 스크롤이 바닥에 도달 했을 때, : document / event
  2. 추가 데이터 10개를 불러옴(AJAX) : axios
  3. 응답 json 데이터 10개를 화면에 붙임 : DRF
  {% endcomment %}
  {% block script %}
  <script>
      let page = 2
      const movieList = document.querySelector('#movieList')
  	dovument.addEventListener('scroll', function(event){
      const {scrollTop, clientHeight, scrollHeight} = document.documentElement
      // 완전 바닥에 도달하는 코드
      if (element.scrollHeight - element.scrollTop === element.clientHeight){
          console.log('바닥이야!')
      }
      if (scrollHeight + clientHeight >= scrollHeight - 5){
          console.log('바닥이야!')
          axios({
              mothod : 'get',
              url:'movies/ajax/?page=${page}'
          })
          	.then(res => {
              	// console.log(res.data)
              	const movies = res.data
                  movies.forEach(movie => {
                      // movie.title, movie.overview
                      const div = document.createElement('div')
                      const h2 = document.createElement('h2')
                      h2.innerText = movie.title
                      const p = document.createElement('p')
                      p.innerText = movie.overview
                      const a = document.createElement('a')
                      a.innerText = '[DETAIL]'
                      a.href = '/movies/${movie.id}'
                      const hr = document.createElement('hr')
                      
                      div.append(h2, p, a, hr)
                      movieList.appendChild(div)
                  })
              	page ++
          })
          	.catch(err => console.log(error(err)))
      }
      
      
  })
  </script>
  
  
  
  {% endblock script %}
  ```

  
