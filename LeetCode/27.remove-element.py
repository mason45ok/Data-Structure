#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        j = 0

        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i

# @lc code=end

