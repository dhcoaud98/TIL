def solution(record):
    answer = []
    result = {}
    userid = []
    answer2 = []
    for r in range(len(record)):
        if record[r][0] == 'L':
            E, U = record[r].split()
        else:
            E, U, N = record[r].split()

        if U not in userid:
            userid.append(U)
        # result[U] = N


        if E == 'Enter':
            answer.append(f'{U}님이 들어왔습니다.')
            result[U] = N
        elif E == 'Leave':
            answer.append(f'{U}님이 나갔습니다.')

        else:
            result[U] = N

    for i in range(len(answer)):
        for user in userid:
            if user in result.keys():
                if user in answer[i]:
                    new_word = answer[i].replace(user, result.get(user))
                    answer2.append(new_word)
                    break


    return answer2

# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
record = ["Enter uid123 uid1234", "Leave uid1234", "Enter uid4567 uid123", "Change uid4567 uid1234", "Leave uid4567"]
print(solution(record))


