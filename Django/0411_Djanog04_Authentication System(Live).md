# 04.11

## django 04_Authentication System

[TOC]

<br>

---

### 1. Authentication System_1

<br>

#### 1. The django Authentication System

* django 인증 시스템은 `django.contrib.auth`에 `django contrib module`로 제공한다. `INSTALLED_APPS`에 이미 포함되어 있다. 

  `django.dontrib.auth` : 인증 프레임워크의 핵심과 기본 모델을 포함

  `django.contrib.contenttypes` : 사용자가 생성한 모델과 권한을 연결할 수 있다. 

* 인증 시스템은 **인증(Authentication)**과 **권한(Authorization)** 부여를 함께 제공(처리) 하며, 이러한 기능이 어느 정도 결합이되어 일반적으로 인증 시스템이라고 한다. 

  1. **Authentication** 인증 : 신원 확인. 사용자가 자기 자신이 누구인지 확인하는 것
  2. **Authorization** 권한, 허가 : 권한 부여. 인증된 사용자가 수행할 수 있는 작업을 결정

1. 두번 째 앱 생성하기

   ```bash
   $ python manage.py startapp accounts
   # 앱 등록하기
   # auth와 관련해 Django 내부적으로 accounts라는 이름으로 사용되고 있기 때문에 되도록 accounts로 지정하는 것을 권장
   ```
   
   ```python
   # settings.py
   
   INSTALLED_APPS = [
       ...,
       'accounts',
       ...,
   ]
   ```
   
   ```python
   # project/urls.py
   
   urlpatterns =[
       ...,
   	path('accounts/', include('accounts.urls')),
       ...,
   ]
   ```
   
   ```python
   # accounts/urls.py
   from django.urls import path
   from . import views
   
   app_name = accounts
   urlpatterns = [
       path()
   ]
   ```

<br>

#### 2. 쿠키와 세션

* HTTP(Hyper text transfer protocol) : HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토톨(규칙, 규약). 웹에서 이루어지는 모든 데이터 교환의 기초이다. 클라이언트 - 서버 프로토콜이기도 하다. 

  **비연결을 지향한다 (connectionless)** : 서버는 요청에 대한 응답을 보낸 후 연결을 끊는다.

  **무상태 (stateless)** : 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않는다. 클라이언트와서버가 주고 받는 메시지들은 서로 완전히 독립니다. 

  클라이언트와 서버의 지속적인 관계를 유지하기 위해 **쿠키와 세션**이 존재한다.

* :small_red_triangle_down: **쿠키(cookie)** : 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각이다. 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치(placed-on)되는 작은 기록 정보이다.(브라우저(클라이언트)는 쿠키를 로컬에 KEY-VALUE)의 데이터 형식으로 저장한다. 이렇게 쿠키를 저장해 놓았다가, 동일한 서버에 재 요청 시 저장된 쿠키를 함께 전송한다.)

  쿠키는 소프트웨어가 아니기 때문에 프로그램처럼 실행 될 수 없으며 악성코드로 설치할 수 없지만, 사용자의 행동을 추적하거나 쿠키를 훔쳐서 해당 사용자의 계정 접근 권한을 획득 할 수도 있다.

  HTTP 쿠키는 상태가 있는 세션을 만들어 준다. 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용한다. *이를 이용해 사용자의 로그인 상태를 유지*할 수 있다. 상태가 없는 HTTP 프로토콜에서 상태 정보를 기억 시켜주기 때문이다. 

  ```tex
  웹 페이지에 접속하며 요청한 웹 페이지를 받으며 쿠키를 저장하고, 클라이언트가 같은 서버에 재 요청 시 요청과 함께 쿠키도 함께 전송
  ```

  1. :star: 세션 관리(Session management)

     로그인, 아이디 자동 완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리

  2. 개인화(Personalization)

     사용자 선호, 테마 등의 설정

  3. 트래킹(Tracking)

     사용자 행동을 기록 및 분석

     개발자 도구 - 네트워크 탭 `Set-cookie`에서 확인할 수 있다. 

