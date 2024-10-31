def maximum(arr):
    if len(arr) == 0:
        return 0
    max_number = arr[0]
    for num in arr:
        if num > max_number:
            max_number = num
    return max_number