import sys
sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    F, N = input().split()
    lst = list(map(int, input().split()))

    cnt = int(F)
    while cnt > 0:
        temp = {}
        used = []
        for l in lst:  # 순서대로 딕셔너리 만들기
            if l not in used:
                used.append(l)
                temp[l] = 0
            temp[l] += 1
        # print(temp)
        max_key = max(temp, key=temp.get)
        # print(max_key)

        used = []
        for j in range(len(lst)):  # 1 턴 진행
            p = lst.pop(0)
            if p == max_key and not used:
                used.append(p)
                cnt -= 1
            else:
                lst.append(p)
                cnt -= 1
                if cnt <= 0:
                    break
    # print(lst)
    print(f'#{tc} {lst[-1]}')




