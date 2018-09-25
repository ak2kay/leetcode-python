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
        
        max_v = [0 for i in range(length+1)]

        max_v[0] = min(nums) - 1
        max_v[1] = nums[0]
        lis = [1 for i in range(length)]

        cur_max = 1
        for i in range(1, length):
            index = self.get_index(max_v[:cur_max+1], nums[i])
            if index >= 0:
                max_v[index+1] = nums[i]
                cur_max = max(cur_max, index+1)
                
        return cur_max

    def get_index(self, max_v, num):
        length = len(max_v)

        if num > max_v[-1]:
            return length - 1
        if num < max_v[0]:
            return -1

        low = 0
        high = length - 1
        while low <= high:
            middle = low + ((high - low) >> 1)
            if max_v[middle] == num:
                return -1
            elif max_v[middle] > num:
                high = middle - 1
            elif max_v[middle+1] > num:
                return middle
            else:
                low = middle + 1

