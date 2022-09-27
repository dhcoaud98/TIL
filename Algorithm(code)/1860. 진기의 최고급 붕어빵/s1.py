import sys
sys.stdin=open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    
    # 붕어빵 준비
    ready = [0] * 11112
    i = 1
    ready[0] == K
    while M*i < 11112:
        ready[M*i] += K
        i += 1

    # people을 카운팅 정렬
    arr = [0] * 11112
    for i in range(N):
        arr[people[i]] += 1

    for i in range(len(arr)-1):
        if ready[0] - arr[0] < 0:
            result = 'Impossible'
            break
        else:
            ready[i+1] += ready[i] - arr[i]
            if ready[i+1] - arr[i+1] >= 0:
                result = 'Possible'
            else:
                result = 'Impossible'
                break

    print(f'#{tc} {result}')