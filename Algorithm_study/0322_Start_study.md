# 03.23

## Start

<br>

### 1. 16 진수를 2진수로

```python
    result = []
    # 16 -> 8 -> 2
    for i in range(len(arr)):
        dec_value = int(arr[i], base=16)
        # print(dec_value)
        bin_value = bin(dec_value)
        # print(f'{6:08b}')
        # print(bin_value[2:].zfill(4))  # 4 비트를 나타내기 위한 방법ㅂ으로 format으로 표현 할 수도 있다.
        r = bin_value[2:].zfill(4)
        result.append(r)

    result = ''.join(result)
```

```python
# 0F97A3

# 000011111001011110100011
```

