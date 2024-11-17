class Solution:
    def gas_station(self, gas, cost):
        n = len(gas)
        curr = start = 0
        for i, (g, c) in enumerate(zip(gas * 2, cost * 2)):
            if i == start + n:
                return start
            curr += g - c
            if curr < 0:
                start = i + 1
                curr = 0

    def canCompleteCircuit(self, gas, cost) -> int:
        if sum(gas) < sum(cost):
            return -1

        curernt_gas = 0
        start = 0
        for i in range(len(gas)):
            curernt_gas += gas[i] - cost[i]
            if curernt_gas < 0:
                curernt_gas = 0
                start = i + 1

        return start

    def canCompleteCircuit2(self, gas, cost) -> int:
        start = 0
        n = len(gas)
        curr = 0
        for i, (g, c) in enumerate(zip(gas * 2, cost * 2)):
            curr += g - c
            if i - start == n:
                return start

            if curr < 0:
                curr = 0
                start += 1
        return -1
solution = Solution()
print(solution.canCompleteCircuit2([1,2,3,4,5], [3,4,5,1,2]))