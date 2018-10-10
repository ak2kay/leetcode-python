#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (26.29%)
# Total Accepted:    133.1K
# Total Submissions: 504.1K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Note:
#
# You can assume that you can always reach the last index.
#
#


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return 0

        cur = 0
        steps = 0
        while cur < length:
            temp = nums[cur]
            if cur + temp >= length-1:
                steps += 1
                return steps
            else:
                most_access = [cur, cur+temp]
                for i in range(cur+1, cur+temp+1):
                    if i + nums[i] > most_access[1]:
                        most_access = [i, i+nums[i]]
                cur_step = temp if most_access[0] == cur else most_access[0] - cur
                cur = most_access[0]
                steps += 1


# if __name__ == "__main__":
#     nums = list(map(int, input().split()))
#     ex = Solution()
#     print(ex.jump(nums))
