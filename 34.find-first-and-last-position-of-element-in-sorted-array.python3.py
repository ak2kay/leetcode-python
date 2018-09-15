#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (31.98%)
# Total Accepted:    219.4K
# Total Submissions: 685.8K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
#
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#
#


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or target is None or len(nums) < 1:
            return [-1, -1]

        first_pos = self.get_index(nums, target)
        last_pos = self.get_index(nums, target, False)

        return [first_pos, last_pos]

    def get_index(self, nums, target, first=True):
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = low + ((high - low) >> 1)
            if nums[middle] == target:
                if first:
                    if middle > 0 and nums[middle-1] == nums[middle]:
                        high = middle - 1
                    else:
                        return middle
                else:
                    if middle < len(nums) - 1 and nums[middle] == nums[middle+1]:
                        low = middle + 1
                    else:
                        return middle
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1

        return -1


# if __name__ == "__main__":
#     nums, target = [5, 7, 7, 8, 8, 10], 6
#     ex = Solution()
#     print(ex.searchRange(nums, target))
