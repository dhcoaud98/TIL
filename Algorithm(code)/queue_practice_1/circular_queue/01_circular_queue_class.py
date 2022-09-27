"""
Index의 순환
 - front와 rear의 위치가 배열의 마지막 인덱스인 n-1을 가리킨 이후에 논리적 
   순환을 통해 배열의 처음 인덱스인 0으로 이동할 수 있도록 만들어야 함
 - 이를 활용하기 위해 나머지 연산자인 mod를 활용할 수 있다. (모듈로 연산) 
"""


class Queue:
    # createQueue
    def __init__(self, n):
        self.size = n
        self.items = [None] * n
        # 원형 큐의 경우 한 칸의 공간을 비워둬서 큐의 공백 및 포화 상태의 구분을 용이하게 한다.
        self.rear = 0
        self.front = 0

    def enQueue(self, item):
        if self.isFull():
            # 여러 가지 방식으로 대응 가능
            # 1. Queue의 크기를 확장하는 방식
            # 2. 이에 대한 예외처리를 해주는 방식
            print('Queue is full!')
        else:
            # rear 값을 조정하여 새로운 원소를 삽입 할 자리 마련
            """
            (rear+1) % self.size? -> 삽입 연산
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
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = item

    def deQueue(self):
        if self.isEmpty():
            print('Queue is empty!')
        else:
            # front 값을 조정하여 삭제 할 자리를 마련
            """
            (front+1) % self.size? -> 삭제 연산

            """
            self.front = (self.front + 1) % self.size
            # 실제 값을 큐에서 삭제하지 않아도 돌고 돌아 어차피 덮어 써질 것이기 때문에 상관없다.
            return self.items[self.front]

    def isEmpty(self):
        # 공백 상태
        # 선형 Queue와 마찬가지로 front와 rear가 같은 경우
        return self.front == self.rear

    def isFull(self):
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
        return self.front == (self.rear + 1) % self.size

    def Qpeek(self):
        return self.items[self.front]


# 최초 q 생성
q = Queue(3)
print('=' * 10, 'q가 비었을때 deQueue', '=' * 10)
q.deQueue()
print()

print('=' * 10, '최초 초기화 상태', '=' * 10)
print(q.size)
print(q.front, q.rear, q.items)
print()

print('=' * 10, '삽입', '=' * 10)
q.enQueue('A')
print()

print('=' * 10, '첫 삽입후, 제거', '=' * 10)
print(q.front, q.rear, q.items)
q.deQueue()
print()

print('=' * 10, '값 2개 삽입', '=' * 10)
print(q.front, q.rear, q.items)
q.enQueue('B')
print(q.front, q.rear, q.items)
print(q.isEmpty())
q.enQueue('C')
print()

print('=' * 10, '포화 상태', '=' * 10)
print(q.front, q.rear, q.items)
print(q.isFull())
print()

print('=' * 10, '포화 상태에서 삽입', '=' * 10)
q.enQueue('D')
print(q.items)


print('=' * 10, '값 제거', '=' * 10)
print(q.deQueue())

print('=' * 10, '재 삽입', '=' * 10)
q.enQueue('D')
print(q.items)
print()
