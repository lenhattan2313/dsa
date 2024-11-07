class Solution:
    def add_bit(self, A, B):
        a = int(A, 2)
        b = int(B, 2)
        while b:
            without_carry = a ^ b
            carry = (a & b) << 1
            a, b = without_carry, carry

        return bin(a)[2:]

solution = Solution()
print(solution.add_bit("101", "1"))