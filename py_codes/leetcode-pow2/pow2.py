# There is a small trick about this problem.
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            # 10000 & 01111 == 0
            return n & (n - 1) == 0
        else:
            return False

test = Solution()
print test.isPowerOfTwo(32)
print test.isPowerOfTwo(16)
