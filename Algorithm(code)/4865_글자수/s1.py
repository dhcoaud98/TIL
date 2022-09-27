import sys

sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    str1 = list(input())
    str2 = list(input())
    temp = []

    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt += 1

        temp.append(cnt)

    max_num = 0
    for i in range(len(temp)):
        if temp[i] > max_num:
            max_num = temp[i]

    print(f'#{tc} {max_num}')
