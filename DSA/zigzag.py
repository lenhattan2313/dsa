# 6. Zigzag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        direction = 1
        i = 0
        arr = [[] for _ in range(numRows)]
        for char in s:
            arr[i].append(char)
            if i == 0:
                direction = 1
            if i == numRows - 1:
                direction = -1

            i+= direction
        for n in range(numRows):
            arr[n] = ''.join(arr[n])

        return ''.join(arr)

solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))