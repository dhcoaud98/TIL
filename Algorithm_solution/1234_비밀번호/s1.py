import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    N, arr = map(int, input().split())
    # N, lst = map(str, input().split())로 받아주면 편함

    # 1. arr을 숫자로 받았기 때문에 문자로 변환해준다.
    temp = ''
    for i in range(N):
        a = chr(arr % 10 + 48)
        temp += a
        arr = arr // 10
    temp = temp[::-1]

    # 2. stack으로 괄호 검색 시행한다.
    stack = [temp[0]]
    for i in range(1, len(temp)):
        if stack == []:
            stack.append(temp[i])
        elif stack[-1] != temp[i]:  # 새로 넣어줄 값이 이전 값과 다르면 push
            stack.append(temp[i])
        elif stack[-1] == temp[i]:  # 새로 넣어줄 값이 이전 값과 같으면 pop
            stack.pop()

    print(f'#{tc} ', end='')
    for j in range(len(stack)):
        print(stack[j], end='')
    print()