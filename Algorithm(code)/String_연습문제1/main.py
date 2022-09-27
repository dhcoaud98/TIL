import sys

sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    str1 = input()
    # 슬라이싱 이용
    print(f'#{tc} {str1[::-1]}')
