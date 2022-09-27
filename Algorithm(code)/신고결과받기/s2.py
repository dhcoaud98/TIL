def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    for r in set(report):  # 미리 중복 제거
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
# id_list = ["con", "ryan"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2
# k = 3
print(solution(id_list, report, k))


