
def power_set(idx):
    if idx < len(data):
        is_selected[idx] = 1
        power_set(idx + 1)
        is_selected[idx] = 0
        power_set(idx + 1)
    else:
        total = 0
        for k in range(len(data)):
            if is_selected[k]:
                total += data[k]
        if total == 1:
            results.append(is_selected[:])

        return results


data = [1] * 3
is_selected = [0] * 3
results = []
power_set(0)  # 자릿수 가져오기
print(results)

arr = [[2, 1, 2], [5, 8, 5], [7, 2, 2]]
s = 0
for i in range(3):
    for j in range(3):
        if results[i][j]:
            s += arr[i][j]


print(s)
