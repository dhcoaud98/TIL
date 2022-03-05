# 03.05

## Django

<br>

### Django 시작하기

1. 새로운 폴더 생성

2. 가상환경 활성화 

   ```bash
   $ python -m venv venv
   $ source venv/Scripts/activate
   ```

   :seedling: 가상환경을 한번 끄고 난 후 다시 사용하기 위해선 반드시 활성화 작업을 해주어야 한다. 

3. Django 설치해주기

   ```bash
   $ pip install
   $ pip install django==3.2.12
   $ pip list
   ```

   :seedling: `$ pip list` 작업은 시작할 때 꼭 확인해 주는 것이 좋다. 로컬 환경에서 시작하지 않도록 해준다. 

4. Project 생성

   ```bash
   $ django-admin startproject <프로젝트 명> .
   $ python manage.py runserver
   ```

   :seedling: 프로젝트 명 뒤에 한칸 띄어쓰기 후 `.`을 꼭 써주어야 한다. 

5. Application 생성

   ```bash
   $ python manage.py startapp <articles>
   ```

   :seedling: 하나의 프로젝트는 여러개의 앱을 가질 수 있다. 

6. Application 등록

   반드시 app 생성 후에 등록하기!! 등록은 project의 `settings.py`에서 할 수 있다. 

   ```python
   INSTALLED_APPS = [
   	'articles',
       ...,
   ]
   ```

   * 

<br>

### Django의 구조

| MTV          | 설명                                                         |
| ------------ | ------------------------------------------------------------ |
| **model**    | 응용프로그램의 데이터 구조를 정의하고 데이터 베이스의 기록을 관리(추가, 수정, 삭제) |
| **template** | 파일의 구조나 레이아웃 정의, `.html`이 모여있는 곳           |
| **view**     | 함수를 작성하는 곳으로 HTTP 요청을 수신하고 HTTP 응답을 반환(이 곳에서 response 와 requests를 사용함.) |

<br>

### Django에서 요청과 응답 사용하기

1. urls.py

   새롭게 만들어진 Application을 등록하고, 서버에서 요청이 들어오면 관련된 함수(view)로 넘겨준다. 

   ```python
   from articles import views
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('index/', views.index),
   ]
   ```

   :red_circle: 동적 라우팅(variable routing) : 주소창에서 직접 검색을 통해 주소를 만드는 것이다. 

   * 다음과 같은 순서로 작성할 수 있다. `views.py`함수에서 인자를 `request`와 `name(사용자에 따라 다르게)`으로 하나더 넘겨주어야 한다. 

     ```python
     # urls.py
     
     from articles import views
     
     urlpatterns = [
         ...,
         path('hello/<str:name>/', views.hello), 
     ]
     ```

     ```python
     # views.py
     
     def hello(request, name):
         context = {
             'name': name,
         }
         return render(request, 'hello.html', context)
     ```

     ```django
     <!-- hello.html -->
     
     {% extends 'base.html' %}
     
     {% block content %}
       <h1>안녕 {{ name }}!</h1>
     {% endblock %}
     ```

2. views.py

   이 곳에서는 서버로 요청보내고 받은 정보를 함수로 작성하는 곳이다. 

   ```python
   def index(request):
       return render(request, 'index.html')
   ```

3. templates

   views.py에서 넘어온 `index.html`을 작성해주는 곳이다. 

<br>

### DTL(Django template language)

template의 `.html`파일에서 작성할 수 있다. 

1. variables

   ```django
   {{ variables }}
   {{ movies.title }}
   ```

2. filters

   ```django
   {{ variable|filter }}
   ```

3. Tags

   ```django
   {% tag %}
   ```

4. comment

   ```django
   {# comment #}
   ```

<br>

### Template inheritance(상속)

1. 파일의 최상단에 `templates`를 생성하고, 그 안에 `base.html`작성

2. project의 `settings.py` 에 반드시 등록 해주어야 상속 템플릿을 사용할 수 있다. 

   ```python
   TEMPLATES = [
       {
           ...,
           'DIRS': [BASE_DIR / 'firstpjt' / 'templates'],
   ...
   ]
   ```

3. 자식 템플릿으로 사용되는 템플릿의 **최상단** 에 연결해주기 (주로 네비게이션 바, 푸터 등 화면을 옮겨도 바뀌지 않는 속성들을 작성)

   ```django
   {% extends 'base.html' %}
   ```

