import sys
sys.stdin = open('input (1).txt')


def Com(a):

    result = 1
    for i in range(18, 18-a, -1):
        result *= i

    div = 1
    for j in range(1, a+1):
        div *= j

    # print(result/div)
    return result/div


TC = int(input())
for tc in range(1, TC+1):
    A, B = map(int, input().split())

    arr = [ 2, 3, 5, 7, 11, 13, 17 ]
    ssumA = 0
    ssumB = 0

    # 장인 A와 장인 B 모두 완제품을 뽑을 확률을 각각 먼저 구한다.
    for a in arr:
        p = Com(a)
        # print(p)
        ssumA = ssumA + p * (A * 0.01)**a * ((100 - A) * 0.01)**(18 - a)
        # print('ssumA = ', ssumA)
        ssumB = ssumB + p * (B * 0.01)**a * ((100 - B) * 0.01)**(18 - a)
        # print('ssumB = ', ssumB )

    # print(1-(1-ssumA)*(1-ssumB))
    print(f'#{tc} {format(1-(1-ssumA)*(1-ssumB),".6f")}')