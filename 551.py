# 557. Reverse Words in a String III
class Solution(object):
    def reverseWords(self, s):
        res = ""
        lst = s.split(" ")
        for elem in lst:
            res = res + elem[::-1]
            res = res + " "

        res = res.strip()

        return res


solution = Solution()
print(solution.reverseWords("Hello World!"))