class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map ={}
        
        for i in range(len(numbers)):
            
            diff = target - numbers[i] 
            if diff in map:
                return [map[diff],i+1]
            else:
                map[numbers[i]] = i+1
        return   [map[diff],i+1]
    
    

        