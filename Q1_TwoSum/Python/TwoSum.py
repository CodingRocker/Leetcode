"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
class solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        dict = {}
        for i in range(size):
            x = nums[i]
            if (target - x in dict):
                return (dict[target - x], i)
            dict[x] = i

