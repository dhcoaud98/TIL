# 03.03

## Django



:mortar_board: **Django Template Language(DTL)**

 Django Template에서 사용하는 Built-in template system이다. **조건, 반복, 변수 치환, 필터**등의 기능을 제공한다. Django가 python으로 작성된 프레임 워크 이기 때문에 python 처럼 봉지만 python이라고 할 수 없다. 

:star2: DTL syntax

1. Variable (변수)

```python
{{ variable }}

template에서 작성하는 것으로 render()에서 작성하면 된다. 특히 render()의 세번째 인자로 {'key':value}와 같이 딕셔너리 형태로 넘겨줄 수 있다. 'key'값이 template에서 사용 가능한 변수명이 된다. 
```

2. Filter(필터)

```python
{{ variable|filter }}

ex) {{ variable|lower }} : 모두 소문자로 출력
60개의 built-in template filters를 제공하며 공식문서를 통해 사용가능
```

3. Tags(태그) : 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일을 함

```python
{% tag %}
{% if %}{% endif %}
{% for %}{% endfor %}
...
```

4. Comment(주석)

```python
{# #}
{% comment %}
    주석
    주석
{% endcomment %}
```



---

:pushpin: **코드 작성 순서** :pushpin:

1. urls.py
2. views.py
3. templates



** **중요** **

1. /throw/ url로 요청을 보냄
2. django의 /throw/ urls.py가 throw view함수를 호출 -> throw 템플릿을 응답
3. throw 템플릿을 응답 받아서 화면을 볼 수 있음
4. throw 템플릿의 form 태그를 통해 데이터를 /catch/로 submit(제출)
5. django의 /catch/ urls.py가 catch view함수를 호출
6. catch view함수는 요청 객체의 데이터를 추출
7. catch view함수는추출한 데이터와 함께 catch템플릿을 응답(렌더링)
8. 클라이언트는  응답 받은 catch 템플릿을 보게 됨
