import sys
sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    # 20짜리의 개수가 M개일 때 경우의 수는 (a/(b*c)) * (2**M)
    M = N//20
    cnt = 1
    for i in range(1, M+1):
        # 20의 개수 = i  ex) 2
        # 10의 개수 = (N-20*i)/10  ex) 1
        # 전체 개수 = i + (N-20*i)/10  ex) 3
        a = b = c = 1
        for k in range(1, int((i + (N-20*i)/10)+1)):
            a *= k
        for m in range(1, int(i+1)):
            b *= m
        for n in range(1, int(((N-20*i)/10)+1)):
            c *= n

        # M값에 따라 나온 경우의 수를 합산
        cnt += (a/(b*c)) * (2**i)
    print(f'#{tc} {int(cnt)}')

