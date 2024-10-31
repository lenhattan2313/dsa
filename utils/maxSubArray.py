

def max_sub_arr(arr):
    if not arr:
        return 0
    curr = arr[0]
    maximum = arr[0]  # Handle cases where all elements might be negative.

    for i in range(1, len(arr)):
        curr = max(arr[i], curr + arr[i])
        maximum = max(maximum, curr)


    return maximum