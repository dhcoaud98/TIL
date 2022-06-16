def solution(places):
    answer = []


    # 체크 함수
    def check(n, m):
        queue = []
        queue.append([n, m])
        visited = []
        visited.append([n, m])
        board[n][m] = 1
        while queue:  # queue가 빌때까지
            q = queue.pop(0)
            x = q[0]
            y = q[1]
            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < 5 and 0 <= ny < 5 and [nx, ny] not in visited:
                    if place[nx][ny] == 'O' or place[nx][ny] == 'P':
                        visited.append([nx, ny])
                        queue.append([nx, ny])
                        if board[x][y] + 1 < board[nx][ny]:
                            board[nx][ny] = board[x][y] + 1

        return board

    # 1. 시작
    for place in places:
        cnt = 1
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append([i, j])

        for x, y in people:
            board = [[float('inf')] * 5 for _ in range(5)]
            print(check(x, y))
            check(x, y)  # check에서 체크함수로 확인
            for i in range(5):
                for j in range(5):
                    if board[i][j] == 3 and place[i][j] == 'P':
                        cnt = 0
                        break
                    if board[i][j] == 2 and place[i][j] == 'P':
                        cnt = 0
                        break
        answer.append(cnt)

    return answer


# places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
places = [["PXOOO", "OOOOO", "PXOOO", "OOOOO", "OOOPO"]]
# places = [['PPPPP', 'OOOOO', 'OOOOO', 'PPPPP', 'PPPPP']]
print(solution(places))

