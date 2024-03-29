# 771. Jewels and Stones
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        res = 0
        for i in jewels:
            res = res + stones.count(i)

        return res


solution = Solution()
print(solution.numJewelsInStones('ac', 'aAbbc'))

# O (n)
