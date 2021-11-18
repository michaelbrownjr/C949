class Solution:
    def __init__(self, nums, target) -> None:
        self.nums = nums
        self.target = target

    def twoSum(self):
        i = 0
        j = 1
        
        while (self.nums[i] + self.nums[j]) != self.target:
            print('%d and %d don\'t match' % (self.nums[i], self.nums[j]))
            if j < len(self.nums) - 1:
                j += 1
            else:
                i += 1
                j-= 1
                    # return('%d and %d does match %d' % (numbers, self.nums[j], self.target))


guesses = Solution([11, 2, 15, 7], 9)
print (guesses.twoSum())
