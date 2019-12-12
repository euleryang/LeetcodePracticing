#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sums = 0
        for i in digits:
            sums = sums * 10 + i #10进制乘以10，进行累和；
        sums_str = str(sums + 1)
        return [int(j) for j in sums_str]
# @lc code=end

