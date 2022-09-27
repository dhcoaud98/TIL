# 원형 큐의 경우 한 칸의 공간을 비워둬서 큐의 공백 및 포화 상태의 구분을 용이하게 한다.

SIZE = 5
Q = [0] * SIZE

"""
Index의 순환
 - front와 rear의 위치가 배열의 마지막 인덱스인 n-1을 가리킨 이후에 논리적 
   순환을 통해 배열의 처음 인덱스인 0으로 이동할 수 있도록 만들어야 함
 - 이를 활용하기 위해 나머지 연산자인 mod를 활용할 수 있다. (모듈로 연산) 
"""

# 초기 공백 상태
front = 0
rear = 0


def is_full():
    global front, rear
    # 포화상태
    # 삽입 할 rear의 다음 위치 = 현재 front
    """
    Queue가 꽉 찬 경우? rear가 front의 바로 뒤에 존재
    - front를 비워두는 이유는 공백 & 포화 상태의 구분을 위함
    
    front == (rear+1) % len(Q) ?
    - rear에 1을 더한 값을 큐의 길이로 나눈다? -> 나누어 떨어지면 다시 0으로 간다.
    
    rear + 1 == front?
    - 될 수도 있고 안될 수도 있다. 왜 그럴까?
    - front가 업데이트 안된 상황에서 rear가 끝으로 가면? 공백 상태로 판단할 수도 있다.
    """
    return front == (rear + 1) % len(Q)


def is_empty():
    global front, rear
    # 공백 상태
    # 선형 Queue와 마찬가지로 front와 rear가 같은 경우
    return front == rear


def enqueue(item):
    global rear
    if is_full():
        # 여러 가지 방식으로 대응 가능
        # 1. Queue의 크기를 확장하는 방식
        # 2. 이에 대한 예외처리를 해주는 방식
        print('Queue is full!')
    else:
        # rear 값을 조정하여 새로운 원소를 삽입 할 자리 마련
        """
          (rear+1) % len(Q)? -> 삽입 연산
          0    1    2    3    4
                            rear
          하나 값을 더 증가 시킴? -> 큐의 사이즈는 총 5이고 마지막 인덱스는 4이다.
          0    1    2    3    4     5
                                  rear+1 -> ????

          이때 rear + 1을 큐의 길이로 나머지 연산을 해보자
          (4 + 1) % 5 -> 0

          하나 값을 더 증가 시킴? -> 0으로 이동
          0    1    2    3    4
        rear+1
        """
        rear = (rear + 1) % len(Q)
        Q[rear] = item


def dequeue():
    global front
    if is_empty():
        print('Queue is empty!')
    else:
        # front 값을 조정하여 삭제 할 자리를 마련
        """
        (front+1) % len(Q)? -> 삭제 연산

        """
        front = (front + 1) % len(Q)
        # 실제 값을 큐에서 삭제하지 않아도 돌고 돌아 어차피 덮어 써질 것이기 때문에 상관없다.
        # 즉, 반환만 해도 문제없다.
        return Q[front]


# enQueue 작업
enqueue(1)
enqueue(2)
enqueue(3)

"""
공백 / 포화 상태의 구분을 위해 front가 있는 자리는 항상 빈자리로 둔다.

1. 선형큐
- front == rear -> 공백 상태인 큐라고 판단

2. 원형큐 
- front == rear -> 공백으로 판단한다. (초기화 front = rear = 0)
- 하지만 큐가 포화 상태가 되어도 front == rear가 같아지는 경우가 생길 수 있음 
"""
print(Q)  # [0, 1, 2, 3] -> rear
print('-------------------')

# deQueue 작업
print(dequeue())  # 1
print(dequeue())  # 2
print(dequeue())  # 3
print('-------------------')

# enQueue
enqueue(4)
print(Q)  # [4, 1, 2, 3]

# deQueue
print(dequeue())  # 4

# enQueue
enqueue(5)
print(Q)  # [4, 5, 2, 3]

print(dequeue())  # 5

# front & rear 그리고 Q의 상태 확인
"""
front == rear == 1
Q => [4, 5, 2, 3]
"""
print(front, rear, Q)
