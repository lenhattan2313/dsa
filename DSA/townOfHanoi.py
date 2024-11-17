class Solution:
    def townOfHanoi(self, n, a, b, c):
        if n == 1:
            print(f'Di chuyen dia 1 tu {a} den {c}')
            return None
        self.townOfHanoi(n - 1, a, c, b)
        print(f'Di chuyen dia {n} tu {a} sang {c}')
        self.townOfHanoi(n - 1, b, a, c)

solution = Solution()
solution.townOfHanoi(3, 'A', 'B', 'C')