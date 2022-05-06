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
   ```

   ```bash
   $ python manage.py migrate
   ```

   * oauth2 검색 