4. 부모 템플릿에서 지정한 요소들 이외에 작성해주고 싶은 것이 있을 경우(overriden)

   ```django
   (1) 부모 템플릿에서 작성해주어야 하는 것
   
   {% block content %}
   {% endblock content %}
   
   (2) 자식 템플릿에서 작성해주어야 하는 것
    
   {% block content %}
   - 이 안에 코드를 작성 - 
   {% endblock content %}
   ```

<br>

### HTML Form





<br>

<br>

<hr>

### 중요사항!!

* 두번째 app을 생성하고 등록 하려면?

  **App URL mapping**

  ```bash
  $ python manage.py startapp app2
  ```

  ```python
  INSTALLED_APPS = [
  	'articles',
      'app2',
      ...,
  ]
  ```

  :small_red_triangle_down:앱이 2개 이상이라면 각각의 앱 안에 **urls.py**를 만들어서 사용할 수 있다. 

  ```python
  # articles/urls.py
  
  from django.urls import path
  from . import views  # 본인의 경로라는 의미에서 .을 사용한다.
  
  
  urlpatterns = [
      path('index/', views.index),
      path('greeting/', views.greeting),
      path('dinner/', views.dinner),
      path('throw/', views.throw),
      path('catch/', views.catch),
      path('hello/<str:name>/', views.hello),
  ]
  ```

  ```python
  # pages/urls.py
  
  from django.urls import path
  
  
  urlpatterns = [
  
  ]
  ```

  <br>

*  project에서 app의 urls.py에 접근하려면?

  **including other URLconfs** : include()를 만나게 되면 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속처리하기 위해 include된 URLconf로 전달한다.

  ```python
  # firstpjt/urls.py
  
  from django.contrib import admin
  from django.urls import path, include
  
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')),
      path('pages/', include('pages.urls')),
  ]
  ```

  <br>

* 주소에 name을 붙여서 사용하려면?

  **Naming URL patterns** : 만약 주소를 변경하게 된다면 환경 내의 모든 주소를 바꾸어 주어야 한다. 이를 방지하기 위해 urls.py에서 경로를 등록할 때 `name='index'`와 같이 지정해주면 간단하게 해결 할 수 있다. 

  ```python
  # articles/urls.py
  
  urlpatterns = [
      path('index/', views.index, name='index'),
      path('greeting/', views.greeting, name='greeting'),
      path('dinner/', views.dinner, name='dinner'),
  	...
  ]
  ```

  ```django
  <!-- index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>만나서 반가워요!</h1>
    <a href="{% url 'greeting' %}">greeting</a>
    <a href="{% url 'dinner' %}">dinner</a>
  {% endblock %}
  ```

  여기서 `a 태그`를 사용한다. `href='{% url 'greeting' %}'`과 같이 작성해주어야 한다. 

  <br>

* URL에도 namespace를 사용할 수 있다!

  **URL namespace** : 앱이 여러개 생성되면 문제가 발생한다. 첫번째 앱의 `index.html`와 두번째 앱의 `index.html`을 구분할 수 없기 때문이다. 이를 위해 url에도 이름을 지정해야 한다. 

  ```python
  # pages/urls.py
  
  app_name = 'pages'
  urlpatterns = [
      path('index/', views.index, name='index'),
  ]
  ```

  ```python
  # articles/urls.py
  
  app_name = 'articles'
  urlpatterns = [
      ...,
  ]
  ```

  :exclamation: `:`연산자를 사용해서 접근한다. 

  ```django
  <!-- articles/templates/index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>만나서 반가워요!</h1>
    <a href="{% url 'articles:greeting' %}">greeting</a>
    <a href="{% url 'articles:dinner' %}">dinner</a>
    <a href="{% url 'articles:throw' %}">throw</a>
  
    <h2><a href="{% url 'pages:index' %}">두번째 앱 index로 이동</a></h2>
  {% endblock %}
  ```

  <br>

* Django에서는 `app_name/templates/`까지의 경로에서 순서대로 `.html`파일을 검색하기 때문에 내가 원하지 않는 `.html`의 파일을 사용할 수 있다. 이를 위해 app내의 template안에 `app_name`과 동일한 폴더를 만들어 준 후 그 안에 `.html`파일을 넣어주는 것이 좋다. 

  예시 ) `app_name/templates/app_name`

  

