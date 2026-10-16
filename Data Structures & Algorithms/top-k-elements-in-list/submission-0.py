class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        
        sorted_num = dict(sorted(seen.items(), key=lambda items : items[1], reverse=True))
        return [key for i, key in enumerate(sorted_num.keys()) if i < k ]
        