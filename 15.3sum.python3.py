#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (22.03%)
# Total Accepted:    383.4K
# Total Submissions: 1.7M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length, res = len(nums), []
        
        if length < 3:
            return res 

        nums.sort()
        
        for left in range(length-2):
            if nums[left] > 0:
                break
            if left > 0 and nums[left] == nums[left-1]:
                continue

            middle = left + 1
            right = length - 1
            while middle < right:
                cur_sum = nums[left] + nums[middle] + nums[right]
                if cur_sum == 0:
                    res.append([nums[left], nums[middle], nums[right]])
                    middle += 1
                    right -= 1
                    while middle < right and nums[middle] == nums[middle-1]:
                        middle += 1
                    while right > middle and nums[right] == nums[right+1]:
                        right -= 1
                elif cur_sum < 0:
                    middle += 1 
                else:
                    right -= 1

        return res

