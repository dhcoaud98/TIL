# 1. 순서가 없는 복원 추출
def pick1(n, picked, to_pick):
    if to_pick == 0:
        return print(picked)

    if not picked:  # 뽑힌게 비어있다면
        smallest = 0
    else:
        smallest = picked[-1]

    for i in range(smallest, n):
        picked.append(i)
        pick1(n, picked, to_pick-1)
        picked.pop()

# 2. 순서가 없는 비복원 추출
def pick2(n, picked, to_pick):
    if to_pick == 0:
        return print(picked)

    if not picked:
        smallest = 0
    else:
        smallest = picked[-1]

    for i in range(smallest, n):
        if i not in picked:
            picked.append(i)
            pick2(n, picked, to_pick-1)
            picked.pop()
# 3. 순서가 있는 복원 추출
def pick3(n, picked, to_pick):
    if to_pick == 0:
        return print(picked)

    for i in range(n):
        picked.append(i)
        pick3(n, picked, to_pick-1)
        picked.pop()
# 4. 순서가 있는 비복원 추출
def pick4(n, picked, to_pick):
    if to_pick == 0:
        return print(picked)

    for i in range(n):
        if i not in picked:
            picked.append(i)
            pick3(n, picked, to_pick-1)
            picked.pop()




n = 4
r = 3
print('순서가 없는 복원 추출')
pick1(n, [], r)  # 4개에서 3개를 뽑겠다.
print('순서가 없는 비복원 추출')
pick2(n, [], r)
print('순서가 있는 복원 추출')
pick3(n, [], r)
print('순서가 있는 비복원 추출')
pick4(n, [], r)






