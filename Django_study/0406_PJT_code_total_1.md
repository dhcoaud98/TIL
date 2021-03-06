# 04.06

## PJT 대비_1

[TOC]

<br>

### 1. 기본 셋팅

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
   $ pip install -r requirements.txt
   $ pip freeze > requirements.txt
   ```

   :seedling: `$ pip list` 작업은 시작할 때 꼭 확인해 주는 것이 좋다. 로컬 환경에서 시작하지 않도록 해준다. 

4. `.gitignore`사용

   * `gitignore.io`에서 생성 후 파일의 최상단에 작성하면됨!
   * `gitignore`는 push 이전에 작성해주어야 함

5. Project 생성

   ```bash
   $ django-admin startproject <프로젝트 명> .
   $ python manage.py runserver
   ```

   :seedling: 프로젝트 명 뒤에 한칸 띄어쓰기 후 `.`을 꼭 써주어야 한다. 

   서버 활성화 후에 로켓 확인하기!

6. Application 생성

   ```bash
   $ python manage.py startapp <articles>
   ```

   :seedling: 하나의 프로젝트는 여러개의 앱을 가질 수 있다. 

7. Application 등록

   반드시 app 생성 후에 등록하기!! 등록은 project의 `settings.py`에서 할 수 있다. 

   ```python
   INSTALLED_APPS = [
   	'articles',
       ...,
   ]
   ```

   <br>

### 2. Django_01(model 사용전)

8. URL 분리(앱 폴더에 urls.py 생성)

   :seedling: 앱 폴더에 urls.py 새롭게 생성 해서 url을 작성하는데, 프로젝트에서 앱의 urls.py에  접근하기 위해 (1)의 부분을 작성해야 한다. 

   ```python
   # 앱 urls.py
   # articles/urls.py
   
   from django.urls import path
   from . import views  # 본인의 경로라는 의미에서 .을 사용한다.
   ```

   ```python
   # 프로젝트 urls.py
   # firstpjt/urls.py
   
   from django.urls import path, include   ---(1)
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('articles/', include('articles.urls')),
       path('pages/', include('pages.urls')),
   ]
   ```

9. **URL namespace** 와 **Naming URL patterns**

   ```python
   # articles/urls.py
   
   app_name = 'articles'   # (1) URL namespace
   urlpatterns = [
       path('index/', views.index, name='index'),   # (2) Naming URL patterns
       path('greeting/', views.greeting, name='greeting'),
       path('dinner/', views.dinner, name='dinner'),
   	...
   ]
   ```

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
   
   <!-- 
   (1) URL namespace의 경우 : 연산자를 사용하여 접근할 것
   (2) Naming URL patterns의 경우 a 태그를 사용하여 접근 할 것
   (1)과 (2)는 함께 사용하기
   -->
   ```

<br>

### 3. Django_02(Model 생성 + CRUD)

1. **models.py** 작성

   ```python
   class Article(models.Model):
   	title = models.CharField(max_length=10)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
       
   """
   created_at 필드에 대한 default 값 설정 -> 1 입력 후 enter
   timezone.now 함수 값 자동 설정 -> 빈 값 상태에서 enter -> migrate를 통해 models.py 수정사항 반영
   """
   ```
   
2. **makemigraions**

   모델의 변경사항을 저장. 설계도 만들기

   ```bash
   $ python manage.py makemigrations
   ```

3. **migrate**

   DB에 반영

   ```bash
   $ python manage.py migrate
   ```

   ```bash
   $ python manage.py sqlmigrate app_name 0001
   $ python manage.py showmigrations
   ```

4. **CRUD** 작성하기!

   | 순서 | 과정                                                    |
   | ---- | ------------------------------------------------------- |
   | 1    | 다음과 같이 **urls.py**에 먼저 작성되어야 한다.         |
   | 2    | 해당 urls을 활성화 시키기 위해 **views.py**에 함수 작성 |
   | 3    | **.html** 작성                                          |

