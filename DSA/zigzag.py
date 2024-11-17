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


    def zigzag(self, s, numRows):
        index, direction = 0, 1
        rows = [[] for _ in range(numRows)]

        for i in range(len(s)):
            rows[index].append(s[i])
            if index == 0:
                direction = 1
            elif index == numRows - 1:
                direction = -1
            index += direction


        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        return ''.join(rows)


solution = Solution()
print(solution.zigzag("PAYPALISHIRING", 3))


