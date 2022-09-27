front = -1
rear = -1
Q = [0] * 10
rear += 1  # enqueue(1)
Q[rear] = 1
rear += 1  # enqueue(2)
Q[rear] = 2
rear += 1  # enqueue(3)
Q[rear] = 3

front += 1
print(Q[front])
front += 1
print(Q[front])
front += 1
print(Q[front])