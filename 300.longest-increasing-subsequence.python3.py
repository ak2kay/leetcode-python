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
            for j in range(cur_max, -1, -1):
                if nums[i] > max_v[j]:
                    lis[i] = j + 1
                    break
            # 如果更新了当前最大值，那么更新max_v
            if lis[i] > cur_max:
                cur_max = lis[i]
                max_v[cur_max] = nums[i]
            # 如果没有更新最大值，那么找到可能被i更新的j
            # 当nums[i] > max_v[j]也就是进入到了上面for循环中的if条件中
            # 如果进入了条件中，那么如果nums[i]比原来max_v[j+1]小的时候才有
            # 更新价值；
            elif nums[i] > max_v[j] and nums[i] < max_v[j+1]:
                max_v[j+1] = nums[i]
        
        return cur_max
