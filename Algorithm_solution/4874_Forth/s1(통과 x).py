import sys
sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    arr = list(map(str, input().split()))

    stack = []
    result = ''
    try:
        for i in range(len(arr)):
            if arr[i] == '1' or arr[i] == '2' or arr[i]=='3' or arr[i]=='4' or arr[i]=='5' or arr[i]=='6' or arr[i]=='7' or arr[i]=='8' or arr[i]=='9' or arr[i]=='10':
                stack.append(arr[i])
            else:
                if arr[i] == '*':
                    a = float(stack[-2]) * float(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(int(a))
                elif arr[i] == '/':
                    a = float(stack[-2]) / float(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(int(a))
                elif arr[i] == '+':
                    a = float(stack[-2]) + float(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(int(a))
                elif arr[i] == '-':
                    a = float(stack[-2]) - float(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(int(a))
                elif arr[i] == '.':
                    result = stack[-1]

    except Exception:
        result = 'error'

    print(f'#{tc} {result}')
