import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    num = int(input())
    arr = [2, 3, 5, 7, 11]
    temp = []

    for i in range(len(arr)):
        cnt = 0
        while True:
            if num % arr[i] == 0:
                num = num // arr[i]
                cnt += 1
            else:
                break
        temp.append(cnt)

    print(f'#{tc} ', end = '')
    print(*temp)