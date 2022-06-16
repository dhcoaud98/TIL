def solution(priorities, location):
    answer = 0
    flag = True
    file = [i for i in range(0, len(priorities))]
    while flag:
        p = priorities.pop(0)
        l = file.pop(0)
        for i in range(len(priorities)):
            if priorities[i] > p:
                priorities.append(p)
                file.append(l)
                break
        else:

            if l == location:
                answer += 1
                flag = False
            else:
                answer += 1
    return answer

priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))