class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lo=0
        maxLen=0
        frequency=0

        for hi in range(len(nums)):
            if(nums[hi]==0):
                frequency+=1
            while(frequency>k):
                if(nums[lo]==0):
                    frequency-=1
                lo+=1
            maxLen=max(maxLen, hi-lo+1)
        return maxLen
