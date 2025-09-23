class Solution:
    def longestKSubstr(self, s, k):
        mapping = {}
        lo = 0
        maxLen = -1

        for hi in range(len(s)):
            mapping[s[hi]] = mapping.get(s[hi], 0) + 1
            
            while len(mapping) > k:
                mapping[s[lo]] -= 1
                if mapping[s[lo]] == 0:
                    mapping.pop(s[lo])
                lo += 1
                
            if len(mapping) == k:
                maxLen = max(maxLen, hi - lo + 1)

        return maxLen

        
        
