class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)          # Count frequency of each number
        return [num for num, freq in count.most_common(k)]
