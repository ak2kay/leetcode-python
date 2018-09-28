#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (28.47%)
# Total Accepted:    239.9K
# Total Submissions: 838K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
#
# string convert(string s, int numRows);
#
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if numRows == 1 or length <= numRows:
            return s

        res = []
        for i in range(numRows):
            # max_delta是打印第一行两个字符串之间的索引距离
            max_delta = numRows * 2 - 2
            j = i
            res.append(s[j])
            # next_must为当前打印行和第一行竖直对应的元素索引
            next_must = j + max_delta
            # next_cur为为斜坡元素
            next_cur = next_must - 2 * i
            while next_cur < length:
                if next_cur != j and next_cur != next_must:
                    res.append(s[next_cur])
                if next_must < length:
                    res.append(s[next_must])
                j += max_delta
                next_must = j + max_delta
                next_cur = next_must - i * 2

        return ''.join(res)


# if __name__ == "__main__":
#     s = 'PAYPALISHIRING'
#     ex = Solution()
#     print(ex.convert(s, 4))
