import sys
sys.stdin=open('input.txt')


for tc in range(1, 11):
    N = int(input())
    tokens = list(map(str, input()))

    # 1. 중위표현식 -> 후위표현식
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
                while stack and stack[-1] != '(':  # 여는 괄호를 만날때 까지
                    result += stack.pop()
                stack.pop()
        else:  # t가 숫자일 경우
            result += t

    # result = 234*5
    # stack = +/
    while stack:
        result += stack.pop()

    # 2. 후위 표현식 계산
    answer = []
    for i in range(len(result)):
        if result[i] == '0' or result[i] == '1' or result[i] == '2' or result[i] == '3' or result[i] == '4' or result[i] == '5' or result[i] == '6' or result[i] == '7' or result[i] == '8' or result[i] == '9':
            answer.append(result[i])
        else:
            if result[i] == '*':
                a = float(answer[-2]) * float(answer[-1])
                answer.pop()
                answer.pop()
                answer.append(a)
            elif result[i] == '/':
                a = float(answer[-2]) / float(answer[-1])
                answer.pop()
                answer.pop()
                answer.append(a)
            elif result[i] == '+':
                a = float(answer[-2]) + float(answer[-1])
                answer.pop()
                answer.pop()
                answer.append(a)
            elif result[i] == '-':
                a = float(answer[-2]) - float(answer[-1])
                answer.pop()
                answer.pop()
                answer.append(a)

    print(f'#{tc} {int(answer[-1])}')