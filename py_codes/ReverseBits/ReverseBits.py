class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        len = 0
        while n:
            num = num * 2
            num += n % 2
            n /= 2
            len += 1
        num = num * pow(2, 32 - len)
        return num

# test = Solution()
# print test.reverseBits(43261596)  # 964176192
