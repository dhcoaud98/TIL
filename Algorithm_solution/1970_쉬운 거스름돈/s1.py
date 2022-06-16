import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    Price = int(input())

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0] * 8

    for i in range(8):
        if Price // money[i] > 0:
            result[i] = Price // money[i]
            Price = Price - result[i] * money[i]
        else:
            continue

    print(f'#{tc}')
    print(*result)

