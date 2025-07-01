#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def backtarck(idx, comb, total):
            if total == target:
                ans.append(comb[:])
                return
            if total > target or idx >= len(candidates):
                return
            comb.append(candidates[idx])
            backtarck(idx, comb, total + candidates[idx])
            comb.pop()
            backtarck(idx + 1, comb, total)
            
            return ans
        return backtarck(0, [], 0)            
            
            
# @lc code=end

