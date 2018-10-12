#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (38.67%)
# Total Accepted:    58K
# Total Submissions: 149.6K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
# 
# 
# Note:
# 
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# 
# 
# 
# Example 1:
# 
# Input: [1, 5, 11, 5]
# 
# Output: true
# 
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# 
# Example 2:
# 
# Input: [1, 2, 3, 5]
# 
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
#
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2:
            return False
        v = total // 2
        resList = [False for i in range(v+1)]
        resList[0] = True

        for i in range(1, len(nums)+1):
            for j in range(v, nums[i-1]-1, -1):
                resList[j] = resList[j] or resList[j-nums[i-1]]
        return resList[v]
