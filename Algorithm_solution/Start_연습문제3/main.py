import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    arr = input()
    text = []

    # 1. 16->8->2
    for i in range(len(arr)):
        oct_value = int(arr[i], base=16)  # 16->8
        # print(oct_value)
        bin_value = bin(oct_value)  # 8 -> 2
        # print(bin_value)
        text.append(bin_value[2:].zfill(4))
    # print(text)
    text = ''.join(text)
    # print(text)
    
    # 2. 앞 뒤로 0의 갯수 찾고, 규칙에 맞게 자르기
    # 여기선 앞뒤로 0의 갯수를 찾고 그중 작은 값만큼 앞 뒤로 0을 제거해준다.
    front = 0
    for i in range(len(text)):
        if text[i] == '0':
            front += 1
        else:
            break
    back = 0
    for i in range(len(text)-1, -1, -1):
        if text[i] == '0':
            back += 1
        else:
            break

    if front >= back:
        text = text[back:-back]
    else:
        text = text[front:-front]
    # 001101111011
    # print(text)

    # 3. 암호비트 패턴 찾기
    pattern = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']
    for i in range(len(text)//6):
        for j in range(10):
            if pattern[j] == text[i*6:i*6+6]:
                print(j, end=' ')
    print()


