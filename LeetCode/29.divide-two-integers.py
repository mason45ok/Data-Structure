#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x = int(dividend/divisor)    
        if(dividend==-2147483648 and divisor==-1) :
            return 2147483647
        return x

# @lc code=end

