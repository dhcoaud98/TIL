import sys
sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    arr = input()
    
    # 주어진 문자열에서 '(, ), {, }, [, ]'만 뽑기
    temp = []
    for i in range(len(arr)):
        if arr[i] == '(' or arr[i] == ')':
            temp.append(arr[i])
        elif arr[i] == '{' or arr[i] == '}':
            temp.append(arr[i])
        elif arr[i] == '[' or arr[i] == ']':
            temp.append(arr[i])

    # 스택 이용해 괄호검사하기 (0번째 인덱스를 넣고 시작)
    answer = [temp[0]]
    for i in range(1, len(temp)):
        if answer == []:
            answer.append(temp[i])
        # '(, {, ['
        elif temp[i] == '(' or temp[i] == '{' or temp[i] == '[':
            answer.append((temp[i]))
        elif temp[i] == ')' or temp[i] == '}' or temp[i] == ']':
            if temp[i] == ')':
                if answer[-1] == '(':
                    answer.pop()
                else:
                    answer.append((temp[i]))
            elif temp[i] == '}':
                if answer[-1] == '{':
                    answer.pop()
                else:
                    answer.append((temp[i]))
            elif temp[i] == ']':
                if answer[-1] == '[':
                    answer.pop()
                else:
                    answer.append((temp[i]))

    # 빈 스택인지 아닌지 찾기
    if answer == []:
        result = 1
    else:
        result = 0
    
    print(f'#{tc} {result}')