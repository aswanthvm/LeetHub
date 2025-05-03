class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = None

        for i in nums:
            if count == 0:
                majority = i
            count +=(1 if i == majority else -1)
        return majority
            

        