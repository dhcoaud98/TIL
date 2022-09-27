import sys

sys.stdin = open('input.txt')


for tc in range(1, 11):
    t = input()
    arr = [list(input()) for _ in range(100)]

    # 1. 가로 행렬 풀기
    # 비교할 문장을 뽑아 temp에 넣고, temp[::-1]과 비교하여 일치하면 result에 넣기로 한다.
    result = []
    temp = []
    N = 100
    for M in range(2, 100):
        for i in range(100):
            for j in range(N-M+1):
                temp = arr[i][j:j+M]  # 회문을 뽑아서 temp에 넣음
                if temp == temp[::-1]:
                    result.append(len(temp))
                    temp = []
                else:
                    temp = []

    # 2. 전치하기
    arr = list(map(list, zip(*arr)))

    # 3. 전치 행렬 풀기
    for M in range(2, 100):
        for i in range(100):
            for j in range(N-M+1):
                temp = arr[i][j:j+M]  # 회문을 뽑아서 temp에 넣음
                if temp == temp[::-1]:
                    result.append(len(temp))
                    temp = []
                else:
                    temp = []

    # 4. result에서 가장 큰 수 뽑기
    max_num = result[0]
    for i in range(len(result)):
        if result[i] >= max_num:
            max_num = result[i]

    print(f'#{tc} {max_num}')

