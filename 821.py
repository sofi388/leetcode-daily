# 821. Shortest Distance to a Character
class Solution(object):
    def shortestToChar(self, s, c):
        res = []
        occur = []
        for i in range(len(s)):
            if s[i] == c:
                occur.append(i)
        for j in range(len(s)):
            if s[j] == c:
                res.append(0)
            else:
                newlist = [abs(j - i) for i in occur]
                newlist = sorted(newlist)
                res.append(newlist[0])

        return res


solution = Solution()
print(solution.shortestToChar('accc', 'a'))
