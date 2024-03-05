#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n  # 如果陣列長度小於等於1，不需要處理重複元素
        
        # 使用雙指針法，快指針用來遍歷整個陣列，慢指針用來表示去重後的陣列的尾部
        slow = 0
        
        for fast in range(1, n):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1  # 返回去除重複後的陣列的長度

# @lc code=end

