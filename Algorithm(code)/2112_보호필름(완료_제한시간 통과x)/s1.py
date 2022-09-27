import sys
import copy
sys.stdin = open('sample_input.txt')


def what_record(m):  # 1. 행 중에서 바꿀 수 있는 모든 경우의 수 구하기

    if m == D:
        if sum(bits) < max_num:
            pick(2, [], sum(bits), bits)
            return
    else:
        bits[m] = 0
        what_record(m+1)
        bits[m] = 1
        what_record(m+1)


def pick(n, picked, to_pick, bit):  # 2

    if to_pick == 0:
        change(bit, picked)
        # print(picked)
        return

    for k in range(n):
        picked.append(k)
        pick(n, picked, to_pick-1, bit)
        picked.pop()


def change(bit, picked):  # 3
    idx = 0
    film = copy.deepcopy(film_base)

    for i in range(D):
        if bit[i] == 1:
            for j in range(W):
                film[i][j] = picked[idx]
            idx += 1
    if idx < max_num:
        pass_k(film, idx)


def pass_k(lst, s):  # 4. 모든 열이 통과하는지?
    global pass_count, max_num
    pass_count = 0
    for i in range(W):
        cnt = 0
        for j in range(D-1):
            if lst[j][i] == lst[j+1][i]:
                cnt += 1
            else:
                cnt = 0
            if cnt == K-1:  # 모든 열이 성능검사 통과
                pass_count += 1
                break
        if i+1 != pass_count:  # 한 열이라도 성능 검사에 통과하지 못하면 그대로 종료
            break

    if pass_count == W:
        if max_num >= s:
            max_num = s


TC = int(input())
for tc in range(1, TC+1):
    D, W, K = map(int, input().split())
    film_base = [list(map(int, input().split())) for _ in range(D)]

    if K == 1:
        max_num = 0
    else:
        pass_count = 0
        max_num = D
        bits = [0] * D
        what_record(0)

    print(f'#{tc} {max_num}')
