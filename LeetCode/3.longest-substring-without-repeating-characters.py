#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        seem = set()
        start = 0
        end = 0
        for end in range(len(s)):
            while s[end] in seem:
                seem.remove(s[start])
                start += 1
            seem.add(s[end])
            if end - start + 1 > maxlen:
                maxlen = end - start + 1
        return maxlen
                
# @lc code=end

