def f(i, N, k):  # i 부분집합에 포함될지 결정할 원소의 인덱스, N전체 원소 개수
    if i == N:  #  한개의 부분집합 완성
        # print(bit, end=' ')
        # for j in range(N): # 1. 부분집합 뽑기
        #     if bit[j]:  # bit의 j번째가 1이면 a의 j번째를 출력
        #         print(a[j], end=' ')
        # print()
        print(bit, end=' ')
        s = 0
        for j in range(N):  # 2. 내가 원하는 합인 경우만 출력
            if bit[j]:  # bit의 j번째가 1이면 a의 j번째를 출력
                s += a[j]
        if s == k:
            for j in range(N):
                if bit[j]:
                    print(a[j], end=' ')

        print()

    else:
        bit[i] = 1
        f(i+1, N, k)
        bit[i] = 0
        f(i+1, N, k)  # 갈림길이 두개이면 f를 두번 호출
    return

a = [1, 2, 3]
bit = [0, 0, 0]
f(0, 3, 4)

