import sys
sys.stdin = open('input.txt')

nanjange = []
for i in range(9):
    nanjange.append(int(input()))

result = []
answer = []
for i in range(1 << 9):  # 공집합을 제외한 모든 부분집합 검사
    result = []
    for j in range(9):  # nanjange의 모든 원소 루프
        if i & (1 << j):  # i의 j번째 비트 검사, j번째 비트가 1이라면 arr[j] 출력
            result.append(nanjange[j])
            if len(result) == 7 and sum(result) == 100:
                answer.append(result)
                break  # break를 하는 이유는 메모리를 줄이기 위해

answer = answer[0]
answer = sorted(answer)
for a in answer:
    print(a)
