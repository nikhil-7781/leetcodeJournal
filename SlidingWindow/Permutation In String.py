class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        pattern_map={}
        string_map={}
        pattern_length=len(s1)
        lo=0

        for h in range(len(s1)):
            pattern_map[s1[h]]=pattern_map.get(s1[h],0)+1
        
        for hi in range(len(s2)):

            string_map[s2[hi]]=string_map.get(s2[hi],0)+1
            
            while(hi-lo+1>pattern_length):
                string_map[s2[lo]]-=1
                if string_map[s2[lo]] == 0:
                    del string_map[s2[lo]]
                lo+=1

            if(string_map==pattern_map):
                return True
            
        return False
