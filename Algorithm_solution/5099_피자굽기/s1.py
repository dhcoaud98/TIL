import sys
from collections import deque
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    # 피자가 몇번째 원소인지 같이
    pizza = deque(enumerate(list(map(int, input().split())), 1))
    print(pizza)
    maker = deque()

    # N 만큼 pizza의 왼쪽에서부터 maker에 넣어준다.
    for i in range(N):
        maker.append(pizza.popleft())
    print(maker)

    # 피자가 한개만 있을 때까지 계속해서 반복한다.
    while len(maker) > 1:
        # 1. 피자의 갯수가 N 보다 작은데 남은 피자가 있을때
        if len(maker) < N and pizza:
            maker.append(pizza.popleft())
        idx, cheeze = maker.popleft()

        # 2-1. 치즈의 양이 0 이라면 제거
        if cheeze//2 == 0:
            continue
        # 2-2. 치즈의 양이 0이 아니라면 오른쪽에 추가해준다.
        else:
            maker.append((idx, cheeze//2))

    print(f'#{tc} {maker[0][0]}')