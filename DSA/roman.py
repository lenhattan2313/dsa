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