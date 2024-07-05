class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string=''.join([char.lower() for char in s if char.isalnum()])

        if string==string[::-1]:
            return True

        return False