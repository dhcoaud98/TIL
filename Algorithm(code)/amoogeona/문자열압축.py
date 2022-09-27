def solution(s):
    answer = len(s)
    # visited = []
    for i in range(1, (len(s) // 2)+1):
        result = []
        for j in range((len(s) // i)+1):
            if j == len(s)//i:
                result.append(s[j*i:])
            else:
                result.append(s[j * i:j * i + i])

        print(result)
        if result[-1] == '':
            result.pop()

        cnt = 1
        short = ''
        for k in range(len(result) - 1):
            if result[k] == result[k + 1]:
                cnt += 1
            else:
                if k == 0:
                    short += result[k]
                    cnt = 1
                elif k == len(result) - 2:
                    short += result[k]
                else:
                    if cnt == 1:
                        short += result[k]
                    else:
                        short += str(cnt) + result[k]
                        cnt = 1

        if cnt == 1:
            short += result[-1]
        else:
            short += str(cnt) + result[-1]
        
        if len(short) <= answer:
            answer = len(short)
        # visited.append(len(short))
        # visited.append(short)

    return answer


# s = "aabbaccc"
# s = "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
s = "xababcdcdababcdcd"
print(solution(s))