5. **URL**

   :seedling: Read

   ```python
   path('index/', views.index, name='index')
   ```

   :seedling: Create

   ```python
   path('new/', views.new, name='new'),
   path('create/', views.create, name='create'),
   path('<int:pk>', view.detail, name='detail'),
   ```

   :seedling: Delete

   ```python
   path('<int:pk>/delete/', views.delete, name='delete')
   ```

   :seedling: Update

   ```python
   path('<int:pk>/edit/', views.edit, name='edit')
   path('<int:pk>/update/', views.update, name='update')
   ```

   ```python
   # 전체 코드
   from . import views
   from django.urls import path
   # 자기 자신의 경로라는 의미에서 .을 사용한다. 
   
   # URL namespace
   app_name = 'articles' 
   urlpatterns = [
       path('', views.index, name='index'),  # 가장 기본 페이지
       path('new', views.new, name='new'),
       path('create', views.create, name='create'),
       path('<int:pk>/detail', views.detail, name='detail'),
       path('<int:pk>/delete', views.delete, name='delete'), 
       path('<int:pk>/edit', views.edit, name='edit'),
       path('<int:pk>/update', views.update, name='update'),
   ]
   ```

   ```python
   # <app_name>/views.py
   from django.shortcuts import render, redirect
   from .models import Article
   
   # 조회
   def index(request):  
   	articles = Article.objects.all()
       content = {
       	'articles': articles,
       	}
       return render(request, 'articles/index.html', context)
   
   # 새로운 것을 작성하겠다는 버튼 만들기 - 작성 후 누르면 create로 넘어간다. 
   def new(request):  
       return render(request, 'articles/new.html')
   
   def create(request):
       # new.html에서 작성한 내용을 가지고 오겠다. 
       title = request.POST.get('title')
       content = request.POST.get('content')
       
       # 생성, 저장
       article = Article(title=title, content=content)
       article.save()
       
       # return render(request, 'articles/create.html')
       # return redirect('article:index')
   	return redirect('article:detail', article.pk)
   
   # 특정 pk값의 속성을 조회
   def detail(request, pk):
   	article = Article.objects.get(pk=pk)
       content = {
           'article': article,
       }
       return render(request, 'articles/detail.html', context)
   
   def delete(request, pk):
   	article = Article.objects.get(pk=pk)
       if request.method == 'POST':  # POST라면 삭제 
   	    article.delete()
       	return redirect('articles:index')
       else:  # 아니라면 detail page 조회
           return redirect('articles:detail', article.pk)
       
   def edit(request, pk):
       article = Article.objects.get(pk=pk)
       context = {
           'article': article,
       }
       return render(request, 'articles/edit.html', context)
   
   def update(request, pk):
       article = Article.objects.get(pk=pk)
       article.title = request.POST.get('title')
       article.content = request.POST.get('content')
       article.save()
       return redirect('articles:detail', article.pk)
   ```

4. **HTML**

   1. `base.html` 작성
   
   ```django
   <!-- templates/base.html -->
   
   <body>
       {% block content %}
       {% endblock %} 
   </body>
   ```
   
   ```django
   # 자식 템플릿
   {% extends 'base.html' %}
   
   {% block content %}
   <!--내용 작성-->
   {% endblock %}
   ```
   
   2. `SETTINGS.py`에 경로 지정

   ```python
   TEMPLATES = [
       {
          ...
          'DIRS': [BASE_DIR/ 'templates'],
          ... 
       }
   ]
   ```
   
   3. 차례로 `html` 작성
   
   ```django
   <!-- templates/articles/index.html -->
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>REVIEW</h1>
     <h2>작성자 : 오채명</h2>
     <a href="{% url 'articles:new' %}">NEW</a>
     <hr>
     {% for article in articles %}
   	<p>{{ article.pk }}</p>
   	<p>{{ article.title }}</p>
   	<p>{{ article.content }}</p>
   	<a href="{% url 'articles:detail' article.pk %}">[detail]</a>
     {% endfor %}
   {% endblock %}
   ```
   
   ```django
   <!-- templates/articles/new.html -->
   
   {% extends 'base.html' %}
   
   {% block content %}
   <h1 class="text-center">NEW</h1>
   <hr>
   <!-- form의 형태를 사용함 -->
   <form action="{% url 'articles:create' %}" method='POST'>
       <label for="title">Title: </label>
       <input type="text" name="title"><br>
       <label for="content">Content: </label>
       <textarea name="content" cols="30" rows="5"></textarea><br>
       <input tye='submit'>
   </form>
   <a href="{% url 'articles:index '%}">뒤로</a>
   {% endblock %}
   ```
   
   ```django
   <!-- templates/articles/detail.html -->
   
   {% extends 'base.html' %}
   
   {% block content %}
     <p>제목 : {{ article.title }}</p>
     <p>내용 : {{ article.content }}</p>
     <a href="{% url 'articles:index' %}" class="btn btn-primary">[뒤로]</a>4
     <form action="{% url 'articles:delete' article.pk %}" method="POST">
       {% csrf_token %}
       <button class="btn btn-danger">[삭제]</button>
     </form>
     <a href="{% url 'articles:edit' article.pk %}" class="btn btn-primary">[수정]</a>
     <hr>
   {% endblock %}
   ```
   
   :small_red_triangle: 삭제 버튼은 `detail`에 있어도 `edit`에 잇어도 됨
   
   ```django
   <!-- templates/articles/edit.html -->
   
   {% extends 'base.html' %}
   
   
   {% block content %}
     <h1>EDIT</h1>
     <hr>
     <form action="{% url 'articles:update' article.pk %}" method="POST">
       {% csrf_token %}
       <label for="title">Title: </label>
       <input type="text" id="title" name="title" value="{{ article.title }}"><br>
       <label for="content">Content: </label>
       <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea>
       <input type="submit">
     </form>
     <a href="{% url 'articles:detail' article.pk %}">back</a>
   {% endblock content %}
   ```

