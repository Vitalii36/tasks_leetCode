'''
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
Example 4:

Input: columnTitle = "FXSHRXW"
Output: 2147483647
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        val = 0
        s = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for  i in columnTitle:
            val = val * 26
            val += s.index(i)
        return val


result = Solution()
columnTitle = "FXSHRXW"
print(result.titleToNumber(columnTitle))
