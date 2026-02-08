class Solution(object): 
    def minEatingSpeed(self, piles, h): 
        left, right = 1, max(piles) 
        answer = right 
         
        while left <= right: 
            mid = (left + right) // 2 
            hours = 0 
             
            for pile in piles: 
                hours += (pile + mid - 1) // mid 
             
            if hours <= h: 
                answer = mid 
                right = mid - 1   # try slower speed 
            else: 
                left = mid + 1    # need faster speed 
         
        return answer 
        