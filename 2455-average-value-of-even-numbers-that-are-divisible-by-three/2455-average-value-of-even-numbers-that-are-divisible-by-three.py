class Solution:
    def averageValue(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                arr.append(num)
        if not arr:
            return 0
        return sum(arr) // len(arr)

        

        