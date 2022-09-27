# stack에 3번 push하기
size = 3
stack = [0] * size
top = -1

def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item
        print(stack[top])



# stack pop 3번 하기
def pop():
    if len(stack) == 0:
        return 0
    else:
        return stack.pop(-1)

push(3, size)
print(pop())
