class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap= {}
        for i in range(len(nums)):
            cur = nums[i]
            x = target - cur
            if x in hashMap:
                return([hashMap[x],i])
            hashMap[nums[i]] = i