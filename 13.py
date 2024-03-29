# 13. Roman to integer
class Solution(object):
    def romanToInt(self, s):
        res = 0
        result = 0
        mylist = list()
        for i in range(len(s)):
            if s[i] == 'I':
                res = 1
            elif s[i] == 'V':
                res = 5
            elif s[i] == 'X':
                res = 10
            elif s[i] == 'L':
                res = 50
            elif s[i] == 'C':
                res = 100
            elif s[i] == 'D':
                res = 500
            elif s[i] == 'M':
                res = 1000
            mylist.append(res)

        mylist.append(0)
        # MCMXCIV
        # '1000 100 1000 10 100 1 5'  --- list

        for i in range(len(s)):
            if i < len(s) - 1 and mylist[i] < mylist[i + 1]:
                result -= mylist[i]
            else:
                result += mylist[i]
        return result


solution = Solution()
print(solution.romanToInt('III'))