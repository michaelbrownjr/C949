# Easy problem from leetcode

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def __init__(self, nums, target) -> None:
        self.nums = nums
        self.target = target

    def twoSum(self):
        i = 0
        j = 1
        
        while (self.nums[i] + self.nums[j]) != self.target:
            if j < len(self.nums) - 1:
                j += 1
            else:
                i += 1
                j-= 1
        return('[%d, %d]' % (i,j))

nums = [30, 12, 10, 1]
target = 40
guesses = Solution(nums, target)
print (guesses.twoSum())
