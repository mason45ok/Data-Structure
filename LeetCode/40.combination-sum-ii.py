#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        
        def backtarck(idx, comb, total):
            if total == target:
                ans.append(comb[:])
            if total > target:
                return
            prev = -1
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue
                comb.append(candidates[i])
                backtarck(i + 1, comb, total + candidates[i])
                comb.pop()
                prev = candidates[i]
            
        backtarck(0, [], 0)
        
        return ans
# @lc code=end

