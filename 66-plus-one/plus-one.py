class Solution:
    def plusOne(self, digits):  
        num_str = "".join(map(str,digits))
        res = []
        for digit in str(int(num_str)+1):
            res.append(int(digit))
        return res