<br>

### 4. Django_03(Model Form)

* 지금까지의 **CRUD**를 **ModelForm**을 이용해 구현하기

1. `forms.py`만들기

   ```python
   # forms.py
   
   from .models import Article
   
   class ArticleForm(forms.ModelForm):
   
       class Meta:
           model = Article
           fields = '__all__'
   ```
   
2. `views.py` 수정하기

   * new 함수 삭제
   * new path 삭제
   * `new.html`을 `create.html`로 변경 
   * edit path 삭제
   * edit 함수 삭제
   * `edit.html`을 `update.html`로 변경!!

   ```python
   from .forms import ArticleForm
   
   
   def create(request):
       if request.method == 'POST':
       	form = ArticleForm(request.POST)
       	if form.is_valid():  # 유효성 검사
           	article = form.save()
           return redirect('articles:detail', article.pk)
       
       else: 
           form = ArticleForm()
       context = {
           'form': form,
       }  # if문 안의 if문을 통과하지 못한경우 context로 넘어옴
       return render(request, 'articles/create.html', context)
   
   def update(request, pk):
       # 기존의 글을 수정하는 것 이므로 form 대신 article을 사용한다. 
       article = Articls.objects.get(pk=pk)  # 조회
       if request.method == 'POST':
           form = ArticleForm(request.POST, instance=article)
           if form.is_valid():
               form.save()
               return redirect('articles:detail', article.pk)
       else:
           form = ArticleForm(instance=article)
       context = {
           'form': form,
           'article': article,
       }
       return render(request, 'articles/update.html', context)
   
   def delete(request, pk):
       # 기존의 글을 삭제하는 것 이므로 form 대신 article을 사용한다. 
       article = Article.objects.get(pk=pk)
       if request.method == 'POST':
           article.delete()
           return redirect('articles:index')
   
       return redirect('articles:detail', article.pk)
   ```

   ```python
   # 전체 코드
   from django.shortcuts import render, redirect
   from .models import Article
   from .forms import ArticleForm
   
   
   # Create your views here.
   def index(request):
       articles = Article.objects.all()
       content = {
           'articles': articles,
       }
       return render(request, 'articles/index.html', content)
   
   def create(request):
       # 새로운 값을 작성 하므로 form 사용
       if request.method == 'POST':  # 기존 create 함수
           form = ArticleForm(request.POST)
           if form.is_valid():  # 유효성 검사
               article = form.save()
           	return redirect('articles:detail', article.pk)
       else:  # 기존 new 함수
           form = ArticleForm()
       content = {
           'form':form,
       }
       return render(request, 'articles/create.html', content)
   
   def detail(request, pk):
       article = Article.objects.get(pk=pk)
       content = {
           'article': article,
       }
       return render(request, 'articles/detail.html', content)
   
   def delete(request, pk):
       # 기존의 값을 삭제하므로 article 사용
       article = Article.objects.get(pk=pk)
       if request.method == 'POST':
           article.delete()
           return redirect('articles:index')
       else:
           return redirect('article:detail', article.pk)
           # return redirect('articles:index')
   
   def update(request, pk):
       # 기존의 값을 수정하므로 article 사용
       article = Article.objects.get(pk=pk)
       if request.method == 'POST':  # 기본 update 함수
           form = ArticleForm(request.POST, instance=article)
           if form.is_valid():
               form.save()
               return redirect('articles:detail', article.pk)
       else:  # 기존 edit 함수
           form = ArticleForm(instance=article)
       content = {
           'form': form,
           'article': article,
       }
       return render(request, 'articles/update.html', content)
   ```

