def solution(progresses, speeds):
    answer = []
    cnt = 0
    while progresses:
        while progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]

        cnt = 0
        while progresses[0] >= 100:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1

            if progresses == []:
                break

        answer.append(cnt)

    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))