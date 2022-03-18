# 03.16

## Django 01

**The Web Framework**

<br>

[TOC]

<br>

### Web Framework

* **Django**는 높은 레벨의 **python web framework**이다. 빠르고, 편리하고, 깔끔한 디자인을 할 수 있다. 

|        title         | content                                                      |
| :------------------: | ------------------------------------------------------------ |
|       **Web**        | **World Wide Web**, 인터넷에 연결된 컴퓨터를 통해 정보를 공유할 수 있는 전 세계적인 정보 공간이다. |
| **Static web page**  | **정적 웹 페이지**이며, 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹페이지이다. 서버가 정적 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 없이 클라이언트에게 응답을 보낸다. 모든 상황에서 모든 사용자에게 동일한 정보를 표시하며 일반적으로 HTML, CSS, JavaScripts로 작성된다. flat page라고도 한다. |
| **Dynamic web page** | **동적 웹 페이지**이며, 웹 페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 이후 클라이언트에게 응답을 보낸다. 동적 웹 페이지는 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다르다. 서버 사이드 프로그래밍 언어인 Python, Java, C++ 등이 사용되며, 파일을 처리하고 데이터 베이스와의 상호작용이 이루어진다. |
|    **Framework**     | 프로그래밍에서 특정 운영 체제를 위한 응용 프로그램 표준 구조를 구현하는 클래스와 라이브러리 모임이다. 재사용할수 있는 수많은 코드를 프레임워크로 통합함으로써 개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 같이 사용할 수 있도록 도와준다. Application framework라고도 한다. |
|  **Web framework**   | _웹 페이지를개발하는 과정에서 겪는 어려움을 줄이는 것을 주 목적_ 으로 데이터베이스 연동, 템플릿 형태의 표준, 세션 관리, 코드 재사용 등의 기능을 포함한다. 동적인 웹 페이지나 웹 애플리케이션, 웹 서비스 개발 보조용으로 만들어지는 Application framework의 일종이다. |

* :grey_exclamation: Django를 사용하는 이유?

  Django는 검증된 python 언어 기반의 Web framework이다. 대규모 서비스에도 안정적이며 Spotify, Instargam, Dropbox, Delivery Hero 등과 같은 곳에서 사용 중이다.  

* **Framework Architecture** -`MVC` Design Pattern (model-view-controller)

  소프트 웨어 공학에서 사용되는 디자인 패턴 중의 하나이다. 이를 통해 사용자 인터페이스로부터 프로그램 로직을 분리하여 애플리케이션의 시각적 요소나 이면에서 실행되는 부분을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있다. 

  Django에서는 `MVT model`이라고 한다. 

  | MVC Pattern | MTV (Django) |                           MTV 설명                           |
  | :---------: | :----------: | :----------------------------------------------------------: |
  |    Model    |    Model     | 응용 프로그램의 데이터 구조를 정의하고 데이터 베이스의 기록을 관리(추가, 수정, 삭제) |
  |    View     |   Template   | 파일의 구조나 레이아웃을 정의. 실제 내용을 보여주는데 사용함. |
  | Controller  |     View     | HTTP 요청을 수신하고 HTTP 응답을 반환. Model을 통해 요청을 충족시키는데 필요한 데이터에 접금. template에게 응답의 서식 설정을 맡김. |

<br>

### Django Intro

**Django 시작하기** 

* 가상환경 생성 및 활성화

  ```bash
  $ python -m venv venv
  $ source venv/Scripts/activate
  ```

* Django 설치하기

  ```bash
  $ pip install django==3.2.12
  $ pip list
  ```

* 프로젝트 생성

  ```bash
  $ django-admin startproject firstpjt .
  ```

  :small_red_triangle: 프로젝트 이름에는 python 이나 django에서 사용중인 키워드를 피해야 한다. '-'(하이픈), class, text 등 도 사용할 수 없다. 

  :small_red_triangle: 프로젝트에는 여러 앱이 포함될 수 있고, 앱은 여러 프로젝트에 있을 수 있다. 

* 서버 활성화하기

  ```bash
  $ python manage.py runserver
  ```

