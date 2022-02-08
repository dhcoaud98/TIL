# Bootstrap study



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

    

2. 컨테이너(containers) : 가장 기본적인 레이아웃 요소이며 **기본 그리드 시스템을 사용할 때** 필요하다. 

   ```python
   .container : 각 반응형 중단점에 max-width를 설정한다. 
   .container-fluid : 모든 중단점에 width: 100%를 설정한다. 
   .container-{breakpoint} : 정의된 중단점까지 width: 100%를 설정한다. {breakpoint}를 넘으면 width: 100%가 아닌 기본 지정 값이 된다. 
   ```

    

3. :star2: 그리드 시스템(Grid system) :  flexbox 그리드를 사용하여 12개의 열 시스템, 6개의 기본 반응형 계층 등 사전 정의된 클래스로 모양과 크기의 레이아웃을 빌드할 수 있다. 

   ```python
   <div class="container">
     <div class="row">
       <div class="col-6">                    ------- (1)
         Column
       </div>
       <div class="col">                    ------- (2)
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

