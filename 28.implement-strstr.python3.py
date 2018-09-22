#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (29.86%)
# Total Accepted:    316K
# Total Submissions: 1.1M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
# Example 1:
#
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
#
# Example 2:
#
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
#
#


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle:
            return 0

        if not needle:
            return 0

        if len(haystack) < len(needle):
            return -1

        len_h, len_n = len(haystack), len(needle)
        next_arr = self.get_next_arr(needle, len_n)
        i = j = 0
        while i < len_h and j < len_n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif next_arr[j] == -1:
                i += 1
            else:
                j = next_arr[j]

        return i - j if j == len_n else -1

    def get_next_arr(self, needle, len_n):
        if len_n == 1:
            return [-1]
        next_arr = [-1 for _ in range(len_n)]
        next_arr[1], i, cur = 0, 2, 0
        while i < len_n:
            if needle[i-1] == needle[cur]:
                next_arr[i] = cur + 1
                cur = next_arr[i]
                i += 1
            elif cur > 0:
                cur = next_arr[cur]
            else:
                next_arr[i] = 0
                i += 1

        return next_arr
