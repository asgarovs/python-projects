class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashNum = {}
        for i in range(0,len(nums)):
            if nums[i] not in hashNum:
                hashNum[nums[i]] = 1
            else:
                return True
        return False