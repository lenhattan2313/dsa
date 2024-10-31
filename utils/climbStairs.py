def climb_stair(costs):
    # n = len(costs)
    # for i in range(2, n):
    #     costs[i] += min(costs[i - 1], costs[i-2])
    # return min(costs[n-1], costs[n-2])

    n = len(costs)
    prev1 = 0
    prev2 = 0

    for i in range(2, n):
        curr = costs[i] + min(prev2, prev1)
        prev2 = prev1
        prev1 = curr

    return min(prev2, prev1)