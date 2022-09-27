def func(idx, N):
    if idx == N:
        print(bit)
        return

    else:
        bit[idx] = 0
        func(idx + 1, N)
        bit[idx] = 1
        func(idx + 1, N)

# [0, 0, 0]
# [0, 0, 1]
# [0, 1, 0]
# [0, 1, 1]
# [1, 0, 0]
# [1, 0, 1]
# [1, 1, 0]
# [1, 1, 1]

a = [1, 2, 3]
N = len(a)
bit = [0] * N

func(0, N)
