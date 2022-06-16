import sys
sys.stdin = open('input.txt')

T = int(input())

change = {}

for _ in range(T):
    arr = input()
    text = []
    # 1. 16 진수를 2진수로 표현하기
    # 16 -> 8 -> 2
    for i in range(len(arr)):
        dec_value = int(arr[i], base=16)  # 16 -> 8
        bin_value = bin(dec_value)  # 8 -> 2
        r = bin_value[2:].zfill(4)  # 4 비트를 나타내기 위한 방법으로 format으로 표현 할 수도 있다.
        text.append(r)
    text = ''.join(text)
    # text = 000011111001011110100011

    for i in range(len(text)//7):
        result = 0
        for j in range(0, 7):
            result = result * 2 + int(text[j])
        text = text[7:]
        print(result, end=' ')

    result = 0
    for i in range(0, len(text)):  # 나머지를 처리해주기
        result = result*2 + int(text[i])
    print(result)
