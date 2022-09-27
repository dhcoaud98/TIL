import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    stringList = str(input())
    stringSubset = []
    for i in range(len(stringList)):
         stringSubset.append(stringList[i:])
    a = sorted(stringSubset)
    print(f'#{tc} {a[N-1]}')
