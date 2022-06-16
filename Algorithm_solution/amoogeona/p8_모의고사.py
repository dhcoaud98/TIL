def solution(answers):
    answer = []
    a1, a2, a3 = 0, 0, 0
    result = []
    p1 = [1, 2, 3, 4, 5]
    for a in range(len(answers)):
        if p1[a] == answers[a % len(p1)]:
            a1 += 1
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    for a in range(len(answers)):
        if p2[a] == answers[a % len(p2)]:
            a2 += 1
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for a in range(len(answers)):
        if p3[a] == answers[a%len(p3)]:
            a3 += 1
    result.append(a1)
    result.append(a2)
    result.append(a3)
    for i in range(3):
        if result[i] == max(result):
            answer.append(i+1)
    return answer

answers = [1, 2, 3, 4, 5]
# answers = [1, 3, 2, 4, 2]
print(solution(answers))