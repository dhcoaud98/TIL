import sys


sys.stdin = open('sample_input.txt')


def f(string):
    stack = []

    for i in string[:-1]:
        if i.isnumeric():
            stack.append(int(i))

        else:
            if len(stack) >= 2:
                if i == '*':
                    a = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(a)
                elif i == '/':
                    a = stack[-2] / stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(int(a))
                elif i == '+':
                    a = stack[-2] + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(a)
                elif i == '-':
                    a = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(a)
                else:  # 사칙 연산 이외의 값이 나오면 오류
                    return 'error'
            else:  # i의 값이 사칙연산인데 stack의 길이가 2 미만인 경우
                return 'error'

    if len(stack) == 1:
        a = stack.pop()
        return a

    else:
        return 'error'


TC = int(input())
for tc in range(1, TC+1):
    arr = input().split()
    print(f'#{tc} {f(arr)}')