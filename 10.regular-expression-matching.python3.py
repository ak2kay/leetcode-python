#
# [10] Regular Expression isMatching
#
# https://leetcode.com/problems/regular-expression-isisMatching/description/
#
# algorithms
# Hard (24.40%)
# Total Accepted:    232.2K
# Total Submissions: 951.8K
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a p (p), implement regular expression
# isisMatching with support for '.' and '*'.
# 
# 
# '.' isMatches any single character.
# '*' isMatches zero or more of the preceding element.
# 
# 
# The isisMatching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not isisMatch the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# Example 4:
# 
# 
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore
# it isisMatches "aab".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
# 
# 
#
# -*- coding:utf-8 -*-
from functools import lru_cache


class Solution:
    # s, pattern都是字符串
    @lru_cache()
    def isMatch(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:
            return True
        # 如果s长度不为0，而pattern长度为0，这种情况不可能匹配成功
        elif len(s) != 0 and len(pattern) == 0:
            return False
        # 如果s长度为0， 而pattern长度不为0，那么可能会有pattern为'（.*）*'的情况
        elif len(s) == 0 and len(pattern) != 0:
            # 如果pattern第二位为0, pattern推进两个
            if len(pattern) > 1 and pattern[1] == '*':
                return self.isMatch(s, pattern[2:])
            else:
                return False
        # 如果s和pattern长度都不为0
        else:
            # pattern第二位为*
            if len(pattern) > 1 and pattern[1] == '*':
                # 如果s[0] != pattern[0]
                if s[0] !=  pattern[0] and pattern[0] != '.':
                    return self.isMatch(s, pattern[2:])
                # 如果s[0] == pattern[0], 那么有三种情况
                    # 1. s不变，pattern后移两步（pattern前两个字符等价于空）
                    # 2. s右移一个， pattern右移两个 （pattern前两个字符等价于一个字符）
                    # 3. s右移一个， pattern不右移 （pattern前两个字符等价于多个字符)）
                else:
                    return self.isMatch(s, pattern[2:]) or \
                           self.isMatch(s[1:], pattern[2:]) or \
                           self.isMatch(s[1:], pattern)
            # pattern第二位不是*
            else:
                # 比较第一位的情况
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.isMatch(s[1:], pattern[1:])
                else:
                    return False

