class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_account_balance=0

        for i in accounts:
            sum_array=sum(i)
            if sum_array>max_account_balance:
                max_account_balance=sum_array
        return max_account_balance


         