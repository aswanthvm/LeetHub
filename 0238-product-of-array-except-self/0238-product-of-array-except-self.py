class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        zeroCount = 0
        product = 1
        
        for i in range(n):
            if nums[i] == 0:
                zeroCount += 1
            else:
                product *= nums[i]
        
        if zeroCount > 1:
            return [0] * n
        
        for i in range(n):
            if zeroCount == 1:
                if nums[i] == 0:
                    result[i] = product
                else:
                    result[i] = 0
            else:
                result[i] = product // nums[i]
        
        return result