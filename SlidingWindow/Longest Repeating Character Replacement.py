class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lo=0
        maxLen=0
        mapping={}
        max_key=0

        for hi in range(len(s)):
            mapping[s[hi]]=mapping.get(s[hi],0)+1
            while((hi-lo+1-max(mapping.values()))>k):
                mapping[s[lo]]-=1
                lo+=1
            maxLen=max(maxLen, hi-lo+1)
        return maxLen



        
