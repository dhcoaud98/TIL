def solution(info, query):
    answer = []
    for i in info:
        number = list(map(str, i.split(' ')))[-1]

        cnt = 0
        for q in query:
            a, b, c, f = map(str, q.split(' and '))
            d, e = map(str, f.split(' '))
            if int(e) > int(number):
                break
            else:
                if a != '-' and a not in i:
                    break
                if b != '-' and b not in i:
                    break
                if c != '-' and c not in i:
                    break
                if d != '-' and d not in i:
                    break
                cnt += 1

        answer.append(cnt)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
