class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht={}
        for i in nums:
            if i in ht:
                ht[i]+=1
            else:
                ht[i]=1
        sort_ht=dict(sorted(ht.items(), key=lambda item: item[1],reverse=True))
        x=list(sort_ht.keys())
        res=[]
        for i in range(k):
            res.append(x[i])
        
        return res  
        