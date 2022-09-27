import sys
sys.stdin=open('imput.txt')

TC = int(input())

for tc in range(1,TC+1):
    string = list(map(str, input()))

    print(string)
    stack = []
    for i in range(len(string)):
        if string[i] == '0' or string[i] == '1' or string[i] == '2' or string[i] == '3' or string[i] == '4' or string[i] == '5' or string[i] == '6' or string[i] == '7' or string[i] == '8' or string[i] == '9':
            stack.append(string[i])
        else:
            if string[i] == '*':
                a = float(stack[-2]) * float(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(a)
            elif string[i] == '/':
                a = float(stack[-2]) / float(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(a)
            elif string[i] == '+':
                a = float(stack[-2]) + float(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(a)
            elif string[i] == '-':
                a = float(stack[-2]) - float(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(a)

    print(stack[-1])