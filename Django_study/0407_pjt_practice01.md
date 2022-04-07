# 04.07

## pjt_django 혼자 만들기

<br>

[TOC]

<br>

---

:star: 모든 과정과 순서는 `TIL`문서의 `0406_pjt`를 기본으로 확인하면 된다. 

1. `urls.py`

   ```python
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

2. `views.py`

   ```python
   from django.shortcuts import render, redirect
   from .models import Article
   
   # Create your views here.
   def index(request):
       articles = Article.objects.all()
       content = {
           'articles': articles,
       }
       return render(request, 'articles/index.html', content)
   
   def new(request):
       return render(request, 'articles/new.html')
   
   def create(request):
       title = request.POST.get('title')
       content = request.POST.get('content')
   
       # 생성, 저장
       article = Article(title=title, content=content)
       article.save()
       content = {
           'article':article, 
       }
       return redirect('articles:index')
   
   def detail(request, pk):
       article = Article.objects.get(pk=pk)
       content = {
           'article': article,
       }
       return render(request, 'articles/detail.html', content)
   
   def delete(request, pk):
       article = Article.objects.get(pk=pk)
       if request.method == 'POST':
           article.delete()
           return redirect('articles:index')
       else:
           return redirect('article:detail', article.pk)
           # return redirect('articles:index')
   
   def edit(request, pk):
       article = Article.objects.get(pk=pk)
       content = {
           'article':article,
       }
       return render(request, 'articles/edit.html', content)
   
   def update(request, pk):
       article = Article.objects.get(pk=pk)
       article.title = request.POST.get('title')
       article.content = request.POST.get('content')
       article.save()
       return redirect('articles:detail', article.pk)
   ```

3. `html`

   ```django
   <!-- index -->
   
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>REVIEW</h1>
     <h2>작성자 : 오채명</h2>
     <a href="{% url 'articles:new' %}">NEW</a>
     <hr>
     {% for article in articles %}
       <p> {{ article.pk }}</p>
       <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
       <p> {{ article.title }}</p>
       <p> {{ article.content }}</p>
       <hr>
     {% endfor %}
   {% endblock %}
   ```

   ```django
   <!-- new -->
   
   {% extends 'base.html' %}
   
   {% block content %}
     <h2>NEW</h2>
     <hr>
     <form action="{% url 'articles:create' %}" method='POST'>
       {% csrf_token %}
       <label for="title">Title: </label>
       <input type="text" name="title" id="title"><br>
       <label for="content">Content: </label>
       <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
       <input type="submit">
     </form>
     <a href="{% url 'articles:index' %}">뒤로</a>
   {% endblock %}
   ```

   ```django
   <!-- detail -->
   
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>{{ article.pk }}</h1>
     <h3>작성자 : 오채명</h3>
     <hr>
       <p> {{ article.pk }}</p>
       <p> 제목 : {{ article.title }}</p>
       <p> 내용 : {{ article.content }}</p>
       {% comment %} <p> 작성시간: </p> {% endcomment %}
       {% comment %} <form action="{% url 'articles:delete' article.pk %}" method="POST">
         {% csrf_token %}
         <input type="submit" value="삭제">
       </form> {% endcomment %}
       <form action="{% url 'articles:delete' article.pk %}" method="POST">
       	{% csrf_token %}
         <button class="btn btn-danger"> 삭제 </button>
   	  </form>
       <a href="{% url 'articles:edit' article.pk %}" class="btn btn-primary"> 수정 </a><br>
       <a href="{% url 'articles:index' %}" class="btn btn-primary"> 뒤로 </a>
       <hr>
   {% endblock %}
   ```

   ```django
   <!-- edit -->
   
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
     <a href="{% url 'articles:detail' article.pk %}"> 뒤로 </a>
   {% endblock content %}
   ```

   
