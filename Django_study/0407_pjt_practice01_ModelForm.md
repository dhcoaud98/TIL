# 04.07

## pjt_django_ModelForm 혼자하기

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
       # path('new', views.new, name='new'),
       path('create', views.create, name='create'),
       path('<int:pk>/detail', views.detail, name='detail'),
       path('<int:pk>/delete', views.delete, name='delete'), 
       # path('<int:pk>/edit', views.edit, name='edit'),
       path('<int:pk>/update', views.update, name='update'),
   ]
   ```

2. `views.py`

   ```python
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

3. `html`

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
   {% endblock %}
   
   ```
   
   ```django
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
   {% endblock %}
   ```
   
   ```django
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
   {% endblock %}
   ```
   
   ```django
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
   
   4. `model`
   
   ```python
   from django.db import models
   
   # Create your models here.
   class Article(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   ```
   
   

