import sys
sys.stdin = open('sample_input.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, arr = map(str, input().split())
    print(f'#{tc} ', end='')
    for i in range(int(N)):

        oct_number = int(arr[i], base=16)
        bin_number = bin(oct_number)
        num = bin_number[2:].zfill(4)  # 자릿수를 4개로 맞춰줌
        print(num, end='')
    print()