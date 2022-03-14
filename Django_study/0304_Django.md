# 03.04

## Django



:mortar_board: **url 요청과 응답** :pushpin: 

```python
import requests   # $ pip install requests 해야함

url = ''

(1)
response = requests.get(url)
lotto = response.json()

(2)
response = requests.get(url, params=params).json()
lott = response.get('')
```

위의 방법으로 url을 요청하고, 응답 받을 수 있다. 



:seedling: 오늘 중요한 부분!! 특히 .gitignore 사용법 기억하기 

1. 가상환경 설정하기

   * 바탕화면에 새로운 폴더 생성

   * git bash 열고 가상환경 만들기

     ```python
     python -m venv venv
     ```

   * 가상 환경 활성화하기

     ```python
     source venv/Scripts/activate
     ```

   * 가상환경의 `list`확인하고, 설치하기

     ```python
     pip list
     pip install -r requirements.txt
     ```

2. `.gitignore`사용하기

   * `gitignore.io`에서 생성 후 파일의 최상단에 작성하면됨!
   * `gitignore`는 push 이전에 작성해주어야 함



:mortar_board: **TMDB 사용하기**(인터넷에서 정보 가져오기)

```python
API_KEY = ''  # 로그인 후 사용
BASE_URL = ''

params = {
    'api_key': API_KEY,
    'page': 1, 
}  # 필수 인자들 확인 후 가져오면 됨.

response = requests.get(BASE_URL, params=params).json()
movie_list = response.get('results')[:6]
```