* 프로젝트 구조 살펴보기

  |  firstpjt   |                             설명                             |
  | :---------: | :----------------------------------------------------------: |
  |   init.py   | Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시 |
  |   asgi.py   | Asynchronous Server Gateway Interface / Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움 |
  | settings.py |               애플리케이션의 모든 설정을 포함                |
  |   urls.py   |          사이트의 url과 적절한 views의 연결을 지정           |
  |   wsgi.py   | Web Server Gateway Interface / Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움 |
  |  manage.py  | Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티 |

* 애플리케이션 생성(일반적으로 Application명은 복수형으로 하는 것을 권장)

  ```bash
  $ python manage.py startapp articles
  ```

  :small_red_triangle: 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담한다. 하나의 프로젝트는 여러 앱을 가진다. 일반적으로 앱은 *하나의 역할 및기능 단위* 로 작성한다.

* 애플리케이션 구조 살펴보기

  | firstpjt  |                             설명                             |
  | :-------: | :----------------------------------------------------------: |
  |  init.py  | Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시 |
  | admin.py  |                관리자용 페이지를 설정하는 곳                 |
  |  apps.py  |                    앱의 정보가 작성된 곳                     |
  | models.py |             앱에서 사용하는 Model을 정의하는 곳              |
  | tests.py  |             프로젝트의 테스트 코드를 작성하는 곳             |
  | views.py  |                  view 함수들이 정의 되는 곳                  |

* **앱 등록**

  프로젝트에서 앱을 사용하기 위해서는 `settings.py`에서`INSTALLED_APPS`의 리스트에 추가해야한다. 반드시 앱 생성 한 후 등록 해야한다!!

<br>



### 요청과 응답

* 요청과 응답하기 위해 가자 중요한 순서는 `urls, view, templatate`이다. 

  1. **urls.py**

     HTTP 요청을 알맞은 view로 전달한다.
  
     ```python
     # urls.py
     
     from django.dontrib import admin
     from django.urls import path
     from articles import views
     
     urlpatterns = [
         path('admin/', admin.site.urls),
         path('indes/', views.index),
     ]
     ```
  
  2. **views.py**
  
     HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수를 작성한다.
  
     Model을 통해 요청에 맞는 필요 데이터에 접근한다.
  
     Template에게 HTTP 응답 서식을 맡긴다. 
  
     ```python
     # views.py
     
     from django.shortcuts import render
     
     def index(request):
         return render(request, 'index.html')
     ```
  
  3. **template**
  
     실제 내용을 보여주는데 사용되는 파일이다. 
     
     파일 구조나 레이아웃을 정의한다.
     
     Template 파일 경로의 기본 값은 app 폴더 안의 templates 폴더로 지정되어 있다. 
     
     ```html
     <h1>안녕!</h1>
     ```

* 추가 사항
  1. LANGUAGE_CODE : 모든 사용자에게 제공되는 번역을 결정할 수 있도록 한다. 이 설정이 적용되려면 USE_I18N이 활성화 되어 있어야 한다. (한국어로 설정할 경우 'ko-kr')
  2. TIME_ZONE : 현재 시간대를 지정한다. USE_TZ가 True인 상태에서 시간을 지정해주어야 오류가 나지 않는다. (USE_L10N은 True일 경우 Django에서는 현재 locale의 형식을 사용해 숫자와 날짜를 표시한다.)

<br>

### Template

* **Django Template** : 데이터 표현을 제어하는 도구이자 표현에 관련된 로직이다. Django template language를 사용한다. 

