"""
1-1. 기본 Queue 구현
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력해야 함)
"""

queue = []

# 먼저 넣은 데이터를
queue.append(1)
queue.append(2)
queue.append(3)

# 먼저 출력한다. (FIFO)
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

# 만약 Queue에 데이터가 남아있다면
if queue:
    # 남은 데이터 출력
    print(queue.pop(0))
print(queue)
