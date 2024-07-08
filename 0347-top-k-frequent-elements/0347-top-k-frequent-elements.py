class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = {}
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        return sorted(counter, key=counter.get, reverse=True)[:k]