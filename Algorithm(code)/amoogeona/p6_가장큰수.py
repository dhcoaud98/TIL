def solution(numbers):
    answer = ''
    result = []
    if numbers.count(0) == len(numbers):  # 히든케이슨
        answer = "0"
    else:
        for number in numbers:
            if number <= 9:
                result.append([number])
            else:
                a = []
                while number > 9:
                    a.append(number % 10)
                    number = number // 10
                a.append(number)
                result.append(a)
        arr = []
        for i in range(len(result)):
            arr.append(result[i][::-1])
        print(arr)

        for i in range(len(arr)):
            idx = 0
            while len(arr[i]) < 4:
                arr[i].append(arr[i][idx])
                idx += 1
            arr[i].append(i)
        print(arr)

        arr = sorted(arr, key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
        print(arr)
        for i in range(len(result)):
             answer += str(numbers[arr[i][4]])

    return answer


# numbers = [6, 10, 2]
# numbers = [3, 30, 34, 5, 9]
# numbers = [20, 2, 999, 998, 23]
# numbers = [330, 30, 303, 3, 33]
numbers = [0, 0, 0]
print(solution(numbers))


