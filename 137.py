# 136. Single Number
class Solution(object):
    def singleNumber(self, nums):
        xor = 0

        for item in nums:
            xor = xor ^ item

        return xor


solution = Solution()
print(solution.singleNumber([1, 2, 2, 1, 4]))

# O(n)