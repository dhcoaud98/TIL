import sys

sys.stdin = open('input.txt')

width = list(map(int, input()))
nums = list(map(int, input().split()))
max_num = 0
answer_list = []

for num in nums:
    if num >= max_num:
        max_num = num

# for j in answer_list:
#     for k in
print(max_num)
# for j in answer_list:
#     # if answer_list[i] - answer_list[i+1]
