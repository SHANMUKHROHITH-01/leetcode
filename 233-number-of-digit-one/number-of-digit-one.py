class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        
        count = 0
        i = 1
        while i <= n:
            # Split n into: prefix, current digit, and suffix
            # Example: n = 1234, i = 100
            # prefix = 12, digit = 3, suffix = 34
            prefix = n // (i * 10)
            digit = (n // i) % 10
            suffix = n % i
            
            if digit == 0:
                # Only the full cycles of prefixes contribute
                count += prefix * i
            elif digit == 1:
                # Full cycles + the partial remaining count from the suffix
                count += prefix * i + (suffix + 1)
            else:
                # The digit is > 1, so the current '1' cycle is complete
                count += (prefix + 1) * i
            
            # Move to the next place value (tens, hundreds, etc.)
            i *= 10
            
        return count