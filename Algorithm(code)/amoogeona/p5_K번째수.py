def solution(array, commands):
    answer = []
    result = []
    for s, e, w in commands:
        result = []
        for i in range(s-1, e):
            result.append(array[i])
        result.sort()
        answer.append(result[w-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
