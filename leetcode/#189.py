__author__ = 'Esmidth'
# Rotate Array
# Denied because the problems may induce the situation that k is less than the length of nums[]
a = [1, 2, 3, 4, 5, 6, 7]
b = 3


def rotate(nums, k):
    n = len(nums)
    temp = nums[n - k:]
    nums2 = nums[:n - k]
    i = 0
    while i < n - k:
        nums[i + k] = nums2[i]
        i += 1
    i = 0
    while i < k:
        nums[i] = temp[i]
        i += 1


rotate(a, b)
print(a)