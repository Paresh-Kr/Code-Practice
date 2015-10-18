class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0
        two = 0
        three = 0
        for i in nums:
            two = two | (one & i)
            one = one ^ i
            print one
            three = ~(one & two)
            one = one & three
            two = two & three
            print one
        return one
test = Solution()
nums = [2, 2, 2, 4]
print test.singleNumber(nums)
