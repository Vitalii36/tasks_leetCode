'''
Given two integer arrays nums1 and nums2, return an array of
their intersection. Each element in the result must be unique
and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''


class Solution:
    def intersection(self, nums1, nums2):
        nums1, nums2, res = list(set(nums1)), list(set(nums2)), []
        start = nums1 if len(nums1) < len(nums2) else nums2
        second = nums2 if len(nums1) < len(nums2) else nums1
        for obj in start:
            if obj in second:
                res.append(obj)
        return res


result = Solution()
nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]

print(result.intersection(nums1, nums2))
