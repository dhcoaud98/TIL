class Queue:
    # createQueue
    def __init__(self, n):
        self.size = n
        self.items = [None] * n
        self.rear = -1
        self.front = -1

    def enQueue(self, item):
        if self.isFull():
            # 여러 가지 방식으로 대응 가능
            # 1. Queue의 크기를 확장하는 방식
            # 2. 이에 대한 예외처리를 해주는 방식
            print('Queue is full!')
        else:
            self.rear += 1
            self.items[self.rear] = item

    def deQueue(self):
        if self.isEmpty():
            print('Queue is empty!')
        else:
            self.front += 1
            return self.items[self.front]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear == self.size - 1

    def Qpeek(self):
        return self.items[self.front]

    def __len__(self):
        return self.rear - self.front


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
print(len(q))
print()

print('=' * 10, '첫 삽입후, 제거', '=' * 10)
print(q.front, q.rear, q.items)
q.deQueue()
print(len(q))
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
print(len(q))
print()

print('=' * 10, '포화 상태에서 삽입', '=' * 10)
q.enQueue('D')
