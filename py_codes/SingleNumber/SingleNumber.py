# XOR bitwise operation
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            result = result ^ i
        return result
test = Solution()
nums = [1, 2, 3, 4, 3, 2, 1]
print test.singleNumber(nums)