* **Django Template Language (DTL)** : 장고에서 사용하는 built-in template system이다. 조건, 반복, 변수 치환, 필터 등의 기능을 제공하고한다. 프레젠테이션을 표현하기 위한 것이다. python 처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 해당 python 코드로 실행되는 것은 아니다. 
  1. **Variable**
  
     ```django
     {{ variable }}
     ```
  
     `views.py`에서 `render()`를 사용하여 정의한 변수를 template 파일로 넘겨 사용한다. 변수면은 영어, 숫자, 밑줄(_)을 사용할 수 있으나 밑줄로는 시작할 수없고, 공백이나 구두점 문자는 사용할 수 없다. 
  
     dot(.)를 사용하여 변수 속성에 접근할 수 있다. 
  
     `render()`의 세번째 인자로 {'key':value} 와 같이 딕셔너리 형태로 넘겨주며, key에 해당하는 문자열이 template에서 사용 가능한 변수명이 된다. 
  
  2. **Filters**
  
     ```django
     {{ variable|filter }}
     
     {# name 변수를 모두 소문자로 출력 #}
     {{ name|lower }}
     ```
  
  3. **Tags**
  
     ```django
     {% tag %}
     
     {% if %}{% endif %}
     ```
  
     출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일을 수행한다. python에서 for문과 if문을 사용하듯이 사용할 수 있으며 일부 태그는 시작과 종료 태그가 필요하다. 
  
  4. **Comments**
  
     ```django
     {# #}
     
     {% comment %}
     	주석
     	주석
     {% endcomment %}
     ```
  
     Django의 주석표현이다. 여러줄의 주석 표현도 가능하다.  
  
* :red_circle: **코드 작성 순서!!!**

  1. urls.py
  2. views.py
  3. templates

  ```python
  import random
  
  def greeting(request):
      foods = ['apple', 'banana', 'coconut']
      pick = random.choice(foods)
      info = {
          'name':'Alice'
      }
      context = {
          'foods': foods,
          'info': info, 
      }
      return render(request, 'greeting.html', context)
  ```

  ```html
  <p>안녕하세요 저는 {{ info.name }} 입니다.</p>
  <p>제가 좋아하는 음식은 {{ foods }} 입니다.</p>
  <p>{{ foods.0 }}을 가장 좋아합니다.</p>
  
  <p>{{ pick }}은 {{ pick|length }}글자</p>
  <p>{{ foods|join:", " }}</p>
  
  <a href = "/index/">뒤로</a>
  ```

* **Template inheritance (템플릿 상속)**

  템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춘다. `base.html`을 만든다. 

  1. 상위폴더에 `templates`만들기

  2. `base.html`만들기 

     ```django
     -- base.html --
     
     <body>
         
         {% block content %}
         {% endblock %}
         
     </body>
     ```

  3. 자식 템플릿에서 부모 템플릿을 확장한다는 것을 알림 (반드시 템플릿 최상단에 작성 되어야 한다. )

     ```django
     -- index.html --
     
     {% extends 'base.html' %}
     
     {% block content %}
     --내용 작성--
     {% endblock %}
     ```

  4. `SETTINGS.PY`의 `TEMPLATES` 안에 경로지정!!

     ```python
     TEMPLATES = [
         {
            ...
            'DIRS': [BASE_DIR/ 'templates'],
            ... 
         }
     ]
     ```

  5. Template Tag - "include" 

     템플릿 내에 다른 템플릿을 "포함(including)"하는 방법

     ```python
     {% include '' %}
     ```

  6. Django의 설계 철학

     * 표현과 로직(view)을 분리한다. 템플릿은 표현에 관련된 로직이다. 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 한다.
     * 중복을 배체한다. 대다수의 동적 웹사이트는 공통의 header, footer, navbar 등의 같은 사이트 공통 디자인을 가지는데 이러한 중복 코드를 없애는 것이다. 

<br>

### HTML Form

1. **HTML "form" element**

   웹에서 사용자의 정보를 입력하는 여러 방식을 제공 (text, button, checkbox, file, hidden, image, password, radio, reset, submit) 하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당한다. 

   * **action** : 입력 데이터가 전송될 URL 지정
   * **method** : 입력 데이터 전달 방식 지정

2. **HTML "input" element**

   사용자로부터 데이터를 입력받기 위해 사용한다. type의 속성에 따라 동작 방식이 달라진다.  핵심속성은 **name**이다.

   * **name** : 중복 가능, 양식을 제출했을 때 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있다. 주요 용도는 **GET/POST** 방식으로 서버에 전달하는 파라미터(name은 key로 value는 value)로 매핑하기 위하미다. 
   * 특히 GET 방식에서 URL은 `?key=value&key=value` 형식으로 데이터를 전달한다.

