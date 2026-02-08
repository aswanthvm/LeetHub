class Solution(object): 
    def shipWithinDays(self, weights, days): 
        left, right = max(weights), sum(weights) 
         
        while left < right: 
            mid = (left + right) // 2 
            days_used = 1 
            current_load = 0 
             
            for w in weights: 
                if current_load + w <= mid: 
                    current_load += w 
                else: 
                    days_used += 1 
                    current_load = w 
             
            if days_used <= days: 
                right = mid 
            else: 
                left = mid + 1 
         
        return left 
        