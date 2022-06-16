import sys
sys.stdin=open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, E = map(int, input().split())
    matrix = list(map(int, input().split()))

    new = []
    for i in range(0, 2 * N, 2):
        if matrix[i] == E:
            new.append(matrix[i + 1])

    if new == []:
        result = [E]
    else:
        result = [E, *new[:]]
        while new:
            n = new.pop(0)
            for i in range(0, 2*N, 2):
                if matrix[i] == n:
                    result.append(matrix[i+1])
                    new.append(matrix[i+1])

    print(f'#{tc} {len(result)}')
