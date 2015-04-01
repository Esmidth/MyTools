__author__ = 'Esmidth'
# Time Limit Exceeded

def rotate(nums, k):
    n = len(nums)
    ii = 0
    while ii < k:
        temp = nums[n - 1]
        for i in range(n - 2, -1, -1):
            nums[i + 1] = nums[i]
            print(nums)
        nums[0] = temp
        ii += 1


a = [1, 2, 3, 4, 5, 6, 7]
rotate(a, 3)
print(a)