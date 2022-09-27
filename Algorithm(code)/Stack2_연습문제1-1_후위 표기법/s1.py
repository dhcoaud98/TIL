import sys
sys.stdin=open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    tokens = list(map(str, input()))


    result = ''
    stack = []
    for t in tokens:
        if t in '*/+-()':
            if not stack:  # 스택이 비어있는 초기에
                stack.append(t)
            elif t == '(':
                stack.append(t)
            elif t in '*/':
                while stack and stack[-1] in '*/':
                    result += stack.pop()  # stack에서 꺼내서 result에 넣기
                stack.append(t)
            elif t in '+-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(t)
            elif t == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
        else:  # t가 숫자일 경우
            result += t


    # result = 234*5
    # stack = +/
    while stack != []:
        result += stack.pop()

    print(f'#{tc} {result}')