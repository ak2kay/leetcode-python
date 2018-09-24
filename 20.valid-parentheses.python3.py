#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (34.54%)
# Total Accepted:    402.5K
# Total Submissions: 1.2M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: 
            return True 
        elif len(s) % 2 == 1:
            return False
        else:
            check_dict = {'(':')', '{':'}', '[':']'}
            stack = []
            for item in s:
                if item in check_dict:
                    stack.append(item)
                else:
                    if not stack or check_dict[stack[-1]] != item:
                        return False
                    else:
                        stack.pop()

            return True if not stack else False



