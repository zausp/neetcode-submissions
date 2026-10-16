class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for b in range(len(nums)):
                if b == i:
                    continue
                if nums[i] + nums[b] == target:
                    return [i,b]
            