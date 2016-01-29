class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        print list(enumerate(sorted(citations, reverse=True)))
        for i, c in enumerate(sorted(citations, reverse=True)):
            if i >= c:
                return i
        return len(citations)


def main():
    m = Solution()
    print m.hIndex([3, 0, 6, 1, 5])
if __name__ == "__main__":
    main()
