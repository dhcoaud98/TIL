import sys
sys.stdin=open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    tokens = list(map(str, input()))

    result = ''
    stack = []
    # 크게 연산자일 경우와 피연산자일 경우로 나눔
    for t in tokens:
        if t in '*/+-()':  # 연산자
            if not stack:
                stack.append(t)
            elif t == '(':
                stack.append(t)
            elif t in '*/':
                while stack and stack[-1] in '*/':
                    result += stack.pop()
                stack.append(t)
            elif t in '+/':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(t)
            elif t == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
        else:  # 피연산자
            result += t

    while stack != []:
        result += stack.pop()

    print(result)