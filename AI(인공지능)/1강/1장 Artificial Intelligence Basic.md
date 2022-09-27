# 1장 Artificial Intelligence Basic





## 1.  인공지능의 시대

1. 클라우드 서비스 제공(소셜 네트워크 포함)

2. 의학

3. 미디어 & 엔터테인먼트 

4. 보안

5. 자율주행

:arrow_forward: 인공지능의 진입장벽이 낮아짐



## 2. 인공지능이란?

* 기계 지능을 다루는 컴퓨터 공학 분야
  * 인간 같은 인지능력을 구현
  * 추론, 문제 해결, 계획, 이해, 학습, 그리고 패턴을 인식[Gottfredson, 1997]

### 1. **퍼셉트론**[Rosenblatt, 1958]

*  1950년대 부터 연구 시작

* 최초로 구현된 인공 신경망 (인풋와 아웃풋이 있을 때 최초로 학습이 가능한 인공 신경망)

  <img src="1장 Artificial Intelligence Basic.assets/image-20220824131940855.png" alt="image-20220824131940855" style="zoom:67%;" />

* w(가중치)를 잘 학습 할수록 기울기가 조정이 되어 높아지는 것을 알 수 있다. 

  <img src="1장 Artificial Intelligence Basic.assets/image-20220824132003164.png" alt="image-20220824132003164" style="zoom:67%;" />

* 단일 신경망으로는 간단한 XOR문제를 풀 수 없다는 것을 알게 된다. 이를 인공지능의 겨울이라고 부른다. 

### 2. 첫 번째 재탄생

* **LeNet5** [Lecun et al., Proceedings of the IEEE 1998]

  * 첫번째 컨볼루션 기반 뉴럴넷 by Yann LeCun,1998

  * 우편 번호 인식에 큰 성공을 거둠

    <img src="1장 Artificial Intelligence Basic.assets/image-20220824103431451.png" alt="image-20220824103431451" style="zoom: 50%;" />

### 3. 두 번째 재탄생 - 딥러닝의 혁신

* (깊은) Convolutional Neural Networks의 재탄생 [AlexNet, NIPS2012]

   

* AlexNet : ImageNet 챌린지 2012에서 큰 격차로 1등

  * 성공이유
    * 데이터 : 데이터의 양이 충분함 
    * 알고리즘 : 알고리즘의 발달 
    * 연산능력 : 게임 그래픽 카드를 사용

* 기계학습 패러다임의 변화 

  * **머신러닝 :arrow_forward: 딥러닝**

  <img src="1장 Artificial Intelligence Basic.assets/image-20220824104011577.png" alt="image-20220824104011577" style="zoom: 50%;" />

### 3. 인공지능의 최종적인 목표

* 사회성을 학습한 인공지능?

* 사람이 세상을 학습하는 방법 : `Multi-modal` 인식

* 지각능력이란? 

  * (입력, 출력) 데이터 : sight, sound, touch, taste, smell

  * 인간은 자라면서 상호작용을 하면서 세상을 배움
  * 인간처럼 multi-modal의 상호관계성으로부터 유용한 정보 수집

* 지각능력이 갖춰진 후 학습 단계

  * multi-modal 인식 :arrow_forward: 계획수립 :arrow_forward: 의사결정

* 기계가 학습을 하는 일반적인 방법
  * 관찰(현상관찰, 상황 파악) :arrow_forward: 이해(경험, 지식 기반으로 상황을 패턴화 :arrow_forward: 평가(기준에 의한 평가, 기준: 사람 또는 시스템) :arrow_forward: 적용(최적 모델 응용)



### 4. 딥러닝의 최근 성과

* 인간은 선한가 악한가? 에 대한 질문에 다음과 같이 결과
  * 제 생각에는 인간은 선하기보다는 악합니다. 첫번째로, 사람의 행동은 그들의 본성(진실성)이 아니라, 사회와 문화와 같은 외적인 요인들의 결과로 나타나기 때문입니다. 두 번재로, 인간의 가치는 시간이 지남에 따라 꾸준하게 감소했기 때문입니다. 

* GPT-3를 활용하여 텍스트로부터 이미지 생성

  <img src="1장 Artificial Intelligence Basic.assets/image-20220824105925876.png" alt="image-20220824105925876" style="zoom:50%;" />

* Art applications
  * Living protraits
* AR & VR appllications - soccer on Tout Tabletop
* 자율주행 관련 applications - RTM3D
* Robot applications - Dense Object Nets
* 인간을 뛰어넘는 인지능력
  * 육안으로는 잘 보이지 않는 것을 관찰 가능하게 해줌