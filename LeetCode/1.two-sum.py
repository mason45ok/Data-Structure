#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        nums.sort()
        n = len(nums)-1
        m = 0
        output=[]
        while m < n :
            if nums[n] - nums[m]== target:
                output.append(m)
                output.append(n)
                break
            elif nums[n]-nums[m]> target:
                n -= 1
            else:
                m += 1     
        return output
# @lc code=end

