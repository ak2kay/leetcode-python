# coding:utf-8 
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (24.99%)
# Total Accepted:    572.1K
# Total Submissions: 2.3M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) < 1:
            return 0
        length = len(s)
        res = [0 for i in range(length)]
        res[0] = 1
        for i in range(1, length):
            search_str = s[:i][::-1]
            if s[i] in search_str:
                index = i - 1 - search_str.index(s[i])
                delta = i - index  # 两个相同字符间的间隔
                if delta <= res[i-1]:
                    res[i] = delta
                    continue
            res[i] = res[i-1] + 1

        return max(res)