* :small_red_triangle_down: **세션(Session)** : 사이트와 특정 브라우저 사이의 '상태(state)'를 **유지**시키는 것이다. 클라이언트가 서버에 접속하면 서버가 특정 `session_id`를 발급하고, 클라이언트는 발급 받은 `session_id`를 쿠키에 전송한다. 쿠키는 요청마다 서버에 함께 전송되므로 서버에서 `session_id`를 확인해 알맞은 로직을 처리한다. ID는 세션을 구별하기 위해 필요하며, 쿠키에는 ID만 저장한다. 

  로그아웃 -> 세션 삭제

  쿠키는 각각의 유효기간이 있다. 유효기간으로 정렬된다. 

* **쿠키 lifetion(수명)** : 쿠키의 수명은 두 가지 방법으로 정의할 수 있다. 

  1. session cookies : 현재 세션이 종료되면 삭제된다. 브라우저가 '현재 세션'이 종료되는 시기를 정의 한다. 일부 브라우저는 다시 시작할 때 세션 복원을 사용해 세션 쿠키가 오래 지속 될 수 있도록 한다.
  2. persistent cookies : Expires 속성에 지정된 날짜 혹은 Max_age 속성에 지정된 기간이 지나면 삭제한다. 

* **seseion in Django**

  Django의 세션은 미들웨어를 통해 구현된다. Django는 특정 `session id`를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션을 알아낸다. 세션 정보는 Django DB의 django_session 테이블에 저장된다. 모든 것을 세션으로 사용하려고 하면 사용자가 많을 때 서버에 부하가 걸릴 수 있다. 

* **Authentication System in MIDDLEWARE**

  1. SessionMiddleware : 요청 전반에 걸쳐 세션을 관리

  2. AuthenticationMIDDLEWARE : 세션을 사용하여 사용자를 요쳥과 연결한다. 

<br>

#### 3. 로그인

* 로그인은 session을 create하는 로직과 같다. django는 우리가 session의 메커니즘에 생각하지 않게끔 도움을 준다. 이를 위해 인증에 관한 built-in forms를 제공한다. 

* **AuthenticationForm**  : 사용자 로그인을 위한 form이다. request를 첫번째 인자로 취한다. 

