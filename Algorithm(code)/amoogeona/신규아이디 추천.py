def solution(new_id):
    answer = ''
    result = ''
    if new_id == "" :
        answer = 'a'
    else:
        # 1. 소문자
        result = new_id.lower()

        # 2. 소, 숫, ., _, -
        for r in result:
            if r.isdigit() or r.isalpha() or r == '.' or r == '-' or r== '_':
                answer += r

        # 3. '.'이 여러개면 1개로 바꿈
        result = ''
        idx = 0
        while idx < len(answer):
            if answer[idx] == '.' and idx != len(answer)-1:
                if answer[idx + 1] == '.':
                    idx += 1
                else:
                    result += '.'
                    idx += 1
            elif answer[idx] == '.' and idx == len(answer)-1:
                result += '.'
                idx += 1
            else:
                result += answer[idx]
                idx += 1

        # 4. 맨앞과 맨 뒤 .은 없애기
        if result[0] == '.':
            result = result[1:]
        if len(result) != 0:
            if result[-1] == '.':
                result = result[0:-1]

        # 5. 빈 문자열
        if result == '':
            result += 'a'

        # 6. 15개 이하
        if len(result) >= 16:
            result = result[0:15]
            if result[-1] == '.':
                result = result[0:14]

        # 7.
        if len(result) <= 2:
            while len(result) < 3:
                result += result[-1]

        answer = result

    return answer


# new_id = "...!@BaT#*..y.abcdefghijklm"  # "bat.y.abcdefghi"
# new_id = "z-+.^."
# new_id = "=.="
# new_id = "123_.def"
# new_id = "abcdefghijklmn.p"  # "abcdefghijklmn"
# new_id = ".-."
new_id = "........................"

print(solution(new_id))