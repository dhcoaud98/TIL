# 2장 Artificial Intelligence Basic



## 1. 기계 학습의 구성요소

1. 경험 사례 (ex. data)
2. 모델 (ex. 인공신경망)
3. 평가기준

### 1. 기계학습이란 무엇인가?

![image-20220825100656641](2장 Artificial Intelligence Basic.assets\image-20220825100656641.png)

* **계산/추론** : 함수를 주고, output이 나오도록 계산
* **최적화** : 한 세트의ㅁ(input, output)을 주고, 관계를 가장 잘 설명하는 f를 찾는 것.

* **일반화** : 학습데이터가 아닌 새로운 데이터를 넣어도 올바른 값이 나오도록 하는 것.



### 2. 가장 좋은 모델 f(x)은 어떻게 찾을 수 있을까?

* Annotation을 통한 학습으로 이루어짐

  <img src="2장 Artificial Intelligence Basic.assets\image-20220825100843471.png" alt="image-20220825100843471" style="zoom:80%;" />

### 3. 문제 정의

* 나는 효율적으로 공부하기 위해서 공부시간과 시험점수와의 관계를 알고 싶음 

  <img src="2장 Artificial Intelligence Basic.assets\image-20220825100920974.png" alt="image-20220825100920974" style="zoom:80%;" />

1. 다음의 데이터를 통해 그래프를 그릴 수 있다. 

<img src="2장 Artificial Intelligence Basic.assets\image-20220825101048054.png" alt="image-20220825101048054" style="zoom:80%;" />

2. 다음의 모델 값을 추적할 수 있다. 오른쪽은 선형 모델로 표현

<img src="2장 Artificial Intelligence Basic.assets\image-20220825101101196.png" alt="image-20220825101101196" style="zoom:80%;" /><img src="2장 Artificial Intelligence Basic.assets\image-20220825101211045.png" alt="image-20220825101211045" style="zoom:80%;" />

3. 현재 모델 f(x)가 얼마 만틈 틀렸는지 어떻게 측정할까?

   <img src="2장 Artificial Intelligence Basic.assets\image-20220825101343726.png" alt="image-20220825101343726" style="zoom:80%;" />

4. 어떻게 하면 현재 모델 f(x)를 개선할 수 있을까?

   <img src="2장 Artificial Intelligence Basic.assets\image-20220825102135084.png" alt="image-20220825102135084" style="zoom:80%;" />

5. Data :arrow_forward: (모델 :arrow_forward: 평가(loss) :arrow_forward: 최적화 :arrow_forward:) :arrow_forward: 좋은 결과 



### 4. 이렇게 학습하면 잠재적인 문제는 무엇이 있을까?

* 세상의 모든 데이터를 다 본 것이 아니기 때문(언더피팅, 오버피팅의 문제가 생김)

  <img src="2장 Artificial Intelligence Basic.assets\image-20220825102837373.png" alt="image-20220825102837373" style="zoom:80%;" />

### 5.  오버피팅을 줄일 수 있는 방법?

1. 충분히 많은 양의 데이터
2. 모델의 복잡도 줄이기
3. 가중치의 Regularization(일반화) 적용하기
4. 드롭아웃(Drop out)



## 2. 기계학습 패러다임의 변화

* 좋은 특징(feature)는 무엇인가? 출력과의 관계를 잘 설명 할 수 있는 것 
  <img src="2장 Artificial Intelligence Basic.assets\image-20220825103511490.png" alt="image-20220825103511490" style="zoom:67%;" />

​	

* Deep Neural Network?
  * 모델이 충분히 크다면 Input과 output의 관계를 모두 학습할 수 있음