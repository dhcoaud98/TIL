import sys

sys.stdin = open('input.txt')

T = int(input())
# 1 ~ 12 준비
nums = range(1, 13)

for tc in range(1, T + 1):
    # N: 부분집합의 개수 / K: N개의 부분집합 요소로 만드는 합
    N, K = map(int, input().split())
    # 최종 결과 (가짓수)
    result = 0

    # 1부터 2^12까지 전부 확인 -> 모든 부분집합의 가짓수 확인
    for i in range(1, 1 << len(nums)):
        # total -> N개의 부분집합의 합
        total = 0
        # 부분집합의 개수 count
        cnt = 0
        # 0 ~ 12 / n+1 필요?
        for j in range(len(nums)):  # 0~12
            if i & (1 << j):
                total += nums[j]
                cnt += 1

        # cnt가 N개이고 그때의 합이 K인 경우만
        if cnt == N and total == K:
            # 1 증가
            result += 1

    print(f'#{tc} {result}')