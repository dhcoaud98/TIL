import sys
sys.stdin = open('sample_input(8).txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    # print(lst)
    temp = [0]*(N+1)
    visited = [0]*(N+1)  # 방문표시하기
    for i in range(M):
        temp[lst[i*2]] = []
    for i in range(M):
        temp[lst[i*2]].append(lst[i*2+1])
    print(temp)
    ans = 0
    idx = 1
    while idx < N+1:
        if temp[idx] == 0 and visited[idx] == 0:  # 쪽지에 번호를 쓰지 않았지도 않고, 방문기록도 없을때
            visited[idx] = 1
            ans += 1
            idx += 1
        elif temp[idx] == 0 and visited[idx] != 0:  # 쪽지에 번호를 쓰지 않았지만 방문기록 있음
            idx += 1
        else:
            if visited[idx] != 0:  # 이미 방문 표시가 되어 있다면 연결값을 미리 -1해준다.
                ans -= 1

            visited[idx] = 1
            base_idx = idx
            for j in range(len(temp[base_idx])):
                if visited[temp[base_idx][j]] == 0:
                    visited[temp[base_idx][j]] = 1
                elif temp[base_idx][j] == base_idx:  # 내가 나를 뽑았을 경우
                    break
                else:
                    ans -= 1
                    break
            idx += 1
            ans += 1

    print(f'#{tc} {ans}')


