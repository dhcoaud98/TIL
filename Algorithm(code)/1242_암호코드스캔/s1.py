import sys
sys.stdin = open('sample2_input.txt')


"""
input을 받을 때 다음의 코드 해석을 편리하게 하기 위해 오른쪽의 0을 모두 지워주고, 행 중복을 제거해주었다. 

tc = 1
['', '000000001DB176C588D26EC']
000000001DB176C588D26EC
000000000000000000000000000000000001110110110001011101101100010110001000110100100110111011

tc = 2
['', '000000000000000000000000000196EBC5A316C578', '000000328D1AF6E4C9BB0000000196EBC5A316C578']
000000000000000000000000000196EBC5A316C578
000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000110010110111010111100010110100011000101101100010101111
000000328D1AF6E4C9BB0000000196EBC5A316C578
000000000000000000000000001100101000110100011010111101101110010011001001101110110000000000000000000000000000000110010110111010111100010110100011000101101100010101111

"""

# 십진수로 만든 코드가 정상 코드인지 확인하는 함수
# 10의 배수인 경우에만 더해준다.
def check(lst):
    visited = []
    my_sum = 0
    # print(lst)
    for i in range(0, len(code_sum)//8):
        answer = lst[i*8:i*8+8]
        # print(answer)
        a = (answer[7]+answer[5]+answer[3]+answer[1])*3+answer[6]+answer[4]+answer[2]+answer[0]
        # print(a)
        if a % 10 == 0 and not visited:
            my_sum += answer[0]+answer[2]+answer[4]+answer[6]+answer[1]+answer[3]+answer[5]+answer[7]
            visited.append(answer)

    return my_sum


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    # 1. 입력을 받을 때 0인 라인을 제거하고 찾기
    arr = sorted(list(set(input().rstrip('0') for _ in range(N))))
    # print(arr)
    table = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111',
             '0001011']
    code_sum = []
    code = []
    cnt = 1
    change = 0

    # 2. 코드 분석하기
    for i in range(1, len(arr)):
        result = ''
        # print(arr[i])
        
        # 2-1. 16진수 코드를 2진수로 표현
        for j in range(len(arr[i])):
            oct = int(arr[i][j], base=16)
            binary = bin(oct)
            binary = binary[2:].zfill(4)
            result += binary
        result = result.rstrip('0')
        # print(result)

        # 2-2. 암호해석(배수를 함께 구해주며 코드를 해석한다.)
        change = 0
        cnt = 1
        k = len(result) - 1
        while k > 0:
            # 2-2-1. 몇 배수인지?
            if result[k] != result[k-1]:
                cnt += 1
                change += 1
                k -= 1
            else:
                cnt += 1
                k -= 1
            if change == 4:  # 암호코드는 1 -> 0 혹은 0 -> 1 코드가 3번만 반복된다.
                cnt -= 1
                # print(cnt)
                
                # 코드 끊어서 담기
                for m in range(8):
                    for n in range(10):
                        if result[-cnt:] == table[n]:
                            result = result[:-cnt]
                            code_sum.append(n)

                change = 0
                cnt = 1

                # 오른쪽의 0의 갯수를 제거하고, k값 변경
                result = result.rstrip('0')
                k = len(result)-1

        code.append(result)
    print(f'#{tc} {check(code_sum)}')
