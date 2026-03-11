class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            sum_sq = 0
            while n > 0:
                digit = n % 10
                sum_sq += digit * digit
                n //= 10
            n = sum_sq
        return n == 1
