# 03.11

## Django Model

<br>

[TOC]

<br>

### 기본 세팅

1. `pjt05` 폴더 생성

2. `.gitignore.py` 파일 생성 : git에 push 할때 빼고 올릴 list 작성

3. 주어진 `requirements.txt`파일이 있다면 다음 명령어로 설치

   ```bash
   $ pip install -r requirements.txt
   ```

4. 가상환경 설치 후 실행

5. `vscode` 열기

6. 프로젝트, 어플리케이션 생성

7. `base.html` 만들고, 설정하기

8. 어플리케이션 `urls.py` 만들기 

   ```python
   # app_name/urls.py
   
   from django.urls import path
   from . import views
   
   app_name = 'movies'
   urlpatterns = [
       ...
   ]
   ```

9. `model`을 만들기 위해 `views.py`에 `import` 할 것

   ```python
   from django.shortcuts import render, redirect
   from .models import Movie
   ```

   

