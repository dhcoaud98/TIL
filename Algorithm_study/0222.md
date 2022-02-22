# 02.22

## Algorithm & Stack 복습



 ### **버블 정렬 복습**

case 1.  오름차순

```python
for i in range(len(arr)-1):                                      # 범위 설정 주의!
	for j in range(len(arr)-(i+1)):                              # 범위 설정 주의!
		if arr[j] > arr[j+1]:
			arr[i], arr[i+1] = arr[i+1], arr[i]
```

case 2. 내림차순

```python
for i in range(len(scores) - 1, 0, -1):                          # 범위 설정 주의!
	for j in range(0, i):
		if scores[j] < scores[j + 1]:
        	scores[j], scores[j + 1] = scores[j + 1], scores[j]
```



### **배열을 input 받을 경우**

```python
N, lst = map(str, input().split())           # list를 str으로 받아 인덱스 접근 가능
N, lst = map(int, input().split())           # list를 int로 받아 인덱스 접근 불가능
```

-

-

-

---

### **스택1**

1) **스택** : 물전을 쌓아 올린 형태의 자료구조이다. 마지막에 삽입한 자료를 가장 먼저 꺼낸다. 후입선출(LIFO: Last In First Out)이라고 부른다.

   * 자료구조: 자료를 선형으로 저장할 저장소, 저장소 자체를 스택이라 부르기도 한다. 스택에서 마지막 삽입된 원소의 위치를 top이라 부른다.

   * 연산:

     ```python
     <삽입> push를 통해 삽입한다.
     
     def push(item):
         s.append(item)
         
     def push(item, size):
         global top
         top += 1
         if top == size:
             print('overflow!')
         else:
             stack[top] = item
            
     size = 10
     stack = [0]*size
     top = -1
     
     push(10, size)
     top += 1
     stack[top] = 20
     
     
     <삭제> pop저장소에서 자료를 꺼내서 삭제한다.
     
     def pop():
         if len(s) == 0:
             return
         else:
             return s.pop(-1):
             
     def pop():
         global top
         if top += 1:
             print('underflow')
             return 0
         else:
             top -= 1
     		return stack[top+1]
     
     print(pop())
     
     - 스택이 공백이 아닌지를 확인하는 연산.isEmpty
     - 스택의 top에 있는 item(원소)을 반환하는 연산. peek
     ```

     

2. **재귀호출**
   * 재귀는 자기 자신을 호출하여 순환 수행하는 것이다. 일반적인 호출방식보다 재귀호출방식을 사용하여 함수를 만들면 프로그램의 크기를 줄일 수 있다. ex) 팩토리얼

3. **Memoization & DP**:star:

   * 피보나치 수를 구하는 함수를 재귀함수로 구현한 알고리즘은 엄청난 중복 호출이 존재하여 속도가 느려질 수 있다. **Memoization**은 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 저장해 다시 계산하지 않도록 하여 실행속도를 빠르게 하는 기술이다. **동적 계획법의 핵심이 되는 기술이다.**

     ```python
     def fibo1(n):
         global memo
         if n >= 2 and len(memo) <= n:
             memo.append(fibo1(n-1)+fibo1(n-2))
         return memo[n]
     
     memo = [0, 1]
     
     # memo = [0, 1]을 미리 작성
     ```

   * 동적 계획(**Dynamic Programming**) 알고리즘은 그리디 알고리즘과 같이 **최적화 문제를 해결하는 알고리즘이다.** 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 방식이다. 

     ```python
     def fibo(n):
         f = [0, 1]
         
         for i in range(2, n+1):
             f.append(f[i-1]+f[i-2])
             
         return f[n]
         
     ```

     

4. **DFS(깊이우선탐색)**

   ```python
   visited = [F] * N  # [F, F, F, F, F, F, F]
   stack = []
   
   def DFS(v):
       
       1. A 방문;
       visited[A] -> stack.append(A)
       2. B 방문;
       visited[B] -> stack.append(B)
       3. D 방문;
       visited[D] -> stack.append(D)
       4. F 방문;
       visited[F] -> stack.append(F)
       5. E 방문;
       visited[E] -> stack.append(E)
       6. c 방문;
       visited[C] -> stack.append(C)
       7. 갯수만큼 돌아감
       pop(stack)
       pop(stack)
       8. G 방문 
       visited[G] -> stack.append(G)
       9. 처음으로 돌아감
       pop(stack)
       pop(stack)
       pop(stack)
       pop(stack)
       
   # 갯수를 구할 수 있음!    
           
       
   ```

   

