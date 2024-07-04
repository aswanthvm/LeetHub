class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        index_s={char:index for index,char in enumerate(s)}
        index_t={char:index for index,char in enumerate(t)}

        ans=0
        for i in index_s:
            ans+=abs(index_s[i]-index_t[i])
        return ans