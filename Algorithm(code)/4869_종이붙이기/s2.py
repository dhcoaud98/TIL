import sys
sys.stdin = open('sample_input.txt')

TC = int(input())

# 런타임에러발생
# factorial 함수
def f(n):
    if n <= 1:
        return n
    else:
        return n*f(n-1)

for tc in range(1, TC+1):
    N = int(input())

    # 20짜리의 개수가 M개일 때 경우의 수는 (a/(b*c)) * (2**M)
    M = N//20
    cnt = 1
    for i in range(1, M+1):
        # 20의 개수 = i
        # 10의 개수 = (N-20*i)/10
        # 전체 개수 = i + (N-20*i)/10
        # a, b, c는 각각 팩토리얼을 나타냄.
        a = f(i + (N-20*i)/10)
        b = f(i)
        c = f((N-20*i)/10)
        # M값에 따라 나온 경우의 수를 합산
        cnt += (a/(b*c)) * (2**i)
    print(f'#{tc} {int(cnt)}')