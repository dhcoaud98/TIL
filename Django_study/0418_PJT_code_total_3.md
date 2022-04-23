# 04.18

## PJT 대비_3 (Like + Profile + Follow)

[TOC]

<br>

### 1. Like + Profile + Follow

```python
# articles/models.py

class Article(models.Model):
    user = models.ForiegnKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
     
    
# accounts/models.py
class User(AbstractUser):
    # symmetrical=False로 둔 이유는 팔로우하면 자동으로 맞팔로우를 만들지 않기 위해
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')  
    ...
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

```python
# articles/urls.py

urlpattenrs = [
    ...
    path('<int:article_pk>/likes/', views.likes, name='likes'),  # 좋아요
]
```

```python
# accounts/urls.py

urlpattenrs = [
    ...,
    path('<username>/', views.profile, name='profile'), # 프로필
    path('<int:user_pk>/follow/', views.follow, name='follow'),  # 팔로우
]
```

```python
# articles/views.py

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:  # 로그인 된 사용자라면?
        article = get_object_or_404(Article, pk=article_pk)
        
        # 좋아요 취소(좋아요 목록에 있는데, 좋아요를 한번 더 눌렀다면 좋아요 취소)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        # 좋아요 
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')
```

```python
# accounts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from dhabgi,dibtrub.auth import get_user_model

@require_POST
def follow(request, user_pk):
    if request.user.is_auenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        if person != request.user:  # 내가 아닌 다른 사람의 일때만
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                persom.followers.add(request.user)
        return redirect('accounts:profile', person.username)  # 나라면?
    return redirect('accounts:login')


def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

```django
<!-- articles/index.html -->


...
<div>
  <form action='{% url 'articles:likes' article.pk %}' method="POST">
    {% csrf_token %}
    {% if user in article.like_users.all %} 
      <input type='submit' value="좋아요 취소">
    {% else %}
      <input type='submit' value="좋아요">
    {% endif %} 
  </form>      
</div>
```

```django
<!-- accounts/profile.html -->
<!-- profile 페이지에 팔로우와 언팔로우 버튼 작성
1. 팔로잉 수/팔로워 수 출력
2. 자기 자신을 팔로우 할 수 없음 -->

{% extends 'base.html' %}

{% block content %}
<h1>{{ person.username }}님의 프로필</h1>

<div>
  <div>
    팔로잉 : {{ person.followerings.all|length }} / 팔로워 : {{ person.followers.all|length }}    
  </div>
  {% if user != person %}
    <div>
      <form action='{% url 'accounts:follow' person.pk %}' method='POST'>
        {% csrf_token %}
        {% if user in person.followers.all %}
          <input type='submit' value='Unfollow'>
        {% else %}
          <input type='submit' value='Follow'>
        {% endif %}
      </form>
    </div>
  {% endif %}
</div>
<hr>
<!-- with 사용 할 수도 있음. --> 

<h2>{{ persen.username }}'s 게시글</h2>
{% for comment in person.comment_ser.all %}
  <div>{{ comment.title }}</div>
{% endfor %}

<hr>

<h2>{{per.username }}'s 댓글</h2>
{% for comment in person.comment_ser.all %}
  <div>{{ comment.content }}</div>
{% endfor %}

<hr>

<h2>{{per.username }}'s 좋아요한 게시글</h2>
{% for article in person.like_articles.all %}
  <div>{{ article.title }}</div>
{% endfor %}

<hr>

<a href='{% url 'articles:index' %}'>back</a>
{% endblock %}
```

```django
<!-- base.html -->

<body>
  <div class='container'>
    {% if request.user.is_authenticated %}
      <h3>Hello, {{ user }}</h3>
      <a href="{% url 'accounts:profile' user.username %}">내 프로필</a>
      ...
  </div>
  ...
</body>
```

```django
<!-- articles/index.html -->
<!-- index 페이지에 작성자 이름 누르면 프로필로 넘어감 -->

<p>
  <b>작성자 : <a href='{% url 'accounts:profile' article.user.username %}'>{{ article.user }}</a></b>
</p>
```





<br>



