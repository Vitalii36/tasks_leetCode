'''
Given an integer array nums, move all 0's to the end
of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        if 0 not in nums:
            return
        n, fin = nums.index(0), len(nums) - nums.count(0)
        while n != fin:
            zero = nums.pop(nums.index(0))
            n = nums.index(0) if 0 in nums else fin
            nums.append(zero)
        return nums
