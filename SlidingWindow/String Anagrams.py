class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        res=[]
        s_map={}
        p_map={}
        p_len=len(p)

        for h in range(p_len):
            p_map[p[h]]=p_map.get(p[h],0)+1
        
        lo=0

        for hi in range(len(s)):
            s_map[s[hi]]=s_map.get(s[hi],0)+1

            while(hi-lo+1>p_len):
                s_map[s[lo]]-=1
                if(s_map[s[lo]]==0):
                    del s_map[s[lo]]
                lo+=1
            if(s_map==p_map):
                res.append(lo)
        return res


        
