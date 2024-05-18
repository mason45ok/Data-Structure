#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        listx = []
        if x < 0:
            return False
        reversed = 0
        temp = x
        while temp != 0:
            reversed = reversed * 10 
            reversed += temp % 10
            temp //= 10
        return (reversed == x)
# @lc code=end

