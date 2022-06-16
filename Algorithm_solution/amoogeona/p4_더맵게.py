def solution(scoville, K):
    answer = 0
    flag = True

    while flag:
        scoville.sort()
        a = min(scoville)
        scoville.remove(a)
        b = min(scoville)
        scoville.remove(b)
        new = a + b * 2
        scoville.append(new)

        for i in range(len(scoville)):
            if scoville[i] < K:
                break
        else:
            flag = False

        answer += 1
    return answer



scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))