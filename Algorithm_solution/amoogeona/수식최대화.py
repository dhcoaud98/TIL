def solution(expression):
    answer = []
    operator = []
    result = []
    number = ''
    for e in expression:  # 1. 입력 list로 만들기
        if e.isdecimal():
            number += e
        elif e in ['+', '-', '*']:
            result.append(int(number))
            result.append(e)
            operator.append(e)
            number = ''
    result.append(int(number))

    def sol(p, result):  # 3. 계산

        for l in p:
            temp = []
            idx = 0
            while idx < len(result):
                if result[idx] != l:
                    temp.append(result[idx])
                    idx += 1
                else:
                    a = temp.pop()
                    b = result[idx + 1]
                    if l == '*':
                        temp.append(a * b)
                        idx += 2
                    elif l == '+':
                        temp.append(a + b)
                        idx += 2
                    elif l == '-':
                        temp.append(a - b)
                        idx += 2
            result = temp
        answer.append(abs(temp[0]))

    def cal(n, k, lst, result):  # 2. 연산자의 순서 결정
        if n == k:
            sol(p, result)
            return

        for i in range(k):
            if used[i] == 0:
                p[n] = lst[i]
                used[i] = 1
                cal(n + 1, k, lst, result)
                used[i] = 0

    Operator = list(set(operator))
    used = [0] * len(Operator)
    p = [0] * len(Operator)
    cal(0, len(Operator), Operator, result)

    return max(answer)

# print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
