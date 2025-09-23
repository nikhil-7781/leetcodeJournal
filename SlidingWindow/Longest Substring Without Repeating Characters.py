class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapping={}
        lo=0
        mLen=0

        if(len(s)==0 or s is None):
            return 0

        for hi in range(len(s)):
            if s[hi] in mapping:
                lo=max(lo, mapping.get(s[hi])+1)
            mapping[s[hi]]=hi
            mLen=max(mLen, hi-lo+1)
        return mLen
