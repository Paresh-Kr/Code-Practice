def decimalToAny(num, n):
    baseStr = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f", 16: "g", 17: "h", 18: "i", 19: "j", 20: "k", 21: "l", 22: "m", 23: "n", 24: "o", 25: "p", 26: "q", 27: "i", 28: "s", 29: "t", 30: "u", 31: "v"}
    new_num_str = ""
    while num != 0:
        remainder = num % n
        if 20 > remainder > 9:
            remainder_string = baseStr[remainder]
        elif remainder >= 20:
            remainder_string = "("+str(remainder)+")"
        else:
            remainder_string = str(remainder)
        new_num_str = remainder_string+new_num_str
        num = num / n
    return new_num_str


def AnyToDecimal(num, n):
    baseStr = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16, "h": 17, "i": 18, "j": 19, "k": 20, "l": 21, "m": 22, "n": 23, "o": 24, "p": 25, "q": 26, "i": 27, "s": 28, "t": 29, "u": 30, "v": 31}
    new_num = 0
    nNum = len(num) - 1
    for i in num:
        new_num = new_num + baseStr[i]*pow(n, nNum)
        nNum = nNum - 1
    return new_num

a = AnyToDecimal('2343001', 8)
b = decimalToAny(a, 17)
print a
print b
# with open('input.txt', 'r') as f:
#     for line in f:
#         a = line.split(',')
#         print AnyToDecimal(a[0], int(a[1]))
