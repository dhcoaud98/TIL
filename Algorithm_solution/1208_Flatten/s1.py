import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    dumps = int(input())
    boxs = list(map(int, input().split()))

    # 1
    # boxs의 최댓값 최솟값 구해서 -1, +1 하기
    cnt = 0
    for dump in range(0, dumps):
        max_num = 0
        min_num = 100
        # 1~dumps 중 첫 번째 (최댓값-1, 최솟값+1)을 위해 최댓값과 최솟값을 구하고, 그 index의 해당값을 구해 +-1 한다..   
        for c in range(0, 100):
            if boxs[c] >= max_num:
                max_num = boxs[c]
                col1 = c
            if boxs[c] <= min_num:
                min_num = boxs[c]
                col2 = c

        boxs[col1] -= 1
        boxs[col2] += 1

        # dumps 횟수 안에 for 문이 끝나게 되면 if문을 통해 for문을 빠져나간다. 
        if boxs[col1] - boxs[col2] <= 1:
            result = boxs[col1] - boxs[col2]
            break

    # 2
    # dumps 만큼 +-한 결과에서 새로운 max_num과 min_num을 찾아야 한다.
    # 마지막 for문에서 min_num 값이 여러개 있는 경우 한 값에 min_num += 1 하게 되면 가장 작은 수는 min_num +=1이 아닌 min_num 값이 되어야 한다.
    # [3, 3, 3, 4, 6, 3] 0번째 인덱스가 최솟값인데 +1 하여 [4, 3, 3, 4, 6, 3]가 되면 0번째 인덱스는 최솟값이 아니기 때문에 최대, 최소를 다시 구해주어야 한다.
    max_num = boxs[0]
    min_num = boxs[-1]

    for c in range(0, 100):
        if boxs[c] >= max_num:
            max_num = boxs[c]
        if boxs[c] <= min_num:
            min_num = boxs[c]
    result = max_num - min_num
    
    # 결과 출력
    print(f'#{tc} {result}')

