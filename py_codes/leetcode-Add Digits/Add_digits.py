class Solution(object):
    def addDigits(self, num):
        while num > 9:
            c = 0
            while num:
                c += num % 10
                num /= 10
            num = c
        return num


def main():
    m = Solution()
    print m.addDigits(48)
if __name__ == "__main__":
    main()
