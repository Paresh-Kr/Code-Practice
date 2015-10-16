class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lenth = len(nums)
        tmp = nums[:]
        for i in range(lenth):
            nums[(i + k) % lenth] = tmp[i]

# test = Solution()
# nums = [1, 2]
# test.rotate(nums, 3)
# print nums
