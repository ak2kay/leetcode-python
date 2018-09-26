#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (25.62%)
# Total Accepted:    370.8K
# Total Submissions: 1.4M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return ''
        length = len(s)
        if length < 2:
            return s
        s = self.str_trans(s)
        length = len(s)
        res = [1 for i in range(length)]
        i = 0
        while i < length:
            j, step = i, 1
            while j-step > -1 and j+step < length and s[j-step] == s[j+step]:
                res[i] += 2
                step += 1
            i += 1

        lp = max(res)
        lp_index = res.index(lp)
        lp = lp // 2
        lp = s[lp_index-lp:lp_index+lp+1]
        return lp.replace('#', '')



        


    def str_trans(self, s):
        s = list(s)
        for i in range(len(s)):
            s[i] = '#' + s[i]
        s.append('#')
        return ''.join(s)
