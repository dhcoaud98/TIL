# Bootstrap study

이곳은 Bootstrap을 공부하고, 기록하는 곳입니다.

-----

   

### 1. 레이아웃

 

1. 중단점(Breakpoint) : **반응형** 레이아웃을 만들때 사용된다. 뷰포트의 크기에 따라서 어떻게 동작할지 결정된다. 다음과 같이 6 종류의 중단점이 있고, 상황에 맞게 **클래스 중위표기**를 사용해 사용해주면 된다. 

   ```python
   X-Small					없음			   <576px
   Small					sm				>=575px
   Medium					md				>=768px 
   Large					lg				>=992px
   Extra large				xl				>=1200px
   Extra extra large		xxl				>=1400px
   ```

    

2. 컨테이너(containers) : 가장 기본적인 레이아웃 요소이며 **기본 그리드 시스템을 사용할 때** 필요하다.  grid 사용시 부모 요소로서 사용하면 된다. 

   ```python
   .container : 각 반응형 중단점에 max-width를 설정한다. 
   .container-fluid : 모든 중단점에 width: 100%를 설정한다. 
   .container-{breakpoint} : 정의된 중단점까지 width: 100%를 설정한다. {breakpoint}를 넘으면 width: 100%가 아닌 기본 지정 값이 된다. 
   ```

    

3. :star2: 그리드 시스템(Grid system) :  flexbox 그리드를 사용하여 12개의 열 시스템, 6개의 기본 반응형 계층 등 사전 정의된 클래스로 모양과 크기의 레이아웃을 빌드할 수 있다. 

   ```python
   <div class="container">
     <div class="row row-cols-2">                      ------- (3)
       <div class="col-6">                             ------- (1)
         Column
       </div>
       <div class="col col-lg-2">                    ------- (2)
         Column
       </div>
       <div class="col">
         Column
       </div>
     </div>
   </div>
   ```

   가장 기본 적인 형태의 `그리드 시스템`의 예이다.

   (1) 세개의 `box`중 첫째 `box`의 열 너비는 6으로 지정해주었으므로 나머지는 자동으로 3이 된다.
   
   (2) 가변너비시스템 :`col col-lg-2`는 기본적으로 `col`이라는 속성으로 자동 배치 되다가 뷰표인트가 lg를 넘어가면 2이 배치된다.
   
   (3) 반응형 `.row-cols-*`를 통해 열의 갯수를 지정할 수 있다. 
   
   (4) `auto`를 사용하면 열에 자연스러운 너비를 지정할 수 있다.
   
   ```python
   <div class="container">
     <div class="row">
       <div class="col-sm-3">
         Level 1: .col-sm-3
       </div>
       <div class="col-sm-9">
         <div class="row">
           <div class="col-8 col-sm-6">
             Level 2: .col-8 .col-sm-6
           </div>
           <div class="col-4 col-sm-6">
             Level 2: .col-4 .col-sm-6
           </div>
         </div>
       </div>
     </div>
   </div>
   ```
   
   (5) 위와 같이 하나의 `column` 안에 `row`를 또 사용하여 중첩할 수 있다.  
   
    

4. 정렬 : flexbox 정렬 유틸리티를 사용하여 가로나 세로로 열을 정렬한다. Bootstrap, css파일 등에 따라 사용하는 형태가 약간씩 달라지기 때문에 잘 확인하고 찾아본 후 사용해야한다. 

   ```python
   * 배치 설정 
   	1. flex-direction : row, row-reverse, column, column-reverse
       2. flex-wrap : wrap, nowrap
   * 공간 나누기 (flex-direction의 방향에 따라서 생각하기!)
   	1. justify-content : flex-start, flex-end, flex-center, space-between, space-around, space-evenly
       2. align-content : flex-start, flex-end, flex-center, space-between, space-around, space-evenly
   * 정렬
   	1. align-items : strech, flex-start, flex-end, flex-center
       2. align-self : strech, flex-start, flex-end, flex-center
   * 기타
   	1. flex-grow : 남은 영역을 아이템에 분배
       2. order : 배치 순서
   ```

​    

5.  열 오프셋(offset) : 오프셋을 사용하면 빈칸을 만들 수 있다. 

   ```python
   <div class="col-md-4 offset-md-2"></div>
   ```

   4개의 열을 포함한 하나의 box 앞에 2개의 열만큼의 공백을 만든다.

  

6. CSS 그리드 : `.g-col-6`과 같이 사용할 수 있다. 부모 요소에 class="gird" 속성을 넣어 주어야 한다. 

  

  

-----

### 2. 컴포넌트

 

1. 
