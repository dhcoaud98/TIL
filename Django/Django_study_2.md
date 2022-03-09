# 03.09

## Django Model

<br>

### Model

"웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구이다."

1. models.py 

   클래스 함수를 작성할 수 있는 곳으로 이 곳에서 'title', 'content' 등의 행 제목을 가진 테이블을 생성시킬 수 있다.  테이블 생성 후 데이터는 `views.py`에서 작성할 수 있다. 

   ```python
   # articles/models.py
   
   class Article(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField() 
       created_at = models.DateTimeField(auto_now_add = True)
       updated_at = models.DateTimeField(auto_now = True)
   ```

2. 데이터베이스(DB) : 체계화된 데이터의 모임.

3. 퀴리(Query) : 데이터를 조회하기 위한 명령어. 조건에 맞는 데이터를 추출하거나 조작하는 명령어로 `Query를 날린다 == DB를 조작한다. `라는 의미이다. 

   ```bash
   $  
   $
   $
   $
   ```

4. **Database의 기본구조**

   1) 스키마: structure, 데이터베이스에서 자료의구조, 표현방법, 관계 등을 정의한 구조

      :star: (jupyter Notebook에서 보여지는 흰색, 회색의 테이블이라고 생각하면 된다. 다음과 같은 구조로 이루어져 있다. 

      | column | datatype |
      | :----: | :------: |
      |   id   |   INT    |
      |  age   |   INT    |
      | phone  |   TEXT   |
      |  ...   |   ...    |

   2) 테이블: 열(필드field, 속성)과 행(레코드record, 튜플)로 이루어진다. SQL 데이터베이스에서는 테이블을 관계라고도 한다. 행의 갯수는 맨 위의 제목칸을 제외하고 나머지를 세어야 한다. 

   3) PK(기본키) : 행의 고유값으로 반드시 설정해야한다. id와 비슷하게 접근하면 된다.