* **login 함수** : `login(request, user, backend=None)`

  현재 세션에 연결하려는 인증 된 사용자가 있는 경우 login()함수가 필요하다. 사용자를 로그인하며 view함수에서 사용된다. HttpRequest 객체와 User 객체가 필요한다. 세션에 user의 ID를 저장(==로그인)
  
  ```python
  # urls.py
  
  path('login/', views.login, name='login'),
  ```
  
  ```python
  # views.py
  from django.shortcuts import render, redirect
  from django.contrib.auth import login as auth_login
  from django.contrib.auth.forms import AuthenticationForm
  from django.views.decorators.http import require_http_methods
  
  
  @require_http_methods(['GET', 'POST'])
  def login(request):
      if request.method == 'POST':
          form = AuthenticationForm(request, request.POST)
          if form.is_vaild():
              # 로그인
              auth_login(request, form.get_user())
              return redirect('articles:index')
      else:
          form = AuthenticationForm()
      context = {
          'form':form, 
      }
      return render(request, 'accounts/login.html', context)
  ```

  ```django
  <!-- templates/accounts/login.html -->
  <!-- create 페이지와 비슷 -->
  
  {% block content %}
  	<h1>로그인</h1>
  	<form action="{% url 'accounts:login' %}" method="POST">
          {% csrf_token %}
          {{ form.as_p }}
          <input type="submit">
  	</form>
  {% endblock content %}
  ```
  
  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```
  
  ```django
  # base.html
  
  <body>
      <div class='container'>
          <h3>Hello, {{ user }} </h3>
          <a href="{% url 'accounts:login' %}">Login</a>
          {% block content %}
          {% endblock content %}
      </div>
  </body>
  ```
  
  우리가 별도로 정보를 넘겨주지 않아도 템플릿이 렌더링 될 때 자동으로 호출 가능한 컨텍스트 데이터 목록이 있다. 작성시 프로세서는 사용 가능한 변수로 적용된다. 
  
  `{{ user }}` : 현재 로그인 한 사용자를 나타내는 auth User 인스턴스(또는 클라이언트가 로그인 하지 않은 경우 AnonymousUser 인스턴스)는 템플릿 변수 {{ user }}에 저장된다. 

#### 4. 로그아웃 

* 로그 아웃은 session을 삭제한다. 

* **logout 함수** : `logout(request)`

  사용자가 로그인 하지 않은 경우 오류를 발생시키지 않는다. 현재 요청에 대한 **session data를 DB에서 완전히 삭제**하고, **클라이언트의 쿠키에서도 sessionid가 삭제** 된다. 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 액세스하는 것을 방지하기 위함이다. 

  ```python
  # urls.py
  
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  ```
  
  ```python
  # views.py
  from django.views.decorators.http import require_http_methods, require_POST
  from django.contrib.auth import logout as auth_logout
  
  @require_POST
  def logout(request):
      auth_logout(request)
      return redirect('articles:index')
  ```
  
  ```django
  # base.html
  
  <body>
      <div class='container'>
          <h3>Hello, {{ user }} </h3>
          <a href="{% url 'accounts:login' %}">Login</a>
          <form action='{% url 'accounts:logout' %}' method="POST">
              {% csrf_token %}
              <input type='submit' value='Logout'>
          </form>
          {% block content %}
          {% endblock content %}
      </div>
  </body>
  ```

#### 5. 로그인과 로그아웃 상태에 대한 접근 제한

로그인 하지않았을 경우 로그인만, 로그인 했을 경우 로그 아웃만 접근 가능

1. **The raw way** : `is_authenticated` attribute

   user model의 속성 중 하나로 모든 user 인스턴스에 대해 항상 True인 읽기 전용 속성이다.(AonymousUser에 대해서는 항상 False) 

   사용자가 인증 되었는지 여부를 알 수 있는 방법이다. 

   권한(permission)과는 관련이없으며, 사용자가 활성화 상태(active)에 있는지만 확인할 수 있고, 유효한 세션을 가지고 있는 지도 확인하지않는다.

   ```django
   # base.html
   
   <body>
       <div class='container'>
           <!-- True(인증 되었는지?) -->
           {% if request.user.is_authenticated %}
             <h3>Hello, {{ user }} </h3>
             <form action='{% url 'accounts:logout' %}' method="POST">
               {% csrf_token %}
               <input type='submit' value='Logout'>
             </form>
           <!-- False -->
           {% else %}
           	<a href="{% url 'accounts:login' %}">Login</a>
   		{% eldif %}
           {% block content %}
           {% endblock content %}
       </div>
   </body>
   ```

   ```python
   # views.py
   from django.shortcuts import render, redirect
   from django.contrib.auth.forms import AuthenticationForm
   from django.contrib.auth import login as auth_login
   from django.views.decorators.http import require_http_methods, require_POST
   from django.contrib.auth import logout as auth_logout
   
   @require_http_methods(['GET', 'POST'])
   def login(request):
       if request.user.is_authenticated:  # (=True)로그인한 상태면 해당 함수를 진행할 수 있음!!
           return redirect('artielcs:index')
           
       if request.method == 'POST':
           form = AuthenticationForm(request, request.POST)
           if form.is_vaild():
               # 로그인
               auth_login(request, form.get_user())
               # return redirect('articles:index')
           	return redirect(request.GET.get('next') or 'articles:index')
       else:
           form = AuthenticationForm()
       context = {
           'form':form, 
       }
       return render(request, 'accounts/login.html', context)
   
   @require_POST
   def logout(request):  # 로그인된 사람만 로그아웃 로직을 사용할 수 있다. 
       if request.user.is_authenticated:
   	    auth_logout(request)
       return redirect('articles:index')
   ```

   ```django
   <!-- articles/index.html -->
   <!-- 인증된 사용자만 게시글 작성 링크 볼 수 있도록 -->
   
   {% block content %}
   	<h1>Articles</h1>
   	{% if request.user.is_authenticated %}
   		<a href="{% url 'articles:create' %}">[CREATE]</a>
   	{% else %}
   		<a href="{% url 'accounts:login' %}">[새 글을작성하려면 로그인 하세요]</a>
   	{% endif %}
   ```

2. The **login_required** decorator

   사용자가 로그인 되어 있지 않으면, `settings.LOGIN_URL`에 설정된 문자열 기반 절대 경로로 redirect한다. `/accounts/login/` 두 번째 app 이름을 accounts로 했던 이유 중 하나

   사용자가 로그인되어 있으면 정상적으로 view 함수를 실행

   인증 성공 시 사용자가 redirect 되어야 하는 경로는 'next'라는 쿼리 문자열 매개 변수에 저장된다. (`/accounts/login/?next=/articles/create`) 원래 하고 싶었던 요청을 값으로 넘겨주고, 로그인 후 해당 페이지로 redirect 될 수 있도록 해준다. 

   * **next** : 로그인이 정상적으로 진행되면 기존에 요청했던 주소로 redirect하기 위해 마치 주소를 keep 해주는 것이다. 단, 별도로 처리해주지 않으면 우리가 view에 설정한 redirect 경로로 이동하게 된다. 

   ```python
   from django.contrib.auth.decorators import login_required
   
   @login_required
   @require_http_mothod(['GET','POST'])
   def create(request):
       pass
   
   @login_required
   @require_http_mothod(['GET','POST'])
   def update(request):
       pass
   
   @login_required
   @require_http_mothod(['GET','POST'])
   def delete(request):
       pass
   ```

   ```django
   {% block content %}
   	<h1>로그인</h1>
   	<form action="" method="POST">
           {% csrf_token %}
           {{ form.as_p }}
           <input type="submit">
   	</form>
   {% endblock content %}
   
   <!-- 현재 URL로(next parameter가 있는) 요청을 보내기 위해 action 값 비우기
   ```
   
   :small_red_triangle_down: 두 데코레이터로 인해 발생하는 구조적 문제와 해결
   
   ```python
   @login_required  # 사용자가 로그인 되어 있지 않은 경우 로그인 페이지로 접근, 사용자 인증을 성공하게 되면 next 뒤의 주소로 redirect 된다. 
   @require_POST  # POST일 경우에만 사용가능
   ```
   
   만약 위의 두가지 데코레이터를 함께 사용하여 비로그인 상태에서 게시글을 삭제하고자 시도 한다면?
   
   ```python
   # articles/views.py
   # 해당 코드는 틀린 코드
   
   @login_required
   @require_POST
   def delete(request, pk):
       article = get_object_or_404(Article, pk=pk)
       article.delete()
       return redirect('articles:index')
   ```
   
   1. redirect로 이동한 로그인 페이지에서 로그인을 시도한다. 
   2. 405 status code를 확인할 수 있다. 
   
   `require_POST`로 작성된 함수에 `login_required`를 함께 사용하는 경우 **에러 발생**하게 된다. 로그인 이후 "next"매개별수를 따라 해당 함수로 다시 redirect 되는데, 이때 `@require_POST` 때문에 405 에러가 발생하게 되는 것이다. 
   
   1. redirect 과정에서 POST 데이터가 손실된다.
   2. redirect 요청은 POST 방식이 불가능하기 때문에 GET 방식으로 요청된다. 
   
   :red_circle: 따라서 `login_required`는 GET method request를 처리할 수 있는 view 함수에서만 사용해야 한다!!
   
   ```python
   # articles/views.py
   
   @require_POST
   def delete(request, pk):
       if request.user.is_authenticated:
   	    article = get_object_or_404(Article, pk=pk)
       	article.delete()
       return redirect('articles:index')
   ```

<br>

<br>

<br>

### 2. Authentication System_2

#### 1. 회원가입

* 회원가입을 위해서는 **UserCreationForm**이 필요하다. 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm이다. 다음과 같이 3개의 필드를 가진다. 
  1. username(from the user model)
  2. password1
  3. password2

* 회원가입 구현하기

  ```django
  <!-- base.html -->
  
  <body>
      <div class='container'>
          <!-- True(인증 되었는지?) -->
          {% if request.user.is_authenticated %}
          <h3>Hello, {{ user }} </h3>
            <form action='{% url 'account:logout' %}' method="POST">
              {% csrf_token %}
              <input type='submit' value='Logout'>
            </form>
          <!-- False -->
          {% else %}
          	<a href="{% url 'accounts:login' %}">Login</a>
          	<a href="{% url 'accounts:signup' %}">signup</a>
  		{% eldif %}
          {% block content %}
          {% endblock content %}
      </div>
  </body>
  ```

  ```python
  # urls.py
  
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('signup/', views.signup, name='signup'),
  ```

  ```python
  # accounts/views.py
  from django.contrib.auth.forms import AuthenticationForm, UserCreationFroem
  
  
  @require_http_method(['GET', 'POST'])
  def signup(request):
      # 로그인 되어 있는 상태라면 회원가입 불가능한 코드 작성
      
      if request.method =='POST':  # 모든 규칙이 통과가 되었다면?
          form = UserCreateForm(requset.POST)
          if form.is_valid():
              user = form.save()
              auth_login(request, user)
              return redirect('articles:index')
      else:  # 회원가입 주소에 들어왔다면?
          form = UserCreateForm()
      context = {
          'form':form
      }
      return render(request, 'accounts/signup.html', context)
  ```

  * 회원 가입 후 자동으로 로그인 

  ```django
  <!-- signup.html -->
  
  {% extents 'base.html' %}
  {% block content %}
  	<h1>회원가입</h1>
  	<form action="{% url 'accounts:signup' %}" method="POST">
          {% csrf_token %}
          {{ form.as_p }}
          <input type="submit">
  	</form>
  {% endblock content %}
  
  ```

#### 2. 회원탈퇴

* 회원 탈퇴는 DB에서 사용자를 삭제하는 것과 같음 

  ```django
  <!-- base.html -->
  
  <body>
      <div class='container'>
          <!-- True(인증 되었는지? == 로그인상태?) -->
          {% if request.user.is_authenticated %}
          <h3>Hello, {{ user }} </h3>
            <form action='{% url 'account:logout' %}' method="POST">
              {% csrf_token %}
              <input type='submit' value='Logout'>
            </form>
            <form action="{% url 'accounts:delete' %}" method="POST">
              {% csrf_token %}
              <input type='submit' value='회원탈퇴'>  
            </form>
          <!-- False(== 비로그인 상태?) -->
          {% else %}
          	<a href="{% url 'accounts:login' %}">Login</a>
          	<a href="{% url 'accounts:signup' %}">signup</a>
  		{% eldif %}
          
          {% block content %}
          {% endblock content %}
      </div>
  </body>
  ```

  ```python
  # urls.py
  
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('signup/', views.signup, name='signup'),
  path('delete/', views.delete, name='delete'),
  ```

  ```python
  @require_POST
  def delete(request):
      if request.user.id_authenticated:
      	request.user.delete()
          auth_logout(request)  # 세션 삭제하기 반드시 회원 탈퇴 후 로그아웃 함수 호출
      return redirect('articles:index')
  ```

#### 3. 회원정보 수정

* 회원 정보 수정은 **UserChangeForm**이라는 ModelForm이 필요하다. 

  ```django
  <!-- articles/update.html -->
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>회원정보수정</h1>
    <hr>
    <form action="{% url 'accounts:update' %}" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit">
    </form>
    <a href="{% url 'articles:index' %}">back</a>
  {% endblock content %}
  
  ```
  
  ```python
  # urls.py
  
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('signup/', views.signup, name='signup'),
  path('delete/', views.delete, name='delete'),
  path('update/', views.update, name='update'),
  ```
  
  ```python
  # accounts/views.py
  
  from django.contrib.auth.forms import AuthenticationForm, UserCreationFroem, UserChangeForm
  
  @require_http_method(['GET', 'POST'])
  def update(request):
  	if request.method == "POST":
          pass
      else:
          form = UserChangeForm(instance=request.user)
      context = {
          'form':form,
      }
      return render(request,'accounts/update.html', context)
  ```
  
  ```django
  <!-- base.html -->
  
  <body>
      <div class='container'>
          <!-- True(인증 되었는지? == 로그인상태?) -->
        {% if request.user.is_authenticated %}
          <h3>Hello, {{ user }} </h3>
          <a href="{% url 'accounts:update' %}">회원정보 수정</a>
          <form action='{% url 'account:logout' %}' method="POST">
              {% csrf_token %}
              <input type='submit' value='Logout'>
          </form>
          <form action="{% url 'accounts:delete' %}" method="POST">
              {% csrf_token %}
              <input type='submit' value='회원탈퇴'>  
          </form>
          <!-- False(== 비로그인 상태?) -->
        {% else %}
           <a href="{% url 'accounts:login' %}">Login</a>
           <a href="{% url 'accounts:signup' %}">signup</a>
  	  {% eldif %}
          
        {% block content %}
        {% endblock content %}
      </div>
  </body>
  ```

  :red_circle: UserChangeForm 사용 시 문제점 : 일반 사용자가 접근해서는 안될 정보들까지 모두 수정이 가능해진다. 따라서 UserChangeForm을 상속받아 CustomChangeForm이라는 서브클래스를 작성해 접근 가능한 필드를 조정해야 한다. 
  
  ```python
  # accounts/forms.py
  from django.contrib.auth.forms import UserChangeForm
  from django.contrib.auth import get_user_model
  
  
  class CustomUserChangeForm(UserChangeForm):
      
      class Meta:
          model = get_user_model()
          fields = ('email', 'first_name', 'last_name') 
  ```

  * `get_user_model()`: 현재 프로젝트에서 활성화된 사용자 모델을 반환한다. django는 user 클래스를 직접 참조하는 대신 `django.contrib.auth.get_user_model()`을 사용하여 참조해야 한다고 강조한다. 
  
  ```python
  # accounts/views.py
  from django.contrib.auth.decorators import login_required
  from .forms import CustomUserChangeForm
  
  @login_required
  @require_http_method(['GET', 'POST'])
  def update(request):
  	if request.method == "POST":
          form = CustomChangeForm(request.POST, instance=request.user)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      else:
          form = CustomUserChangeForm(instance=request.user)
      context = {
          'form':form,
      }
      return render(request,'accounts/update.html', context)
  ```

#### 4. 비밀번호 변경

* 비밀번호 변경은 **PasswordChangeForm**을 사용한다. 

  사용자가 비밀번호를 변경할 수 있도록 하는 form으로 이전 비밀번호를 입력하여 비밀번호를 변경할 수  있도록 한다. 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPassWordForm을 상속받는 서브 클래스를 사용할 수 있다. 

  ```python
  # urls.py
  
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('signup/', views.signup, name='signup'),
  path('delete/', views.delete, name='delete'),
  path('update/', views.update, name='update'),
  path('password/', views.change_password, name='change_password'),
  ```

  ```django
  <!-- accounts/change_password.html -->
  
  {% extents 'base.html' %}
  
  {% block content %}
  	<h1>비밀번호 변경</h1>
  	<form action="{% url 'accounts:change_password' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
  	</form>
  {% endblock content %}
  ```

  * 암호 변경 시 세션 무효화 방지 `update_session_auth_hash(request, user)` 현재 요청과 새 session hash가 파생 될 업데이트 된 사용자 객체를 가져오고, session hash를 적절하게 업데이트 한다. 비밀번호가 변경되면 기존 세셔과의 회원 인증 정보가 일치하지 않으므로 로그인상태를 유지할 수 없기 때문이다. 암호가 변경되어도 로그아웃되지 않도록 새로운 password hash로 session을 업데이트 한다. 

  ```python
  # accounts/views.py
  from django.contrib.auth.forms import AuthenticationForm, UserCreationFroem, UserChangeForm, PasswordChangeForm,
  from django.contrib.auth import update_session_auth_hash
  
  @login_required
  @require_http_method(['GET', 'POST'])
  def change_password(request):
      if request.method == 'POST':
          form = PasswordChangeForm(request.user, request.POST)
          if form.is_valid():
              form.save()
              update_session_auth_hash(request, form.user)
              return redirect('articles:index')
      else:
          form = PasswordChangeForm(request.user)
      context = {
          'form': form,
      }
      return render(request, 'accounts/change_password.html', context)
  ```

  
