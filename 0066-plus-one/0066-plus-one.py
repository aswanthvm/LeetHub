class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i= len(digits)-1
        while(digits[i] == 9 and i>=0):
            if (i == 0):
                tempArray = [0]*(len(digits)+1)
                tempArray[0] = 1
                return tempArray
            digits[i] = 0
            i-=1
        digits[i] += 1
        return digits
        


        

            
        