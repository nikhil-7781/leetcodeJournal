class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        table={}
        res=[]

        for hi in range(len(nums)):
            n=nums[hi]
            complement=target-n

            if complement in table:
                res.append(table[complement])
                res.append(hi)
            else:
                table[n]=hi
        return res
                

        
