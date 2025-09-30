class Solution:
    def minWindow(self, s: str, t: str) -> str:

        

        
        s_map={}
        t_map={}
        res=""
        cLen=float('inf')
        
        for hi in range(len(t)):
            t_map[t[hi]]=t_map.get(t[hi], 0)+1
        
        lo=0
        have=0
        need=len(t_map)

        for hi in range(len(s)):
            s_map[s[hi]]=s_map.get(s[hi], 0)+1

            if s[hi] in t_map and s_map[s[hi]]==t_map[s[hi]]:
                have+=1

            while(have==need):
                if(hi-lo+1<cLen):
                    cLen=hi-lo+1
                    res=s[lo:hi+1]
                
                s_map[s[lo]]-=1
                if s[lo] in t_map and s_map[s[lo]]<t_map[s[lo]]:
                    have-=1
                lo+=1
        return res
            
