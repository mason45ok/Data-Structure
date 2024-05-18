#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lens = len(nums)    
        n = lens-1
        m = 0
        while m <= n :
            mid = (m + n)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                n = mid - 1
            else:            
                m = mid + 1
        # 處理目標值小於整個陣列的情況
        if n < 0:
            return 0
        # 處理目標值大於整個陣列的情況
        elif m >= lens:
            return lens
        else:
        # 如果循環結束，表示目標值不在陣列中，且 m 所指向的位置是應該插入的位置
            return m
# @lc code=end

