import sys


sys.stdin = open('sample_input.txt')


TC = int(input())

for tc in range(1, TC+1):
    arr = [list(input()) for _ in range(5)]

    # 최대 길이의 행 찾기
    max_num = 0
    for i in range(5):
        if len(arr[i]) >= max_num:
            max_num = len(arr[i])

    # 모든 행을 max_num 으로 맞추기
    for i in range(5):
        if len(arr[i]) < max_num:
            for j in range(max_num-len(arr[i])):
                arr[i].append('_')

    # 세로로 읽기
    result = ''
    for i in range(max_num):
        for j in range(5):
            result += arr[j][i]

    # 공백을 메꾸기 위한 _ 문자를 공백으로 처리하여 출력
    print(f'#{tc} ' , end='')
    print(result.replace('_', ''))



