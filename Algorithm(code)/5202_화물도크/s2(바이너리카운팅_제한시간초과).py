import sys
sys.stdin = open('sample_input.txt')


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 순열을 쓰게 되면 n > > 12일 때 시간 복잡도가 증가하게 되므로 바이너리 카운팅 사용
    for i in range(1 << N):  # 배열 N의 부분 집합의 개수
        boxs = []
        for j in range(0, N):
            if i & (1 << j):
                boxs.append(arr[j])
                # print(arr[j], end='')
        # print(boxs)

        # 겹치는 시간이 있나?
        if len(boxs) > result:
            hours = [0] * 24
            for k in boxs:
                for t in range(k[0], k[1]):
                    hours[t] += 1
            # print(hours)
            for k in range(len(hours)):
                if hours[k] >= 2:
                    break
                if k == 23:  # 중복 없이 끝까지 탐색 했을 경우
                    if result <= len(boxs):
                        result = len(boxs)
    
    print(f'#{tc} {result}')
