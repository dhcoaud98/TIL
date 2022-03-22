# 03.22

## Queue

<br>

#### 1. enumerate

반복문 사용 시 몇 번째 반복문인지 확인이 필요하다. 이때 사용하게 되는데 인덱스 번호와 컬렉션의 원소를 tuple의 형태로 반환한다. 

```python
pizza = deque(enumerate(list(map(int, input().split())), 1))
```

<br>

#### 2. deque()

```python
from collections import deque

# 빈큐 만들기
deque1 = deque()
# 원소가 있는 큐 만들기
deque2 = deque([1, 2, 3])

# 위에서 input 받은 pizza 값의 왼쪽에서 부터 하나씩 꺼낸후 deque1에 넣어준다.
deque1.append(pizza.popleft())

# 원소 수 알아내기
print(len(deque1))
```

