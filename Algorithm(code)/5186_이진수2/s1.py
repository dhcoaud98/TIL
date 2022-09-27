import sys
sys.stdin=open('sample_input.txt')

TC = int(input())
for tc in range(1, TC+1):
    dec = float(input())
    number = dec % 2
    cnt = 1
    result = ''

    while number != 0:
        cnt += 1
        number = number * 2
        result += str(int(number))
        number = number % 1
        if cnt >= 13:
            result = 'overflow'
            number = 0

    print(f'#{tc} {result}')

