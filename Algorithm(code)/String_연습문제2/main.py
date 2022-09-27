import sys

sys.stdin = open('input.txt')

TC = 6

def itoa(M):
    new_str = ''
    if M >= 0:
        while M != 0:
            m = chr((M % 10)+48)  # 숫자 2를 아스키 코드에서 문자 '2'로 뽑기 위한 식
            M = M // 10
            new_str = m + new_str
        return new_str
    else:
        M = (-1) * M
        while M != 0:
            m = chr((M % 10)+48)
            M = M // 10
            new_str = m + new_str
        return new_str


for tc in range(1, TC+1):
    M = int(input())
    print(f'#{tc} {itoa(M)} {type(itoa(M))}')
