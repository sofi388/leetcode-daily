# 645. Set mismatch
class Solution(object):
    def findErrorNums(self, nums):
        numbers = [0] * len(nums)  # marking numbers in sequence 1 ... n
        reps = []  # result
        index = 0  # index of repeated number
        for item in nums:
            if numbers[item - 1] == 0:  # check for previous occurrence
                numbers[item - 1] += 1  # mark occurrence
            elif numbers[item - 1] != 0:  # if is a first repetition of this number
                reps.append(item)  # remember the number

        for num in numbers:  # check if some number is missed
            if num == 0:
                reps.append(numbers.index(num) + 1)  # append the missing number
        # reps.append(index)
        return reps


solution = Solution()
print(solution.findErrorNums([1, 2, 2, 4]))

# O(n)
