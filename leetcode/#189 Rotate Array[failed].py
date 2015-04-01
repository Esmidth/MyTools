__author__ = 'Esmidth'


def rotate(nums, k):
    n = len(nums)
    temp = nums[k+1:]
    i = n - k - 1
    ii = 0
    while ii < n - k:
        nums[i], nums[i + k] = nums[i + k], nums[i]
        ii += 1
        i -= 1
    ii = 0
    while ii < k:
        nums[ii] = temp[ii]
        ii += 1


a = [1, 2, 3, 4, 5, 6, 7]
rotate(a, 3)
print(a)
