#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lens = len(height)
        first = 0
        last = lens - 1
        maxarea = 0
        while last > first:
            if height[first] >= height[last]:
                area = height[last]*(last-first)
            else :
                area = height[first]*(last-first)
            if area > maxarea:
                maxarea = area
            if height[first]>height[last]:
                last-=1
            else:
                first+=1
        return maxarea
            
            
# @lc code=end

