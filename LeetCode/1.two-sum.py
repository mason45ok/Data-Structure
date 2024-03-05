#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n-1):
            cur = nums[i]
            x = target - cur
            for k in range(len(nums)):
                if x == nums[k] and k!=i:
                    return [i,k]
        
            
        
        
        
# @lc code=end

