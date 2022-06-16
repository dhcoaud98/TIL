import sys

sys.stdin = open('imput.txt')

for TC in range(1, 3):
    arr = input()
    print(arr)

    stack = []
    result = True
    for i in range(len(arr)):
        # 입력 문자가 '('일 경우
        if arr[i] == '(':
            stack.append(arr[i])
        # 입력 문자가 ')'일 경우
        else:
            if stack[-1] == '(':
                stack.pop()
            # 입력 문자가 ')'인데 stack이 없을 경우
            elif stack == []:
                result = False

    # []
    # ['(', '(', '(', '(']
    if stack == []:
        print('True')
    else:
        print('False')



