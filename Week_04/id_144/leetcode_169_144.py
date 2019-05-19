class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        start = nums[0]
        for i in range(len(nums)):
            if i == 0:
                continue
            if start == nums[i]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    start = nums[i+1]
        return start
