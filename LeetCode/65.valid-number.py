#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # 去除首尾空格
        
        seen_digit = False
        seen_dot = False
        seen_e = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in ['+', '-']:
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
            elif char == '.':
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif char in ['e', 'E']:
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False
            else:
                return False
        
        return seen_digit

# @lc code=end

