class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_z = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                num_z += 1
        if num_z == 0:
            pass
        else:
            tmp = nums
            j = 0
            for i in range(len(tmp)):
                if tmp[i] != 0:
                    nums[j] = tmp[i]
                    j += 1
            nums[j:] = [0] * num_z
test = Solution()
nums = [0, 1, 0, 3, 12]
test.moveZeroes(nums)
print nums
