def fibonacci(n):
    if n <= 2:
        return 1
    prev1 = 1
    prev2 = 1
    for i in range(n - 2):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1
