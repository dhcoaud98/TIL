def solution(id_list, report, k):
    answer = [0] * len(id_list)
    temp = { id_list[p] : f'{p}' for p in range(len(id_list))}
    # print(temp)
    result = { f'{id_list[_]}': 0 for _ in range(len(id_list))}
    visited = []
    result2 = { f'{id_list[_]}': [] for _ in range(len(id_list))}
    # print(result)

    for r in range(len(report)):
        R, L = report[r].split()
        if [R, L] not in visited:
            # result[L] += 1
            result2[L].append(temp[R])
            visited.append([R, L])

    # print(result)
    # print(result2)
    temp2 = []
    for i in id_list:
        if len(result2[i]) >= 2:
            temp2.append(result2[i])
    # print(temp2)

    for m in range(len(temp2)):
        for n in range(len(temp2[m])):
            answer[int(temp2[m][n])] += 1



    # for r in range(len(report)):
    #     R, L = report[r].split()
    #     if [R, L] not in visited:
    #         result[L].append(temp[R])
    #         visited.append([R, L])
    # print(result)
    # for i in id_list:
    #     if len(result[i]) >= k:
    #         for j in range(len(result[i])):
    #             answer[int(result[i][j])] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
# id_list = ["con", "ryan"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2
# k = 3
print(solution(id_list, report, k))
