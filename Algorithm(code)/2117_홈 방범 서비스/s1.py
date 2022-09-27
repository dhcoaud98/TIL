import sys
import copy
sys.stdin = open('sample_input.txt')

def home():
    global total
    cnt = 0
    for y in range(N):
        for x in range(N):
            if total[y][x] == 3:
                cnt += 1
    return cnt

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #print(arr)
    
    max_home = 0
    for i in range(N):
        for j in range(N):
            # 파란칠 하기
            for k in range(0, N+1):
                total = copy.deepcopy(arr)
                # 윗줄 파란칠
                blue = 1
                for n in range(i-k, i):
                    a = blue//2
                    for m in range(j-a, j+a+1):
                        if 0 <= n < N and 0 <= m < N:
                            total[n][m] += 2
                    blue += 2

                # 현재 줄
                for m in range(j-k, j+k+1):
                    if 0 <= m < N:
                        total[i][m] += 2

                # 아랫줄 파란칠
                blue = 2*k - 1
                for n in range(i+1, i+1+k):
                    a = blue//2
                    for m in range(j-a, j+a+1):
                        if 0 <= n < N and 0 <= m < N:
                            total[n][m] += 2
                    blue -= 2
                #print(total)

                # 총비용 = 입금-운영비용
                home_count = home()
                #print(home_count)
                pay = (home_count * M) - ((k+1)*(k+1)+k*k)
                #print(k, (k+1)*(k+1)+k*k)

                if pay >= 0:
                    #print(home_count)
                    if home_count >= max_home:
                        max_home = home_count

    print(f'#{tc} {max_home}')
