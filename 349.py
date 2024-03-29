# 349. Intersection of Two Arrays
class Solution(object):
    def intersection(self, nums1, nums2):
        res = []
        for i in nums1:
            if nums2.count(i) > 0 and i not in res:
                res.append(i)
        return res


solution = Solution()
print(solution.intersection([1, 2], [2, 3]))
