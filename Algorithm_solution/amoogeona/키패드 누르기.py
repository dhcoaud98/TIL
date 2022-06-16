def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    lefthand = [3, 0]
    righthand = [3, 2]

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            for i in range(4):
                for j in range(3):
                    if keypad[i][j] == n:
                        lefthand = [i, j]
        elif n in [3, 6, 9]:
            answer += 'R'
            for i in range(4):
                for j in range(3):
                    if keypad[i][j] == n:
                        righthand = [i, j]
        elif n in [2, 5, 8, 0]:
            for i in range(4):
                for j in range(3):
                    if keypad[i][j] == n:
                        next_num = [i, j]
                        # lefthand = [0, 1]
                        # righthand = [3, 1]
                        # next_num = [2, 1]
            l = abs(lefthand[0] - next_num[0]) + abs(lefthand[1] - next_num[1])
            r = abs(righthand[0] - next_num[0]) + abs(righthand[1] - next_num[1])
            if l < r:
                lefthand = next_num
                answer += 'L'
            elif l > r:
                righthand = next_num
                answer += 'R'
            elif l == r:
                if hand == 'right':
                    righthand = next_num
                    answer += 'R'
                else:
                    lefthand = next_num
                    answer += 'L'

    return answer


numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

print(solution(numbers, hand))