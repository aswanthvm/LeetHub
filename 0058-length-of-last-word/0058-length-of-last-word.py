class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_list=s.split()
        return(len(new_list[-1]))
        


        