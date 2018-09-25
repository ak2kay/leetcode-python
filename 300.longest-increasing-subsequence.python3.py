#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (39.22%)
# Total Accepted:    154.8K
# Total Submissions: 394.3K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# Example:
# 
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4. 
# 
# Note: 
# 
# 
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
#
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return length
        
        res = [1 for i in range(length)]
        for i in range(1, length):
            res[i] = 1
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], res[j]+1)

        return max(res)

