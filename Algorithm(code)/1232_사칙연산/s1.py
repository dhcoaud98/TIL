import sys
sys.stdin = open('input.txt')

# 제일 뒤에서부터 계산해도 될 것같음!!
for tc in range(1, 11):
    N = int(input())
    temp = [0] * (N + 1)
    result = []
    # 1. input 받은 값들을 인덱스에 따라 사칙연산 혹은 수를 temp에 저장해 줌.
    # tc.1 ) [0, '-', '-', '10', '88', '65']
    for i in range(N):
        matrix = list(map(str, input().split()))
        temp[int(matrix[0])] = matrix[1]
        result.append(matrix)
    # print(temp)
    # print(result)

    # 2. 사칙연산 인 경우에만 뒤에서 부터 계산 할 예정.
    # 기본적인 이진트리의 순서대로가 아닌 자식 노드의 번호가 입력에서 주어졌으므로 그에 따라 계산해야 함.
    for i in range(len(result)-1, -1, -1):
        ans = result[i]
        if len(ans) == 4:  # 주어진 값이 사칙연산인 경우
            if ans[1] == '+':
                temp[int(ans[0])] = 0
                temp[int(ans[0])] = float(temp[int(ans[2])]) + float(temp[int(ans[3])])
            elif ans[1] == '-':
                temp[int(ans[0])] = 0
                temp[int(ans[0])] = float(temp[int(ans[2])]) - float(temp[int(ans[3])])
            elif ans[1] == '*':
                temp[int(ans[0])] = 0
                temp[int(ans[0])] = float(temp[int(ans[2])]) * float(temp[int(ans[3])])
            else:
                temp[int(ans[0])] = 0
                temp[int(ans[0])] = float(temp[int(ans[2])]) / float(temp[int(ans[3])])

    print(f'#{tc} {int(temp[1])}')
