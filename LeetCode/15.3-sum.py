#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 原地排序，不需要再用 list() 包裹
        s = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == 0:
                    s.add((nums[i], nums[j], nums[k]))  # 將三個數字打包成一個 tuple
                    j += 1
                    k -= 1
                elif curr_sum > 0:
                    k -= 1
                else:
                    j += 1
        output = list(s)
        output.sort()
        return output

# @lc code=end

