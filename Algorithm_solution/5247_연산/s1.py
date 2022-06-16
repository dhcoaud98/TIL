import sys
from collections import deque
sys.stdin = open('sample_input.txt')


"""
문제 풀이 오류: 처음에는 '동철이의 일분배', '전기버스'로 접근하면 될것이라 판단했지만 하나의 result에 대해서
+1, -1, *2, -10의 결과값을 전부 저장하고, queue에서 사용할 것 처럼 모두 사용하면 된다. 
.pop(0) 와 .popleft()의 결과는 같지만 .pop(0)의 경우 계산 결과가 느릴 수 있으므로 deque를 사용한다. 
"""

def f(result, cnt):
    global min_cnt
    deq = deque([(result, cnt)])
    visited = set()  # 중복 방지
    visited.add(result)

    while deq:
        n, c = deq.popleft()

        if n == M:  # 해당하는 값이 있다면 c를 반환
            return c

        if n * 2 not in visited and n * 2 <= 1000000:
            deq.append((n * 2, c + 1))
            visited.add(n * 2)
        if n + 1 not in visited and n + 1 <= 1000000:
            deq.append((n + 1, c + 1))
            visited.add(n + 1)
        if n - 1 not in visited and n - 1 <= 1000000:
            deq.append((n - 1, c + 1))
            visited.add(n - 1)
        if n - 10 not in visited and n - 10 <= 1000000:
            deq.append((n - 10, c + 1))
            visited.add(n - 10)


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    min_cnt = float('inf')


    print(f'#{tc} {f(N, 0)}')
