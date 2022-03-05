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
   $ python manage.py startapp <앱 명>
   ```

   :seedling: 하나의 프로젝트는 여러개의 앱을 가질 수 있다. 

6. Application 등록

   반드시 app 생성 후에 등록하기!! 등록은 project의 `settings.py`에서 할 수 있다. 

   ```python
   INSTALLED_APPS = [
   	'articles',
       ...
   ]
   ```

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

