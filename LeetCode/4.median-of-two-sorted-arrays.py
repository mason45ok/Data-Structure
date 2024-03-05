#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        lens = len(nums)
        n = 0.0
        if lens%2 == 0 :
            n = (nums[lens//2]+nums[lens//2-1])/2.0  
        else:
            n = nums[lens//2]
        return n
# @lc code=end

