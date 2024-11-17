class Solution:
    def intToRoman(self, num: int) -> str:
        hash = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                'CD': 400, 'CM': 900}
        ans = ''
        length = len(str(num))
        sorted_hash = dict(sorted(hash.items(), key=lambda item: item[1], reverse=True))
        for key, value in sorted_hash.items():
            if num % value < value:
                s = num // value
                ans += key * s
                num -= s * value

        return ans

    def romanToInt(self, str):
        hash = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(str)):
            if i < len(str) - 1 and hash[str[i]] < hash[str[i + 1]]:
                total -= hash[str[i]]
            else:
                total += hash[str[i]]
        return total

    def intToRoman2(self, num):
        hash = {
            1: "I",
            5: "V", 4: "IV",
            10: "X", 9: "IX",
            50: "L", 40: "XL",
            100: "C", 90: "XC",
            500: "D", 400: "CD",
            1000: "M", 900: "CM",
        }
        roman = ''

        sorted_h = dict(sorted(hash.items(), key=lambda x: x[0], reverse=True))
        for i, r in sorted_h.items():
            if num % i < i:
                s = num // i
                roman += r * s
                num -= s * i
        return roman


solution = Solution()
print(solution.intToRoman2(3479))
