import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    arr = list(map(int, input()))
    print(arr)
    length = len(arr) // 7

    for i in range(length):
        result = 0
        # 7개씩 7개의 배열세트에 접근
        for j in range(i*7, i*7+7):
            result = result * 2 + arr[j]
        print(result, end=' ')

    print()