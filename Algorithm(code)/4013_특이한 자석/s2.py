import sys
import copy
from collections import deque

sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(4)]
    new = copy.deepcopy(magnetic)

    result = []
    for i in range(N):
        # 1. 자기 자신은 먼저 돌리기
        index, direction = map(int, input().split())

        direct = direction  # direction은 바뀌지 않는 값이므로
        idx = index  # index는 바뀌지 않는 값이므로
        result = deque(new[idx - 1])
        if direct == 1:
            result.rotate(1)
        else:
            result.rotate(-1)
        new[idx-1] = result

        # 2. 오른쪽 자석 탐색
        idx += 1
        while 0 <= idx <= 4: 
            direct = direct * (-1)
            if magnetic[idx - 2][2] != magnetic[idx - 1][6]:
                result = deque(magnetic[idx - 1])
                if direct == 1:
                    result.rotate(1)
                else:
                    result.rotate(-1)
                new[idx - 1] = result
            else:  # 더이상 탐색필요 없다면
                break
            idx += 1

        # 왼쪽 자석 탐색
        direct = direction
        idx = index
        idx -= 1
        while 0 < idx < 4:
            direct = direct * (-1)
            if magnetic[idx - 1][2] != magnetic[idx][6]:
                result = deque(magnetic[idx - 1])
                if direct == 1:
                    result.rotate(1)
                else:
                    result.rotate(-1)
                new[idx - 1] = result
            else:  # 더이상 탐색필요 없다면
                break
            idx -= 1
        magnetic = [[0] * 8 for _ in range(4)]

        # 4. 깊은 복사(deque는 copy.deepcopy를 사용할 수 없기 때문)
        for j in range(4):
            for k in range(8):
                magnetic[j][k] = new[j][k]
    
    # 5. 결과 출력
    result = 0
    for i in range(4):
        if new[i][0] == 1:
            result += 2 ** i

    print(f'#{tc} {result}')