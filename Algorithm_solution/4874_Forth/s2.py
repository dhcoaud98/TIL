import sys
sys.stdin = open('sample_input.txt')


def f(string):
    stack = []

    for i in string[:-1]:
        if i.isnumeric():
            stack.append(int(i))

        else:
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                if i == '*':
                    stack.append(b*a)
                elif i == '/':
                    stack.append(int(b / a))
                elif i == '+':
                    stack.append(b + a)
                elif i == '-':
                    stack.append(b - a)
                else:  # 사칙 연산 이외의 값이 나오면 오류
                    return 'error'
            else:  # i의 값이 사칙연산인데 stack의 길이가 2 미만인 경우
                return 'error'

    if len(stack) == 1:
        c = stack.pop()
        return c

    else:
        return 'error'


TC = int(input())
for tc in range(1, TC+1):
    arr = input().split()
    print(f'#{tc} {f(arr)}')
