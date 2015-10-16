class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        else:
            return n % 2 + self.hammingWeight(n / 2)

# test = Solution()
# print test.hammingWeight(11)
# print test.hammingWeight(0)
