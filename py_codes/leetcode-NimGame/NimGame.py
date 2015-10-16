class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 2 or n == 3:
            return True
        elif n >= 4 and n % 4 == 0:
            return False
        else:
            return True

# test = Solution()
# print test.canWinNim(4)
# print test.canWinNim(6)
