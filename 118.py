# 118. Pascals Triangle
class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        # Recursion
        list_result = self.generate(numRows - 1)
        prev_row = list_result[-1]
        list_in = [1]

        for i in range(1, numRows - 1):
            list_in.append(prev_row[i - 1] + prev_row[i])

        list_in.append(1)
        list_result.append(list_in)

        return (list_result)


solution = Solution()
print(solution.generate(3))

# O(n)
