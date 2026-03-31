class Solution:
    def numberToWords(self, num: int) -> str:
        """
        Convert non-negative integer to English words (LeetCode 273).
        """
        if num == 0:
            return "Zero"
        
        # Numbers 1-19
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", 
                   "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", 
                   "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        # Tens
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", 
               "Seventy", "Eighty", "Ninety"]
        
        # Groups of thousands
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n: int) -> str:
            if n < 20:
                return below_20[n]
            if n < 100:
                return tens[n//10] + (" " + helper(n%10) if n%10 else "")
            return below_20[n//100] + " Hundred" + (" " + helper(n%100) if n%100 else "")
        
        result, group = [], 0
        while num > 0:
            num, r = divmod(num, 1000)
            if r:
                result.append(helper(r) + " " + thousands[group])
            group += 1
        
        return " ".join(result[::-1]).strip()