3. `'html` 수정하기

   ```django
   <!-- index -->
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>REVIEW</h1>
     <h2>작성자 : 오채명</h2>
     <a href="{% url 'articles:create' %}">CREATE</a>
     <hr>
     {% for article in articles %}
       <p>글번호 : {{ article.pk }}</p>
       <a href="{% url 'articles:detail' article.pk %}"> 세부사항 </a>
       <p>글 제목 : {{ article.title }}</p>
       <p>글 내용 : {{ article.content }}</p>
       <hr>
     {% endfor %}
   {% endblock content %}
   
   
   <!-- create -->
   {% extends 'base.html' %}
   
   {% block content %}
     <h2>NEW</h2>
     <hr>
     <form action="{% url 'articles:create' %}" method='POST'>
       {% csrf_token %}
       {{ form.as_p }}   
       <input type="submit">
     </form>
     <a href="{% url 'articles:index' %}">뒤로</a>
   {% endblock content %}
   
   <!-- detail -->
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>{{ article.pk }}</h1>
     <h3>작성자 : 오채명</h3>
     <hr>
       <p>글 번호 : {{ article.pk }}</p>
       <p>글 제목 : {{ article.title }}</p>
       <p>글 내용 : {{ article.content }}</p>
       <form action="{% url 'articles:delete' article.pk %}" method="POST">
       	{% csrf_token %}
         <button class="btn btn-danger"> 삭제 </button>
   	  </form>
       <a href="{% url 'articles:update' article.pk %}" class="btn btn-primary"> 수정 </a><br>
       <a href="{% url 'articles:index' %}" class="btn btn-primary"> 뒤로 </a>
       <hr>
   {% endblock content %}
   
   <!-- update -->
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>EDIT</h1>
     <hr>
     <form action="{% url 'articles:update' article.pk %}" method="POST">
       {% csrf_token %}
       {{ form.as_p}}
       <input type="submit">
     </form>
     <a href="{% url 'articles:detail' article.pk %}"> 뒤로 </a>
   {% endblock content %}
   ```

   <br>

### 5. Admin 

1. **Automatic admin interface**

   사용자가 아닌 서버의 관리자가 활용하기 위한 페이지이다. model class를 admin.py에 등록하고 관리한다. 레코드 생성 여부 확인에 매우 유용하며, 직접 레코드를 삽입할 수도 있다. 

2. **admin 생성**

   ```bash
   $ python manage.py createsuperuser
   ```

   관리자 계성 생성 후 서버를 실행한 다음 '/admin'으로 가서 관리자 페이지 로그인한다.

   비밀번호는 보호를 위해 화면에 나타나지 않지만 제대로 입력 되고 있는 것이다. 

3. **admin 등록**

   admin.py는 관리자 사이트에 Article 객체가 관리가 인터페이스를 가지고 있다는 것을 알려준다. 

   ```python
   # movies/admin.py
   
   from django.contrib import admin
   from .models import Article
   
   class ArticleAdmin(admin.ModelAdmin):
       list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
   
   # admin site에 register 하겠다. 
   admin.site.register(Article, ArticleAdmin)
   ```
   
   'list_display'는 models.py에서 정의한 각각의 속성(컬럼)들의 값(레코드)을 admin 페이지에 출력하도록 설정
