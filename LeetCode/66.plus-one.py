#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lens = len(digits)-1
        output = []
        x = digits[lens]
        for i in range(lens-1, -1 , -1) :
            x = x * 10
            x += digits[i]
        x += 1
        while x > 0:
            temp = x % 10
            output.append(temp)         
            x = x // 10
        return output
# @lc code=end

