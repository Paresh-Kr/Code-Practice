class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_Dict = {}
        for i in nums:
            if i not in nums_Dict:
                nums_Dict[i] = i
            elif i in nums_Dict:
                return True
            else:
                pass
        return False
test = Solution()
print test.containsDuplicate([1, 2, 3, 4])
