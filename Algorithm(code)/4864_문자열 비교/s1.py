import sys

sys.stdin=open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    P = input()
    T = input()
    result = 0

    for i in range(len(T)-len(P)+1):
        if T[i:i+len(P)] == P[:]:
            result = 1
            break

    print(f'#{tc} {result}')