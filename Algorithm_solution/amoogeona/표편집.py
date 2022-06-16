def solution(n, k, cmd):
    answer = ''
    result = [i for i in range(n)]  # 바뀌지 않음
    temp = []
    now_visited = k
    delete_row = []

    while cmd:
        p = cmd.pop(0)

        if len(p) >= 3:  # 위 아래 선택하기
            direct, num = p.split(' ')
            if direct == 'U':
                now_visited -= int(num)
            else:
                now_visited += int(num)
            print(now_visited)
        else:  # 행동

            if p == 'C':  # 삭제
                delete_row.append(result)
                for j in range(now_visited):
                    temp.append(result[j])
                for j in range(now_visited + 1, len(result)):
                    temp.append(result[j])

                if now_visited == len(result) - 1:  # 마지막 행이었다면 올라가기
                    now_visited -= 1

                result = temp
                temp = []
                print(result)
            else:  # 되돌리기
                result = delete_row.pop()
                print(result)


    return result

# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))