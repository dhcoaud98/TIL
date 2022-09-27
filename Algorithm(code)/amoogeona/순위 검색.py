def solution(info, query):
    answer = []
    for q in query:
        a, b, c, f = map(str, q.split(' and '))
        d, e = map(str, f.split(' '))
        # answer.append([d, e])

        pass_people = 0
        for i in info:
            cnt = 0
            a1, b1, c1, d1, e1 = map(str, i.split(' '))
            if a == '-':
                cnt += 1
            elif a == a1:
                cnt += 1
            else:
                continue

            if b == '-':
                cnt += 1
            elif b == b1:
                cnt += 1
            else:
                continue

            if c == '-':
                cnt += 1
            elif c == c1:
                cnt += 1
            else:
                continue

            if d == '-':
                cnt += 1
            elif d == d1:
                cnt += 1
            else:
                continue

            if e == '-':
                cnt += 1
            elif int(e) <= int(e1):
                cnt += 1
            else:
                continue

            pass_people += 1

        answer.append(pass_people)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
