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

<br>

<br>

#### 3. DFS vs BFS :star:

* DFS : 스택, 재귀

  가장 깊은 곳까지 들어갔다가 나와야 하기때문에!! 

  ```python
  def DFS_with_adj_list(graph, root):
      visited = []
      stack = [root]
  
      while stack:
          n = stack.pop()     ---(1)
          if n not in visited:
              visited.append(n)
              stack += graph[n] - set(visited)
      return visited
  
  print(BFS_with_adj_list(graph_list, root_node))
  ```

  (1) `.pop()`에서 처럼 ()안에 숫자가 없으면 제일 오른쪽의 값을 가져오기 때문에 DFS

* BFS : 큐

  루트의 인접한 노드를 모두 방문하고, 다음 높이의 노드를 방문하기 때문에!!

  ```python
  from collections import deque
  
  def BFS_with_adj_list(graph, root):
      visited = []
      queue = deque([root])
  
      while queue:
          n = queue.popleft()      ---(1)
          if n not in visited:
              visited.append(n)
              queue += graph[n] - set(visited)
      return visited
    
  print(BFS_with_adj_list(graph_list, root_node))
  ```

  (1) `.popleft()` 혹은 `.pop(0)`을 사용하면 제일 왼쪽의 노드를 탐색하기 때문에 BFS
