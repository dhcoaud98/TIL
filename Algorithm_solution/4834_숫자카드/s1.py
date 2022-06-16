import sys

sys.stdin = open('sample_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    cnt = int(input())
    nums = list(map(int, input()))            # ex) [4, 9, 6, 7, 9]
    result = [0] * 10

    # 1. 카드에 적힌 숫자와 카드가 몇 장인지 리스트화 하기
    for num in nums:
        result[num] += 1                     # [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]

    # 2. result에서 가장 큰 값 찾기
    c = result[0]
    for r in result:
        if r >= c:
            c = r

    # 3. result에서 가장 큰 값을 가지고 있는 인덱스를 찾기 (result의 인덱스는 0~9로 고정이므로 range(0, 10)을 사용했다.
    for r in range(0, 10):
        if result[r] >= c:
            max_num = r


    print(f'#{tc} {max_num} {c}')