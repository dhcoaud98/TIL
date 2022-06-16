"""
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입하자
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력하자
  (1, 2, 3을 차례대로 출력해야 함)
"""
# 1-2. queue 모듈
import queue

# queue 생성
q = queue.Queue()

# enqueue
print(q.empty())  # queue가 비어있는지 확인 - True

# put -> queue에 데이터를 넣는 메서드
q.put(1)
q.put(2)
q.put(3)
print(q.empty())  # queue가 비어있는지 확인 - False
print(q.qsize())  # 데이터의 크기 확인 - 3

print('--------------------------------------')

# dequeue

# get -> queue에서 데이터를 꺼내는 메서드
print(q.get())  # 1
print(q.get())  # 2
print(q.get())  # 3
print(q.qsize())  # 데이터의 크기 확인 - 0
