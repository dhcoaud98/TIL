import sys

sys.stdin = open('s_input.txt')

TC = int(input())
for tc in range(1, TC+1):
    D, A, B, P = map(float,input().split())

    # 1. 파리가 B와 부딪힐 때까지 달리는 거리
    a = D / (A+P) * P
    # 2. 남은 거리 = 전체 거리 - 움직인 거리
    b = D - (D/(A+P)*(A+B))
    # 3. 파리가 이동한 나머지를 a에 더해줌
    a += b / (A+B) * P
    print(f'#{tc} ''%.6f' %a)

