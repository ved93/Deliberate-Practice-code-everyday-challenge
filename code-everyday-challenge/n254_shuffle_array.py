# Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

# Implement the Solution class:

# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.

# https://leetcode.com/problems/shuffle-an-array/discuss/783073/Python-or-Easy-Solution
# https://leetcode.com/problems/shuffle-an-array/discuss/1401778/My-adventure-with-this-problem



class Solution:

    def __init__(self, nums  ):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        import random
        new_list = self.nums.copy()
        for i in range(len(new_list)):  # O(n)
            j = random.randint(0, i)
            print(i,j)
            new_list[i], new_list[j] = new_list[j], new_list[i]

        return new_list




if __name__ == "__main__":
    # ["Solution", "shuffle", "reset", "shuffle"]
    # [[[1, 2, 3]], [], [], []]
    nums = [1,2,3,4,5]
    obj = Solution(nums)
    param_1 = obj.reset()
    param_2 = obj.shuffle()
    print(param_2)