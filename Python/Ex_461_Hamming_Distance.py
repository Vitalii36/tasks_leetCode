'''
The Hamming distance between two integers is the number
of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance
between them.


Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding
bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1


Constraints:

0 <= x, y <= 231 - 1
'''


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_bit, res = x ^ y, 0
        while xor_bit > 0:
            xor_bit = xor_bit & (xor_bit - 1)
            res += 1
        return res

result = Solution()
x = 3
y = 1

print(result.hammingDistance(x, y))
