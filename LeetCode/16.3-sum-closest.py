#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mins = float('inf')  # 使用正無窮來初始化最小差距
        result = 0
        for i in range(len(nums)):
            j = i + 1
            k = len(nums)-1
            while j < k :
                curr_sum = nums[i] + nums[j] + nums[k]
                diff = abs(curr_sum - target)

                if diff < mins:
                    mins = diff
                    result = curr_sum

                if curr_sum == target:
                    return result
                elif curr_sum > target:
                    k -= 1
                else:
                    j += 1
        return result
                
# @lc code=end

