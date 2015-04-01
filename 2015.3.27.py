__author__ = 'Esmidth'


class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        b = nums[:n - k]
        nums = nums[n - k:]

        for i in b:
            nums.append(i)