3. **HTML "label" element**

   label과 input요소 연결의 주요 이점으로는 시각적기능과 함께 화면 리더기에서 label을 읽어 사용자가 입력해야하는 텍스트가 무엇인지 더 쉽게 이해할 수 있도록 돕는 프로그래밍적 이점이 있다. label을 클릭하면 input에 초점(focus)를 맞추거나 활성화(activate) 시킬 수 있다. 

4. **HTML "for" attribute**

   `for`은 `id`와 함께 사용된다. for 속성의 값과 일치하는 id를 가진 문서의 첫 번째 요소를 제어한다.  

5. **HTML "id" attribute**

   `id`는 전체 문서에서 고유해야하는 식별자를 정의 한다. linking, scripting, styling시에 요소를 식별한다. 

6. **HTML** (Hyper Text Transfer Protocol)

   웹에서 이루어지는 모든 데이터 교환의 기초이다. 주어진 리소스가 수행 할 작업을 나타내는 request methods를 정의한다. 

   :small_red_triangle:  HTTP requset method 종류 : GET, POST, PUT, DELETE

7. **HTML request method - GET**

   `GET`은 서버로부터 **정보를 조회**하는데 사용한다. 이는 읽기만 가능하다. 데이터를 서버로 전송할 때 body가 아닌 Query String Parameters를 통해 전송한다. 우리가 서버에 요청을 하면 HTML 문서 파일 한장을 받는데, 이때 사용하는 요청의 방식이 GET이다. 

<br>

### URL 

:red_circle: **중요사항!!**

1. **Variable Routing**

   URL 주소를 변수로 사용한다. URL에서 검색을 통해 view 함수의 인자로 넘길 수 있다. 이때 `name`과 `age`를 view의 인자로 넘겨주어야 사용할 수 있다. 

   ```python
   path('movies/<int:score>', ...),
   path('users/<str:name>/<int:age>', views.hello),
   ```

   ```python
   def hello(requset, name, age):
       context = {
           'name': name,
           'age': age,
       }
       return render(request, 'hello.html', context)
   ```

2. **APP URL mapping**

   app의 view 함수가 많아지면서 사용하는 path()가 많아지고, app이 늘어나면서 프로젝트의 `urls.py`에서 모두 관리하는 것은 프로젝트 유지 보수에 악영향을 미친다. 이런 문제를 해결하기위해 각 app에 `urls.py`를 작성하게 된다.

   ```python
   # settings.py
   
   INSTALLED_APPS = [
   	'pages',
       ...,
   ]
   ```

   ```python
   # pages/urls.py
   
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

3. **Including other URLconfs**

   프로젝트에서 앱의 `urls.py`에 접근 할 수도 있다. `include`를 사용하는데 include()를 만나게 되면 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속처리하기 위해 include된 URLconf로 전달한다.  

   ```python
   # firstpjt/urls.py
   
   from django.contrib import admin
   from django.urls import path, include   ---(1)
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('articles/', include('articles.urls')),
       path('pages/', include('pages.urls')),
   ]
   ```

   (1)의 부분을 꼭 작성해주어야함!!

4. **Naming URL patterns**

   주소를 변경되는 경우에 모든 파일에서 변경해주어야 하는 일을 방지하기위해 `urls.py`에서 경로를 등록할 때 `name='index'`와 같이 지정해주면 간단하게 해결할 수 있다.  

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


5. **URL namespace**

   URL에도 namespace를 사용할 수 있다! 앱이 여러개 생성되면 문제가 발생한다. 첫번째 앱의 `index.html`와 두번째 앱의 `index.html`을 구분할 수 없기 때문이다. 이를 위해 url에도 이름을 지정해야 한다. 

   ```python
   # pages/urls.py
   
   app_name = 'pages'
   urlpatterns = [
       ...,
       path('index/', views.index, name='index'),
       ...,
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

6. **url template tag**

   ```django
   {% url ' ' %}
   ```

   `naming URL pattern`과 `URL namespace`에서 사용한 방법으로 a태그에서 사용한다. 

<br>

<br>
